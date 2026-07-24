---
title: "Ausnahmen und Abweichungen"
document-id: SASD-GOV-006
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
depends-on: [SASD-GOV-001, SASD-GOV-005, SASD-GOV-007]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Ausnahmen und Abweichungen

## 1. Zweck

Dieses Dokument definiert die kontrollierte Abweichung von einer anwendbaren SASD-Anforderung.

## 2. Abgrenzung

| Zustand | Bedeutung |
|---|---|
| `Not Applicable` | Auslösebedingung liegt nicht vor |
| `Open` | Anforderung anwendbar, aber noch nicht erfüllt |
| `Exception Proposed` | Ausnahme beantragt, noch nicht genehmigt |
| `Exception Approved` | Risiko und Kompensation ausdrücklich genehmigt |
| `Alternative Satisfied` | anderes Mittel erfüllt nachweislich dasselbe Ergebnis |

## 3. Normative Anforderungen

| Anforderungs-ID | Normative Anforderung |
|---|---|
| `SASD-GOV-REQ-500` | Eine Ausnahme MUSS sich auf mindestens eine konkrete anwendbare Anforderungs-ID beziehen. |
| `SASD-GOV-REQ-501` | Eine Ausnahme MUSS den betroffenen Projektstand, Bereich oder Release eindeutig benennen. |
| `SASD-GOV-REQ-502` | Eine Ausnahme MUSS die Abweichung und ihre fachliche Begründung beschreiben. |
| `SASD-GOV-REQ-503` | Eine Ausnahme MUSS Risiken und mögliche Auswirkungen dokumentieren. |
| `SASD-GOV-REQ-504` | Eine Ausnahme MUSS kompensierende Maßnahmen oder die begründete Abwesenheit solcher Maßnahmen nennen. |
| `SASD-GOV-REQ-505` | Eine Ausnahme MUSS eine verantwortliche Person oder Rolle besitzen. |
| `SASD-GOV-REQ-506` | Eine Ausnahme MUSS einen Genehmigungsstatus besitzen. |
| `SASD-GOV-REQ-507` | Eine genehmigte Ausnahme MUSS Genehmiger und Datum nennen. |
| `SASD-GOV-REQ-508` | Eine Ausnahme MUSS ein Ablaufdatum, ein Ereignis oder ein dauerhaftes Neubewertungskriterium besitzen. |
| `SASD-GOV-REQ-509` | Eine unbefristete Ausnahme SOLLTE nur verwendet werden, wenn regelmäßige Neubewertung keinen sinnvollen Nutzen bietet. |
| `SASD-GOV-REQ-510` | Eine Ausnahme DARF NICHT verwendet werden, um eine noch nicht bewertete Anforderung als erfüllt darzustellen. |
| `SASD-GOV-REQ-511` | Eine offene Umsetzungslücke DARF NICHT als genehmigte Ausnahme bezeichnet werden. |
| `SASD-GOV-REQ-512` | Not Applicable KANN nur verwendet werden, wenn die Auslösebedingung nachweislich fehlt. |
| `SASD-GOV-REQ-513` | Eine bewusste alternative Umsetzung KANN als erfüllt bewertet werden, wenn das geforderte Ergebnis gleichwertig nachgewiesen ist. |
| `SASD-GOV-REQ-514` | Eine Ausnahme von einem Verbot MUSS besonders auf Missbrauchs-, Security- und Datenschutzrisiken geprüft werden. |
| `SASD-GOV-REQ-515` | Production-Ausnahmen SOLLTEN eine unabhängige Prüfung erhalten, wenn erhebliche Risiken verbleiben. |
| `SASD-GOV-REQ-516` | Ausnahmen mit rechtlicher Wirkung MÜSSEN durch zuständige fachkundige Stellen bewertet werden; der SASD Standard ersetzt keine Rechtsberatung. |
| `SASD-GOV-REQ-517` | Eine Ausnahme MUSS im Alignment- oder Release-Nachweis sichtbar sein, wenn sie den bewerteten Umfang betrifft. |
| `SASD-GOV-REQ-518` | Eine abgelaufene Ausnahme MUSS geschlossen, verlängert oder als offene Lücke neu bewertet werden. |
| `SASD-GOV-REQ-519` | Eine verlängerte Ausnahme MUSS erneut begründet und risikobewertet werden. |
| `SASD-GOV-REQ-520` | Eine geschlossene Ausnahme MUSS Abschlussdatum und Abschlussgrund dokumentieren. |
| `SASD-GOV-REQ-521` | Wiederkehrende ähnliche Ausnahmen SOLLTEN einen Änderungsvorschlag am Standard oder Profil auslösen. |
| `SASD-GOV-REQ-522` | Eine Ausnahme DARF NICHT behaupten, andere externe Verpflichtungen außer Kraft zu setzen. |
| `SASD-GOV-REQ-523` | Das Ausnahmeregister MUSS für Reviewer und Releaseverantwortliche auffindbar sein. |
| `SASD-GOV-REQ-524` | Sensible Ausnahmedetails KÖNNEN vertraulich behandelt werden, MÜSSEN aber in öffentlicher Dokumentation mindestens angemessen abstrahiert sichtbar bleiben, wenn eine Alignment-Aussage betroffen ist. |
| `SASD-GOV-REQ-525` | Eine Ausnahme MUSS zwischen temporärer Risikobehandlung und dauerhafter Designentscheidung unterscheiden. |
| `SASD-GOV-REQ-526` | Eine dauerhafte alternative Designentscheidung SOLLTE zusätzlich als ADR dokumentiert werden. |
| `SASD-GOV-REQ-527` | Eine Ausnahmegenehmigung DARF NICHT pauschal auf unbekannte zukünftige Releases übertragen werden. |

## 4. Mindestinhalt eines Ausnahmeprotokolls

- eindeutige Ausnahme-ID,
- betroffene Anforderungs-IDs,
- Scope und Projektstand,
- Begründung,
- Risiko und Auswirkungen,
- kompensierende Maßnahmen,
- Verantwortlicher,
- Genehmiger und Status,
- Gültigkeit und Neubewertung,
- Abschlusskriterien.

## 5. Verwandte Dokumente

- [Exception Record Template](../../templates/documents/EXCEPTION-RECORD-TEMPLATE.md)
- [Compliance- und Alignment-Modell](COMPLIANCE.md)
- [Änderungsprozess](CHANGE-PROCESS.md)
