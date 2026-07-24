---
title: "Versionierung des Standards"
document-id: SASD-GOV-004
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
depends-on: [SASD-GOV-002, SASD-GOV-003]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Versionierung des Standards

## Grundsatz

Das Repository verwendet Semantic Versioning für veröffentlichte Gesamtstände des Standards.

## Versionstypen

- `0.x.y`: Entwicklung vor dem ersten stabilen Standard,
- `1.0.0-rc.n`: Release Candidates,
- `1.0.0`: erste stabile Version,
- Patch-Version: kompatible Klarstellungen und Korrekturen,
- Minor-Version: neue kompatible Inhalte, Profile oder Funktionen,
- Major-Version: nicht kompatible normative Änderungen.

## Tags und Releases

Veröffentlichte Standardstände MÜSSEN durch einen Git-Tag markiert werden. Ein GitHub Release SOLLTE Release Notes und Hinweise zu Kompatibilität, Migration und bekannten Einschränkungen enthalten.

## Dokumentversionen

Einzelne Dokumente besitzen zusätzlich eine eigene Version gemäß `DOCUMENT-METADATA.md`. Die Dokumentversion ersetzt nicht die Version des Gesamtstandards.
