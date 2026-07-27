#!/usr/bin/env python3
"""Generate or check the deterministic SASD prompt catalog and checksums."""

from __future__ import annotations

import argparse
import sys

from prompt_package_common import build_catalog, canonical_json, package_paths, repository_root


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="Write generated catalog files.")
    mode.add_argument("--check", action="store_true", help="Check generated catalog files.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo = repository_root()
    paths = package_paths(repo)
    catalog, markdown, checksums = build_catalog(repo)
    expected = {
        paths["catalog"]: canonical_json(catalog),
        paths["catalog_markdown"]: markdown,
        paths["checksums"]: canonical_json(checksums),
    }
    if args.write:
        for path, content in expected.items():
            path.write_text(content, encoding="utf-8")
            print(f"WROTE {path.relative_to(repo)}")
        return 0
    failures = []
    for path, content in expected.items():
        if not path.is_file():
            failures.append(f"missing generated file: {path.relative_to(repo)}")
        elif path.read_text(encoding="utf-8") != content:
            failures.append(f"outdated generated file: {path.relative_to(repo)}")
    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        print(f"\nPrompt catalog failures: {len(failures)}")
        return 1
    print(f"OK   prompt catalog: {catalog['prompt_count']} prompts")
    print(f"OK   package checksums: {checksums['file_count']} files")
    print("\nPrompt catalog failures: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
