---
prompt-id: "SASD-PROMPT-REVIEW-011"
title: "Repository-CI und Merge Gate prüfen"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "review"
language: "de"
summary: "Prüft exakte Commit-Evidenz, plattformübergreifende Jobs und tatsächliche Ruleset-Aktivierung."
variables: ["repository_url", "evidence", "environment", "constraints", "output_language"]
tags: ["ci", "merge-gate", "ruleset", "evidence"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# Repository-CI und Merge Gate prüfen
## Zweck

Prüfe die CI-Aktivierung und Branch-Governance für **{{repository_url}}**.

## Eingaben

- GitHub-Actions- und Ruleset-Nachweise: {{evidence}}
- lokale und Remote-Umgebung: {{environment}}
- geplante Schutzregeln und Randbedingungen: {{constraints}}

## Arbeitsauftrag

1. Bestätige Repository-Identität und exakte Commit-SHA.
2. Prüfe abgeschlossene GitHub-Actions-Läufe für genau diesen Commit.
3. Bestätige erfolgreiche Linux-, Windows- und aggregierte Merge-Gate-Jobs.
4. Prüfe hochgeladene Evidenzartefakte und deren Commitbezug.
5. Unterscheide Ruleset-Datei, API-Plan, tatsächliche Aktivierung und Enforcement.
6. Prüfe Required Check Context, Strict Policy, Force-Push- und Löschschutz.
7. Dokumentiere Rollback und Maintainerzugang.

## Qualitätsregeln

- Workflow-Quelltext ist kein erfolgreicher Lauf.
- Ein vorhandenes Ruleset-Template ist kein aktives Ruleset.
- Evidenz aus einem anderen Commit ist nicht übertragbar.
- Schreibberechtigungen und Bypass-Regeln kritisch prüfen.

## Ausgabeformat

Liefere in {{output_language}} eine Matrix mit Verified, Prepared, Pending, Failed oder Not Applicable, dazu Blocker, API-/UI-Nachweise und Aktivierungsempfehlung.
