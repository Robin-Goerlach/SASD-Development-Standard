---
prompt-id: "SASD-PROMPT-REVIEW-007"
title: "Pilotwelle verifizieren"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "review"
language: "de"
summary: "Verifiziert eine umgesetzte Pilotwelle gegen Plan, Commit und tatsächliche Ausführungsnachweise."
variables: ["project_name", "repository_url", "pilot_wave_plan", "evidence", "environment", "current_state", "output_language"]
tags: ["pilot", "verification", "ci", "runtime"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core", ".NET", "Desktop"]
last-reviewed: "2026-07-25"
---

# Pilotwelle verifizieren
## Zweck

Verifiziere die umgesetzte Pilotwelle von **{{project_name}}**.

## Eingaben

- Repository und Zielcommit: {{repository_url}}
- Wellenplan: {{pilot_wave_plan}}
- bereitgestellte Nachweise: {{evidence}}
- Umgebung: {{environment}}
- erwarteter Zielzustand: {{current_state}}

## Arbeitsauftrag

1. Trenne Sourceinspection, vorbereitetes Artefakt, lokale Ausführung, CI-Ausführung und berichtete Aussage.
2. Prüfe exakte Commit-SHA, Befehle, Exitcodes und Evidenzpfade.
3. Verifiziere Build, Tests, ursprüngliches Fehlerszenario, frische und bestehende Daten, Fehlerpfade und Rollback.
4. Behandle Workflowdateien nicht als erfolgreichen CI-Lauf.
5. Aktualisiere Gaps zu Open, Artifact Prepared, Evidence Pending, Closed, Not Applicable oder Exception.
6. Entscheide Passed, Partial oder Failed.

## Qualitätsregeln

- Ein Defekt gilt erst bei reproduziertem Szenario oder äquivalentem Regressionstest als behoben.
- Nächste Welle bei Blocker, Datenrisiko oder unbestätigter Migration stoppen.
- Keine Evidenz aus einem anderen Commit übertragen.

## Ausgabeformat

Liefere in {{output_language}}: Verifikationsübersicht, Command-/Result-Tabelle, Daten- und Laufzeitszenarien, CI-Nachweis, fehlende Kriterien, Gap-Updates und Entscheidung.
