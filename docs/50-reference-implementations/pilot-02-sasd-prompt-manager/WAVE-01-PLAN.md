---
title: "Pilot 02 Wave-01-Plan – SASD Prompt Manager"
document-id: SASD-REF-PILOT-207
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
depends-on: [SASD-REF-PILOT-206, SASD-PROC-004]
---

# Wave 01 – SASD Prompt Manager

## Ziel

Einen konkreten, reproduzierbaren und risikobasiert geprüften Ausgangsstand herstellen, ohne Produktumfang oder UI grundlegend zu verändern.

## Arbeitspakete

1. sauberen Clone erstellen und Commit-SHA dokumentieren,
2. SDK-, NuGet- und Windows-Voraussetzungen erfassen,
3. Restore, Release-Build und Tests ausführen,
4. Projektabhängigkeiten und Composition Root prüfen,
5. CI mit Build, Test und Audit einrichten oder vorhandene CI verifizieren,
6. Testdaten und isolierte Datenpfade für Persistenztests schaffen,
7. Import/Export- und Backup/Restore-Roundtrip prüfen,
8. Secret-Warnung mit positiven und negativen Testfällen absichern,
9. Security Policy und SASD-Alignment ergänzen,
10. Wave-Review und Gap Register aktualisieren.

## Akzeptanzkriterien

- alle Befehle sind an einen Commit gebunden,
- Build und bestehende Tests sind grün,
- mindestens ein automatisierter Persistenz-/Recovery-Test ist vorhanden,
- Secret-Erkennung besitzt nachvollziehbare Grenzen,
- CI-Ergebnis und Artefakte sind dokumentiert,
- keine neue Produktionsassembly wurde ohne belegten Bedarf eingeführt.
