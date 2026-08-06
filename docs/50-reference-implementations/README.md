---
title: "Referenzimplementierungen"
document-id: SASD-REF-001
document-type: informative
status: Proposed
version: 0.12.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-08-06
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-GOV-007, SASD-PROC-005]
---

# Referenzimplementierungen

Dieses Verzeichnis dokumentiert die praktische Erprobung des SASD Development Standard an realen SASD-Projekten. Der Quellcode verbleibt in den jeweiligen Projekt-Repositories; hier werden Auswahl, Klassifikation, Ausgangslage, Migrationswellen, Nachweise und Erkenntnisse versioniert.

## Katalog

- [Referenzimplementierungskatalog](REFERENCE-IMPLEMENTATION-CATALOG.md)

## Pilotprogramm

1. [Pilotprogramm](PILOT-PROGRAM.md)
2. [Evidenzmodell](PILOT-EVIDENCE-MODEL.md)
3. [Pilotportfolio](PILOT-PORTFOLIO.md)
4. [Version-1.0-Pilot-Readiness](VERSION-1.0-PILOT-READINESS.md)
5. [Feedbacklog](PILOT-FEEDBACK-LOG.md)
6. [Feedbackübersicht](PILOT-FEEDBACK-SUMMARY.md)

## Repository-Self-Hosting

Das Standard-Repository ist selbst eine Referenzanwendung. CI-Recovery, Remote-Evidenz und Branch-Ruleset-Aktivierung sind unter [`repository-self-hosting/`](repository-self-hosting/) dokumentiert.

## Pilotportfolio

| Pilot | Kategorie | Zielstufe | Status | Umsetzung | Verifikation | Nächster Schritt |
|---|---|---|---|---|---|---|
| [Pilot 01 – SASD TaskHost Local](pilot-01-sasd-taskhost-local/README.md) | Small | Recommended | In Execution | Artifact Prepared | Pending | praktische Wave-01-Integration und Validierung |
| [Pilot 02 – SASD Prompt Manager](pilot-02-sasd-prompt-manager/README.md) | Medium | Recommended | Baseline Assessed | Not Started | Pending | lokaler Baseline-Clone und Wave 01 |
| [Pilot 03 – SASD Mail Workbench](pilot-03-sasd-mail-workbench/README.md) | Large / Complex | Recommended, später Production-Gate | Baseline Assessed | Not Started | Pending | lokaler Baseline-Clone und Wave 01 |

Die [TaskHost Remote Technical Baseline](pilot-01-sasd-taskhost-local/REMOTE-BASELINE-EVIDENCE-2026-08-06.md) ist erfolgreich. Sie bestätigt Restore, Build, Audit und Publish für einen exakten öffentlichen Zielcommit, nicht aber Tests, Laufzeitverhalten oder den Pilotabschluss.

## Wichtige Abgrenzung

Die drei Größenklassen sind ausgewählt und bewertet. Die Referenzdokumentation ist informativ und ersetzt weder Build-/Testnachweise noch Änderungen im Ziel-Repository. `Baseline Assessed`, `Artifact Prepared`, `Committed` und `Verified` bleiben bewusst getrennte Zustände.
