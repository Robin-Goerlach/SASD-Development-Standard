---
prompt-id: "SASD-PROMPT-DEBUG-001"
title: "Systematische Fehleranalyse"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "debugging"
language: "de"
summary: "Strukturiert Reproduktion, Hypothesen, Experimente, Ursache, Fix und Regressionstest."
variables: ["project_name", "issue_description", "reproduction_steps", "logs_and_errors", "code_context", "environment", "evidence", "output_language"]
tags: ["debugging", "root-cause", "reproduction", "regression"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core", ".NET", "Desktop"]
last-reviewed: "2026-07-25"
---

# Systematische Fehleranalyse
## Zweck

Untersuche den Fehler in **{{project_name}}** systematisch.

## Eingaben

- Fehlerbild: {{issue_description}}
- Reproduktionsschritte: {{reproduction_steps}}
- Logs und Meldungen: {{logs_and_errors}}
- relevanter Code: {{code_context}}
- Umgebung: {{environment}}
- vorhandene Nachweise: {{evidence}}

## Arbeitsauftrag

1. Trenne Beobachtung, Vermutung und bestätigte Tatsache.
2. Erzeuge eine minimale, reproduzierbare Fehlerbeschreibung.
3. Formuliere priorisierte Hypothesen mit erwarteten Beobachtungen.
4. Schlage kleine diagnostische Experimente vor.
5. Bestimme die technische Ursache erst nach Evidenz.
6. Entwirf den kleinsten sicheren Fix und einen Regressionstest.
7. Prüfe Nebenwirkungen, Datenmigration, Rollback und Monitoring.

## Qualitätsregeln

- Keine zufälligen Änderungen ohne Hypothese.
- Keine Ursache allein aus einer Fehlermeldung ableiten.
- Keine produktiven Daten verändern, bevor Sicherung und Rückweg geklärt sind.
- Ein verschwundener Fehler ist noch keine bestätigte Ursache.

## Ausgabeformat

Liefere in {{output_language}}: Befund, Reproduktion, Hypothesenmatrix, Diagnoseplan, Ursache, Fixplan, Regressionstest, Risiken und Verifikationsbefehle.
