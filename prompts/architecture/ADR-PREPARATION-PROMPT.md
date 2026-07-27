---
prompt-id: "SASD-PROMPT-ARCH-001"
title: "Architecture Decision Record vorbereiten"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "architecture"
language: "de"
summary: "Erstellt einen prüfbaren ADR-Entwurf mit Optionen, Entscheidungskriterien und Konsequenzen."
variables: ["project_name", "decision_topic", "architecture_context", "requirements", "constraints", "source_material", "output_language"]
tags: ["adr", "architecture", "decision", "tradeoffs"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# Architecture Decision Record vorbereiten
## Zweck

Erstelle für **{{project_name}}** einen prüfbaren ADR-Entwurf zum Thema **{{decision_topic}}**.

## Eingaben

- Kontext: {{architecture_context}}
- Anforderungen: {{requirements}}
- Randbedingungen: {{constraints}}
- Quellen und Versuche: {{source_material}}

## Arbeitsauftrag

Beschreibe Entscheidungsproblem, Kontext, Annahmen, Entscheidungskriterien, mindestens zwei realistische Optionen sowie den Status quo. Bewerte Vor- und Nachteile, Sicherheit, Datenschutz, Betrieb, Wartung, Migration, Lock-in und technische Schulden. Formuliere eine klare Entscheidung, Konsequenzen, Folgemaßnahmen und Kriterien für eine spätere Neubewertung.

## Qualitätsregeln

- Erfinde keine Testergebnisse oder Quellen.
- Trenne Tatsachen, Annahmen und Bewertung.
- Eine bereits getroffene Entscheidung darf nicht durch nachträgliche Scheinoptionen legitimiert werden.
- Bei unzureichender Evidenz ist „Entscheidung vertagen und Spike durchführen“ zulässig.

## Ausgabeformat

Erzeuge in {{output_language}} einen ADR mit Status Proposed, Kontext, Kriterien, Optionen, Entscheidung, Konsequenzen, Risiken, Verifikation und Reviewdatum.
