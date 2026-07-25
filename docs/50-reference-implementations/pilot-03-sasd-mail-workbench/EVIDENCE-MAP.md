---
title: "Pilot 03 Evidenzzuordnung – SASD Mail Workbench"
document-id: SASD-REF-PILOT-308
document-type: informative
status: Draft
version: 0.11.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-25
applies-to-quality-levels: [Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-REF-PILOT-002, SASD-REF-PILOT-304, SASD-GOV-007]
---

# Evidenzzuordnung – SASD Mail Workbench

| Evidenz-ID | Klasse | Quelle | Beobachtung | Einschränkung |
|---|---|---|---|---|
| P03-EV-001 | O | öffentliches Repository am 2026-07-25 | Root mit CI, docs, src, tests, zentralen Build-/Paketdateien, Security, Changelog und Roadmap | keine lokale Ausführung |
| P03-EV-002 | O | `src/` | Application.Contracts, Application, Bootstrap.Console, Domain, ExtensionModel, Infrastructure und Persistence sichtbar | Abhängigkeiten nicht kompiliert geprüft |
| P03-EV-003 | O | `tests/` | Application-, Architecture-, Domain-, Infrastructure- und Persistence-Tests sichtbar | Ergebnisse und Umfang unbekannt |
| P03-EV-004 | O | `docs/` | ADR, Architektur, Entwicklung, Formal, Qualität, Requirements und Repository dokumentiert | Aktualität nicht vollständig geprüft |
| P03-EV-005 | R | README 0.3.1 | Rohmail-Fingerprints, Staging, atomare Übernahme, SQLite-Migrationen und Wiederanlauf beschrieben | Funktionsaussagen nicht unabhängig verifiziert |
| P03-EV-006 | R | README | keine Mailprotokolle und keine fertige GUI im aktuellen Stand | bewusster Scope, kein Defekt |
| P03-EV-301 | V geplant | lokaler Build/Test | vollständige Solution und fünf Testprojekte | offen |
| P03-EV-302 | V geplant | Recovery-Testmatrix | Migration, Staging, Abbruch und Wiederanlauf | offen |
| P03-EV-303 | V geplant | Security Review | Threat Model, Testdaten und Production Gate | offen |
| P03-EV-304 | V geplant | CI-Run | grüner Workflow für Ziel-Commit | offen |
