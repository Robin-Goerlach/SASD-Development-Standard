---
title: "Ausnahmen und Abweichungen"
document-id: SASD-GOV-006
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
depends-on: [SASD-GOV-001, SASD-GOV-007]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Ausnahmen und Abweichungen

## 1. Zweck

Dieses Dokument definiert, wie ein Projekt begründet und kontrolliert von einer anwendbaren SASD-Anforderung abweichen kann. Eine Ausnahme ist eine bewusste Risikobehandlung, kein Ersatz für eine noch nicht durchgeführte Bewertung.

## 2. Abgrenzung

- **Nicht anwendbar:** Die auslösende Projekteigenschaft liegt nachweislich nicht vor.
- **Offene Lücke:** Die Anforderung ist anwendbar, aber noch nicht erfüllt.
- **Ausnahme:** Die Nichterfüllung wurde mit Risiko, Kompensation, Verantwortung und Gültigkeit ausdrücklich genehmigt.
- **Änderungsvorschlag:** Die allgemeine Standardregel soll für zukünftige Fassungen geändert werden.

Diese Fälle DÜRFEN NICHT miteinander verwechselt werden.

## 3. Mindestinhalt eines Ausnahmeprotokolls

Jede relevante Ausnahme MUSS dokumentieren:

- eindeutige Ausnahme-ID,
- betroffene Anforderungs-ID,
- Projekt, Projektstand und Geltungsbereich,
- Grund der Abweichung,
- Risiko und mögliche Auswirkungen,
- alternative oder kompensierende Maßnahmen,
- verantwortliche Entscheidung und Genehmigung,
- Beginn, Status und Ablauf- oder Prüfdatum,
- Kriterien für Behebung, Verlängerung oder Schließung.

## 4. Bewertung und Genehmigung

Eine Ausnahme MUSS vor ihrer Nutzung bewertet und genehmigt werden. Rückwirkende Dokumentation ist nur bei ungeplanten Vorfällen zulässig und MUSS zeitnah nachgeholt werden.

Der Genehmiger MUSS die fachlichen Auswirkungen verstehen oder geeignete Expertise einbeziehen. Bei Einzelentwicklern KANN dieselbe Person Antragsteller und Genehmiger sein; die strukturierte Selbstprüfung und Risikobegründung bleiben verpflichtend.

## 5. Grenzen

Eine SASD-Ausnahme DARF NICHT:

- gesetzliche, vertragliche oder regulatorische Pflichten außer Kraft setzen,
- ein nicht akzeptiertes hohes Risiko lediglich umbenennen,
- ohne Ablauf- oder Prüfdatum dauerhaft offen bleiben,
- mehrere nicht zusammenhängende Anforderungen pauschal abdecken,
- die gewählte Qualitätsstufe faktisch entwerten.

Für Verbote zum Schutz von Geheimnissen, produktiven Daten, Integrität oder menschlicher Sicherheit sind Ausnahmen nur mit belastbarer Rechtsgrundlage, vertiefter Risikobewertung und angemessenen Schutzmaßnahmen zulässig.

## 6. Kompensierende Maßnahmen

Kompensierende Maßnahmen MÜSSEN das konkrete Risiko adressieren und hinsichtlich Wirksamkeit prüfbar sein. Beispiele sind:

- zusätzliche manuelle Prüfung,
- eingeschränkter Funktions- oder Nutzerumfang,
- technische Isolation,
- erhöhte Überwachung,
- kürzere Gültigkeit,
- zusätzliche Backups oder Rollback-Möglichkeiten,
- unabhängige Freigabe.

## 7. Lebenszyklus

Ausnahmen besitzen mindestens die Zustände:

- `Proposed`,
- `Approved`,
- `Expired`,
- `Closed`,
- `Rejected`.

Eine abgelaufene Ausnahme deckt eine Anforderung nicht mehr ab. Verlängerungen MÜSSEN erneut begründet und genehmigt werden.

## 8. Wiederkehrende Ausnahmen

Wiederkehrende oder projektübergreifende Ausnahmen SOLLTEN als möglicher Änderungsbedarf am Standard bewertet werden. Eine Ausnahme ändert den Standard nicht automatisch.

## 9. Nachweis

Das [Exception Record Template](../../templates/documents/EXCEPTION-RECORD-TEMPLATE.md) KANN verwendet werden. Die Ausnahme MUSS aus der Compliance-Erklärung oder Requirement-Matrix auffindbar sein.
