---
prompt-id: "SASD-PROMPT-REQ-003"
title: "Anforderungs-Traceability prüfen"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "requirements"
language: "de"
summary: "Prüft die Rückverfolgbarkeit zwischen Zielen, Anforderungen, Architektur, Tests und Releases."
variables: ["project_name", "goals", "requirements", "architecture_context", "evidence", "source_material", "output_language"]
tags: ["traceability", "requirements", "tests", "coverage"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# Anforderungs-Traceability prüfen
## Zweck

Prüfe die Rückverfolgbarkeit der Anforderungen von **{{project_name}}**.

## Eingaben

- Ziele: {{goals}}
- Anforderungen: {{requirements}}
- Architektur und Umsetzung: {{architecture_context}}
- vorhandene Nachweise: {{evidence}}
- zusätzliche Quellen: {{source_material}}

## Arbeitsauftrag

1. Ordne Ziele den Anforderungen zu.
2. Ordne Anforderungen Architekturentscheidungen, Komponenten, Tests, Dokumenten und Releases zu.
3. Identifiziere Anforderungen ohne Umsetzung oder Nachweis.
4. Identifiziere Funktionen und technische Komplexität ohne Anforderungsbezug.
5. Unterscheide offen, nicht anwendbar, Ausnahme, umgesetzt und verifiziert.

## Qualitätsregeln

- Vorhandener Testcode ist kein erfolgreicher Testnachweis.
- Eine Implementierungsbehauptung ohne konkrete Datei, Commit oder Laufnachweis bleibt unbestätigt.
- Mehrdeutige oder widersprüchliche Anforderungen separat markieren.

## Ausgabeformat

Liefere in {{output_language}} eine Traceability-Matrix, Lücken, Überimplementierung, Konflikte, priorisierte Korrekturen und benötigte Nachweise.
