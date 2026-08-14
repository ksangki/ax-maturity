#!/usr/bin/env python3
"""Build the GitHub Pages book from the reviewed Markdown chapters."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = (
    "chapters/00_intro_draft.md",
    "chapters/00_opening_draft.md",
    *(f"chapters/{number:02d}_draft.md" for number in range(1, 16)),
    "chapters/99_epilogue_draft.md",
    "chapters/A1_appendix_a_draft.md",
    "chapters/A2_appendix_b_draft.md",
    "chapters/A3_appendix_c_draft.md",
)


def strip_front_matter(markdown: str, source: Path) -> str:
    lines = markdown.splitlines()
    if not lines or lines[0].strip() != "---":
        return markdown.rstrip() + "\n"

    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return "\n".join(lines[index + 1 :]).rstrip() + "\n"
    raise ValueError(f"닫히지 않은 YAML front matter: {source}")


def main() -> int:
    pandoc = shutil.which("pandoc")
    if not pandoc:
        print("pandoc을 찾을 수 없습니다.", file=sys.stderr)
        return 1

    sources = [ROOT / relative for relative in CHAPTERS]
    missing = [str(path.relative_to(ROOT)) for path in sources if not path.is_file()]
    if missing:
        print(f"원고 파일이 없습니다: {', '.join(missing)}", file=sys.stderr)
        return 1

    combined = "\n\n".join(
        strip_front_matter(path.read_text(encoding="utf-8"), path)
        for path in sources
    )

    temp_dir = Path(tempfile.mkdtemp(prefix=".site-build-", dir=ROOT))
    combined_path = temp_dir / "book.md"
    output_path = temp_dir / "index.html"
    combined_path.write_text(combined, encoding="utf-8")

    command = [
        pandoc,
        str(combined_path),
        "--from=markdown+smart",
        "--to=html5",
        "--standalone",
        f"--template={ROOT / 'site/template.html'}",
        f"--metadata-file={ROOT / 'site/metadata.yaml'}",
        "--wrap=auto",
        f"--output={output_path}",
    ]

    try:
        subprocess.run(
            command,
            cwd=ROOT,
            check=True,
            env={**os.environ, "LC_ALL": "C.UTF-8"},
        )
        destination = ROOT / "docs/index.html"
        destination.parent.mkdir(parents=True, exist_ok=True)
        output_path.replace(destination)
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

    print(f"생성 완료: {destination.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
