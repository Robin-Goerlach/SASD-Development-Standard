---
title: "Anforderungsmanagement"
document-id: SASD-CORE-002
document-type: normative
status: Approved
version: 0.9.0
standard-version: "1.0"
approval-bundle: SASD-NORMATIVE-BASELINE-0.9.0
approval-review-state: approved
language: de
authoritative: true
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
approved-on: 2026-07-24
approval-record: SASD-REF-BASELINE-007
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core]
depends-on: [SASD-FND-003, SASD-GOV-001, SASD-CORE-001, SASD-CORE-006]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Anforderungsmanagement

## 1. Zweck

Dieses Dokument definiert, wie Ziele, Scope, funktionale und nicht funktionale Anforderungen, Annahmen, Akzeptanzkriterien und Änderungen nachvollziehbar verwaltet werden.

## 2. Geltungsbereich

Die Anforderungen dürfen je nach Projektgröße in einer einzelnen Projektbeschreibung, in Issues oder in eigenständigen Dokumenten geführt werden. Entscheidend sind Auffindbarkeit, Eindeutigkeit, Prüfbarkeit und Änderungsnachvollziehbarkeit.

## 3. Begriffe

- **Ziel:** angestrebter Nutzen oder Zustand.
- **Anforderung:** nachprüfbare Eigenschaft, Fähigkeit oder Einschränkung.
- **Akzeptanzkriterium:** Bedingung, anhand derer die Erfüllung bewertet wird.
- **Annahme:** noch nicht bestätigte Grundlage einer Entscheidung.
- **Nicht-Ziel:** ausdrücklich ausgeschlossener Umfang.
- **Constraint:** technische, rechtliche, zeitliche oder organisatorische Einschränkung.

## 4. Normative Anforderungen

### 4.1 Problem, Nutzen und Zielgruppe

| ID | Anforderung |
|---|---|
| SASD-REQ-001 | Das zu lösende Problem MUSS verständlich beschrieben werden. |
| SASD-REQ-002 | Der erwartete Nutzen MUSS von der geplanten technischen Lösung getrennt beschrieben werden. |
| SASD-REQ-003 | Zielgruppen, Nutzer oder betroffene Stakeholder MÜSSEN benannt werden, soweit sie bekannt sind. |
| SASD-REQ-004 | Erfolgsindikatoren oder überprüfbare Projektziele SOLLTEN definiert werden. |

### 4.2 Scope und Nicht-Ziele

| ID | Anforderung |
|---|---|
| SASD-REQ-010 | Der aktuelle Scope MUSS dokumentiert sein. |
| SASD-REQ-011 | Wesentliche Nicht-Ziele MÜSSEN dokumentiert werden, wenn sonst Fehlannahmen oder Scope Creep wahrscheinlich sind. |
| SASD-REQ-012 | Annahmen und offene Fragen MÜSSEN als solche gekennzeichnet sein. |
| SASD-REQ-013 | Neue Anforderungen DÜRFEN NICHT stillschweigend in einen freigegebenen Meilenstein aufgenommen werden. Auswirkungen MÜSSEN bewertet werden. |

### 4.3 Anforderungstypen

Ein Projekt SOLLTE mindestens folgende Arten unterscheiden:

- funktionale Anforderungen,
- Qualitäts- oder nicht funktionale Anforderungen,
- Sicherheits- und Datenschutzanforderungen,
- Betriebs- und Wartungsanforderungen,
- Daten- und Migrationsanforderungen,
- rechtliche, lizenzbezogene oder organisatorische Constraints.

| ID | Anforderung |
|---|---|
| SASD-REQ-020 | Anforderungen MÜSSEN so formuliert sein, dass eine fachkundige Person erkennen kann, was erfüllt werden soll. |
| SASD-REQ-021 | Wesentliche Qualitätsattribute wie Sicherheit, Wartbarkeit, Performance, Verfügbarkeit oder Bedienbarkeit MÜSSEN konkretisiert werden, wenn sie für den Projekterfolg relevant sind. |
| SASD-REQ-022 | Lösungsdetails SOLLTEN nicht als fachliche Anforderungen formuliert werden, sofern keine echte technische Einschränkung besteht. |
| SASD-REQ-023 | Widersprüchliche Anforderungen MÜSSEN aufgelöst oder ausdrücklich als offener Konflikt dokumentiert werden. |

### 4.4 Identifikation und Status

| ID | Anforderung |
|---|---|
| SASD-REQ-030 | Für Recommended und Production MÜSSEN wesentliche Anforderungen eine stabile Kennung oder eine anderweitig eindeutige Referenz besitzen. |
| SASD-REQ-031 | Der Status einer Anforderung MUSS unterscheidbar sein, beispielsweise Proposed, Accepted, Implemented, Verified, Rejected oder Deferred. |
| SASD-REQ-032 | Quelle, Begründung oder verantwortlicher Stakeholder SOLLTE für risikoreiche oder umstrittene Anforderungen dokumentiert werden. |
| SASD-REQ-033 | Gelöschte oder verworfene Anforderungen SOLLTEN nachvollziehbar bleiben, wenn ihre Historie spätere Entscheidungen erklärt. |

Empfohlene Kennungskategorien:

```text
REQ-F-###    funktional
REQ-Q-###    Qualitätsattribut
REQ-SEC-###  Sicherheit
REQ-OPS-###  Betrieb
REQ-DATA-### Daten und Migration
REQ-CON-###  Constraint
```

