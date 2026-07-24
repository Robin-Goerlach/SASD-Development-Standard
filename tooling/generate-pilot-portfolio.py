#!/usr/bin/env python3
"""Generate the reference pilot portfolio from pilot.json manifests."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

DATE = "2026-07-24"
VERSION = "0.7.0"


def render(repo: Path) -> str:
    base = repo / "docs" / "50-reference-implementations"
    manifests = sorted(base.glob("pilot-*/pilot.json"))
    rows = []
    for path in manifests:
        data = json.loads(path.read_text(encoding="utf-8"))
        rel_readme = path.parent.relative_to(base).as_posix() + "/README.md"
        profiles = ", ".join(data["profiles"])
        rows.append(
            f'| {data["pilot_id"]} | [{data["title"]}]({rel_readme}) | '
            f'{data["category"]} | {data["quality_level"]} | {profiles} | {data["status"]} |'
        )

    body = [
        "---",
        'title: "Pilotportfolio für Version 1.0"',
        "document-id: SASD-REF-PILOT-003",
        "document-type: informative",
        "status: Draft",
        f"version: {VERSION}",
        'standard-version: "1.0"',
        "language: de",
        "authoritative: false",
        "owner: SASD Development Standard Maintainer",
        f"last-updated: {DATE}",
        "applies-to-quality-levels: [Minimum, Recommended, Production]",
        "applies-to-profiles: [Core, DotNet, Desktop]",
        "depends-on: [SASD-REF-PILOT-001, SASD-REF-PILOT-002]",
        "---",
        "",
        "# Pilotportfolio für Version 1.0",
        "",
        "Diese Datei wird aus den `pilot.json`-Manifesten erzeugt.",
        "",
        "| Pilot-ID | Pilot | Kategorie | Qualitätsstufe | Profile | Status |",
        "|---|---|---|---|---|---|",
    ]
    body.extend(rows or ["| — | Noch kein Pilot registriert | — | — | — | — |"])
    body += [
        "",
        "## Statushinweis",
        "",
        "`Wave Planned` bedeutet, dass Klassifikation, Assessment und Wellenplan vorliegen. Es bedeutet nicht, dass Änderungen im Ziel-Repository bereits ausgeführt wurden.",
        "",
    ]
    return "\n".join(body)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    target = repo / "docs" / "50-reference-implementations" / "PILOT-PORTFOLIO.md"
    generated = render(repo)
    if args.check:
        current = target.read_text(encoding="utf-8") if target.exists() else ""
        if current != generated:
            print("FAIL pilot portfolio is not current")
            return 1
        print("OK   pilot portfolio is current")
        return 0
    target.write_text(generated, encoding="utf-8", newline="\n")
    print(f"Wrote {target.relative_to(repo)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
