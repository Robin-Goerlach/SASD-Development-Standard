---
prompt-id: "SASD-PROMPT-RESEARCH-003"
title: "Technologieauswahl bewerten"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "research"
language: "de"
summary: "Vergleicht Technologien anhand von Projektanforderungen, Lebenszyklus und Betriebsrisiken."
variables: ["project_name", "requirements", "architecture_context", "constraints", "source_material", "quality_level", "output_language"]
tags: ["technology-selection", "tradeoffs", "architecture", "lifecycle"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# Technologieauswahl bewerten
## Zweck

Bewerte Technologieoptionen für **{{project_name}}** anhand nachvollziehbarer Kriterien.

## Eingaben

- Anforderungen: {{requirements}}
- Architekturkontext: {{architecture_context}}
- Randbedingungen: {{constraints}}
- bekannte Optionen und Quellen: {{source_material}}
- Qualitätsstufe: {{quality_level}}

## Arbeitsauftrag

1. Formuliere Entscheidungskriterien und ihre Gewichtung.
2. Vergleiche mindestens zwei realistische Optionen und den Status quo.
3. Berücksichtige Reife, Supportzeitraum, Lizenz, Plattformen, Ökosystem, Sicherheit, Betrieb, Testbarkeit, Migration, Lernaufwand und Exit-Strategie.
4. Identifiziere irreversible Entscheidungen und Lock-in-Risiken.
5. Empfehle bei Unsicherheit einen Spike oder Prototyp mit klaren Messgrößen.

## Qualitätsregeln

- Keine Technologie nur wegen Popularität oder persönlicher Vorliebe auswählen.
- Support- und Versionsdaten müssen aktuell verifiziert werden.
- Anschaffungsaufwand und langfristige Wartung getrennt bewerten.
- Die Empfehlung muss zum Qualitätsniveau und zur Teamgröße passen.

## Ausgabeformat

Erzeuge in {{output_language}}: Kriterienmatrix, Optionen, Risiken, Empfehlung, Gegenargumente, Validierungsexperiment und ADR-Vorschlag.
