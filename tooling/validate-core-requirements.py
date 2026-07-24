#!/usr/bin/env python3
"""Validate requirement IDs in the SASD Core Standard.

The script checks that requirement identifiers are unique, use an approved
Core prefix, and that every Core Draft document contains at least one
requirement identifier. It has no external Python dependencies.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

REQUIREMENT = re.compile(r"\b(SASD-(?:QL|LC|REQ|ARCH|DOC|REP|QUAL|SEC|TEST|REL|MNT|KM|AI)-\d{3})\b")
CORE_FILES = {
    "QUALITY-LEVELS.md",
    "PROJECT-LIFECYCLE.md",
    "REQUIREMENTS.md",
    "ARCHITECTURE.md",
    "DOCUMENTATION.md",
    "REPOSITORY.md",
    "QUALITY.md",
    "SECURITY.md",
    "TESTING.md",
    "RELEASES.md",
    "MAINTENANCE.md",
    "KNOWLEDGE-MANAGEMENT.md",
    "AI-ASSISTED-DEVELOPMENT.md",
}


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    core = repo / "docs" / "10-core-standard"
    occurrences: dict[str, list[tuple[Path, int]]] = defaultdict(list)
    failures = 0

    for name in sorted(CORE_FILES):
        path = core / name
        if not path.exists():
            print(f"FAIL missing Core document: {path.relative_to(repo)}")
            failures += 1
            continue

        text = path.read_text(encoding="utf-8")
        found = 0
        for line_no, line in enumerate(text.splitlines(), start=1):
            for requirement_id in REQUIREMENT.findall(line):
                occurrences[requirement_id].append((path, line_no))
                found += 1

        if found == 0:
            print(f"FAIL no requirement IDs: {path.relative_to(repo)}")
            failures += 1
        else:
            print(f"OK   {path.relative_to(repo)}: {found} requirements")

    for requirement_id, locations in sorted(occurrences.items()):
        if len(locations) > 1:
            failures += 1
            formatted = ", ".join(
                f"{path.relative_to(repo)}:{line_no}" for path, line_no in locations
            )
            print(f"FAIL duplicate {requirement_id}: {formatted}")

    print(f"\nValidated {len(occurrences)} unique Core requirement IDs; failures: {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
