---
prompt-id: "SASD-PROMPT-RELEASE-004"
title: "Release Notes erstellen"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "release"
language: "de"
summary: "Erstellt ehrliche, nutzerorientierte Release Notes aus Changelog, Scope und Nachweisen."
variables: ["project_name", "release_version", "release_scope", "evidence", "source_material", "target_audience", "output_language"]
tags: ["release-notes", "changelog", "known-issues", "communication"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# Release Notes erstellen
## Zweck

Erstelle Release Notes für **{{project_name}} {{release_version}}**.

## Eingaben

- Releaseumfang: {{release_scope}}
- verifizierte Änderungen und Nachweise: {{evidence}}
- Changelog, Known Issues und Migrationshinweise: {{source_material}}
- Zielgruppe: {{target_audience}}

## Arbeitsauftrag

1. Formuliere Nutzen und wesentliche Änderungen aus Nutzersicht.
2. Trenne Added, Changed, Fixed, Security, Deprecated und Removed.
3. Nenne Voraussetzungen, Upgrade, Migration, Backup und Rollback.
4. Dokumentiere bekannte Einschränkungen und offene Risiken.
5. Verlinke Dokumentation, Prüfsummen und Supportwege.
6. Kennzeichne Pre-release-Status und Stabilitätsgrenzen eindeutig.

## Qualitätsregeln

- Nur verifizierte Änderungen als abgeschlossen darstellen.
- Keine Marketingübertreibungen oder Sicherheitsgarantien.
- Breaking Changes und Datenmigrationen prominent platzieren.
- Keine sensiblen internen Details offenlegen.

## Ausgabeformat

Erzeuge in {{output_language}} veröffentlichungsfertige Markdown-Release-Notes mit Zusammenfassung, Highlights, Upgrade, Checksums, Known Issues, Support und Verifikationshinweis.