### 4.5 Akzeptanzkriterien

| ID | Anforderung |
|---|---|
| SASD-REQ-040 | Jede wesentliche Anforderung MUSS ein prüfbares Akzeptanzkriterium oder einen definierten Nachweis besitzen. |
| SASD-REQ-041 | Akzeptanzkriterien MÜSSEN beobachtbares Verhalten oder messbare Eigenschaften beschreiben. |
| SASD-REQ-042 | Reine Formulierungen wie „schnell“, „sicher“ oder „benutzerfreundlich“ DÜRFEN NICHT ohne Kontext oder Prüfkriterium als abschließende Anforderung verwendet werden. |
| SASD-REQ-043 | Bei nicht vollständig automatisierbaren Kriterien MUSS die manuelle Prüfung beschrieben werden. |

### 4.6 Priorisierung

| ID | Anforderung |
|---|---|
| SASD-REQ-050 | Anforderungen SOLLTEN priorisiert werden. |
| SASD-REQ-051 | Priorität MUSS von Umsetzungsstatus und technischer Schwierigkeit unterscheidbar sein. |
| SASD-REQ-052 | Sicherheits-, Datenintegritäts- und Wiederherstellungsanforderungen DÜRFEN NICHT allein wegen fehlender Sichtbarkeit für Endnutzer als niedrig priorisiert behandelt werden. |
| SASD-REQ-053 | Ein Meilenstein MUSS einen klar abgegrenzten Anforderungssatz besitzen. |

Ein mögliches Prioritätsschema ist Must, Should, Could, Won't for now. Andere nachvollziehbare Modelle sind zulässig.

### 4.7 Nachverfolgbarkeit

| ID | Anforderung |
|---|---|
| SASD-REQ-060 | Für Recommended MUSS nachvollziehbar sein, welche Tests oder Abnahmen wesentliche Anforderungen verifizieren. |
| SASD-REQ-061 | Für Production MUSS eine bidirektionale Nachverfolgbarkeit zwischen wesentlichen Anforderungen, Implementierungsartefakten, Risiken und Verifikationsnachweisen möglich sein. |
| SASD-REQ-062 | Architekturentscheidungen, die Anforderungen wesentlich einschränken oder verändern, MÜSSEN referenziert werden. |
| SASD-REQ-063 | Ein Test ohne erkennbaren Zweck SOLLTE ebenso vermieden werden wie eine wesentliche Anforderung ohne Nachweis. |

### 4.8 Änderungen

| ID | Anforderung |
|---|---|
| SASD-REQ-070 | Änderungen an freigegebenen Anforderungen MÜSSEN hinsichtlich Scope, Architektur, Sicherheit, Daten, Tests, Dokumentation, Migration und Betrieb bewertet werden. |
| SASD-REQ-071 | Die Entscheidung über wesentliche Änderungen MUSS nachvollziehbar dokumentiert werden. |
| SASD-REQ-072 | Veraltete Anforderungen MÜSSEN als ersetzt, verworfen oder nicht mehr anwendbar gekennzeichnet werden. |
| SASD-REQ-073 | Änderungen DÜRFEN NICHT nachträglich so dokumentiert werden, als seien sie von Anfang an unverändert geplant gewesen. |

## 5. Zuordnung zu Qualitätsstufen

| Element | Minimum | Recommended | Production |
|---|---|---|---|
| Problem, Ziel, Scope | kompakt MUSS | strukturiert MUSS | geprüft und freigegeben MUSS |
| Nicht-Ziele | SOLLTE | MUSS | MUSS |
| stabile Kennungen | KANN | wesentliche Anforderungen MUSS | alle freigaberelevanten Anforderungen MUSS |
| Akzeptanzkriterien | für kritische Nutzung MUSS | für wesentliche Anforderungen MUSS | vollständig und nachvollziehbar MUSS |
| Traceability | KANN | Anforderung zu Nachweis MUSS | bidirektional MUSS |
| formale Änderungsbewertung | KANN | wesentliche Änderungen SOLLTE | wesentliche Änderungen MUSS |

## 6. Verantwortlichkeiten

Der Projektverantwortliche entscheidet über Scope und Priorität. Fachliche Stakeholder bestätigen Anforderungen, soweit vorhanden. Entwickler und Reviewer weisen auf technische, sicherheitsbezogene und betriebliche Konsequenzen hin.

## 7. Nachweise und Prüfkriterien

Geeignete Nachweise sind:

- Project Charter, Lastenheft oder Requirements-Dokument,
- priorisierte Issues oder Backlog,
- Akzeptanzkriterien,
- Traceability-Tabelle,
- Änderungsentscheidungen,
- Test- und Abnahmeberichte.

## 8. Ausnahmen und Abweichungen

Kleine Projekte dürfen Anforderungen in README oder Roadmap integrieren. Die Kompaktheit DARF nicht dazu führen, dass Zweck, Scope, Risiken oder Akzeptanz unklar werden.

## 9. Verwandte Dokumente

- [Projektlebenszyklus](PROJECT-LIFECYCLE.md)
- [Architekturstandard](ARCHITECTURE.md)
- [Teststandard](TESTING.md)
- [Dokumentationsstandard](DOCUMENTATION.md)
