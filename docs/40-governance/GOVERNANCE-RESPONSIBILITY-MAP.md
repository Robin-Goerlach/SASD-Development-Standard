---
title: "Governance Responsibility Map"
document-id: SASD-REF-GOV-001
document-type: informative
status: Draft
version: 0.8.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-GOV-001, SASD-GOV-002, SASD-GOV-003, SASD-GOV-004, SASD-GOV-005, SASD-GOV-006, SASD-GOV-007]
normative-keywords: []
---

# Governance Responsibility Map

## Zweck

Die Matrix verhindert Doppelzuständigkeiten und zeigt, wo eine Governance-Frage primär geregelt wird.

| Thema | Primär zuständig | Unterstützend |
|---|---|---|
| Bedeutung MUSS/SOLLTE/KANN | `NORMATIVE-LANGUAGE.md` | Qualitätsstufen, Profile |
| Status Planned bis Retired | `DOCUMENT-LIFECYCLE.md` | Versionierung, Change Process |
| YAML-Front-Matter und IDs | `DOCUMENT-METADATA.md` | Dokumentkatalog, Validatoren |
| Tags, Releases und SemVer | `VERSIONING.md` | Releaseprozess, Changelog |
| Standardänderungen | `CHANGE-PROCESS.md` | Pilotfeedback, Versionierung |
| Abweichungen einzelner Projekte | `EXCEPTIONS.md` | Alignment-Modell |
| Projektbewertung und Evidenz | `COMPLIANCE.md` | Pilot Evidence Model |
| Inhaltliche Dokumentrollen | `CONTENT-ARCHITECTURE.md` | Dokumentkatalog |
| Freigabe eines Dokuments | `DOCUMENT-LIFECYCLE.md` | Approval Record, Review Checklist |
| Freigabe eines Gesamtrelease | `VERSIONING.md` | Acceptance Criteria, Release Record |

## Konfliktregel

Bei Überschneidungen gilt zuerst die explizite Vorrangregel der Inhaltsarchitektur. Innerhalb der Governance hat das thematisch primär zuständige Dokument Vorrang; Widersprüche müssen über den Änderungsprozess behoben werden.
