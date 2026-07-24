---
title: "Pilot 01 Gap Register – SASD TaskHost Local"
document-id: SASD-REF-PILOT-105
document-type: informative
status: Draft
version: 0.7.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-REF-PILOT-104, SASD-GOV-006, SASD-GOV-007]
---

# Gap Register – SASD TaskHost Local

## Statuslegende

- `Open`: noch nicht begonnen
- `In Progress`: Umsetzung läuft
- `Evidence Pending`: umgesetzt, Nachweis fehlt
- `Closed`: geprüft abgeschlossen
- `Not Applicable`: begründet nicht anwendbar
- `Exception`: genehmigte Abweichung

## Register

| Gap-ID | Schwere | Bereich | Befund | Zielwelle | Status | Abschlussnachweis |
|---|---|---|---|---|---|---|
| P01-GAP-001 | Blocker | Laufzeit/Persistenz | gemeldeter SQLite-Syntaxfehler verhindert stabilen Start | Wave 01 | Open | Starttest und Regressionstest |
| P01-GAP-002 | Major | Tests | kein Testprojekt in der Solution sichtbar | Wave 01 | Open | `dotnet test` mit DB-Initialisierungstest |
| P01-GAP-003 | Major | Reproduzierbarkeit | SDK-Version nicht repositoryweit festgelegt | Wave 01 | Open | `global.json` und dokumentierter SDK-Lauf |
| P01-GAP-004 | Major | Qualität | zentrale Build-/Analyzer-Basis nicht sichtbar | Wave 01 | Open | `.editorconfig`, `Directory.Build.props`, sauberer Build |
| P01-GAP-005 | Major | CI | kein automatischer Windows-Build sichtbar | Wave 01 | Open | erfolgreicher CI-Lauf |
| P01-GAP-006 | Major | Lizenz | Lizenzentscheidung offen und keine LICENSE sichtbar | Wave 01 | Open | dokumentierte Entscheidung und LICENSE |
| P01-GAP-007 | Minor | Security | kein Security-Meldeweg sichtbar | Wave 01 | Open | `SECURITY.md` |
| P01-GAP-008 | Major | Standardanwendung | kein SASD-Alignment-/Abweichungsnachweis im Zielprojekt | Wave 01 | Open | `docs/standards/SASD-ALIGNMENT.md` |
| P01-GAP-009 | Major | Daten | Backup-Restore nicht verifiziert | Wave 02 | Open | Restore-Testprotokoll |
| P01-GAP-010 | Major | Diagnose | Logging und Crashdiagnose unklar | Wave 02 | Open | Diagnosekonzept und Test |
| P01-GAP-011 | Major | Release | kein installierbares oder portables Release nachgewiesen | Wave 02 | Open | Release Record und Smoke Test |
| P01-GAP-012 | Minor | Dokumentation | README-Screenshot fehlt laut Projektstatus | Wave 02 | Open | Screenshot mit fiktiven Daten |
| P01-GAP-013 | Major | Supply Chain | Paketupdates und Schwachstellen nicht geprüft | Wave 01 | Open | Paketreview und dokumentierte Entscheidung |
| P01-GAP-014 | Observation | Architektur | Root-Projekt liegt nicht unter `src/` | keine Änderung geplant | Not Applicable | Small-Projekt-Regel und Entscheidung P01-DEC-003 |
| P01-GAP-015 | Observation | Architektur | keine getrennten Domain/Application/Infrastructure-Projekte | keine Änderung geplant | Not Applicable | Scope- und Größenbegründung |

## Priorisierungsregel

Blocker und Datenintegritätsrisiken werden vor kosmetischen Repository-Anpassungen bearbeitet. Wave 01 darf nicht als abgeschlossen gelten, wenn P01-GAP-001 lediglich dokumentiert, aber nicht technisch verifiziert behoben wurde.
