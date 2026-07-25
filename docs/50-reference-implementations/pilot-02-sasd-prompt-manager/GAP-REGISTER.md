---
title: "Pilot 02 Gap Register – SASD Prompt Manager"
document-id: SASD-REF-PILOT-205
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
depends-on: [SASD-REF-PILOT-204, SASD-GOV-006]
---

# Gap Register – SASD Prompt Manager

| Gap-ID | Priorität | Bereich | Beobachtung | Zielzustand | Geplante Welle | Status |
|---|---|---|---|---|---|---|
| P02-GAP-001 | Blocker | Baseline | vollständige Commit-ID und lokaler Toolchain-Nachweis fehlen | reproduzierbarer Baseline-Record | Wave 01 | Open |
| P02-GAP-002 | Major | Build | Restore und Release-Build nicht unabhängig geprüft | dokumentierter erfolgreicher Build | Wave 01 | Open |
| P02-GAP-003 | Major | Tests | öffentlich nur Domain-Testprojekt sichtbar | risikobasierte Tests für Application, Infrastructure und Datenzugriff | Wave 01 | Open |
| P02-GAP-004 | Major | CI | keine CI im sichtbaren Root bestätigt | Windows-CI für Restore, Build, Test und Audit | Wave 01 | Open |
| P02-GAP-005 | Major | Security | kein bestätigter öffentlicher Security-Kontaktweg | `SECURITY.md` und dokumentierte Grenzen | Wave 01 | Open |
| P02-GAP-006 | Major | Secrets | Secret-Warnung nicht technisch verifiziert | Tests und dokumentierte False-Positive-/False-Negative-Grenzen | Wave 01 | Open |
| P02-GAP-007 | Major | Daten | Persistenz, Migration und Datenpfade nicht verifiziert | idempotente Initialisierung und dokumentierte Pfade | Wave 01 | Open |
| P02-GAP-008 | Major | Recovery | Backup/Restore und Import/Export-Roundtrip nicht geprüft | automatisierter oder reproduzierbarer Recovery-Nachweis | Wave 01 | Open |
| P02-GAP-009 | Minor | Toolchain | `global.json` und zentrale Paketverwaltung nicht bestätigt | bewusste, dokumentierte Toolchain-Entscheidung | Wave 01 | Open |
| P02-GAP-010 | Minor | Dokumentation | Screenshot-Pfad und aktuelle Projektstatusdarstellung prüfen | konsistente README-Navigation | Wave 01 | Open |
| P02-GAP-011 | Minor | Alignment | kein SASD-Alignment-Record | profil- und stufenbezogene Bewertung | Wave 01 | Open |
| P02-GAP-012 | Later | Release | Installer/Update- und Release-Smoke-Test nicht bewertet | angemessenes Desktop-Releaseverfahren | Wave 02 | Planned |
