---
title: "Normative Sprache"
document-id: SASD-GOV-001
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
depends-on: [SASD-FND-004, SASD-FND-005]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Normative Sprache

## 1. Zweck

Dieses Dokument definiert die verbindliche Sprache des SASD Development Standard. Es stellt sicher, dass Anforderungen unabhängig von Dokument, Profil oder Projekt gleich interpretiert werden.

## 2. Schlüsselwörter

| Schlüsselwort | Bedeutung | Behandlung einer Abweichung |
|---|---|---|
| **MUSS / MÜSSEN** | verbindliche positive Anforderung | Erfüllung, Not Applicable oder genehmigte Ausnahme |
| **DARF NICHT / DÜRFEN NICHT** | verbindliches Verbot | nur über genehmigte Ausnahme |
| **SOLLTE / SOLLTEN** | starke Empfehlung | begründete Abweichung |
| **SOLLTE NICHT / SOLLTEN NICHT** | starke Negativempfehlung | begründete Abweichung |
| **KANN / KÖNNEN** | zulässige Option | keine Begründung erforderlich |

## 3. Normative Anforderungen

| Anforderungs-ID | Normative Anforderung |
|---|---|
| `SASD-GOV-REQ-001` | Normative Schlüsselwörter MÜSSEN in Großbuchstaben geschrieben werden, wenn sie Verbindlichkeit ausdrücken. |
| `SASD-GOV-REQ-002` | Die Wörter MUSS und MÜSSEN MÜSSEN als verbindliche positive Anforderung interpretiert werden. |
| `SASD-GOV-REQ-003` | Die Wörter DARF NICHT und DÜRFEN NICHT MÜSSEN als verbindliches Verbot interpretiert werden. |
| `SASD-GOV-REQ-004` | Die Wörter SOLLTE und SOLLTEN MÜSSEN als starke Empfehlung interpretiert werden, deren Abweichung begründet werden muss. |
| `SASD-GOV-REQ-005` | Die Wörter SOLLTE NICHT und SOLLTEN NICHT MÜSSEN als starke Negativempfehlung interpretiert werden. |
| `SASD-GOV-REQ-006` | Die Wörter KANN und KÖNNEN MÜSSEN als zulässige Option ohne Erfüllungspflicht interpretiert werden. |
| `SASD-GOV-REQ-007` | Kleingeschriebene Alltagssprache wie „muss“ oder „kann“ SOLLTE in normativen Dokumenten vermieden werden, wenn keine normative Bedeutung beabsichtigt ist. |
| `SASD-GOV-REQ-008` | Jede normative Anforderung MUSS eine eindeutige Anforderungs-ID besitzen, sobald das zuständige Dokument den Status Proposed erreicht. |
| `SASD-GOV-REQ-009` | Eine Anforderungs-ID DARF NICHT nach Veröffentlichung für eine andere Bedeutung wiederverwendet werden. |
| `SASD-GOV-REQ-010` | Eine normative Anforderung MUSS so formuliert sein, dass Anwendbarkeit und erwartetes Ergebnis nachvollziehbar bewertet werden können. |
| `SASD-GOV-REQ-011` | Eine normative Anforderung SOLLTE genau eine primäre Verpflichtung enthalten. |
| `SASD-GOV-REQ-012` | Mehrere logisch untrennbare Teilpflichten KÖNNEN in einer Anforderung zusammengefasst werden, wenn eine getrennte Bewertung keinen Mehrwert bietet. |
| `SASD-GOV-REQ-013` | Bedingte Anforderungen MÜSSEN die auslösende Bedingung ausdrücklich benennen. |
| `SASD-GOV-REQ-014` | Beispiele, Hinweise und Begründungen DÜRFEN keine zusätzlichen versteckten MUSS-Anforderungen erzeugen. |
| `SASD-GOV-REQ-015` | Tabellen, Checklisten und Vorlagen KÖNNEN normative Dokumente konkretisieren, DÜRFEN ihnen aber NICHT widersprechen. |
| `SASD-GOV-REQ-016` | Bei einem Widerspruch MUSS die in der Inhaltsarchitektur definierte Vorrangregel angewendet werden. |
| `SASD-GOV-REQ-017` | Eine SOLLTE-Abweichung MUSS mindestens kurz begründet werden, wenn sie ein relevantes Risiko, eine Schnittstelle oder einen langfristig gepflegten Projektbestand betrifft. |
| `SASD-GOV-REQ-018` | Eine MUSS-Abweichung MUSS nach dem Ausnahmeprozess dokumentiert und genehmigt werden. |
| `SASD-GOV-REQ-019` | Eine nicht anwendbare Anforderung MUSS als Not Applicable mit begründeter fehlender Auslösebedingung dokumentiert werden, wenn ein formales Assessment durchgeführt wird. |
| `SASD-GOV-REQ-020` | Übersetzungen MÜSSEN kenntlich machen, ob sie autoritativ oder informativ sind. |
| `SASD-GOV-REQ-021` | Bei Bedeutungsunterschieden MUSS die als authoritative gekennzeichnete Fassung maßgeblich sein. |
| `SASD-GOV-REQ-022` | Normative Begriffe DÜRFEN NICHT zur bloßen Betonung verwendet werden. |
| `SASD-GOV-REQ-023` | Anforderungen SOLLTEN aktiv, präzise und ohne unnötige Mehrdeutigkeit formuliert werden. |
| `SASD-GOV-REQ-024` | Unbestimmte Begriffe wie „angemessen“, „wesentlich“ oder „kritisch“ MÜSSEN durch Kontext, Kriterien oder dokumentierte Projektentscheidung konkretisiert werden. |

## 4. Formulierungsregeln

Normative Anforderungen folgen bevorzugt diesem Muster:

```text
<Subjekt oder Geltungsbereich> <normatives Schlüsselwort> <prüfbares Ergebnis> [unter <Bedingung>].
```

Beispiel:

> Ein veröffentlichtes Release MUSS einem eindeutigen Git-Tag zugeordnet sein.

Nicht geeignet sind reine Wunschformulierungen, rhetorische Aussagen oder Anforderungen ohne erkennbare Bewertungsmöglichkeit.

## 5. Verhältnis zu Qualitätsstufen

Eine Qualitätsstufe ändert nicht die Bedeutung eines Schlüsselworts. Sie entscheidet, welche Anforderungen anwendbar werden oder welche zusätzliche Konkretisierung gilt. Eine als MUSS anwendbare Anforderung bleibt verbindlich.

## 6. Informative Inhalte

Abschnitte mit Überschriften wie „Begründung“, „Beispiel“, „Hinweis“ oder „Rationale“ sind informativ, sofern sie keine ausdrücklich referenzierte normative Anforderung wiedergeben.

## 7. Verwandte Dokumente

- [Inhaltsarchitektur](../00-foundation/CONTENT-ARCHITECTURE.md)
- [Ausnahmen und Abweichungen](EXCEPTIONS.md)
- [Compliance- und Alignment-Modell](COMPLIANCE.md)
