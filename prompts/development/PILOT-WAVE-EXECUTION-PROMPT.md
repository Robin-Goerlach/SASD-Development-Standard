---
prompt-id: "SASD-PROMPT-DEV-002"
title: "Pilot-Migrationswelle ausführen"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "development"
language: "de"
summary: "Führt eine freigegebene Pilotwelle evidenzbasiert und ohne Scope-Ausweitung aus."
variables: ["project_name", "repository_url", "pilot_wave_plan", "current_state", "evidence", "environment", "output_language"]
tags: ["pilot", "migration", "execution", "evidence"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core", ".NET", "Desktop"]
last-reviewed: "2026-07-25"
---

# Pilot-Migrationswelle ausführen
## Zweck

Führe die freigegebene Pilotwelle für **{{project_name}}** aus.

## Eingaben

- Repository: {{repository_url}}
- Wellenplan: {{pilot_wave_plan}}
- bestätigter Ist-Zustand: {{current_state}}
- vorhandene Evidenz: {{evidence}}
- Umgebung: {{environment}}

## Arbeitsauftrag

1. Sichere Daten und reproduziere den Ausgangszustand.
2. Führe ausschließlich die definierte Welle aus.
3. Behebe Blocker vor kosmetischen Änderungen.
4. Sichere Fehlerkorrekturen durch Regressionstests ab.
5. Halte Änderungen reversibel und Commitgrenzen klein.
6. Dokumentiere Build-, Test-, Laufzeit- und CI-Ergebnisse getrennt.
7. Aktualisiere Gap Register, Evidenzmap und Lessons Learned.

## Qualitätsregeln

- Keine echten Nutzerdaten in Tests.
- Keine Architekturänderung ohne konkreten Nutzen.
- Ein vorbereitetes Artefakt ist kein integrierter Zielstand.
- Keine formale SASD-Alignment-Aussage vor erfolgreicher Verifikation.

## Ausgabeformat

Liefere in {{output_language}}: Ausgangsstand, Änderungen, Ursache/Lösung, Befehle und Ergebnisse, Daten- und Rollbackprüfung, Gap-Updates, verbleibende Risiken, Commitvorschläge und Standardfeedback.
