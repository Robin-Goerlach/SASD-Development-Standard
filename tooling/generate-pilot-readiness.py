#!/usr/bin/env python3
"""Generate Version 1.0 pilot-readiness evidence from pilot manifests."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

DATE = "2026-07-25"
VERSION = "0.11.0"
SIZE_LABELS = {
    "Small": "kleines Werkzeug",
    "Medium": "mittlere Desktopanwendung",
    "Large": "komplexere geschichtete Anwendung",
}


def technical_state(data: dict) -> str:
    implementation = data.get("implementation_state", "Not Started")
    verification = data.get("verification_state", "Pending")
    if implementation == "Not Started":
        return "Umsetzung nicht begonnen"
    if implementation == "Artifact Prepared":
        return "Artefakt vorbereitet; technische Verifikation ausstehend"
    if implementation == "Committed" and verification != "Passed":
        return "Zielstand committed; Verifikation ausstehend"
    if implementation == "Verified" and verification == "Passed":
        return "technisch verifiziert"
    return f"{implementation}; {verification}"


def render(repo: Path) -> str:
    base = repo / "docs/50-reference-implementations"
    manifests = [json.loads(path.read_text(encoding="utf-8")) for path in sorted(base.glob("pilot-*/pilot.json"))]
    by_size = {item.get("project_size"): item for item in manifests}
    rows: list[str] = []
    for size in ("Small", "Medium", "Large"):
        item = by_size.get(size)
        if item is None:
            rows.append(f"| {SIZE_LABELS[size]} | — | fehlt | fehlt |")
            continue
        rows.append(
            f'| {SIZE_LABELS[size]} | {item["title"]} | {item["status"]} | {technical_state(item)} |'
        )

    assessed = sum(item.get("status") in {"Baseline Assessed", "Wave Planned", "In Execution", "Wave Validated", "Pilot Closed"} for item in manifests)
    verified = sum(item.get("verification_state") == "Passed" for item in manifests)
    body = [
        "---",
        'title: "Pilot-Readiness für Version 1.0"',
        "document-id: SASD-REF-PILOT-007",
        "document-type: informative",
        "status: Draft",
        f"version: {VERSION}",
        'standard-version: "1.0"',
        "language: de",
        "authoritative: false",
        "owner: SASD Development Standard Maintainer",
        f"last-updated: {DATE}",
        "applies-to-quality-levels: [Recommended, Production]",
        "applies-to-profiles: [Core, DotNet, Desktop]",
        "depends-on: [SASD-FND-007, SASD-REF-PILOT-001, SASD-REF-PILOT-002, SASD-REF-PILOT-003]",
        "---",
        "",
        "# Pilot-Readiness für Version 1.0",
        "",
        "Diese Datei wird deterministisch aus den Pilotmanifesten erzeugt.",
        "",
        "## Abdeckung",
        "",
        "| Erforderliche Kategorie | Pilot | Bewertungszustand | Technischer Zustand |",
        "|---|---|---|---|",
        *rows,
        "",
        "## Zusammenfassung",
        "",
        f"- registrierte Piloten: **{len(manifests)}**",
        f"- mindestens als Baseline bewertet: **{assessed}**",
        f"- technisch mit `Passed` verifiziert: **{verified}**",
        "- abgedeckte Größenklassen: **" + ", ".join(size for size in ("Small", "Medium", "Large") if size in by_size) + "**",
        "",
        "## Bewertung",
        "",
        "Die strukturelle Größenabdeckung aus `SASD-FND-007` ist hergestellt, wenn Small, Medium und Large vorhanden sind. "
        "Dies ist ein Portfolio- und Dokumentationsnachweis, kein Build-, Test-, Laufzeit- oder CI-Nachweis der Ziel-Repositories.",
        "",
        "## Release-Bedeutung",
        "",
        "Für einen Release Candidate ist mindestens ein praktisch ausgeführter und überprüfter Pilotdurchlauf weiterhin erforderlich. "
        "Für die stabile Version 1.0 sollen alle drei Baselines gegen konkrete Commits bestätigt und die wesentlichen Erkenntnisse konsolidiert werden.",
        "",
        "## Offene Pilot-Blocker",
        "",
        "1. TaskHost Local Wave 01 im Ziel-Repository committen und verifizieren.",
        "2. Prompt Manager Baseline in einem lokalen Clone bestätigen und Wave 01 ausführen.",
        "3. Mail Workbench Baseline in einem lokalen Clone bestätigen und Wave 01 ausführen.",
        "4. gemeinsame Lessons Learned und Standardänderungsbedarf konsolidieren.",
        "",
    ]
    return "\n".join(body)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    target = repo / "docs/50-reference-implementations/VERSION-1.0-PILOT-READINESS.md"
    generated = render(repo)
    if args.check:
        if not target.exists() or target.read_text(encoding="utf-8") != generated:
            print("FAIL Version 1.0 pilot readiness is not current")
            return 1
        print("OK   Version 1.0 pilot readiness is current")
        return 0
    target.write_text(generated, encoding="utf-8", newline="\n")
    print(f"Wrote {target.relative_to(repo)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
