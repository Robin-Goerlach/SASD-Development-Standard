---
title: "Pilotportfolio für Version 1.0"
document-id: SASD-REF-PILOT-003
document-type: informative
status: Draft
version: 0.11.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-25
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-REF-PILOT-001, SASD-REF-PILOT-002]
---

# Pilotportfolio für Version 1.0

Diese Datei wird deterministisch aus den `pilot.json`-Manifesten erzeugt.

| Pilot-ID | Pilot | Größe | Kategorie | Qualitätsstufe | Profile | Lebenszyklus | Umsetzung | Verifikation |
|---|---|---|---|---|---|---|---|---|
| SASD-PILOT-001 | [Pilot 01 – SASD TaskHost Local](pilot-01-sasd-taskhost-local/README.md) | Small | small-dotnet-desktop-legacy-migration | Recommended | Core, DotNet, Desktop | In Execution | Artifact Prepared | Pending |
| SASD-PILOT-002 | [Pilot 02 – SASD Prompt Manager](pilot-02-sasd-prompt-manager/README.md) | Medium | medium-dotnet-desktop-maintained-application | Recommended | Core, DotNet, Desktop | Baseline Assessed | Not Started | Pending |
| SASD-PILOT-003 | [Pilot 03 – SASD Mail Workbench](pilot-03-sasd-mail-workbench/README.md) | Large | complex-layered-dotnet-mail-platform | Recommended | Core, DotNet, Desktop | Baseline Assessed | Not Started | Pending |

## Statushinweis

`Baseline Assessed` bestätigt eine dokumentierte Ausgangsbewertung, aber keinen lokalen Build oder Laufzeittest. `Artifact Prepared` bestätigt ein geprüftes Updateartefakt, nicht dessen Integration. `Pending` blockiert die Aussagen `Wave Validated` und `Pilot Closed`.
