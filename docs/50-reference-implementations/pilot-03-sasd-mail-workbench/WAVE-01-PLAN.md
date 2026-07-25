---
title: "Pilot 03 Wave-01-Plan – SASD Mail Workbench"
document-id: SASD-REF-PILOT-307
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
depends-on: [SASD-REF-PILOT-306, SASD-PROC-004]
---

# Wave 01 – SASD Mail Workbench

## Ziel

Die bereits umfangreiche technische Grundlage als reproduzierbaren und sicherheitsbewerteten Referenzstand nachweisen.

## Arbeitspakete

1. sauberen Clone, Commit-SHA und SDK erfassen,
2. Restore, Release-Build und alle fünf Testprojekte ausführen,
3. CI-Lauf und Artefakte dem Commit zuordnen,
4. Solution-Dependency-Graph und Architecture-Testregeln dokumentieren,
5. synthetische Maildaten und Datenschutzregeln prüfen,
6. Fehlerfälle für Staging, Dateiumbenennung, SQLite-Migration und Wiederanlauf ausführen,
7. Threat Model für untrusted Bytes, Pfade, HTML, Anhänge und künftige Credentials erstellen,
8. Desktopprofil-Anwendbarkeit und Production-Gate dokumentieren,
9. Gap Register und Lessons Learned aktualisieren.

## Akzeptanzkriterien

- alle Projekte bauen und Tests sind grün,
- Architekturabhängigkeiten entsprechen dokumentierten Regeln,
- mindestens drei Recovery-/Fehlerinjektionsszenarien sind nachgewiesen,
- Testmails sind synthetisch oder freigegeben,
- Security- und Production-Grenzen sind explizit,
- fehlende Protokoll- und UI-Funktionen werden nicht als Pilotfehler umgedeutet.
