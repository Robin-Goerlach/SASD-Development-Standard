---
title: "Foundation and Governance Review 0.8.0"
document-id: SASD-REF-GOV-002
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
depends-on: [SASD-FND-001, SASD-FND-002, SASD-FND-003, SASD-FND-004, SASD-FND-005, SASD-FND-006, SASD-FND-007, SASD-GOV-001, SASD-GOV-002, SASD-GOV-003, SASD-GOV-004, SASD-GOV-005, SASD-GOV-006, SASD-GOV-007]
normative-keywords: []
---

# Foundation and Governance Review 0.8.0

## 1. Reviewziel

Der Review prüfte die Foundation- und Governance-Schicht auf Vollständigkeit, interne Widersprüche, eindeutige Zuständigkeiten, Solo-Maintainer-Tauglichkeit und Freigabereife.

## 2. Umfang

Geprüft wurden:

- sieben Foundation-Dokumente,
- sieben normative Governance-Dokumente,
- Inhaltsarchitektur und Dokumentkatalog,
- Metadaten und Abhängigkeiten,
- Versionierungs- und Änderungsregeln,
- Ausnahmen und Alignment,
- Version-1.0-Akzeptanzkriterien,
- angrenzende Pilot-Evidenzregeln.

## 3. Wesentliche Befunde

### 3.1 Versionierung und Änderungsprozess waren zu knapp

Die bisherigen Dokumente beschrieben Semantic Versioning und Änderungsvorschläge nur grundsätzlich. Es fehlten klare Regeln für Dokumentversionen, Tags, Release Records, Änderungsarten, Breaking Changes und Security Corrections.

**Korrektur:** Beide Dokumente wurden vollständig ausgearbeitet und auf Proposed 0.8.0 angehoben.

### 3.2 Governance-Anforderungen waren nicht einzeln referenzierbar

Core, Profile und Prozesse besaßen stabile Anforderungs-IDs, die Governance jedoch nicht.

**Korrektur:** 232 eindeutige IDs im Bereich `SASD-GOV-REQ-001` bis `SASD-GOV-REQ-639` wurden in reservierten Dokumentbereichen eingeführt.

### 3.3 Fachliche Freigabe und GitHub Release waren nicht sauber getrennt

Ein Tag oder Release durfte nicht versehentlich als fachliche Approval interpretiert werden.

**Korrektur:** Dokumentlebenszyklus und Versionierung trennen nun `reviewed`, `approved` und `published` ausdrücklich.

### 3.4 Solo-Maintainer-Freigabe benötigte eine belastbare Regel

Der Standard richtet sich ausdrücklich an Einzelentwickler. Ein obligatorischer zweiter Reviewer wäre daher unpraktikabel.

**Korrektur:** Ein zeitlich oder methodisch getrennter dokumentierter Selbstreview ist zulässig; fachkundige externe Prüfung bleibt für besondere Risiken empfohlen.

### 3.5 Evidence und Alignment mussten Pilotfeedback aufnehmen

Der erste Pilot zeigte, dass vorbereitete Artefakte, Testcode und Workflowdateien nicht mit ausgeführten Ergebnissen gleichgesetzt werden dürfen.

**Korrektur:** Diese Unterscheidung ist jetzt direkt in `COMPLIANCE.md` normativ verankert.

## 4. Reviewmethoden

- Vergleich der Dokumentzuständigkeiten,
- Prüfung der Status- und Versionsübergänge,
- Prüfung aller Dokumentabhängigkeiten,
- Anwendungsfälle für Solo-Maintainer, Open Source und Production,
- Review von Release- und Änderungsszenarien,
- Prüfung gegen bisherige Pilotbefunde,
- Ausführung aller Repositoryvalidatoren.

## 5. Ergebnis

Die Foundation- und Governance-Dokumente sind fachlich konsistent und **bereit für den formalen Maintainer-Approval-Review**. Dieser Reviewnachweis selbst erteilt noch keine Freigabe.

## 6. Offene Freigabeschritte

1. Maintainer liest Projektcharta, Scope, Prinzipien und Glossar.
2. Maintainer prüft die sieben Governance-Dokumente anhand der Approval Checklist.
3. Offene Befunde werden geschlossen oder dokumentiert.
4. Ein Document Approval Record wird erstellt.
5. Erst danach werden die freigegebenen Dokumente auf `Approved` gesetzt.
