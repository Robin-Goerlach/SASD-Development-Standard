---
prompt-id: "SASD-PROMPT-RELEASE-003"
title: "Version 1.0 Release Candidate prüfen"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "release"
language: "de"
summary: "Prüft den RC gegen exakten Commit, CI, Pilot, Ruleset, Artefakte und Releaseunterlagen."
variables: ["repository_url", "release_version", "evidence", "source_material", "output_language"]
tags: ["release-candidate", "ci", "pilot", "checksums"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# Version 1.0 Release Candidate prüfen
## Zweck

Prüfe den vorgeschlagenen SASD Release Candidate **{{release_version}}**.

## Eingaben

- Repository und exakter Commit: {{repository_url}}
- CI-, Pilot- und Ruleset-Nachweise: {{evidence}}
- Plan, Blockerregister, Release Record, Notes, Known Issues, Manifest und Prüfsummen: {{source_material}}

## Arbeitsauftrag

1. Bestätige Approved-Dokumente und unveränderte Approval-Manifeste.
2. Bestätige Ubuntu, Windows und `SASD merge gate` für den Releasecommit.
3. Bestätige mindestens einen praktisch ausgeführten Pilotdurchlauf.
4. Unterscheide aktives Ruleset und committed Template.
5. Verifiziere Archive, Prüfsummen, sichere Pfade und Reproduzierbarkeit.
6. Identifiziere jedes Pending, jeden Blocker und jede nicht erklärte Ausnahme.
7. Prüfe die ehrliche Kennzeichnung als Pre-release.

## Qualitätsregeln

- Keine Freigabe allein aufgrund von Quellcode, Workflowdateien, Testdateien oder Vorlagen.
- Releaseartefakte müssen exakt den geprüften Dateien entsprechen.
- Eine Entscheidung trotz Abweichung muss befristet und dokumentiert sein.

## Ausgabeformat

Empfehle in {{output_language}}: Approve RC, Approve with explicit temporary decision oder Do not approve; ergänze Gate-Tabelle, Evidenzlinks, Blocker und Abschlussaktionen.
