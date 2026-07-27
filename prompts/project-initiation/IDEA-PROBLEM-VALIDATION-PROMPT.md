---
prompt-id: "SASD-PROMPT-INIT-003"
title: "Idee und Problem validieren"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "project-initiation"
language: "de"
summary: "Prüft, ob ein Projekt ein reales Problem löst und welchen minimalen validierbaren Umfang es benötigt."
variables: ["project_name", "project_description", "target_users", "goals", "constraints", "source_material", "output_language"]
tags: ["idea", "problem-validation", "mvp", "scope"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# Idee und Problem validieren
## Zweck

Prüfe kritisch, ob **{{project_name}}** ein klar beschriebenes Problem löst und wie die Idee mit geringem Aufwand validiert werden kann.

## Eingaben

- Idee: {{project_description}}
- Zielgruppen: {{target_users}}
- angenommene Ziele: {{goals}}
- Randbedingungen: {{constraints}}
- vorhandenes Material: {{source_material}}

## Arbeitsauftrag

1. Formuliere das Problem unabhängig von der vorgeschlagenen Lösung.
2. Identifiziere betroffene Nutzer, Häufigkeit, Auswirkungen und bestehende Umgehungen.
3. Trenne belegte Tatsachen, Annahmen und Wunschvorstellungen.
4. Benenne Alternativen, einschließlich „nichts entwickeln“ und vorhandene Werkzeuge verwenden.
5. Definiere die kleinste Validierung, die die kritischste Annahme prüft.
6. Leite messbare Erfolgs- und Abbruchkriterien ab.
7. Kennzeichne Funktionen, die erst nach erfolgreicher Validierung sinnvoll sind.

## Qualitätsregeln

- Keine Markt- oder Nutzerbehauptung ohne Quelle oder Kennzeichnung als Annahme.
- Keine Featureliste als Ersatz für eine Problemdefinition.
- Bevorzuge reversible Experimente vor langfristiger Architektur.
- Berücksichtige Aufwand, Lernwert, Wartung und Alternativkosten.

## Ausgabeformat

Erzeuge in {{output_language}}: Problemstatement, Zielgruppen, Annahmenmatrix, Alternativen, Validierungsexperiment, Messgrößen, Abbruchkriterien und nächste Entscheidung.
