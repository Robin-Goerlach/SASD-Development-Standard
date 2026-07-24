---
title: "Compliance- und Alignment-Modell"
document-id: SASD-GOV-007
document-type: normative
status: Proposed
version: 0.8.0
standard-version: "1.0"
language: de
authoritative: true
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-CORE-006, SASD-GOV-001, SASD-GOV-002, SASD-GOV-006]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Compliance- und Alignment-Modell

## 1. Zweck

Dieses Dokument definiert, wie Projekte die Anwendung des Standards bewerten, nachweisen und kommunizieren. Der Standard verwendet den Begriff **Alignment**, solange keine externe Zertifizierung angeboten wird.

## 2. Bewertungszustände

| Gesamtstatus | Bedeutung |
|---|---|
| `Not Assessed` | keine belastbare Bewertung |
| `Assessment in Progress` | begonnen, aber unvollständig |
| `Partially Aligned` | offene anwendbare MUSS-Lücken |
| `Aligned with Exceptions` | nur genehmigte Ausnahmen verbleiben |
| `Aligned` | alle anwendbaren MUSS-Anforderungen erfüllt oder Not Applicable |

## 3. Einzelstatus

| Einzelstatus | Bedeutung |
|---|---|
| `Satisfied` | erfüllt und belegt |
| `Not Applicable` | Bedingung nicht vorhanden |
| `Exception` | genehmigte Ausnahme |
| `Open` | anwendbar, aber nicht erfüllt |
| `Not Assessed` | noch nicht bewertet |

## 4. Normative Anforderungen

