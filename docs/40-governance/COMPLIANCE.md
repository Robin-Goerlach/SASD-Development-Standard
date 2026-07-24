---
title: "Compliance- und Alignment-Modell"
document-id: SASD-GOV-007
document-type: normative
status: Proposed
version: 0.2.0
standard-version: "1.0"
language: de
authoritative: true
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-CORE-006, SASD-GOV-001, SASD-GOV-006]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Compliance- und Alignment-Modell

## 1. Zweck

Dieses Dokument definiert, wie ein Projekt die Anwendung des SASD Development Standard bewertet, nachweist und kommuniziert. Der Standard verwendet bewusst den Begriff **Alignment**, solange keine formale Zertifizierung oder externe Auditierung angeboten wird.

## 2. Bezugsrahmen

Jede Bewertung MUSS eindeutig benennen:

- die angewendete Standardversion oder den Commit,
- den Status der bewerteten Standarddokumente,
- die angewendeten Profile,
- die primäre Qualitätsstufe,
- bereichsweise Hochstufungen,
- den bewerteten Projektstand oder Release,
- das Datum und die verantwortliche Person.

Eine Aussage ohne diesen Bezugsrahmen ist nicht reproduzierbar.

## 3. Statuswerte

| Status | Bedeutung |
|---|---|
| `Not Assessed` | Es wurde noch keine strukturierte Bewertung durchgeführt. |
| `Assessment in Progress` | Die Bewertung läuft; Ergebnisse oder Nachweise sind unvollständig. |
| `Partially Aligned` | Der Standard wird angewendet, aber Pflichtanforderungen sind offen, nicht bewertet oder nicht gültig abgedeckt. |
| `Aligned with Exceptions` | Alle anwendbaren Pflichtanforderungen sind erfüllt oder durch gültige, dokumentierte Ausnahmen abgedeckt. |
| `Aligned` | Alle anwendbaren MUSS- und DARF-NICHT-Anforderungen sind erfüllt; notwendige Begründungen und Nachweise sind vorhanden. |

Ein Projekt DARF den Status `Aligned` oder `Aligned with Exceptions` nur für einen eindeutig identifizierbaren Projektstand verwenden.

## 4. Status einzelner Anforderungen

Für jede bewertete Anforderung wird einer der folgenden Werte verwendet:

| Requirement status | Bedeutung |
|---|---|
| `Satisfied` | Die Anforderung ist erfüllt und der Nachweis ist benannt. |
| `Not Applicable` | Die auslösende Projekteigenschaft liegt nicht vor; die Begründung ist dokumentiert. |
| `Exception` | Eine gültige Ausnahme nach `EXCEPTIONS.md` deckt die Abweichung ab. |
| `Open` | Die Anforderung ist anwendbar, aber noch nicht erfüllt. |
| `Not Assessed` | Die Anwendbarkeit oder Erfüllung wurde noch nicht bewertet. |

`Not Applicable` DARF NICHT verwendet werden, um Aufwand zu vermeiden oder eine fehlende Umsetzung zu verschleiern.

## 5. Bewertungsvorgehen

Eine Bewertung umfasst mindestens:

1. Projektklassifikation und Qualitätsstufe bestätigen,
2. anwendbare Profile bestimmen,
3. bedingte Anforderungen gegen die Projekteigenschaften prüfen,
4. MUSS- und DARF-NICHT-Anforderungen bewerten,
5. relevante SOLLTE- und SOLLTE-NICHT-Abweichungen begründen,
6. Nachweise verlinken oder eindeutig benennen,
7. offene Maßnahmen und Ausnahmen erfassen,
8. Gesamtstatus bestimmen,
9. nächste Prüfung festlegen.

## 6. Nachweise

Nachweise KÖNNEN unter anderem sein:

- Dokumente und konkrete Abschnitte,
- Quellcode, Konfiguration oder Repository-Einstellungen,
- Build-, Test- oder Scanergebnisse,
- Releases, Prüfsummen oder Artefakte,
- ADRs und Freigabeentscheidungen,
- Betriebs-, Backup- und Wiederherstellungsnachweise,
- Reviewprotokolle und ausgefüllte Checklisten.

Nachweise MÜSSEN so konkret sein, dass eine spätere Prüfung erkennen kann, worauf sich die Bewertung stützte. Ein bloßer Eintrag „erledigt“ ist für wesentliche Production-Anforderungen nicht ausreichend.

## 7. Bewertung von Draft und Proposed

Draft- und Proposed-Dokumente sind nach dem Dokumentlebenszyklus noch nicht verbindlich. Projekte KÖNNEN sie pilotieren und einen **Pilot Alignment Status** dokumentieren.

Eine solche Vorabbewertung MUSS ausdrücklich erkennen lassen, dass sie sich nicht auf eine freigegebene Standardversion bezieht. Sie dient dazu, Unklarheiten, übermäßigen Aufwand und fehlende Nachweise vor der Freigabe des Standards zu erkennen.

## 8. Einzelentwickler und Selbstprüfung

Eine Person KANN Autor, Implementierer, Reviewer und Freigabeverantwortlicher sein. In diesem Fall:

- MUSS die Bewertung anhand einer strukturierten Matrix oder Checkliste erfolgen,
- SOLLTE zwischen Umsetzung und Selbstreview ein zeitlicher oder methodischer Abstand liegen,
- SOLLTEN kritische Annahmen und Risiken ausdrücklich erneut geprüft werden,
- SOLLTE bei hohem Risiko eine unabhängige Fachprüfung eingeholt werden.

KI-Reviews KÖNNEN Hinweise liefern, ersetzen aber keine menschliche Verantwortung und keine ausdrücklich verlangte unabhängige Prüfung.

## 9. Pflege und Gültigkeit

Eine Bewertung MUSS erneut geprüft werden, wenn sich mindestens einer der folgenden Punkte wesentlich ändert:

- Qualitätsstufe oder Profile,
- Scope, Architektur oder Datenarten,
- Betriebsmodell oder Nutzerkreis,
- Sicherheits- oder Ausfallrisiko,
- Hauptversion des Projekts,
- angewendete Standardversion.

Production-Projekte SOLLTEN zusätzlich regelmäßige Überprüfungsintervalle festlegen.

## 10. Kommunikation

README oder Projektdokumentation SOLLTEN den Gesamtstatus kompakt nennen und auf die vollständige Compliance-Erklärung verweisen.

Ein Projekt DARF keine externe Zertifizierung, Auditierung oder Garantie behaupten, die durch den SASD Development Standard oder eine Selbstauskunft nicht tatsächlich erbracht wird.

## 11. Verwandte Dokumente

- [Qualitätsstufen und Anwendbarkeit](../10-core-standard/QUALITY-LEVELS.md)
- [Ausnahmen und Abweichungen](EXCEPTIONS.md)
- [Compliance-Template](../../templates/documents/SASD-COMPLIANCE-TEMPLATE.md)
- [Requirement-Matrix-Template](../../templates/documents/CORE-REQUIREMENT-MATRIX-TEMPLATE.md)
