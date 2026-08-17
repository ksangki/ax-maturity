#!/usr/bin/env python3
"""Validate EPUB structure, embedded chapter images, and statistical charts."""

from __future__ import annotations

import json
import posixpath
import sys
import zipfile
from collections import Counter
from pathlib import Path, PurePosixPath
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
XHTML_NS = "http://www.w3.org/1999/xhtml"


def main() -> int:
    manifest = json.loads((ROOT / "book_manifest.json").read_text(encoding="utf-8"))
    epub_path = ROOT / f"나는-이-게임을-안다-v{manifest['version']}.epub"
    failures: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            failures.append(message)

    if not epub_path.is_file() or not zipfile.is_zipfile(epub_path):
        print(f"유효한 EPUB 파일이 없습니다: {epub_path.name}", file=sys.stderr)
        return 1

    with zipfile.ZipFile(epub_path) as archive:
        names = set(archive.namelist())
        require(archive.read("mimetype") == b"application/epub+zip", "mimetype 오류")

        chapter_count = 0
        editorial_figures = 0
        chapter_images: list[tuple[str, str]] = []
        stat_dashboards = 0
        stat_charts = 0
        stat_chart_labels = 0
        stat_values: list[int] = []
        stat_bar_svgs = 0
        stat_hidden_bars = 0
        stat_width_errors: list[str] = []
        axmm_structures = 0
        axmm_structure_labels = 0
        axmm_cells = 0
        responsive_imgs: list[str] = []

        for name in sorted(item for item in names if item.endswith(".xhtml")):
            try:
                root = ElementTree.fromstring(archive.read(name))
            except ElementTree.ParseError as error:
                failures.append(f"XHTML 파싱 오류: {name}: {error}")
                continue

            # 리더는 src보다 srcset을 우선한다. pandoc이 src만 EPUB 안의
            # 경로로 고치므로 srcset이 남아 있으면 없는 파일을 가리켜 그림이
            # 빈칸이 된다. src가 멀쩡해도 대체되지 않는다.
            for image in root.iter(f"{{{XHTML_NS}}}img"):
                leftover = sorted(
                    attr for attr in ("srcset", "sizes") if attr in image.attrib
                )
                if leftover:
                    responsive_imgs.append(f"{name}:{','.join(leftover)}")

            for heading in root.iter(f"{{{XHTML_NS}}}h1"):
                text = "".join(heading.itertext()).strip()
                if text and text[0].isdigit() and "장." in text:
                    chapter_count += 1

            for element in root.iter():
                classes = element.attrib.get("class", "").split()
                if "editorial-figure" in classes:
                    editorial_figures += 1
                if "stat-dashboard" in classes:
                    stat_dashboards += 1
                if "stat-chart" in classes:
                    stat_charts += 1
                    if element.attrib.get("role") == "img" and element.attrib.get("aria-label", "").strip():
                        stat_chart_labels += 1
                if "axmm-structure" in classes:
                    axmm_structures += 1
                if "axmm-map-grid" in classes:
                    if element.attrib.get("role") == "img" and (
                        element.attrib.get("aria-label", "").strip()
                        or element.attrib.get("aria-labelledby", "").strip()
                    ):
                        axmm_structure_labels += 1
                if "axmm-cell" in classes:
                    axmm_cells += 1
                if {"stat-wide-bar", "stat-mini-bar"}.intersection(classes):
                    stat_bar_svgs += 1
                    if element.attrib.get("aria-hidden") == "true" and element.attrib.get("focusable") == "false":
                        stat_hidden_bars += 1
                if "stat-fill" in classes and element.attrib.get("data-value", "").isdigit():
                    data_value = int(element.attrib["data-value"])
                    stat_values.append(data_value)
                    try:
                        if float(element.attrib.get("width", "")) != data_value:
                            stat_width_errors.append(f"{data_value}:{element.attrib.get('width', '')}")
                    except ValueError:
                        stat_width_errors.append(f"{data_value}:{element.attrib.get('width', '')}")
                if element.tag == f"{{{XHTML_NS}}}img" and "editorial-figure" in {
                    parent_class
                    for ancestor in root.iter()
                    for parent_class in ancestor.attrib.get("class", "").split()
                    if element in list(ancestor)
                }:
                    chapter_images.append((name, element.attrib.get("src", "")))

        require(chapter_count == 15, f"장 제목 수: {chapter_count} (예상 15)")
        require(editorial_figures == 15, f"본문 삽화 figure 수: {editorial_figures} (예상 15)")
        require(len(chapter_images) == 15, f"본문 삽화 img 수: {len(chapter_images)} (예상 15)")
        require(stat_dashboards == 4, f"통계 대시보드 수: {stat_dashboards} (예상 4)")
        require(stat_charts == 5, f"통계 그래프 수: {stat_charts} (예상 5)")
        require(stat_chart_labels == 5, f"통계 그래프 접근성 라벨 수: {stat_chart_labels} (예상 5)")
        require(stat_bar_svgs == 18, f"통계 막대 SVG 수: {stat_bar_svgs} (예상 18)")
        require(stat_hidden_bars == 18, f"보조기기에서 숨긴 장식 막대 수: {stat_hidden_bars} (예상 18)")
        require(
            Counter(stat_values)
            == Counter([13, 99, 58, 75, 16, 84, 24, 45, 20, 28, 34, 31, 7, 8, 44, 40, 4, 4]),
            f"통계 그래프 값 오류: {stat_values}",
        )
        require(not stat_width_errors, f"통계 막대 너비 오류: {stat_width_errors}")
        require(axmm_structures == 1, f"AXMM 전체 구조도 수: {axmm_structures} (예상 1)")
        require(axmm_structure_labels == 1, f"AXMM 구조도 접근성 라벨 수: {axmm_structure_labels} (예상 1)")
        require(axmm_cells == 30, f"AXMM 구조도 문항 셀 수: {axmm_cells} (예상 30)")

        for document, source in chapter_images:
            resolved = posixpath.normpath(
                posixpath.join(str(PurePosixPath(document).parent), source)
            )
            require(resolved in names, f"EPUB 삽화 누락: {document} -> {source}")

        require(
            not responsive_imgs,
            f"EPUB img에 반응형 속성이 남아 있습니다(그림이 빈칸이 됩니다): {responsive_imgs}",
        )

        stylesheets = [name for name in names if name.endswith(".css")]
        css = "\n".join(archive.read(name).decode("utf-8") for name in stylesheets)
        require(".stat-dashboard" in css, "EPUB 통계 그래프 스타일 누락")
        require(".stat-fill--leader" in css, "EPUB 막대 색상 스타일 누락")
        require(".axmm-map-grid" in css, "EPUB AXMM 구조도 스타일 누락")

    if failures:
        print("EPUB 검증 실패:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(
        "EPUB 검증 통과: "
        f"chapters={chapter_count} editorial_figures={editorial_figures} "
        f"embedded_images={len(chapter_images)} stat_dashboards={stat_dashboards} "
        f"stat_charts={stat_charts} stat_bars={stat_bar_svgs} accessibility_labels={stat_chart_labels} "
        f"axmm_structures={axmm_structures} axmm_cells={axmm_cells}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
