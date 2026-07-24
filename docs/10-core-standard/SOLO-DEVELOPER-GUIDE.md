---
title: "Leitfaden für Einzelentwickler"
document-id: SASD-REF-003
document-type: informative
status: Draft
version: 0.1.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core]
depends-on: [SASD-CORE-001, SASD-CORE-004, SASD-CORE-006, SASD-CORE-007, SASD-GOV-006, SASD-GOV-007]
normative-keywords: []
---

# Leitfaden für Einzelentwickler

## 1. Ziel

Der SASD Development Standard soll Qualität erhöhen, nicht einen Einzelentwickler mit Unternehmensbürokratie belasten. Dieser Leitfaden zeigt, wie mehrere Rollen zusammengelegt und Inhalte kompakt geführt werden können, ohne wichtige Entscheidungen oder Risiken zu verlieren.

## 2. Grundsatz: Inhalte statt Dateimenge

Der Standard verlangt erforderliche **Informationen und Nachweise**, nicht für jeden Inhalt zwingend eine eigene Datei.

Ein kleines Minimum-Projekt kann Projektziel, Scope, Architekturübersicht, Testschritte und Wartungsstatus in einem guten README führen. Ein Production-Projekt benötigt aufgrund von Risiko, Betrieb und Nachweisbedarf meist getrennte Dokumente.

## 3. Kompakte Artefaktsätze

### Minimum

Ein kleiner Artefaktsatz kann bestehen aus:

- `README.md` mit Ziel, Scope, Nutzung, einfacher Architektur, Testweg und Einschränkungen,
- Lizenzstatus,
- kleiner Roadmap oder Aufgabenliste,
- Security-Baseline,
- Changelog oder nachvollziehbaren Tags bei Releases,
- benanntem Wartungsstatus.

### Recommended

Typischerweise zusätzlich:

- strukturierte Anforderungen oder gepflegte Issues,
- Architekturdokument und wesentliche ADRs,
- Teststrategie und reproduzierbare Prüfungen,
- Sicherheits- und Wartungsbetrachtung,
- Release Notes und Changelog,
- `docs/SASD-COMPLIANCE.md`.

### Production

Typischerweise zusätzlich:

- formalisierte Risiko- und Bedrohungsbetrachtung,
- Deployment-, Betriebs- und Diagnoseanleitung,
- Backup-, Restore-, Rollback- und Incident-Verfahren,
- releasebezogene Prüfnachweise,
- Abhängigkeits- und Supply-Chain-Nachweise,
- geregelte Freigabe und End-of-Life-Planung.

## 4. Rollen zusammenlegen

Eine Person kann Product Owner, Entwickler, Tester, Maintainer und Reviewer sein. Sinnvolle Ersatzmechanismen für fehlende personelle Trennung sind:

- feste Checklisten statt Erinnerung aus dem Kopf,
- zeitversetzter Selbstreview,
- Vergleich gegen Anforderungen vor dem Lesen der Implementierung,
- automatisierte Tests und statische Prüfungen,
- getrennte Release-Checkliste,
- dokumentierte Annahmen und offene Risiken,
- punktuelle externe Prüfung bei hohem Risiko.

## 5. Praktischer Arbeitsrhythmus

### Projektstart

1. Problem, Nutzen, Scope und Nicht-Ziele festhalten.
2. Qualitätsstufe und Profile wählen.
3. Risiken und bereichsweise Hochstufungen bestimmen.
4. ersten Meilenstein und Definition of Done festlegen.

### Während eines Meilensteins

1. Änderung einer Anforderung, einem Fehler oder einer Wartungsaufgabe zuordnen.
2. Architektur- und Sicherheitsfolgen prüfen.
3. Tests und Dokumentation im selben Änderungsvorgang aktualisieren.
4. offene Schulden und Annahmen sichtbar halten.

### Vor Commit oder Merge

1. Build und relevante Tests ausführen.
2. Diff ohne Nebenabsicht lesen.
3. Geheimnisse, Debugreste und unbeabsichtigte Artefakte prüfen.
4. Commit verständlich beschreiben.

### Vor Release

1. Definition of Done und Release-Checkliste ausführen.
2. Release Notes, Version und Artefakte prüfen.
3. Migration, Backup, Restore oder Rollback bewerten.
4. Compliance-Stand und bekannte Einschränkungen aktualisieren.

### Nach Release oder Vorfall

1. Fehler, Supportfragen und Lessons Learned erfassen.
2. Anforderungen, Checklisten oder Tooling verbessern.
3. technische Schulden priorisieren.

## 6. Was nicht erforderlich ist

Für kleine Projekte ist normalerweise nicht erforderlich:

- jede Rolle durch eine andere Person zu besetzen,
- für jeden Abschnitt ein eigenes Dokument anzulegen,
- formale Meetings oder Freigabegremien zu simulieren,
- umfassende Diagrammsammlungen ohne Entscheidungsnutzen zu pflegen,
- Production-Nachweise für ein ungefährliches Wegwerfexperiment zu erzeugen.

Nicht zulässig ist dagegen, Risiken oder Pflichtinhalte allein mit dem Hinweis „Einzelprojekt“ zu ignorieren.

## 7. Hilfsmittel

- [Core-Standard-Adoptionscheckliste](../../checklists/project-initiation/CORE-STANDARD-ADOPTION-CHECKLIST.md)
- [Selbstreview-Checkliste](../../checklists/development/CORE-STANDARD-SELF-REVIEW-CHECKLIST.md)
- [Definition of Done](../../checklists/development/DEFINITION-OF-DONE-CHECKLIST.md)
- [Compliance-Template](../../templates/documents/SASD-COMPLIANCE-TEMPLATE.md)
- [Requirement-Matrix-Template](../../templates/documents/CORE-REQUIREMENT-MATRIX-TEMPLATE.md)
