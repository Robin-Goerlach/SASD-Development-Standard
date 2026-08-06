#!/usr/bin/env python3
"""Validate repository layout and dependency-free text-file hygiene."""

from __future__ import annotations

import sys
from pathlib import Path


TEXT_SUFFIXES = {
    ".json", ".md", ".props", ".ps1", ".py", ".sh", ".template", ".txt", ".yaml", ".yml"
}
IGNORED_PARTS = {".git", "artifacts", "__pycache__", ".pytest_cache", ".mypy_cache"}
FORBIDDEN_NAMES = {".DS_Store", "Thumbs.db", "Desktop.ini"}


def is_text_file(path: Path) -> bool:
    return path.suffix.lower() in TEXT_SUFFIXES or path.name.endswith((".csproj.template", ".yml.template"))


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    failures: list[str] = []

    nested_root = repo / "SASD-Development-Standard"
    if nested_root.exists():
        failures.append("unexpected nested repository directory: SASD-Development-Standard/")

    for path in sorted(repo.rglob("*")):
        relative = path.relative_to(repo)
        if any(part in IGNORED_PARTS for part in relative.parts):
            continue
        if path.is_symlink():
            failures.append(f"symbolic links are not allowed in the baseline repository: {relative}")
            continue
        if not path.is_file():
            continue
        if path.name in FORBIDDEN_NAMES or path.suffix.lower() == ".pyc":
            failures.append(f"forbidden generated or operating-system file: {relative}")
            continue
        if not is_text_file(path):
            continue

        raw = path.read_bytes()
        if b"\r" in raw:
            failures.append(f"non-LF line ending in text file: {relative}")
        if raw.startswith(b"\xef\xbb\xbf"):
            failures.append(f"UTF-8 BOM is not allowed: {relative}")
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError as error:
            failures.append(f"file is not valid UTF-8: {relative}: {error}")
            continue
        if text and not text.endswith("\n"):
            failures.append(f"text file has no final newline: {relative}")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if line.rstrip(" \t") != line:
                failures.append(f"trailing whitespace: {relative}:{line_number}")
            if "\t" in line and path.suffix.lower() in {".json", ".md", ".py", ".yaml", ".yml"}:
                failures.append(f"tab character in structured text: {relative}:{line_number}")

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        print(f"\nRepository hygiene failures: {len(failures)}")
        return 1

    print("OK   repository root is not duplicated")
    print("OK   no forbidden generated files or symbolic links")
    print("OK   checked text files are UTF-8 with LF endings and final newlines")
    print("OK   no trailing whitespace or structured-text tabs")
    print("\nRepository hygiene failures: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
