---
prompt-id: "SASD-PROMPT-RESEARCH-002"
title: "Technische Primärquellen recherchieren"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "research"
language: "de"
summary: "Plant und dokumentiert eine technische Recherche mit Primärquellen und klarer Unsicherheit."
variables: ["project_name", "project_context", "source_material", "constraints", "output_language"]
tags: ["research", "primary-sources", "evidence", "technology"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# Technische Primärquellen recherchieren
## Zweck

Führe eine belastbare technische Recherche für **{{project_name}}** durch.

## Eingaben

- Fragestellung und Kontext: {{project_context}}
- bereits bekannte Quellen: {{source_material}}
- Randbedingungen: {{constraints}}

## Arbeitsauftrag

1. Zerlege die Fragestellung in prüfbare Teilfragen.
2. Priorisiere offizielle Dokumentation, Standards, Spezifikationen, Quellcode und wissenschaftliche Primärquellen.
3. Dokumentiere Veröffentlichungsdatum, Gültigkeitsbereich und Versionsbezug.
4. Vergleiche widersprüchliche Aussagen und erkläre Unterschiede.
5. Trenne Fakten, Interpretation, Empfehlung und offene Unsicherheit.
6. Leite konkrete Auswirkungen auf Anforderungen, Architektur, Risiken und Tests ab.

## Qualitätsregeln

- Keine Sekundärquelle als alleinige Basis einer kritischen Entscheidung, wenn eine Primärquelle verfügbar ist.
- Keine veraltete Version stillschweigend auf einen aktuellen Stand übertragen.
- Kurze, urheberrechtskonforme Zitate; ansonsten paraphrasieren.
- Fehlende Evidenz offen benennen.

## Ausgabeformat

Liefere in {{output_language}}: Forschungsfragen, Quellenregister, Befunde, Konflikte, Schlussfolgerungen, Projektfolgen und verbleibende Prüfaufgaben.
