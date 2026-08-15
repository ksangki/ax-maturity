#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  AUTO_IMPROVE_HOME=/path/to/auto-improve \
  GEMINI_API_KEY=... \
  scripts/run_auto_improve_book.sh <chapter.md> <tag> [max-iterations]

Example:
  AUTO_IMPROVE_HOME=../auto-improve \
  GEMINI_API_KEY=... \
  scripts/run_auto_improve_book.sh chapters/04_draft.md ch04-pilot 4
EOF
}

if [[ $# -lt 2 || $# -gt 3 ]]; then
  usage >&2
  exit 2
fi

artifact="$1"
tag="$2"
max_iterations="${3:-4}"

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

if [[ ! -f "$artifact" ]]; then
  echo "artifact not found: $artifact" >&2
  exit 2
fi

: "${AUTO_IMPROVE_HOME:?Set AUTO_IMPROVE_HOME to a crimeacs/auto-improve checkout}"
: "${GEMINI_API_KEY:=${GOOGLE_API_KEY:-}}"
if [[ -z "$GEMINI_API_KEY" ]]; then
  echo "Set GEMINI_API_KEY or GOOGLE_API_KEY" >&2
  exit 2
fi

upstream="$AUTO_IMPROVE_HOME/improve.py"
if [[ ! -f "$upstream" ]]; then
  echo "upstream improve.py not found: $upstream" >&2
  exit 2
fi

runtime_dir="${TMPDIR:-/tmp}/ax-book-auto-improve"
runtime="$runtime_dir/improve_book.py"
mkdir -p "$runtime_dir"
python3 scripts/patch_auto_improve_for_book.py "$upstream" "$runtime"

export GEMINI_API_KEY
export IMPROVE_ARTIFACT_CHARS="${IMPROVE_ARTIFACT_CHARS:-24000}"
export IMPROVE_CRITERIA_CHARS="${IMPROVE_CRITERIA_CHARS:-8000}"

# Keep the upstream defaults unless the caller deliberately chooses two models.
# The patched runtime uses IMPROVE_EVALUATOR for rubric scoring and pairwise judging.
export IMPROVE_MUTATOR="${IMPROVE_MUTATOR:-gemini-flash-latest}"
export IMPROVE_EVALUATOR="${IMPROVE_EVALUATOR:-gemini-flash-latest}"

python3 "$runtime" \
  --artifact "$artifact" \
  --criteria criteria/ax-book-quality.md \
  --tag "$tag" \
  --max-iterations "$max_iterations" \
  --candidates "${IMPROVE_CANDIDATES:-3}" \
  --eval-runs "${IMPROVE_EVAL_RUNS:-2}" \
  --threshold "${IMPROVE_THRESHOLD:-92}"

cat <<EOF

Review only the verified branch diff before merging:
  git diff main...improve/$tag -- $artifact
  python3 $runtime --status --tag $tag

Then rebuild and validate the book:
  bash scripts/build-site.sh
  python3 scripts/validate_site.py
EOF
