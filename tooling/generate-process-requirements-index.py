#!/usr/bin/env python3
"""Generate an index of all normative operational-process requirements."""

from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

FILES = [
    "NEW-PROJECT.md",
    "PROJECT-CLASSIFICATION.md",
    "ARCHITECTURE-DECISION-PROCESS.md",
    "REVIEW-PROCESS.md",
    "LEGACY-MIGRATION.md",
    "RELEASE-PROCESS.md",
    "PROJECT-ARCHIVAL.md",
]
ROW = re.compile(r"^\|\s*(SASD-PROC-REQ-\d{3})\s*\|\s*(.*?)\s*\|\s*$")
TITLE = re.compile(r'^title:\s*"?(.*?)"?\s*$', re.MULTILINE)


def build(repo: Path) -> str:
    folder = repo / "docs" / "30-processes"
    rows = []
    counts = []
    for name in FILES:
        text = (folder / name).read_text(encoding="utf-8")
        title = TITLE.search(text).group(1)
        found = []
        for line in text.splitlines():
            match = ROW.match(line)
            if match:
                found.append((match.group(1), match.group(2)))
        counts.append((title, name, len(found)))
        rows.extend((rid, statement, title, name) for rid, statement in found)
    lines = [
        "---",
        'title: "Index der Prozessanforderungen"',
        "document-id: SASD-REF-PROC-003",
        "document-type: informative",
        "status: Draft",
        "version: 0.9.0",
        'standard-version: "1.0"',
        "language: de",
        "authoritative: false",
        "owner: SASD Development Standard Maintainer",
        "last-updated: 2026-07-24",
        "applies-to-quality-levels: [Minimum, Recommended, Production]",
        "applies-to-profiles: [Core, DotNet, Desktop]",
        "depends-on: [SASD-PROC-001, SASD-PROC-002, SASD-PROC-003, SASD-PROC-004, SASD-PROC-005, SASD-PROC-006, SASD-PROC-007]",
        "---",
        "",
        "# Index der Prozessanforderungen",
        "",
        "Diese Datei wird aus den normativen Prozessdokumenten erzeugt und nicht manuell bearbeitet.",
        "",
        "## Umfang",
        "",
        "| Dokument | Anforderungen |",
        "|---|---:|",
    ]
    lines.extend(f"| [{title}]({name}) | {count} |" for title, name, count in counts)
    lines += ["", f"**Gesamt:** {len(rows)} Anforderungen", "", "## Anforderungen", "", "| ID | Anforderung | Quelle |", "|---|---|---|"]
    lines.extend(f"| {rid} | {statement} | [{title}]({name}) |" for rid, statement, title, name in rows)
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    target = repo / "docs" / "30-processes" / "PROCESS-REQUIREMENTS-INDEX.md"
    generated = build(repo)
    if args.check:
        if not target.exists() or target.read_text(encoding="utf-8") != generated:
            print(f"FAIL generated file is stale: {target.relative_to(repo)}")
            return 1
        print(f"OK   generated file is current: {target.relative_to(repo)}")
        return 0
    target.write_text(generated, encoding="utf-8", newline="\n")
    print(f"Generated {target.relative_to(repo)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
