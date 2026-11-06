# Build Log: 나는 이 게임을 안다 v1.0.3

- **Date:** 2026-11-07
- **Output:** `나는-이-게임을-안다-v1.0.3.epub` (루트 + `docs/epub/`)
- **Size:** 1562159 bytes
- **Build:** `./scripts/build-site.sh` (build_site → validate_site → build_epub → validate_epub)
- **Site check:** passed (chapters 15, figures 16, internal_links 129, TOC 21/21 링크 해석)
- **EPUB check:** passed (editorial_figures 15, embedded_images 15, stat_dashboards 4, stat_charts 5, axmm_cells 30)
- **epubcheck:** 0 fatal / 0 error / 0 warning
- **Playwright:** 웹·발표 자료 390px·1440px 가로 넘침 0, 오프닝 영상 블록·발표 자료 링크 유지
- **변경:** 1장 소제목 하나를 v1.0.1 문장으로 되돌림, 내용·수치 변경 없음 (`proofread_log.md`).

---

# Build Log — 나는 이 게임을 안다 v1.0.2

- **Date:** 2026-11-07
- **Output:** `나는-이-게임을-안다-v1.0.2.epub` (루트 + `docs/epub/`)
- **Size:** 1562021 bytes
- **Build:** `./scripts/build-site.sh` (build_site → validate_site → build_epub → validate_epub)
- **Site check:** passed (chapters 15, figures 16, internal_links 129, TOC 21/21 링크 해석)
- **EPUB check:** passed (editorial_figures 15, embedded_images 15, stat_dashboards 4, stat_charts 5, axmm_cells 30)
- **epubcheck:** 0 fatal / 0 error / 0 warning
- **Playwright:** 웹·발표 자료 390px·1440px 가로 넘침 0
- **변경:** 문체 2차 점검(한국어 표현 지침), 275곳 정리, 내용·수치 변경 없음 (`proofread_log.md`). 발표 자료·README 문구도 같은 기준으로 정리.

---

# Build Log — 나는 이 게임을 안다 v1.0.1

- **Date:** 2026-11-01
- **Output:** `나는-이-게임을-안다-v1.0.1.epub` (루트 + `docs/epub/`)
- **Size:** 1562008 bytes
- **Build:** `./scripts/build-site.sh` (build_site → validate_site → build_epub → validate_epub), pandoc 3.9.0.2
- **Site check:** passed (chapters 15, figures 16, internal_links 129, TOC 21/21 링크 해석)
- **EPUB check:** passed (editorial_figures 15, embedded_images 15, stat_dashboards 4, stat_charts 5, axmm_cells 30)
- **epubcheck:** 0 fatal / 0 error / 0 warning
- **변경:** 문체 점검 — AI 문체 패턴 109곳 정리, 내용·수치 변경 없음 (`proofread_log.md`). 웹 오프닝 영상 블록을 `site/template.html`로 옮겨 재빌드에도 남게 함.

---

# Build Log — 나는 이 게임을 안다 v1.0.0

- **Date:** 2026-08-16T12:29:18Z
- **Output:** `나는-이-게임을-안다-v1.0.0.epub`
- **Size:** 1659624 bytes
- **Pandoc exit:** 0
- **Archive and metadata check:** passed
- **Embedded chapter illustrations:** 15
- **Statistical dashboards / charts:** 4 / 5
- **AXMM structure diagrams / cells:** 1 / 30
- **epubcheck:** skipped (epubcheck not installed)

## Metadata
- title: 나는 이 게임을 안다
- author: 김상기
- language: ko
- version: 1.0.0
- pub_date: 2026-08-15
