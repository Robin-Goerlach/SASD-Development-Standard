#!/usr/bin/env python3
"""Generate or validate the deterministic repository file manifest."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


EXCLUDED_PARTS = {".git", "artifacts", "__pycache__", ".pytest_cache", ".mypy_cache"}
MANIFEST_NAME = "REPOSITORY-MANIFEST.txt"


def entries(repo: Path) -> list[str]:
    result: list[str] = []
    for path in repo.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(repo)
        if relative.name == MANIFEST_NAME:
            continue
        if any(part in EXCLUDED_PARTS for part in relative.parts):
            continue
        result.append(relative.as_posix())
    return sorted(result, key=lambda item: item.casefold())


def rendered(repo: Path) -> str:
    return "\n".join(entries(repo)) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Fail when the committed manifest is stale.")
    mode.add_argument("--write", action="store_true", help="Rewrite the committed manifest.")
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[1]
    manifest = repo / MANIFEST_NAME
    expected = rendered(repo)

    if args.write:
        manifest.write_text(expected, encoding="utf-8")
        print(f"Wrote {MANIFEST_NAME} with {len(entries(repo))} entries")
        return 0

    if not manifest.is_file():
        print(f"FAIL missing {MANIFEST_NAME}")
        return 1
    actual = manifest.read_text(encoding="utf-8")
    if actual != expected:
        actual_set = set(actual.splitlines())
        expected_set = set(expected.splitlines())
        for item in sorted(expected_set - actual_set):
            print(f"MISSING {item}")
        for item in sorted(actual_set - expected_set):
            print(f"STALE   {item}")
        print(f"FAIL {MANIFEST_NAME} is stale; run: python tooling/generate-repository-manifest.py --write")
        return 1

    print(f"OK   {MANIFEST_NAME}: {len(entries(repo))} entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
