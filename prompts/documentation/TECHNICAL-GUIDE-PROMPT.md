---
prompt-id: "SASD-PROMPT-DOC-003"
title: "Technische Anleitung erstellen"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "documentation"
language: "de"
summary: "Erstellt eine reproduzierbare Installations-, Betriebs- oder Troubleshooting-Anleitung."
variables: ["project_name", "document_type", "target_audience", "environment", "source_material", "constraints", "evidence", "output_language"]
tags: ["guide", "operations", "installation", "troubleshooting"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# Technische Anleitung erstellen
## Zweck

Erstelle für **{{project_name}}** eine technische Anleitung vom Typ **{{document_type}}**.

## Eingaben

- Zielgruppe: {{target_audience}}
- Zielumgebung: {{environment}}
- Quellen und Befehle: {{source_material}}
- Randbedingungen: {{constraints}}
- getestete Nachweise: {{evidence}}

## Arbeitsauftrag

1. Definiere Zweck, Voraussetzungen und unterstützte Umgebung.
2. Beschreibe Schritte in reproduzierbarer Reihenfolge.
3. Erkläre erwartete Ergebnisse und Erfolgskontrollen.
4. Ergänze sichere Fehlerbehandlung, Rollback, Backup und Troubleshooting.
5. Trenne getestete Befehle von noch zu bestätigenden Varianten.
6. Vermeide unnötige Wiederholung und verlinke autoritative Details.

## Qualitätsregeln

- Keine destruktiven Befehle ohne Warnung, Sicherung und Rückweg.
- Keine Zugangsdaten in Beispielen.
- Relative und plattformgerechte Pfade bevorzugen.
- Versionen und Datum nennen, wenn Verhalten zeitabhängig ist.

## Ausgabeformat

Erzeuge in {{output_language}} eine vollständige Markdown-Anleitung mit Voraussetzungen, Schritten, Checks, Rollback, Troubleshooting, Security-Hinweisen und bekannten Grenzen.
