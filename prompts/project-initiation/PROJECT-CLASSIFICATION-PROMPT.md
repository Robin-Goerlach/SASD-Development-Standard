---
prompt-id: "SASD-PROMPT-INIT-002"
title: "SASD-Projektklassifikation"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "project-initiation"
language: "de"
summary: "Trennt Projektgröße, Qualitätsstufe, Lebensdauer, Risikomerkmale und Profile."
variables: ["project_name", "project_description", "project_context", "constraints", "quality_level", "profiles", "evidence", "output_language"]
tags: ["classification", "quality-level", "risk", "profiles"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# SASD-Projektklassifikation
## Zweck

Klassifiziere **{{project_name}}** nach dem SASD Development Standard.

## Eingaben

- Beschreibung: {{project_description}}
- Kontext: {{project_context}}
- Randbedingungen: {{constraints}}
- vorläufige Qualitätsstufe: {{quality_level}}
- vorläufige Profile: {{profiles}}
- verfügbare Nachweise: {{evidence}}

## Arbeitsauftrag

Trenne ausdrücklich:

1. strukturelle Größe: Small, Medium oder Large,
2. erwarteten Lebenszyklus,
3. Qualitätsstufe: Minimum, Recommended oder Production,
4. Risikomerkmale,
5. anwendbare Profile,
6. erforderliche Dokumentations-, Test- und Reviewtiefe.

Bewerte Datenvertraulichkeit, Integrität, Verfügbarkeit, Wiederherstellung, externe Erreichbarkeit, Verteilung, privilegierte Zugriffe, rechtliche Vorgaben, Drittanbieterabhängigkeiten und Auswirkungen fehlerhafter Ergebnisse.

## Qualitätsregeln

- Projektgröße und Qualitätsstufe dürfen nicht gleichgesetzt werden.
- Ein kleines sicherheitskritisches Werkzeug kann Production-Anforderungen benötigen.
- Unbekannte Tatsachen bleiben unbekannt und werden nicht geschätzt.
- Jede Empfehlung benötigt eine nachvollziehbare Begründung.

## Ausgabeformat

Liefere in {{output_language}} eine Klassifikationstabelle, Begründung, Risikomerkmale, Profile, erforderliche Startartefakte, offene Fragen und Auslöser für eine spätere Neubewertung.
