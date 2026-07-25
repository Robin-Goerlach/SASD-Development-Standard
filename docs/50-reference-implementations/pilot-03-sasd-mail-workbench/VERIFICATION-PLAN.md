---
title: "Pilot 03 Verifikationsplan – SASD Mail Workbench"
document-id: SASD-REF-PILOT-312
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
depends-on: [SASD-REF-PILOT-307, SASD-REF-PILOT-002]
---

# Verifikationsplan – SASD Mail Workbench

## Automatische Nachweise

- `dotnet --info`, Restore und Release-Build,
- alle fünf Testprojekte mit TRX-Ergebnissen,
- Architecture Tests separat sichtbar,
- NuGet-Audit,
- Migration von mindestens einem älteren Testkatalog,
- Crash-/Recovery- und Deduplizierungstests,
- CI-Lauf für exakt denselben Commit.

## Manuelle Nachweise

- Bootstrap-/Konsolenlauf in isoliertem Arbeitsverzeichnis,
- Sichtprüfung der erzeugten Rohdateien und relativen Pfade,
- Wiederanlauf nach absichtlich abgebrochenem Import,
- Prüfung der Sample-Mails auf personenbezogene Daten,
- Review des Threat Models und der Production-Gates.

## Abschlussgate

Die Welle darf erst `Passed` sein, wenn Datenintegrität, Recovery, Architektur und Security für denselben Commit nachgewiesen sind.
