#!/usr/bin/env python3
"""Dependency-free structural checks for the generated book site."""

from __future__ import annotations

import json
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.hrefs: list[str] = []
        self.local_sources: list[str] = []
        self.figures: list[dict[str, object]] = []
        self.chapter_count = 0
        self.chapter_figures = 0
        self.leader_summaries = 0
        self.reading_aids = 0
        self.table_count = 0
        self.stat_dashboards = 0
        self.stat_charts = 0
        self.stat_chart_labels = 0
        self.stat_values: list[int] = []
        self.stat_bar_svgs = 0
        self.stat_hidden_bars = 0
        self.stat_width_errors: list[str] = []
        self.axmm_structures = 0
        self.axmm_structure_labels = 0
        self.axmm_cells = 0
        self.awaiting_chapter_figure = False
        self.in_chapter_h1 = False
        self.current_figure: dict[str, object] | None = None
        self.meta: dict[str, str] = {}
        self.canonical = ""
        self.in_json_ld = False
        self.json_ld_text: list[str] = []
        self.json_ld: list[dict[str, object]] = []

    @staticmethod
    def attr_map(attrs: list[tuple[str, str | None]]) -> dict[str, str]:
        return {key: value or "" for key, value in attrs}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = self.attr_map(attrs)
        classes = values.get("class", "").split()

        if self.awaiting_chapter_figure:
            if tag == "figure" and "editorial-figure" in classes:
                self.chapter_figures += 1
            self.awaiting_chapter_figure = False

        element_id = values.get("id")
        if element_id:
            self.ids.append(element_id)

        if tag == "a" and values.get("href"):
            self.hrefs.append(values["href"])

        if tag == "h1" and values.get("id", "").startswith("장.-"):
            self.chapter_count += 1
            self.in_chapter_h1 = True

        if "leader-summary" in classes:
            self.leader_summaries += 1
        if "reading-aid" in classes:
            self.reading_aids += 1
        if "stat-dashboard" in classes:
            self.stat_dashboards += 1
        if "stat-chart" in classes:
            self.stat_charts += 1
            if values.get("role") == "img" and values.get("aria-label", "").strip():
                self.stat_chart_labels += 1
        if "axmm-structure" in classes:
            self.axmm_structures += 1
        if "axmm-map-grid" in classes:
            if values.get("role") == "img" and (
                values.get("aria-label", "").strip() or values.get("aria-labelledby", "").strip()
            ):
                self.axmm_structure_labels += 1
        if "axmm-cell" in classes:
            self.axmm_cells += 1
        if tag == "svg" and {"stat-wide-bar", "stat-mini-bar"}.intersection(classes):
            self.stat_bar_svgs += 1
            if values.get("aria-hidden") == "true" and values.get("focusable") == "false":
                self.stat_hidden_bars += 1
        if "stat-fill" in classes and values.get("data-value", "").isdigit():
            data_value = int(values["data-value"])
            self.stat_values.append(data_value)
            try:
                if float(values.get("width", "")) != data_value:
                    self.stat_width_errors.append(f"{data_value}:{values.get('width', '')}")
            except ValueError:
                self.stat_width_errors.append(f"{data_value}:{values.get('width', '')}")
        if tag == "table":
            self.table_count += 1

        if tag == "figure" and "editorial-figure" in classes:
            self.current_figure = {
                "cover": "cover-figure" in classes,
                "images": [],
            }
            self.figures.append(self.current_figure)

        if tag == "img":
            src = values.get("src", "")
            if src:
                self.local_sources.append(src)
            if self.current_figure is not None:
                images = self.current_figure["images"]
                assert isinstance(images, list)
                images.append(values)

        if tag == "meta":
            key = values.get("name") or values.get("property")
            if key:
                self.meta[key] = values.get("content", "")

        if tag == "link" and values.get("rel") == "canonical":
            self.canonical = values.get("href", "")

        if tag == "script" and values.get("type") == "application/ld+json":
            self.in_json_ld = True
            self.json_ld_text = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "h1" and self.in_chapter_h1:
            self.in_chapter_h1 = False
            self.awaiting_chapter_figure = True
        if tag == "figure":
            self.current_figure = None
        if tag == "script" and self.in_json_ld:
            self.in_json_ld = False
            try:
                payload = json.loads("".join(self.json_ld_text))
                if isinstance(payload, dict):
                    self.json_ld.append(payload)
            except json.JSONDecodeError:
                pass

    def handle_data(self, data: str) -> None:
        if self.in_json_ld:
            self.json_ld_text.append(data)


def local_path(value: str) -> Path | None:
    if not value or value.startswith(("http://", "https://", "data:")):
        return None
    return DOCS / value.split("?", 1)[0].split("#", 1)[0]


