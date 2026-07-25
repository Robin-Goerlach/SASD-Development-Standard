---
title: "Pilot 02 Evidenzzuordnung – SASD Prompt Manager"
document-id: SASD-REF-PILOT-208
document-type: informative
status: Draft
version: 0.11.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-25
applies-to-quality-levels: [Recommended]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-REF-PILOT-002, SASD-REF-PILOT-204, SASD-GOV-007]
---

# Evidenzzuordnung – SASD Prompt Manager

| Evidenz-ID | Klasse | Quelle | Beobachtung | Einschränkung |
|---|---|---|---|---|
| P02-EV-001 | O | öffentliches Repository am 2026-07-25 | Root mit `docs`, `scripts`, `src`, `tests`, `.editorconfig`, `Directory.Build.props`, Lizenz, README und Solution | keine lokale Ausführung |
| P02-EV-002 | O | `src/` | App, Application, Domain und Infrastructure sichtbar | Abhängigkeitsrichtung nicht kompiliert geprüft |
| P02-EV-003 | O | Domain-Testprojekt | viele fachliche Testbereiche sichtbar | Anzahl und Ergebnis der Tests unbekannt |
| P02-EV-004 | R | README | lokaler Prompt Manager mit Projekten, Tags, Versionierung, Export, Backup und Sicherheitswarnungen | Funktionsumfang nicht unabhängig verifiziert |
| P02-EV-005 | O | Root | Apache-2.0-Lizenz und zentrale Buildprops sichtbar | Lizenz- und Buildwirkung nicht lokal geprüft |
| P02-EV-301 | V geplant | sauberer Clone und `dotnet`-Nachweise | Baseline-Commit, Build und Tests | offen |
| P02-EV-302 | V geplant | Persistenz-/Recovery-Test | Import/Export und Backup/Restore | offen |
| P02-EV-303 | V geplant | CI-Run | Build, Test und Audit für Ziel-Commit | offen |
| P02-EV-304 | V geplant | manueller Windows-Test | Desktop-Grundfunktionen und Fehlerdarstellung | offen |
