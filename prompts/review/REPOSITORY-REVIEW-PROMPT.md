---
prompt-id: "SASD-PROMPT-REVIEW-001"
title: "Repository vollständig prüfen"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "review"
language: "de"
summary: "Prüft Struktur, Build, Dokumentation, Sicherheit, Tests, Releases und Auffälligkeiten."
variables: ["project_name", "repository_url", "repository_tree", "quality_level", "profiles", "evidence", "constraints", "output_language"]
tags: ["repository-review", "quality", "security", "documentation"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# Repository vollständig prüfen
## Zweck

Prüfe das Repository **{{project_name}}** umfassend.

## Eingaben

- Repository: {{repository_url}}
- Dateibaum: {{repository_tree}}
- Qualitätsstufe: {{quality_level}}
- Profile: {{profiles}}
- Build-, Test- und CI-Nachweise: {{evidence}}
- Randbedingungen: {{constraints}}

## Arbeitsauftrag

Bewerte Repository-Identität, README, Lizenz, Verzeichnisstruktur, Buildreproduzierbarkeit, Abhängigkeiten, Secrets, Konfiguration, Architektur, Codequalität, Tests, CI, Security, Datenhaltung, Dokumentation, Releasefähigkeit und bekannte Probleme. Ordne Befunde nach Blocker, Major, Minor und Observation und verknüpfe sie mit konkreten SASD-Anforderungen.

## Qualitätsregeln

- Öffentliche Dateien und erfolgreiche Ausführung als unterschiedliche Evidenz behandeln.
- Keine fehlende Datei behaupten, ohne den geprüften Scope zu nennen.
- Keine kosmetische Vereinheitlichung vor funktionalen und sicherheitsrelevanten Risiken.
- Overengineering ausdrücklich vermeiden.

## Ausgabeformat

Liefere in {{output_language}}: Executive Summary, Stärken, Befundtabelle, Evidenzklasse, Anforderungsbezug, Priorität, Migrationswellen, schnelle Verbesserungen und Verifikationsbefehle.
