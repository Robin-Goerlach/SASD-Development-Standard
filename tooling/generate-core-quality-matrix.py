#!/usr/bin/env python3
"""Generate a consolidated, informative Core quality-level matrix."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

CORE_FILES = [
    "QUALITY-LEVELS.md", "PROJECT-LIFECYCLE.md", "REQUIREMENTS.md",
    "ARCHITECTURE.md", "DOCUMENTATION.md", "REPOSITORY.md", "QUALITY.md",
    "SECURITY.md", "TESTING.md", "RELEASES.md", "MAINTENANCE.md",
    "KNOWLEDGE-MANAGEMENT.md", "AI-ASSISTED-DEVELOPMENT.md",
]


def title_from_front_matter(text: str) -> str:
    match = re.search(r'^title:\s*"?(.*?)"?$', text, re.MULTILINE)
    return match.group(1) if match else "Core document"


def quality_rows(text: str) -> list[tuple[str, str, str, str]]:
    lines = text.splitlines()
    rows: list[tuple[str, str, str, str]] = []
    in_table = False
    for line in lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) == 4 and cells[1:] == ["Minimum", "Recommended", "Production"]:
            in_table = True
            continue
        if in_table and re.fullmatch(r"[:\- ]+", "".join(cells)):
            continue
        if in_table:
            if not line.startswith("|") or len(cells) != 4:
                in_table = False
                continue
            rows.append(tuple(cells))
    return rows


def build(repo: Path) -> str:
    core = repo / "docs" / "10-core-standard"
    sections: list[tuple[str, str, list[tuple[str, str, str, str]]]] = []
    count = 0
    for name in CORE_FILES:
        text = (core / name).read_text(encoding="utf-8")
        rows = quality_rows(text)
        count += len(rows)
        sections.append((name, title_from_front_matter(text), rows))

    out = [
        "---",
        'title: "Konsolidierte Qualitätsstufenmatrix"',
        "document-id: SASD-REF-006",
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
        "# Konsolidierte Qualitätsstufenmatrix",
        "",
        "> Automatisch erzeugte, nicht normative Vergleichsansicht. Maßgeblich bleiben die jeweiligen Core-Dokumente. Aktualisierung: `python tooling/generate-core-quality-matrix.py`.",
        "",
        f"Die Übersicht konsolidiert **{count}** Maßnahmen aus den Qualitätsstufentabellen.",
        "",
    ]
    for name, title, rows in sections:
        out.extend([
            f"## [{title}]({name})",
            "",
            "| Maßnahme oder Artefakt | Minimum | Recommended | Production |",
            "|---|---|---|---|",
        ])
        if rows:
            for cells in rows:
                out.append("| " + " | ".join(cells) + " |")
        else:
            out.append("| Keine eigene Matrix erkannt | — | — | — |")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    target = repo / "docs" / "10-core-standard" / "CORE-QUALITY-LEVEL-MATRIX.md"
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
