#!/usr/bin/env python3
"""Build the EPUB from the synchronized manuscript and local book assets."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

# 원고의 <img>는 웹용 반응형 속성을 달고 있다. pandoc은 src만 EPUB 안의
# 경로로 고쳐 쓰고 srcset은 손대지 않는데, 리더는 srcset을 우선한다.
# 그러면 EPUB에 없는 경로를 가리켜 그림이 통째로 빈칸이 된다. HTML 규칙상
# srcset 후보가 없으면 src로 되돌아가지 않으므로 EPUB에서는 걷어낸다.
RESPONSIVE_IMG_ATTRS = re.compile(r'\s+(?:srcset|sizes)="[^"]*"')


def main() -> int:
    pandoc = shutil.which("pandoc")
    if not pandoc:
        print("pandoc을 찾을 수 없습니다.", file=sys.stderr)
        return 1

    manifest_path = ROOT / "book_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    version = manifest["version"]
    destination = ROOT / f"나는-이-게임을-안다-v{version}.epub"

    manuscript = ROOT / "04_manuscript.md"
    cover = ROOT / manifest["cover_image"]
    stylesheet = ROOT / "site/epub.css"
    required = [manuscript, manifest_path, cover, stylesheet]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
    if missing:
        print(f"EPUB 입력 파일이 없습니다: {', '.join(missing)}", file=sys.stderr)
        return 1

    temp_dir = Path(tempfile.mkdtemp(prefix=".epub-build-", dir=ROOT))
    output_path = temp_dir / destination.name

    epub_manuscript = temp_dir / "manuscript-for-epub.md"
    source = manuscript.read_text(encoding="utf-8")
    stripped, removed = RESPONSIVE_IMG_ATTRS.subn("", source)
    if not removed:
        print("반응형 이미지 속성을 찾지 못했습니다. 원고 형식이 바뀐 것 같습니다.", file=sys.stderr)
        shutil.rmtree(temp_dir, ignore_errors=True)
        return 1
    epub_manuscript.write_text(stripped, encoding="utf-8")

    resource_path = os.pathsep.join((str(ROOT), str(ROOT / "docs")))
    command = [
        pandoc,
        str(epub_manuscript),
        "--from=markdown+smart",
        "--to=epub3",
        f"--metadata-file={manifest_path}",
        f"--epub-cover-image={cover}",
        f"--resource-path={resource_path}",
        f"--css={stylesheet}",
        "--toc",
        f"--output={output_path}",
    ]

    try:
        subprocess.run(
            command,
            cwd=ROOT,
            check=True,
            env={**os.environ, "LC_ALL": "C.UTF-8"},
        )
        output_path.replace(destination)
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

    print(f"생성 완료: {destination.relative_to(ROOT)} ({destination.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
