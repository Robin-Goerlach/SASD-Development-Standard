---
prompt-id: "SASD-PROMPT-DOC-001"
title: "README und Repository-Dokumentation erstellen"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "documentation"
language: "de"
summary: "Erstellt eine ehrliche, navigierbare README und ein angemessenes Dokumentationsset."
variables: ["project_name", "project_description", "target_users", "repository_tree", "current_state", "requirements", "constraints", "target_audience", "output_language"]
tags: ["readme", "documentation", "repository", "onboarding"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# README und Repository-Dokumentation erstellen
## Zweck

Erstelle oder überarbeite die Repository-Dokumentation für **{{project_name}}**.

## Eingaben

- Beschreibung: {{project_description}}
- Zielgruppen: {{target_users}}
- Repository-Struktur: {{repository_tree}}
- tatsächlicher Status: {{current_state}}
- Anforderungen: {{requirements}}
- Randbedingungen: {{constraints}}
- Adressaten: {{target_audience}}

## Arbeitsauftrag

Erstelle eine README mit Zweck, Status, Nutzen, Funktionen, Nicht-Zielen, Voraussetzungen, Build/Start, Tests, Konfiguration, Datenpfaden, Sicherheit, Dokumentationsnavigation, Roadmap, Beitrag und Lizenz. Leite ergänzende Dokumente nach Projektgröße ab und verlinke sie konsistent.

## Qualitätsregeln

- Keine Funktion, Buildbarkeit oder Reife behaupten, die nicht belegt ist.
- Befehle müssen kopierbar und zum tatsächlichen Repository passen.
- Keine Secrets oder lokale absolute Pfade.
- Historische Planung und aktuellen Stand klar trennen.

## Ausgabeformat

Liefere in {{output_language}} eine vollständige README sowie eine Liste anzulegender oder zu aktualisierender Dokumente und defekter Links.