def main() -> int:
    failures: list[str] = []
    html_path = DOCS / "index.html"
    if not html_path.is_file():
        print("docs/index.html이 없습니다.", file=sys.stderr)
        return 1

    parser = SiteParser()
    parser.feed(html_path.read_text(encoding="utf-8"))

    def require(condition: bool, message: str) -> None:
        if not condition:
            failures.append(message)

    require(parser.chapter_count == 15, f"장 제목 수: {parser.chapter_count} (예상 15)")
    require(parser.chapter_figures == 15, f"장 제목 직후 삽화 수: {parser.chapter_figures} (예상 15)")
    require(len(parser.figures) == 16, f"전체 삽화 수: {len(parser.figures)} (예상 16)")
    require(parser.leader_summaries == 15, f"리더 요약 카드 수: {parser.leader_summaries} (예상 15)")
    require(parser.reading_aids >= 9, f"읽기 보조 요소 수: {parser.reading_aids} (최소 9)")
    require(parser.table_count >= 10, f"표 수: {parser.table_count} (최소 10)")
    require(parser.stat_dashboards == 4, f"통계 대시보드 수: {parser.stat_dashboards} (예상 4)")
    require(parser.stat_charts == 5, f"통계 그래프 수: {parser.stat_charts} (예상 5)")
    require(parser.stat_chart_labels == 5, f"통계 그래프 접근성 라벨 수: {parser.stat_chart_labels} (예상 5)")
    require(parser.stat_bar_svgs == 18, f"통계 막대 SVG 수: {parser.stat_bar_svgs} (예상 18)")
    require(parser.stat_hidden_bars == 18, f"보조기기에서 숨긴 장식 막대 수: {parser.stat_hidden_bars} (예상 18)")
    require(
        Counter(parser.stat_values)
        == Counter([13, 99, 58, 75, 16, 84, 24, 45, 20, 28, 34, 31, 7, 8, 44, 40, 4, 4]),
        f"통계 그래프 값 오류: {parser.stat_values}",
    )
    require(not parser.stat_width_errors, f"통계 막대 너비 오류: {parser.stat_width_errors}")
    require(parser.axmm_structures == 1, f"AXMM 전체 구조도 수: {parser.axmm_structures} (예상 1)")
    require(parser.axmm_structure_labels == 1, f"AXMM 구조도 접근성 라벨 수: {parser.axmm_structure_labels} (예상 1)")
    require(parser.axmm_cells == 30, f"AXMM 구조도 문항 셀 수: {parser.axmm_cells} (예상 30)")

    all_images: list[tuple[dict[str, str], bool]] = []
    for figure in parser.figures:
        images = figure["images"]
        assert isinstance(images, list)
        require(len(images) == 1, "삽화 figure에는 img가 정확히 하나여야 합니다.")
        if images:
            image = images[0]
            assert isinstance(image, dict)
            all_images.append((image, bool(figure["cover"])))

    for image, cover in all_images:
        src = image.get("src", "")
        require(bool(image.get("alt", "").strip()), f"alt 누락: {src}")
        require(image.get("width") == "1408", f"width 오류: {src}")
        require(image.get("height") in {"919", "939"}, f"height 오류: {src}")
        require(image.get("decoding") == "async", f"decoding 오류: {src}")
        require(bool(image.get("sizes")), f"sizes 누락: {src}")
        srcset = image.get("srcset", "")
        require("704w" in srcset and "1408w" in srcset, f"srcset 오류: {src}")

        if cover:
            require(image.get("loading") == "eager", "표지 이미지는 eager 로딩이어야 합니다.")
            require(image.get("fetchpriority") == "high", "표지 이미지 우선순위가 high가 아닙니다.")
        else:
            require(image.get("loading") == "lazy", f"본문 이미지 lazy 누락: {src}")

        for candidate in [src, *(part.strip().split()[0] for part in srcset.split(",") if part.strip())]:
            path = local_path(candidate)
            require(path is None or path.is_file(), f"이미지 파일 없음: {candidate}")

    duplicate_ids = [key for key, count in Counter(parser.ids).items() if count > 1]
    require(not duplicate_ids, f"중복 ID: {duplicate_ids}")
    known_ids = set(parser.ids)
    broken_anchors = [href for href in parser.hrefs if href.startswith("#") and unquote(href[1:]) not in known_ids]
    require(not broken_anchors, f"깨진 내부 링크: {broken_anchors[:10]}")

    for source in parser.local_sources:
        path = local_path(source)
        require(path is None or path.is_file(), f"로컬 자산 없음: {source}")

    required_meta = {
        "description",
        "robots",
        "og:title",
        "og:description",
        "og:url",
        "og:image",
        "twitter:card",
        "twitter:title",
        "twitter:image",
    }
    missing_meta = sorted(required_meta - parser.meta.keys())
    require(not missing_meta, f"메타데이터 누락: {missing_meta}")
    require(parser.canonical == "https://ksangki.github.io/ax-maturity/", "canonical URL 오류")
    require(any(item.get("@type") == "Book" for item in parser.json_ld), "Book JSON-LD 누락 또는 오류")
    require((DOCS / "assets/images/social-cover.jpg").is_file(), "소셜 공유 이미지 누락")

    for number in range(1, 16):
        source = ROOT / f"chapters/{number:02d}_draft.md"
        markdown = source.read_text(encoding="utf-8")
        require(markdown.count('<figure class="editorial-figure">') == 1, f"원고 삽화 블록 오류: {source.relative_to(ROOT)}")
        require(f"ch{number:02d}-" in markdown, f"원고 이미지 경로 오류: {source.relative_to(ROOT)}")
        require("srcset=" in markdown and "sizes=" in markdown, f"원고 반응형 이미지 속성 누락: {source.relative_to(ROOT)}")
        require(markdown.count("::: {.leader-summary}") == 1, f"리더 요약 카드 원본 오류: {source.relative_to(ROOT)}")

    if failures:
        print("사이트 검증 실패:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(
        "사이트 검증 통과: "
        f"chapters={parser.chapter_count} figures={len(parser.figures)} "
        f"leader_summaries={parser.leader_summaries} reading_aids={parser.reading_aids} tables={parser.table_count} "
        f"stat_dashboards={parser.stat_dashboards} stat_charts={parser.stat_charts} stat_bars={parser.stat_bar_svgs} "
        f"axmm_structures={parser.axmm_structures} axmm_cells={parser.axmm_cells} "
        f"internal_links={sum(href.startswith('#') for href in parser.hrefs)} "
        "metadata=ok responsive_images=ok source_images=ok"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
