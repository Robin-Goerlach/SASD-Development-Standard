---
title: "Metadaten für Standarddokumente"
document-id: SASD-GOV-003
document-type: normative
status: Proposed
version: 0.1.0
standard-version: "1.0"
language: de
authoritative: true
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-GOV-001, SASD-GOV-002]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Metadaten für Standarddokumente

## 1. Zweck

Dieses Dokument definiert das YAML-Front-Matter für Dokumente des SASD Development Standard. Metadaten ermöglichen Navigation, Versionskontrolle, automatische Prüfung und spätere Publikation.

## 2. Pflichtfelder für normative Dokumente

| Feld | Bedeutung | Beispiel |
|---|---|---|
| `title` | lesbarer Dokumenttitel | `"Dokumentationsstandard"` |
| `document-id` | stabile eindeutige Kennung | `SASD-CORE-004` |
| `document-type` | `normative`, `informative` oder `supporting` | `normative` |
| `status` | Dokumentstatus | `Draft` |
| `version` | Version des Dokuments | `0.1.0` |
| `standard-version` | Zielversion des Gesamtstandards | `"1.0"` |
| `language` | Sprachcode | `de` |
| `authoritative` | autoritative Fassung | `true` |
| `owner` | verantwortliche Rolle | `SASD Development Standard Maintainer` |
| `last-updated` | Datum der letzten inhaltlichen Änderung | `2026-07-24` |
| `applies-to-quality-levels` | betroffene Qualitätsstufen | `[Minimum, Recommended, Production]` |
| `applies-to-profiles` | betroffene Profile | `[Core]` |
| `depends-on` | Dokument-IDs fachlicher Abhängigkeiten | `[SASD-FND-003]` |
| `normative-keywords` | verwendetes Regelvokabular | `[MUSS, SOLLTE, KANN]` |

## 3. Optionale Felder

| Feld | Zweck |
|---|---|
| `supersedes` | ersetzt ein älteres Dokument oder eine ältere Dokument-ID |
| `superseded-by` | verweist auf den Nachfolger |
| `reviewers` | benannte Prüfer oder Rollen |
| `review-date` | Datum der letzten formalen Prüfung |
| `next-review` | geplante nächste Prüfung |
| `source-commit` | Commit der erzeugten Publikation |
| `translation-of` | Dokument-ID und Version der Ausgangsfassung |
| `tags` | zusätzliche Klassifikation |

## 4. Beispiel

```yaml
---
title: "SASD Dokumentationsstandard"
document-id: SASD-CORE-004
document-type: normative
status: Draft
version: 0.1.0
standard-version: "1.0"
language: de
authoritative: true
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core]
depends-on: [SASD-FND-003, SASD-GOV-001]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---
```

## 5. Regeln für Dokument-IDs

Dokument-IDs MÜSSEN repositoryweit eindeutig und nach erstmaliger Veröffentlichung stabil sein.

Verwendete Präfixe:

| Präfix | Dokumentgruppe |
|---|---|
| `SASD-FND` | Foundation |
| `SASD-CORE` | Core Standard |
| `SASD-PROF-DOTNET` | C#/.NET-Profil |
| `SASD-PROF-DESKTOP` | Desktopprofil |
| `SASD-PROC` | Prozesse |
| `SASD-GOV` | Governance |
| `SASD-REF` | Referenzimplementierungen |

Die Nummer identifiziert die Dokumentrolle, nicht die Reihenfolge der Bearbeitung.

## 6. Versionsregeln

Die Dokumentversion folgt Semantic Versioning im vereinfachten Sinn:

- Patch: redaktionelle oder kompatible Klarstellung,
- Minor: neue kompatible Inhalte oder Anforderungen,
- Major: grundlegende Änderung der Dokumentrolle oder nicht kompatible Neufassung.

Vor Version 1.0 des Gesamtstandards dürfen Dokumentversionen mit `0.x.y` beginnen.

## 7. Datumsregeln

`last-updated` wird nur bei einer inhaltlichen Änderung angepasst. Reine Formatierung ohne Inhaltsänderung SOLLTE das Datum nicht verändern.

Datumswerte verwenden ISO 8601 im Format `YYYY-MM-DD`.

## 8. Autoritative Fassungen

Innerhalb derselben Dokumentversion DARF nur eine Sprachfassung `authoritative: true` tragen, sofern keine ausdrücklich zweisprachige Governance beschlossen wurde.

## 9. Prüfung

Das Repository SOLLTE ein Tool bereitstellen, das mindestens folgende Fehler erkennt:

- fehlendes Front-Matter,
- fehlende Pflichtfelder,
- doppelte Dokument-IDs,
- unbekannte Statuswerte,
- ungültige Dokumenttypen,
- nicht vorhandene Abhängigkeiten.
