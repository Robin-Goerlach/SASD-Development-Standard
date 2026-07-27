---
prompt-id: "SASD-PROMPT-INIT-004"
title: "Scope und Nicht-Ziele festlegen"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "project-initiation"
language: "de"
summary: "Formuliert einen begrenzten Projektumfang und schützt vor unkontrollierter Ausweitung."
variables: ["project_name", "project_description", "goals", "requirements", "constraints", "non_goals", "quality_level", "output_language"]
tags: ["scope", "non-goals", "prioritization", "milestone"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# Scope und Nicht-Ziele festlegen
## Zweck

Definiere für **{{project_name}}** einen klaren Scope und explizite Nicht-Ziele.

## Eingaben

- Beschreibung: {{project_description}}
- Ziele: {{goals}}
- bekannte Anforderungen: {{requirements}}
- Randbedingungen: {{constraints}}
- bisherige Nicht-Ziele: {{non_goals}}
- Qualitätsstufe: {{quality_level}}

## Arbeitsauftrag

1. Formuliere den Produktkern in höchstens fünf Sätzen.
2. Ordne Anforderungen in Must, Should, Could und Won't for now ein.
3. Lege funktionale und nichtfunktionale Grenzen fest.
4. Benenne bewusst ausgeschlossene Plattformen, Nutzergruppen, Integrationen und Betriebsmodelle.
5. Definiere Kriterien für Scope-Änderungen.
6. Formuliere einen ersten Releaseumfang, der eigenständig nutzbar und prüfbar ist.

## Qualitätsregeln

- Nicht-Ziele müssen konkret und überprüfbar sein.
- Spätere Optionen dürfen nicht als aktuelle Verpflichtung erscheinen.
- Qualitäts- und Sicherheitsanforderungen dürfen nicht als „Feature für später“ verdrängt werden.
- Scope muss zur verfügbaren Kapazität passen.

## Ausgabeformat

Liefere in {{output_language}}: Produktkern, In-Scope, Out-of-Scope, Priorisierung, Releasegrenze, Änderungsregeln und offene Konflikte.