| Anforderungs-ID | Normative Anforderung |
|---|---|
| `SASD-GOV-REQ-600` | Jede Alignment-Bewertung MUSS eine eindeutige Bezugsfassung des Standards nennen. |
| `SASD-GOV-REQ-601` | Die Bezugsfassung MUSS als Version, Tag oder unveränderlicher Commit angegeben werden. |
| `SASD-GOV-REQ-602` | Eine Bewertung MUSS die angewendeten Profile und Qualitätsstufen nennen. |
| `SASD-GOV-REQ-603` | Bereichsweise Hochstufungen MÜSSEN dokumentiert werden. |
| `SASD-GOV-REQ-604` | Eine Bewertung MUSS den bewerteten Projektcommit, Release oder Artefaktstand nennen. |
| `SASD-GOV-REQ-605` | Eine Bewertung MUSS Datum und verantwortliche Person oder Rolle nennen. |
| `SASD-GOV-REQ-606` | Jede anwendbare MUSS-Anforderung MUSS als Satisfied, Not Applicable, Exception oder Open bewertet werden. |
| `SASD-GOV-REQ-607` | Nicht bewertete Anforderungen MÜSSEN als Not Assessed sichtbar bleiben. |
| `SASD-GOV-REQ-608` | Not Applicable MUSS eine begründete fehlende Auslösebedingung besitzen. |
| `SASD-GOV-REQ-609` | Exception MUSS auf ein gültiges Ausnahmeprotokoll verweisen. |
| `SASD-GOV-REQ-610` | Satisfied MUSS einen angemessenen Nachweis oder eine nachvollziehbare Beobachtung besitzen. |
| `SASD-GOV-REQ-611` | Open MUSS als offene Lücke und nicht als Ausnahme dargestellt werden. |
| `SASD-GOV-REQ-612` | Eine Gesamtbewertung DARF NICHT eine bessere Stufe behaupten, als ihre anwendbaren Einzelbewertungen tragen. |
| `SASD-GOV-REQ-613` | Aligned MUSS voraussetzen, dass alle anwendbaren MUSS-Anforderungen erfüllt oder nachweislich nicht anwendbar sind. |
| `SASD-GOV-REQ-614` | Aligned with Exceptions MUSS voraussetzen, dass verbleibende Nichterfüllungen ausschließlich genehmigte Ausnahmen sind. |
| `SASD-GOV-REQ-615` | Partially Aligned MUSS verwendet werden, wenn offene anwendbare MUSS-Lücken verbleiben. |
| `SASD-GOV-REQ-616` | Assessment in Progress MUSS verwendet werden, wenn die Bewertung begonnen, aber nicht abgeschlossen ist. |
| `SASD-GOV-REQ-617` | Not Assessed MUSS verwendet werden, wenn keine belastbare Bewertung vorliegt. |
| `SASD-GOV-REQ-618` | Eine formale stabile Alignment-Aussage MUSS auf einer veröffentlichten Bezugsfassung mit Approved-Dokumenten beruhen. |
| `SASD-GOV-REQ-619` | Bewertungen gegen Draft- oder Proposed-Dokumente MÜSSEN als Pilot Alignment bezeichnet werden. |
| `SASD-GOV-REQ-620` | Eine Alignment-Aussage DARF NICHT als Zertifizierung bezeichnet werden, solange kein formales Zertifizierungsprogramm existiert. |
| `SASD-GOV-REQ-621` | Eine Alignment-Aussage DARF NICHT gesetzliche, regulatorische oder vertragliche Compliance ersetzen. |
| `SASD-GOV-REQ-622` | Evidence MUSS zwischen geplant, vorbereitet, statisch geprüft und ausgeführt unterscheiden. |
| `SASD-GOV-REQ-623` | Vorhandener Testcode DARF NICHT als erfolgreicher Testlauf gewertet werden. |
| `SASD-GOV-REQ-624` | Eine Workflow-Datei DARF NICHT als erfolgreicher CI-Lauf gewertet werden. |
| `SASD-GOV-REQ-625` | Ein vorbereitetes Patch- oder ZIP-Artefakt DARF NICHT als integrierter Zielstand gewertet werden. |
| `SASD-GOV-REQ-626` | Runtime-Verhalten MUSS durch ausgeführte Nachweise oder nachvollziehbare manuelle Prüfung belegt werden. |
| `SASD-GOV-REQ-627` | Sicherheitsrelevante Aussagen SOLLTEN mit stärkerer Evidenz als reine Dokumentenbeobachtung belegt werden. |
| `SASD-GOV-REQ-628` | Evidenz MUSS den bewerteten Commit oder Artefaktstand zuordnen lassen. |
| `SASD-GOV-REQ-629` | Veraltete Evidenz MUSS bei relevanten Änderungen erneut bewertet werden. |
| `SASD-GOV-REQ-630` | Eine Bewertung MUSS ihren Scope und bewusste Ausschlüsse nennen. |
| `SASD-GOV-REQ-631` | Eine Bewertung SOLLTE eine Requirement Matrix oder gleichwertige nachvollziehbare Zuordnung verwenden. |
| `SASD-GOV-REQ-632` | Ein Release mit Alignment-Aussage MUSS offene Ausnahmen und wesentliche Known Issues sichtbar machen. |
| `SASD-GOV-REQ-633` | Selbstbewertungen MÜSSEN ausdrücklich als Self-Assessment gekennzeichnet werden. |
| `SASD-GOV-REQ-634` | Unabhängige Reviews MÜSSEN Reviewer, Umfang und verwendete Evidenz nennen. |
| `SASD-GOV-REQ-635` | Ein Assessment Record MUSS aufbewahrt werden, solange die zugehörige Alignment-Aussage öffentlich oder betrieblich relevant ist. |
| `SASD-GOV-REQ-636` | Eine widerrufene Alignment-Aussage MUSS mit Grund und Ersatzstatus dokumentiert werden. |
| `SASD-GOV-REQ-637` | Ein Projekt KANN höhere Qualitätsanforderungen einzelner Bereiche anwenden, ohne seine Gesamtstufe vollständig hochzustufen. |
| `SASD-GOV-REQ-638` | Eine niedrigere deklarierte Qualitätsstufe DARF NICHT verwendet werden, um bekannte hohe Risiken zu verschleiern. |
| `SASD-GOV-REQ-639` | Die Bewertung MUSS externe Verpflichtungen zusätzlich berücksichtigen, wenn diese strenger als der SASD Standard sind. |

## 5. Evidenzstufen

| Klasse | Aussagekraft |
|---|---|
| `P` | geplant |
| `A` | Artefakt vorbereitet |
| `S` | statisch geprüft |
| `E` | ausgeführt und Ergebnis erfasst |
| `I` | unabhängig geprüft |

Eine höhere Evidenzklasse ersetzt nicht automatisch fachliche Bewertung. Sie beschreibt, wie direkt der Nachweis den behaupteten Zustand belegt.

## 6. Bewertungsumfang

Ein Assessment nennt mindestens:

- Bezugsfassung des Standards,
- Projektstand,
- Profile und Qualitätsstufe,
- Scope und Ausschlüsse,
- Requirement Matrix,
- Evidenz,
- Ausnahmen und offene Lücken,
- Gesamtstatus,
- verantwortliche Person und Datum.

## 7. Verwandte Dokumente

- [SASD Compliance Template](../../templates/documents/SASD-COMPLIANCE-TEMPLATE.md)
- [Core Requirement Matrix Template](../../templates/documents/CORE-REQUIREMENT-MATRIX-TEMPLATE.md)
- [Ausnahmen](EXCEPTIONS.md)
- [Pilot Evidence Model](../50-reference-implementations/PILOT-EVIDENCE-MODEL.md)
