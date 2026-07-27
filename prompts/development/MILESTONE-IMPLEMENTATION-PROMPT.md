---
prompt-id: "SASD-PROMPT-DEV-001"
title: "Begrenzten Milestone implementieren"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "development"
language: "de"
summary: "Steuert eine begrenzte Implementierung mit Tests, Dokumentation und nachvollziehbaren Commitgrenzen."
variables: ["project_name", "repository_tree", "implementation_scope", "acceptance_criteria", "architecture_context", "constraints", "evidence", "output_language"]
tags: ["implementation", "milestone", "tests", "commits"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core", ".NET", "Desktop"]
last-reviewed: "2026-07-25"
---

# Begrenzten Milestone implementieren
## Zweck

Implementiere den begrenzten Milestone für **{{project_name}}**.

## Eingaben

- Repository-Struktur: {{repository_tree}}
- Umfang: {{implementation_scope}}
- Akzeptanzkriterien: {{acceptance_criteria}}
- Architekturkontext: {{architecture_context}}
- Randbedingungen: {{constraints}}
- vorhandene Nachweise: {{evidence}}

## Arbeitsauftrag

1. Prüfe Ausgangsstand, Build und relevante Tests vor Änderungen.
2. Begrenze die Arbeit strikt auf den vereinbarten Scope.
3. Implementiere in kleinen, nachvollziehbaren Schritten.
4. Ergänze Fehlerbehandlung, Logging, Tests und Dokumentation dort, wo der Milestone sie benötigt.
5. Vermeide allgemeines Refactoring ohne direkten Nutzen.
6. Dokumentiere ausgeführte Befehle, Ergebnisse und nicht verifizierte Aussagen.
7. Bereite sinnvolle Commitgrenzen und Commit-Messages vor.

## Qualitätsregeln

- Kein erfolgreicher Build- oder Testclaim ohne Laufnachweis.
- Keine API- oder Schemaänderung ohne Auswirkungen und Migration zu dokumentieren.
- Öffentliche APIs und nicht offensichtliche Entscheidungen verständlich dokumentieren.
- Offene Risiken und Restarbeiten ehrlich ausweisen.

## Ausgabeformat

Liefere in {{output_language}}: Änderungen, Begründung, Dateien, Tests, Befehle, Ergebnisse, Risiken, Abweichungen, Dokumentationsupdates und Commitvorschläge.
