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

    if failures:
        print("사이트 검증 실패:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(
        "사이트 검증 통과: "
        f"chapters={parser.chapter_count} figures={len(parser.figures)} "
        f"internal_links={sum(href.startswith('#') for href in parser.hrefs)} "
        "metadata=ok responsive_images=ok source_images=ok"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
