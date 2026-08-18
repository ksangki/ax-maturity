#!/usr/bin/env python3
"""site/cover.html을 cover.png로 렌더한다.

표지가 한 번 그려진 뒤 아무도 다시 손대지 못하는 이미지가 되지 않도록,
디자인을 HTML로 두고 이 스크립트가 렌더만 맡는다. 표지를 고치려면
site/cover.html을 고치고 이 스크립트를 다시 돌리면 된다.

build-site.sh에는 넣지 않았다. 표지는 원고가 바뀔 때마다 다시 그릴
대상이 아니고, Playwright는 이 저장소의 다른 어떤 것도 요구하지 않는
무거운 의존성이다.

    pip install playwright && playwright install chromium
    python3 scripts/build_cover.py
"""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "site/cover.html"
OUTPUT = ROOT / "cover.png"
WIDTH, HEIGHT = 1600, 2560


def main() -> int:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print(
            "Playwright가 필요하다:\n"
            "  pip install playwright && playwright install chromium",
            file=sys.stderr,
        )
        return 1

    if not SOURCE.is_file():
        print(f"표지 원본이 없다: {SOURCE.relative_to(ROOT)}", file=sys.stderr)
        return 1

    with sync_playwright() as play:
        browser = play.chromium.launch()
        page = browser.new_page(viewport={"width": WIDTH, "height": HEIGHT})
        page.goto(SOURCE.as_uri(), wait_until="load")
        page.wait_for_timeout(600)  # 웹폰트가 아니라 시스템 폰트라 짧게 족하다

        # 본문이 넘치면 잘린 표지가 조용히 만들어진다. 렌더 전에 막는다.
        overflow = page.evaluate("document.body.scrollHeight")
        if overflow > HEIGHT:
            print(
                f"표지 내용이 {overflow}px로 {HEIGHT}px를 넘는다. "
                "site/cover.html의 크기를 줄여야 한다.",
                file=sys.stderr,
            )
            browser.close()
            return 1

        page.screenshot(path=str(OUTPUT))
        browser.close()

    print(f"생성 완료: {OUTPUT.relative_to(ROOT)} ({OUTPUT.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
