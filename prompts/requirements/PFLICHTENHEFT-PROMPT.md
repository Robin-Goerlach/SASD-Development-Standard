---
prompt-id: "SASD-PROMPT-REQ-002"
title: "Pflichtenheft ableiten"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "requirements"
language: "de"
summary: "Leitet aus freigegebenen Anforderungen eine technische und organisatorische Umsetzungsspezifikation ab."
variables: ["project_name", "requirements", "architecture_context", "constraints", "quality_level", "profiles", "source_material", "output_language"]
tags: ["requirements", "pflichtenheft", "solution-design", "acceptance"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# Pflichtenheft ableiten
## Zweck

Leite für **{{project_name}}** ein Pflichtenheft aus den bereitgestellten Anforderungen ab.

## Eingaben

- Lastenheft oder Anforderungen: {{requirements}}
- Architekturkontext: {{architecture_context}}
- Randbedingungen: {{constraints}}
- Qualitätsstufe: {{quality_level}}
- Profile: {{profiles}}
- weitere Quellen: {{source_material}}

## Arbeitsauftrag

1. Ordne jede technische Maßnahme einer Anforderung zu.
2. Beschreibe Systemgrenzen, Komponenten, Datenhaltung, Schnittstellen, Fehlerbehandlung, Logging, Security, Tests, Deployment und Betrieb.
3. Lege messbare Abnahmekriterien und Nachweise fest.
4. Kennzeichne offene Architekturentscheidungen als ADR-Kandidaten.
5. Plane Meilensteine und Übergaben proportional zur Projektgröße.

## Qualitätsregeln

- Keine Anforderung stillschweigend ändern oder entfernen.
- Abweichungen vom Lastenheft explizit dokumentieren.
- Technische Details müssen nachvollziehbar, testbar und wartbar sein.
- Keine unnötigen Schichten oder Technologien einführen.

## Ausgabeformat

Erzeuge in {{output_language}} ein strukturiertes Markdown-Pflichtenheft mit Traceability-Matrix, Lösungskonzept, Daten- und Schnittstellenspezifikation, Testkonzept, Rollout, Risiken und offenen Entscheidungen.
