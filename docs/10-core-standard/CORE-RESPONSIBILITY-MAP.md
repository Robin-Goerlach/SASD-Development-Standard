---
title: "Verantwortungsmatrix des Core Standard"
document-id: SASD-REF-002
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
depends-on: [SASD-CORE-001, SASD-CORE-002, SASD-CORE-003, SASD-CORE-004, SASD-CORE-005, SASD-CORE-006, SASD-CORE-007, SASD-CORE-008, SASD-CORE-009, SASD-CORE-010, SASD-CORE-011, SASD-CORE-012, SASD-CORE-013]
normative-keywords: []
---

# Verantwortungsmatrix des Core Standard

## 1. Zweck

Diese informative Matrix grenzt die Zuständigkeiten der Core-Dokumente voneinander ab. Sie hilft Autoren, neue Regeln am richtigen Ort zu ergänzen und absichtliche Querschnittsanforderungen von unnötigen Duplikaten zu unterscheiden.

## 2. Primäre Zuständigkeiten

| Dokument | Leitfrage | Primäre Verantwortung | Nicht primär zuständig für |
|---|---|---|---|
| Projektlebenszyklus | **Wann** wird etwas entschieden oder geprüft? | Phasen, Gates, Übergänge, Projektstatus | Detailregeln einzelner Fachbereiche |
| Anforderungen | **Was** soll erreicht oder verhindert werden? | Problem, Scope, Anforderungen, Akzeptanz, Priorisierung, Traceability | konkrete Architektur- oder Testtechnik |
| Architektur | **Wie ist das System strukturiert?** | Grenzen, Komponenten, Abhängigkeiten, Datenflüsse, Qualitätsattribute, ADR-Inhalt | langfristige Ablage von Wissen |
| Dokumentation | **Wie wird Information auffindbar und aktuell gehalten?** | Source of Truth, Dokumentrollen, Schreib- und Pflegequalität | fachlicher Inhalt anderer Standards |
| Repository | **Wo und wie werden Änderungen versioniert?** | Repository-Aufbau, Git, Plattformkonfiguration, Branches, Artefaktablage | fachliche Releasefreigabe |
| Qualitätsstufen | **Wie tief muss eine Regel angewendet werden?** | Klassifikation, Skalierung, Anwendbarkeit, Hierarchie | fachliche Detailkontrollen |
| Qualität | **Wann ist eine Änderung gut genug?** | Qualitätsziele, Definition of Done, Reviews, statische Prüfung, Schulden | Testmethoden im Detail |
| Sicherheit | **Wie werden Schutzbedarf und Risiken kontrolliert?** | Security, Datenschutz, Secrets, Supply Chain, Schwachstellen | allgemeiner Wartungsprozess |
| Tests | **Wie wird erwartetes Verhalten nachgewiesen?** | Teststrategie, Testarten, Daten, Umgebungen, Nachweise | Releaseidentität und Veröffentlichung |
| Releases | **Wie wird ein Stand freigegeben und ausgeliefert?** | Version, Umfang, Freigabe, Release Notes, Artefakte, Rollback | täglicher Betrieb nach Freigabe |
| Wartung | **Wie bleibt das Projekt nutzbar und wiederherstellbar?** | Updates, Betrieb, Diagnose, Backup, Incident, Migration, EOL | einmalige Releaseentscheidung |
| Wissensmanagement | **Wie bleibt Wissen erhalten und übertragbar?** | ADR-Aufbewahrung, Runbooks, Lessons Learned, Quellen, Übergabe | Definition der Architekturentscheidung selbst |
| KI-gestützte Entwicklung | **Wie wird KI sicher und überprüfbar eingesetzt?** | Kontextschutz, Prüfung, Agentenrechte, Promptqualität, KI-Artefakte | allgemeine Dokument- oder Testregeln |

## 3. Zulässige Querschnittsanforderungen

Ein Thema darf in mehreren Dokumenten erscheinen, wenn jedes Dokument eine andere Verantwortung beschreibt. Beispiele:

| Thema | Dokumente | Abgrenzung |
|---|---|---|
| Geheimnisse | Security, Documentation, Repository, AI | Security definiert den Schutz; andere Dokumente verbieten konkrete Ablage- oder Übertragungswege. |
| Architekturentscheidungen | Architecture, Knowledge Management, Lifecycle | Architecture definiert Inhalt; Knowledge Management Aufbewahrung; Lifecycle Zeitpunkt und Gate. |
| Backup und Restore | Security, Maintenance, Testing | Security definiert Schutz; Maintenance Betrieb und Ziele; Testing den Wirksamkeitsnachweis. |
| Provenance und Signaturen | Repository, Releases, Security | Repository definiert Ablage/Plattform; Releases Freigabeumfang; Security Risikozweck. |
| Prompts | AI, Knowledge Management, Documentation | AI definiert Erstellung und Prüfung; Knowledge Management Aufbewahrung; Documentation Source of Truth. |
| Traceability | Requirements, Testing, Releases | Requirements definiert Beziehung; Testing und Releases liefern konkrete Nachweise. |

## 4. Regel für neue Anforderungen

Vor einer neuen Core-Anforderung sollte geprüft werden:

1. Welches Dokument besitzt die primäre fachliche Verantwortung?
2. Ist die Aussage dort bereits vorhanden?
3. Benötigt ein zweites Dokument wirklich eine eigene, anders abgegrenzte Kontrollhandlung?
4. Reicht stattdessen ein Verweis auf die bestehende Anforderung?
5. Entsteht ein abweichender Verbindlichkeitsgrad oder ein Konflikt?

Der [Core Consistency Validator](../../tooling/validate-core-consistency.py) erkennt exakte Textduplikate. Fachlich ähnliche Anforderungen benötigen weiterhin eine inhaltliche Prüfung.
