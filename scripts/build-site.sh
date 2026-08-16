#!/usr/bin/env bash
set -euo pipefail

ax_repo_root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$ax_repo_root"

python3 scripts/build_site.py
python3 scripts/validate_site.py
python3 scripts/build_epub.py
python3 scripts/validate_epub.py
