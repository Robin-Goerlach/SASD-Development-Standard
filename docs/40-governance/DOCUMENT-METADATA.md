---
title: "Metadaten für Standarddokumente"
document-id: SASD-GOV-003
document-type: normative
status: Approved
version: 0.8.0
standard-version: "1.0"
language: de
authoritative: true
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
approved-on: 2026-07-24
approval-record: SASD-REF-GOV-005
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-GOV-001, SASD-GOV-002]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Metadaten für Standarddokumente

## 1. Zweck

Dieses Dokument definiert das maschinenlesbare YAML-Front-Matter für Dokumente des Standards.

## 2. Dokumenttypen

| Wert | Bedeutung |
|---|---|
| `normative` | enthält verbindliche Regeln oder Definitionen |
| `informative` | erklärt, begründet, berichtet oder zeigt Beispiele |
| `supporting` | Vorlage, Checkliste, Prompt oder operatives Hilfsmittel |

## 3. Pflichtfelder

| Feld | Pflicht | Beispiel |
|---|---|---|
| `title` | alle | `"Versionierung des Standards"` |
| `document-id` | alle | `SASD-GOV-004` |
| `document-type` | alle | `normative` |
| `status` | alle | `Proposed` |
| `version` | alle | `0.8.0` |
| `standard-version` | alle | `"1.0"` |
| `language` | alle | `de` |
| `authoritative` | alle | `true` |
| `owner` | alle | `SASD Development Standard Maintainer` |
| `last-updated` | alle | `2026-07-24` |
| `applies-to-quality-levels` | normativ | `[Minimum, Recommended, Production]` |
| `applies-to-profiles` | normativ | `[Core, DotNet, Desktop]` |
| `depends-on` | alle | `[SASD-GOV-001]` |
| `normative-keywords` | normativ | `[MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]` |

## 4. Normative Anforderungen

| Anforderungs-ID | Normative Anforderung |
|---|---|
| `SASD-GOV-REQ-200` | Jedes Dokument unter docs MUSS YAML-Front-Matter besitzen, sofern es nicht ausdrücklich als Verzeichnis-README ausgenommen ist. |
| `SASD-GOV-REQ-201` | Jedes Standarddokument MUSS eine repositoryweit eindeutige document-id besitzen. |
| `SASD-GOV-REQ-202` | Die document-id MUSS über Umbenennungen und Statusübergänge hinweg stabil bleiben. |
| `SASD-GOV-REQ-203` | Das Feld document-type MUSS einen zulässigen Typ enthalten. |
| `SASD-GOV-REQ-204` | Das Feld status MUSS einen im Dokumentlebenszyklus definierten Status enthalten. |
| `SASD-GOV-REQ-205` | Das Feld version MUSS eine syntaktisch gültige Dokumentversion enthalten. |
| `SASD-GOV-REQ-206` | Das Feld standard-version MUSS die Ziel- oder Bezugsfassung des Gesamtstandards nennen. |
| `SASD-GOV-REQ-207` | Das Feld language MUSS einen eindeutigen Sprachcode enthalten. |
| `SASD-GOV-REQ-208` | Das Feld authoritative MUSS eindeutig festlegen, ob das Dokument die maßgebliche Fassung ist. |
| `SASD-GOV-REQ-209` | Das Feld owner MUSS eine verantwortliche Rolle oder Person nennen. |
| `SASD-GOV-REQ-210` | Das Feld last-updated MUSS das Datum der letzten inhaltlichen Änderung im Format YYYY-MM-DD enthalten. |
| `SASD-GOV-REQ-211` | Normative Dokumente MÜSSEN applies-to-quality-levels angeben. |
| `SASD-GOV-REQ-212` | Normative Dokumente MÜSSEN applies-to-profiles angeben. |
| `SASD-GOV-REQ-213` | Das Feld depends-on MUSS alle normativ wesentlichen Dokumentabhängigkeiten über Dokument-IDs nennen. |
| `SASD-GOV-REQ-214` | Normative Dokumente MÜSSEN ihre verwendeten normativen Schlüsselwörter deklarieren. |
| `SASD-GOV-REQ-215` | Informative Dokumente DÜRFEN NICHT durch Metadaten eine eigenständige normative Wirkung behaupten. |
| `SASD-GOV-REQ-216` | Erzeugte Dokumente SOLLTEN generated: true und ihre Generatorquelle nennen. |
| `SASD-GOV-REQ-217` | Ein Dokument mit authoritative: false MUSS bei möglicher Verwechslung auf die autoritative Quelle verweisen. |
| `SASD-GOV-REQ-218` | Abhängigkeiten DÜRFEN NICHT auf unbekannte Dokument-IDs zeigen. |
| `SASD-GOV-REQ-219` | Zirkuläre Abhängigkeiten SOLLTEN vermieden und bei fachlicher Notwendigkeit dokumentiert werden. |
| `SASD-GOV-REQ-220` | Metadatenwerte MÜSSEN maschinenlesbar und ohne versteckte Mehrdeutigkeit formuliert sein. |
| `SASD-GOV-REQ-221` | Optionale Metadatenfelder DÜRFEN NICHT Pflichtfelder ersetzen. |
| `SASD-GOV-REQ-222` | Dateipfad und Dokument-ID SOLLTEN im Dokumentkatalog übereinstimmen. |
| `SASD-GOV-REQ-223` | Ein Statuswechsel MUSS das Feld last-updated aktualisieren. |
| `SASD-GOV-REQ-224` | Eine normative Bedeutungsänderung MUSS die Dokumentversion erhöhen. |
| `SASD-GOV-REQ-225` | Reine Format- oder Rechtschreibkorrekturen KÖNNEN ohne Dokumentversionssprung erfolgen, wenn keine veröffentlichte Fassung betroffen ist. |
| `SASD-GOV-REQ-226` | Veröffentlichte Dokumente SOLLTEN eine nachvollziehbare Versionsänderung für jede inhaltliche Korrektur erhalten. |
| `SASD-GOV-REQ-227` | Ein Dokument DARF NICHT gleichzeitig als authoritative und als bloße Übersetzung gekennzeichnet sein, sofern keine Mehrsprachigkeitsregel beide Fassungen ausdrücklich gleichstellt. |
| `SASD-GOV-REQ-228` | Die Metadatenprüfung MUSS vor Proposed, Approved und Release erfolgreich sein. |
| `SASD-GOV-REQ-229` | Spezialisierte Profile KÖNNEN zusätzliche Metadatenfelder definieren, sofern diese dem Basismodell nicht widersprechen. |

## 5. Beispiel

```yaml
---
title: "Beispieldokument"
document-id: SASD-EXAMPLE-001
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
depends-on: [SASD-GOV-001]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---
```

## 6. Verwandte Dokumente

- [Dokumentlebenszyklus](DOCUMENT-LIFECYCLE.md)
- [Dokumentkatalog](../00-foundation/DOCUMENT-CATALOG.md)
- [Normative Dokumentvorlage](../../templates/documents/NORMATIVE-DOCUMENT-TEMPLATE.md)
