---
prompt-id: "SASD-PROMPT-REQ-001"
title: "Lastenheft erstellen"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "requirements"
language: "de"
summary: "Erstellt ein lösungsneutrales Lastenheft aus Projektidee und Stakeholderbedarf."
variables: ["project_name", "project_description", "target_users", "stakeholders", "goals", "constraints", "non_goals", "source_material", "quality_level", "output_language"]
tags: ["requirements", "lastenheft", "stakeholders", "scope"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# Lastenheft erstellen
## Zweck

Erstelle ein lösungsneutrales Lastenheft für **{{project_name}}**.

## Eingaben

- Beschreibung: {{project_description}}
- Zielgruppen: {{target_users}}
- Stakeholder: {{stakeholders}}
- Ziele: {{goals}}
- Randbedingungen: {{constraints}}
- Nicht-Ziele: {{non_goals}}
- Quellen: {{source_material}}
- Qualitätsstufe: {{quality_level}}

## Arbeitsauftrag

Beschreibe Ausgangssituation, Ziele, Stakeholder, Einsatzkontext, funktionale Anforderungen, Qualitätsanforderungen, Daten, Schnittstellen, Sicherheit, Datenschutz, Betrieb, Migration, Abnahme und Projektgrenzen. Vergib stabile Anforderungs-IDs und formuliere prüfbare Akzeptanzkriterien, ohne die technische Umsetzung vorwegzunehmen.

## Qualitätsregeln

- Anforderungen müssen eindeutig, notwendig, konsistent und testbar sein.
- Technische Lösungen nur als Randbedingung aufnehmen, wenn sie tatsächlich vorgegeben sind.
- Annahmen und offene Punkte separat führen.
- Sicherheits-, Datenschutz- und Wiederherstellungsanforderungen nicht auslassen.
- Keine erfundenen Stakeholderentscheidungen.

## Ausgabeformat

Erzeuge in {{output_language}} ein vollständiges Markdown-Lastenheft mit Dokumentstatus, Glossar, Anforderungskatalog, Prioritäten, Abnahmekriterien, Risiken und offenen Punkten.
