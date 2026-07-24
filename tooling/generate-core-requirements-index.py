#!/usr/bin/env python3
"""Generate the derived Core requirements index.

The generated Markdown file is informative and must not be edited manually.
The script uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIREMENT = re.compile(r"^\|\s*(SASD-(?:QL|LC|REQ|ARCH|DOC|REP|QUAL|SEC|TEST|REL|MNT|KM|AI)-\d{3})\s*\|\s*(.*?)\s*\|\s*$")
CORE_FILES = [
    "QUALITY-LEVELS.md", "PROJECT-LIFECYCLE.md", "REQUIREMENTS.md",
    "ARCHITECTURE.md", "DOCUMENTATION.md", "REPOSITORY.md", "QUALITY.md",
    "SECURITY.md", "TESTING.md", "RELEASES.md", "MAINTENANCE.md",
    "KNOWLEDGE-MANAGEMENT.md", "AI-ASSISTED-DEVELOPMENT.md",
]


def build(repo: Path) -> str:
    core = repo / "docs" / "10-core-standard"
    groups: list[tuple[str, list[tuple[str, str]]]] = []
    total = 0
    for name in CORE_FILES:
        path = core / name
        entries: list[tuple[str, str]] = []
        for line in path.read_text(encoding="utf-8").splitlines():
            match = REQUIREMENT.match(line)
            if match:
                entries.append((match.group(1), match.group(2)))
        total += len(entries)
        groups.append((name, entries))

    out = [
        "---",
        'title: "Core-Anforderungsindex"',
        "document-id: SASD-REF-005",
        "document-type: informative",
        "status: Draft",
        "version: 0.1.0",
        'standard-version: "1.0"',
        "language: de",
        "authoritative: false",
        "owner: SASD Development Standard Maintainer",
        "last-updated: 2026-07-24",
        "applies-to-quality-levels: [Minimum, Recommended, Production]",
        "applies-to-profiles: [Core]",
        "depends-on: [SASD-CORE-001, SASD-CORE-002, SASD-CORE-003, SASD-CORE-004, SASD-CORE-005, SASD-CORE-006, SASD-CORE-007, SASD-CORE-008, SASD-CORE-009, SASD-CORE-010, SASD-CORE-011, SASD-CORE-012, SASD-CORE-013]",
        "normative-keywords: []",
        "generated: true",
        "---",
        "",
        "# Core-Anforderungsindex",
        "",
        "> Automatisch erzeugtes, nicht normatives Navigationsdokument. Änderungen erfolgen in den Quelldokumenten und anschließend über `python tooling/generate-core-requirements-index.py`.",
        "",
        f"Der Index enthält **{total}** Core-Anforderungen.",
        "",
    ]
    for name, entries in groups:
        title = name.removesuffix(".md").replace("-", " ").title()
        out.extend([
            f"## [{title}]({name})",
            "",
            "| ID | Anforderung |",
            "|---|---|",
        ])
        for req_id, statement in entries:
            out.append(f"| `{req_id}` | {statement} |")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    target = repo / "docs" / "10-core-standard" / "CORE-REQUIREMENTS-INDEX.md"
    expected = build(repo)
    if args.check:
        actual = target.read_text(encoding="utf-8") if target.exists() else ""
        if actual != expected:
            print(f"FAIL generated file is outdated: {target.relative_to(repo)}")
            return 1
        print(f"OK   generated file is current: {target.relative_to(repo)}")
        return 0
    target.write_text(expected, encoding="utf-8", newline="\n")
    print(f"Generated {target.relative_to(repo)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
