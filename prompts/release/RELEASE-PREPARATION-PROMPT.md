---
prompt-id: "SASD-PROMPT-RELEASE-001"
title: "Release vorbereiten"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "release"
language: "de"
summary: "Erstellt einen risikobasierten Release-Readiness-Plan mit Artefakten, Tests und Rollback."
variables: ["project_name", "release_version", "release_scope", "quality_level", "evidence", "constraints", "security_context", "output_language"]
tags: ["release", "readiness", "rollback", "artifacts"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# Release vorbereiten
## Zweck

Bereite Release **{{release_version}}** von **{{project_name}}** vor.

## Eingaben

- Scope: {{release_scope}}
- Qualitätsstufe: {{quality_level}}
- vorhandene Nachweise: {{evidence}}
- Randbedingungen: {{constraints}}
- Security- und Datenschutzkontext: {{security_context}}

## Arbeitsauftrag

Prüfe Version, Releaseart, Scope, Kompatibilität, sauberen Build, automatisierte und manuelle Tests, Security, Abhängigkeiten, Lizenz, Datenmigration, Backup, Rollback, Release Notes, Changelog, Nutzerhinweise, unveränderte Artefakte, Prüfsummen, Signierung, Freigaberollen, Nachprüfung und Hotfix-/Abbruchverfahren.

## Qualitätsregeln

- Fehlende Nachweise bleiben offen.
- Workflowdateien und Testquellcode sind keine erfolgreichen Läufe.
- Releaseartefakte dürfen nach Verifikation nicht neu gebaut oder verändert werden.
- Offene Risiken müssen in Release Record und Known Issues sichtbar sein.

## Ausgabeformat

Liefere in {{output_language}}: Readiness-Entscheidung, Gate-Tabelle, Blocker, Artefaktplan, Test- und Migrationsplan, Rollback, Release Notes-Gliederung und genaue Abschlussbefehle.
