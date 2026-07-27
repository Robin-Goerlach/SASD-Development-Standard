---
prompt-id: "SASD-PROMPT-DEV-003"
title: "Code kommentieren und dokumentieren"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "development"
language: "de"
summary: "Ergänzt verständliche XML-Dokumentation und Begründungskommentare ohne den Code nachzuerzählen."
variables: ["project_name", "code_context", "target_audience", "constraints", "output_language"]
tags: ["documentation", "xml-comments", "code-comments", "maintainability"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: [".NET"]
last-reviewed: "2026-07-25"
---

# Code kommentieren und dokumentieren
## Zweck

Verbessere die Verständlichkeit des bereitgestellten Codes aus **{{project_name}}**.

## Eingaben

- Code und Dateikontext: {{code_context}}
- Zielgruppe: {{target_audience}}
- Vorgaben: {{constraints}}

## Arbeitsauftrag

1. Ergänze XML-Dokumentation für öffentliche oder fachlich wichtige APIs.
2. Erkläre Zweck, Parameter, Rückgabewerte, Ausnahmen und relevante Nebenwirkungen.
3. Ergänze normale Kommentare nur für Gründe, Randbedingungen, Algorithmen, Risiken oder Workarounds.
4. Entferne oder vermeide Kommentare, die lediglich den Code wiederholen.
5. Benenne unklare Namen oder zu komplexe Strukturen, statt sie nur mit Kommentaren zu kaschieren.

## Qualitätsregeln

- Keine falschen Garantien oder nicht belegten Thread-Safety-Aussagen.
- Dokumentation muss mit dem tatsächlichen Verhalten übereinstimmen.
- Beispiele dürfen keine Secrets oder personenbezogenen Daten enthalten.
- Kommentare sollen wartbar und präzise sein.

## Ausgabeformat

Liefere in {{output_language}} den überarbeiteten Code, eine Liste wesentlicher Dokumentationsentscheidungen und Hinweise auf verbleibende Verständlichkeitsprobleme.
