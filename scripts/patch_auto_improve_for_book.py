#!/usr/bin/env python3
"""Patch a pinned auto-improve checkout for long-form book chapters.

The upstream tool intentionally optimizes compact text artifacts and truncates the
artifact in several evaluator/mutator prompts. AX book chapters are longer, so this
script creates a runtime copy with larger prompt windows and routes rubric scoring
through the evaluator model as well as the final pairwise gate.

It never modifies the upstream checkout in place.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected 1 occurrence, found {count}")
    return text.replace(old, new, 1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="path to upstream improve.py")
    parser.add_argument("output", help="path for patched runtime improve_book.py")
    args = parser.parse_args()

    src = pathlib.Path(args.source)
    out = pathlib.Path(args.output)
    text = src.read_text(encoding="utf-8")

    marker = 'EVALUATOR_MODEL = os.environ.get("IMPROVE_EVALUATOR", "gemini-flash-latest")\n'
    text = replace_once(
        text,
        marker,
        marker
        + '\nBOOK_ARTIFACT_CHARS = int(os.environ.get("IMPROVE_ARTIFACT_CHARS", "24000"))\n'
        + 'BOOK_CRITERIA_CHARS = int(os.environ.get("IMPROVE_CRITERIA_CHARS", "8000"))\n',
        "context constants",
    )

    replacements = {
        "{artifact_content[:12000]}": "{artifact_content[:BOOK_ARTIFACT_CHARS]}",
        "{artifact_content[:8000]}": "{artifact_content[:BOOK_ARTIFACT_CHARS]}",
        "{artifact_content[:6000]}": "{artifact_content[:BOOK_ARTIFACT_CHARS]}",
        "{first_text[:8000]}": "{first_text[:BOOK_ARTIFACT_CHARS]}",
        "{second_text[:8000]}": "{second_text[:BOOK_ARTIFACT_CHARS]}",
        "{criteria_content[:3000]}": "{criteria_content[:BOOK_CRITERIA_CHARS]}",
        "{criteria_content[:2000]}": "{criteria_content[:BOOK_CRITERIA_CHARS]}",
        "{criteria_content[:1500]}": "{criteria_content[:BOOK_CRITERIA_CHARS]}",
        "{criteria[:2500]}": "{criteria[:BOOK_CRITERIA_CHARS]}",
    }
    for old, new in replacements.items():
        if old not in text:
            raise RuntimeError(f"upstream shape changed; missing token: {old}")
        text = text.replace(old, new)

    # Upstream evaluate_once() calls llm_call(), which selects IMPROVE_MUTATOR.
    # Keep candidate generation on the mutator, but make numeric rubric scoring use
    # the same evaluator path as the final pairwise gate.
    pattern = re.compile(
        r"    response = llm_call\(prompt, temperature=0\.0\)  # deterministic\n"
        r"    if not response:\n"
        r"        return 0, \"\{\}\"\n\n"
        r"    text = response\.strip\(\)\n"
        r"    if text\.startswith\(\"```\"\):\n"
        r"        text = \"\\n\"\.join\(text\.split\(\"\\n\"\)\[1:\]\)\n"
        r"    if text\.endswith\(\"```\"\):\n"
        r"        text = text\[:-3\]\.strip\(\)\n\n"
        r"    try:\n"
        r"        data = json\.loads\(text\)\n"
        r"        return int\(data\.get\(\"total_score\", 0\)\), json\.dumps\(data, indent=2\)\n"
        r"    except Exception:\n"
        r"        m = re\.search\(r'\"total_score\"\\s\*:\\s\*\(\\d\+\)', text\)\n"
        r"        if m:\n"
        r"            return int\(m\.group\(1\)\), text\n"
        r"        return 0, text\[:500\]\n"
    )

    # The exact regex above is intentionally strict, but keep a simpler anchored
    # fallback for harmless upstream formatting changes.
    match = pattern.search(text)
    if match:
        text = text[: match.start()] + (
            '    data = _gemini_json(prompt)\n'
            '    if not data:\n'
            '        return 0, "{}"\n'
            '    return int(data.get("total_score", 0)), json.dumps(data, indent=2, ensure_ascii=False)\n'
        ) + text[match.end() :]
    else:
        start = text.find("    response = llm_call(prompt, temperature=0.0)  # deterministic", text.find("def evaluate_once"))
        end = text.find("\n\n\ndef evaluate(", start)
        if start < 0 or end < 0:
            raise RuntimeError("evaluate_once shape changed; refusing a partial patch")
        text = text[:start] + (
            '    data = _gemini_json(prompt)\n'
            '    if not data:\n'
            '        return 0, "{}"\n'
            '    return int(data.get("total_score", 0)), json.dumps(data, indent=2, ensure_ascii=False)'
        ) + text[end:]

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"patched runtime: {out}")
    print("artifact chars:", 24000)
    print("criteria chars:", 8000)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"patch failed: {exc}", file=sys.stderr)
        raise SystemExit(2)
