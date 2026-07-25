#!/usr/bin/env python3
"""Generate the curated quality-level matrix for operational processes."""

from __future__ import annotations
import argparse
import sys
from pathlib import Path

ROWS = [
    ("Projektklassifikation", "Kompakte begründete Einstufung", "Vollständiges Risikomerkmal- und Artefaktmodell", "Formale Schutzbedarfs- und Betriebsprüfung"),
    ("Projektinitialisierung", "Projektbrief, Baseline, erster Meilenstein", "Getrennte Anforderungen, Architektur, Tests und Wartung", "Formales Readiness Gate mit Security und Betrieb"),
    ("Architekturentscheidungen", "ADRs für zentrale irreversible Entscheidungen", "ADR-Index, Kriterien, Review und Folgemaßnahmen", "Unabhängige Fachprüfung kritischer Entscheidungen"),
    ("Reviews", "Strukturierter Selbstreview und Automatisierung", "Peer- oder zeitlich getrennter Review mit Finding-Tracking", "Unabhängige Spezialreviews und formale Freigabe"),
    ("Legacy-Migration", "Baseline, Sicherung und wenige reversible Schritte", "Assessment, Backlog, Wellen und Regressionstests", "Formale Daten-, Rollback- und Betriebsübergabe"),
    ("Releases", "Version, sauberer Build, Kerntests und Smoke-Test", "Readiness-Nachweis, Prüfsummen, Upgradehinweise", "Signierung/Integrität, formale Freigabe und Überwachung"),
    ("Archivierung", "Statushinweis, letzter Stand, Daten- und Zugangsbereinigung", "Inventar, Kommunikation, Wissens- und Infrastrukturabschluss", "Formale Daten-/Security-Freigabe und Wiederherstellungskonzept"),
]


def build() -> str:
    lines = [
        "---", 'title: "Qualitätsstufenmatrix der operativen Prozesse"', "document-id: SASD-REF-PROC-004",
        "document-type: informative", "status: Draft", "version: 0.9.0", 'standard-version: "1.0"',
        "language: de", "authoritative: false", "owner: SASD Development Standard Maintainer",
        "last-updated: 2026-07-24", "applies-to-quality-levels: [Minimum, Recommended, Production]",
        "applies-to-profiles: [Core, DotNet, Desktop]",
        "depends-on: [SASD-PROC-001, SASD-PROC-002, SASD-PROC-003, SASD-PROC-004, SASD-PROC-005, SASD-PROC-006, SASD-PROC-007]",
        "---", "", "# Qualitätsstufenmatrix der operativen Prozesse", "",
        "Diese erzeugte Übersicht ersetzt nicht die normativen Prozessdokumente.", "",
        "| Prozess | Minimum | Recommended | Production |", "|---|---|---|---|",
    ]
    lines.extend(f"| {a} | {b} | {c} | {d} |" for a, b, c, d in ROWS)
    lines += ["", "## Interpretationshinweise", "",
              "- Recommended ist der Normalfall für dauerhaft gepflegte SASD-Projekte.",
              "- Ein kleines Projekt kann aufgrund von Daten-, Security- oder Betriebsrisiken Production-Tiefe benötigen.",
              "- Artefakte dürfen proportional zusammengeführt werden, solange Entscheidungen und Nachweise auffindbar bleiben.",
              "- Profile dürfen strengere oder technologiespezifische Prozessschritte ergänzen."]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    target = repo / "docs" / "30-processes" / "PROCESS-QUALITY-LEVEL-MATRIX.md"
    generated = build()
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
