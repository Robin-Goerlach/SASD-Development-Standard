#!/usr/bin/env python3
"""Check relative Markdown links in the SASD Development Standard repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
SKIPPED_PREFIXES = ("http://", "https://", "mailto:", "tel:", "#")


def clean_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    # Optional Markdown title: (path "title")
    if " " in target and not target.startswith(("http://", "https://")):
        target = target.split(" ", 1)[0]
    return unquote(target.split("#", 1)[0])


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    markdown_files = sorted(repo.rglob("*.md"))
    failures = 0
    checked = 0

    for source in markdown_files:
        text = source.read_text(encoding="utf-8")
        for line_no, line in enumerate(text.splitlines(), start=1):
            for match in LINK_PATTERN.finditer(line):
                raw = match.group(1).strip()
                if raw.startswith(SKIPPED_PREFIXES):
                    continue
                target = clean_target(raw)
                if not target:
                    continue
                checked += 1
                resolved = (source.parent / target).resolve()
                try:
                    resolved.relative_to(repo.resolve())
                except ValueError:
                    print(f"FAIL {source.relative_to(repo)}:{line_no}: link leaves repository: {raw}")
                    failures += 1
                    continue
                if not resolved.exists():
                    print(f"FAIL {source.relative_to(repo)}:{line_no}: missing target: {raw}")
                    failures += 1

    print(f"Checked {checked} relative Markdown links; failures: {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
