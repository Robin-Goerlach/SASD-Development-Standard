---
title: "Pilot 01 Gap Register – SASD TaskHost Local"
document-id: SASD-REF-PILOT-105
document-type: informative
status: Draft
version: 0.8.0
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
- `Artifact Prepared`: Änderung ist in einem geprüften Overlay enthalten, aber nicht als Zielstand verifiziert
- `Evidence Pending`: committed oder umgesetzt; erforderlicher Abschlussnachweis fehlt
- `Closed`: geprüft abgeschlossen
- `Not Applicable`: begründet nicht anwendbar
- `Exception`: genehmigte Abweichung

## Register

| Gap-ID | Schwere | Bereich | Befund | Zielwelle | Status | Abschlussnachweis |
|---|---|---|---|---|---|---|
| P01-GAP-001 | Blocker | Laufzeit/Persistenz | gemeldeter SQLite-Syntaxfehler verhindert laut Baseline stabilen Start; Ursache im sichtbaren Stand nicht eindeutig reproduziert | Wave 01 | Artifact Prepared | Windows-Starttest mit frischer und bestehender Testdatenbank plus Regressionstest |
| P01-GAP-002 | Major | Tests | kein Testprojekt in der Baseline sichtbar | Wave 01 | Artifact Prepared | erfolgreicher `dotnet test`-Lauf des neuen Testprojekts |
| P01-GAP-003 | Major | Reproduzierbarkeit | SDK-Version in der Baseline nicht repositoryweit festgelegt | Wave 01 | Artifact Prepared | committed `global.json` und dokumentierter SDK-Lauf |
| P01-GAP-004 | Major | Qualität | zentrale Build-/Analyzer-Basis in der Baseline nicht sichtbar | Wave 01 | Artifact Prepared | committed `.editorconfig`, `Directory.Build.props` und erfolgreicher Build |
| P01-GAP-005 | Major | CI | kein automatischer Windows-Build in der Baseline sichtbar | Wave 01 | Artifact Prepared | erfolgreicher Workflow-Lauf mit Commit- und Run-ID |
| P01-GAP-006 | Major | Lizenz | Lizenzentscheidung in der Baseline offen | Wave 01 | Artifact Prepared | Eigentümerbestätigung, ADR und committed LICENSE |
| P01-GAP-007 | Minor | Security | kein Security-Meldeweg in der Baseline sichtbar | Wave 01 | Artifact Prepared | committed `SECURITY.md` und geprüfter Meldeweg |
| P01-GAP-008 | Major | Standardanwendung | kein SASD-Alignment-/Abweichungsnachweis in der Baseline | Wave 01 | Artifact Prepared | committed Alignment-Dokument mit offenem Status |
| P01-GAP-009 | Major | Daten | Backup-Restore nicht verifiziert | Wave 02 | Open | Restore-Testprotokoll |
| P01-GAP-010 | Major | Diagnose | Logging und Crashdiagnose in der Baseline unklar | Wave 02 | Artifact Prepared | praktischer Fehlerfall- und Logpfadtest; Umfang für Wave 02 neu bewerten |
| P01-GAP-011 | Major | Release | kein installierbares oder portables Release nachgewiesen | Wave 02 | Open | Release Record und Smoke Test |
| P01-GAP-012 | Minor | Dokumentation | README-Screenshot fehlt laut Projektstatus | Wave 02 | Open | Screenshot mit fiktiven Daten |
| P01-GAP-013 | Major | Supply Chain | Paketupdates und Schwachstellen in der Baseline nicht geprüft | Wave 01 | Artifact Prepared | dokumentierter NuGet-Audit und erfolgreicher CI-Lauf |
| P01-GAP-014 | Observation | Architektur | Root-Projekt liegt nicht unter `src/` | keine Änderung geplant | Not Applicable | Small-Projekt-Regel und Entscheidung P01-DEC-003 |
| P01-GAP-015 | Observation | Architektur | keine getrennten Domain/Application/Infrastructure-Projekte | keine Änderung geplant | Not Applicable | Scope- und Größenbegründung |

## Aktueller Zustand

```text
Wave-01-Gaps im Overlay vorbereitet: 9
Wave-01-Gaps technisch geschlossen: 0
Not Applicable: 2
Wave-02-Gaps offen: 3
Teilweise vorgezogener Diagnoseumfang: 1
```

## Priorisierungsregel

Blocker und Datenintegritätsrisiken werden vor kosmetischen Repository-Anpassungen bearbeitet. Wave 01 darf nicht als abgeschlossen gelten, wenn P01-GAP-001 lediglich durch robusteren Code und vorbereitete Tests adressiert, aber nicht unter Windows mit repräsentativen Datenbankzuständen verifiziert wurde.
