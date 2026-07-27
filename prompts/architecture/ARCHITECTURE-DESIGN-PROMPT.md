---
prompt-id: "SASD-PROMPT-ARCH-002"
title: "Projektarchitektur entwerfen"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "architecture"
language: "de"
summary: "Entwirft eine proportionale Architektur aus Anforderungen, Risiken und Betriebsmodell."
variables: ["project_name", "requirements", "project_context", "constraints", "quality_level", "profiles", "source_material", "output_language"]
tags: ["architecture", "components", "interfaces", "data-flow"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# Projektarchitektur entwerfen
## Zweck

Entwirf eine angemessene Architektur für **{{project_name}}**.

## Eingaben

- Anforderungen: {{requirements}}
- Kontext: {{project_context}}
- Randbedingungen: {{constraints}}
- Qualitätsstufe: {{quality_level}}
- Profile: {{profiles}}
- Quellen und bestehende Entscheidungen: {{source_material}}

## Arbeitsauftrag

1. Definiere Systemkontext, Akteure, Vertrauensgrenzen und externe Abhängigkeiten.
2. Leite Komponenten und Verantwortlichkeiten aus Anforderungen ab.
3. Beschreibe Abhängigkeitsrichtung, Schnittstellen, Datenflüsse und Fehlerpfade.
4. Plane Konfiguration, Secrets, Logging, Persistenz, Migration, Backup, Tests und Deployment.
5. Identifiziere ADR-Kandidaten und technische Risiken.
6. Zeige ein minimales Startmodell und mögliche spätere Skalierung, ohne sie vorwegzunehmen.

## Qualitätsregeln

- Keine Architektur nur aufgrund eines Musternamens wählen.
- Kleine Projekte dürfen klein bleiben.
- Sicherheits- und Betriebsaspekte sind Teil der Architektur.
- Jede zusätzliche Schicht benötigt einen konkreten Nutzen.

## Ausgabeformat

Erzeuge in {{output_language}}: Architekturübersicht, Kontextdiagramm in Mermaid, Komponenten, Datenflüsse, Schnittstellen, Querschnittsthemen, Deployment, Risiken, ADR-Liste und Validierungsplan.
