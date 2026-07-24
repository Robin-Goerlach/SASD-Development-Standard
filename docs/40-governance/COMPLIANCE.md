---
title: "Compliance-Modell"
document-id: SASD-GOV-007
document-type: normative
status: Draft
version: 0.1.0
standard-version: "1.0"
language: de
authoritative: true
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-CORE-006, SASD-GOV-006]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Compliance-Modell

## Grundidee

Compliance ist kein bloßes Ja/Nein-Merkmal. Ein Projekt dokumentiert:

- angewendete Standardversion,
- angewendete Profile,
- gewählte Qualitätsstufe,
- Projektklassifikation,
- erfüllte Anforderungen und Nachweise,
- offene Maßnahmen,
- genehmigte Abweichungen.

## Statusangaben

Ein Projekt SOLLTE seinen Stand mindestens als einen der folgenden Werte beschreiben:

- `Not Assessed`,
- `Assessment in Progress`,
- `Partially Aligned`,
- `Aligned with Exceptions`,
- `Aligned`.

Die Aussage bezieht sich immer auf eine konkrete Standardversion, Profile und Qualitätsstufe.

## Nachweis

Die Datei `docs/SASD-COMPLIANCE.md` SOLLTE die zentrale projektspezifische Compliance-Erklärung bilden. Eine Vorlage befindet sich unter `templates/documents`.
