#!/usr/bin/env python3
"""Generate the reference pilot portfolio from pilot.json manifests."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

DATE = "2026-07-25"
VERSION = "0.11.0"


def render(repo: Path) -> str:
    base = repo / "docs" / "50-reference-implementations"
    manifests = sorted(base.glob("pilot-*/pilot.json"))
    rows: list[str] = []
    for path in manifests:
        data = json.loads(path.read_text(encoding="utf-8"))
        rel = path.parent.relative_to(base).as_posix() + "/README.md"
        profiles = ", ".join(data["profiles"])
        rows.append(
            f'| {data["pilot_id"]} | [{data["title"]}]({rel}) | {data["project_size"]} | '
            f'{data["category"]} | {data["quality_level"]} | {profiles} | {data["status"]} | '
            f'{data.get("implementation_state", "—")} | {data.get("verification_state", "—")} |'
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
        "Diese Datei wird deterministisch aus den `pilot.json`-Manifesten erzeugt.",
        "",
        "| Pilot-ID | Pilot | Größe | Kategorie | Qualitätsstufe | Profile | Lebenszyklus | Umsetzung | Verifikation |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    body.extend(rows or ["| — | Noch kein Pilot registriert | — | — | — | — | — | — | — |"])
    body += [
        "",
        "## Statushinweis",
        "",
        "`Baseline Assessed` bestätigt eine dokumentierte Ausgangsbewertung, aber keinen lokalen Build oder Laufzeittest. "
        "`Artifact Prepared` bestätigt ein geprüftes Updateartefakt, nicht dessen Integration. "
        "`Pending` blockiert die Aussagen `Wave Validated` und `Pilot Closed`.",
        "",
    ]
    return "\n".join(body)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    target = repo / "docs/50-reference-implementations/PILOT-PORTFOLIO.md"
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
