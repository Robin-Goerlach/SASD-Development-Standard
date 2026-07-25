---
title: "Wissensmanagement"
document-id: SASD-CORE-012
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
depends-on: [SASD-FND-003, SASD-GOV-001, SASD-CORE-003, SASD-CORE-004, SASD-CORE-006]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Wissensmanagement

## 1. Zweck

Dieses Dokument definiert, wie Projektwissen dauerhaft, auffindbar, verständlich und übergabefähig gespeichert wird. Wissen darf nicht ausschließlich im Kopf einzelner Personen, in flüchtigen Chats oder in nicht dokumentierten Routinen verbleiben.

## 2. Geltungsbereich

Projektwissen umfasst Anforderungen, Entscheidungen, Architektur, Betriebswissen, Fehlerbilder, Wiederherstellung, Lessons Learned, Glossare, externe Quellen und wiederverwendbare Prompts.

## 3. Normative Anforderungen

### 3.1 Wissensquellen und Source of Truth

| ID | Anforderung |
|---|---|
| SASD-KM-001 | Ein Projekt MUSS benennen, wo verbindliches Projektwissen gespeichert wird. |
| SASD-KM-002 | Chats, E-Mails und persönliche Notizen DÜRFEN NICHT die einzige Quelle für wesentliche Anforderungen, Entscheidungen oder Betriebsabläufe sein. |
| SASD-KM-003 | Relevantes Wissen aus flüchtigen Kommunikationskanälen MUSS zeitnah in die dauerhafte Projektdokumentation übertragen werden. |
| SASD-KM-004 | Widersprüchliche Wissensquellen MÜSSEN aufgelöst oder hinsichtlich ihrer Autorität gekennzeichnet werden. |

### 3.2 Architekturentscheidungen

| ID | Anforderung |
|---|---|
| SASD-KM-010 | Wesentliche technische Entscheidungen MÜSSEN mit Kontext, Entscheidung, Alternativen und Konsequenzen dokumentiert werden. |
| SASD-KM-011 | ADRs oder gleichwertige Entscheidungsnachweise MÜSSEN stabil referenzierbar sein. |
| SASD-KM-012 | Ersetzte Entscheidungen MÜSSEN erhalten und als superseded gekennzeichnet werden. |
| SASD-KM-013 | Entscheidungen DÜRFEN NICHT nachträglich so verändert werden, dass ihr ursprünglicher Kontext verloren geht. |
| SASD-KM-014 | Wiederkehrende Entscheidungsgründe SOLLTEN in Prinzipien, Guidelines oder Templates überführt werden. |

### 3.3 Betriebs- und Diagnosewissen

| ID | Anforderung |
|---|---|
| SASD-KM-020 | Wiederkehrende Betriebs-, Installations-, Diagnose- und Wiederherstellungsaufgaben MÜSSEN in angemessenem Umfang dokumentiert werden. |
| SASD-KM-021 | Production-Projekte MÜSSEN Runbooks oder gleichwertige Betriebsanweisungen für kritische Abläufe besitzen. |
| SASD-KM-022 | Troubleshooting-Dokumentation SOLLTE Symptome, Prüfschritte, typische Ursachen, sichere Maßnahmen und Eskalationspunkte enthalten. |
| SASD-KM-023 | Lokale, nicht reproduzierbare Expertenkenntnisse MÜSSEN priorisiert dokumentiert werden, wenn ihr Verlust den Betrieb oder die Wartung gefährden würde. |

### 3.4 Glossar und Begriffe

| ID | Anforderung |
|---|---|
| SASD-KM-030 | Projektspezifische Begriffe, Abkürzungen und Domänenkonzepte SOLLTEN in einem Glossar oder an einer zentralen Stelle erklärt werden. |
| SASD-KM-031 | Ein Begriff MUSS konsistent verwendet werden, wenn unterschiedliche Bedeutungen zu Fehlern führen könnten. |
| SASD-KM-032 | Veraltete Begriffe SOLLTEN mit ihrem Nachfolger oder einer Migrationsnotiz versehen werden. |

### 3.5 Lessons Learned

| ID | Anforderung |
|---|---|
| SASD-KM-040 | Nach wesentlichen Releases, Migrationen, Vorfällen oder gescheiterten Ansätzen SOLLTEN Lessons Learned erfasst werden. |
| SASD-KM-041 | Lessons Learned SOLLTEN Beobachtung, Ursache, Auswirkung und konkrete Verbesserung unterscheiden. |
| SASD-KM-042 | Wiederverwendbare Erkenntnisse SOLLTEN in Standards, Checklisten, Templates oder Automatisierung überführt werden. |
| SASD-KM-043 | Lessons Learned DÜRFEN NICHT zur persönlichen Schuldzuweisung verwendet werden. |

### 3.6 Quellen und externe Referenzen

| ID | Anforderung |
|---|---|
| SASD-KM-050 | Externe Quellen, auf denen wesentliche Entscheidungen beruhen, SOLLTEN mit Titel, Herausgeber, Version oder Datum und Zugriffspfad referenziert werden. |
| SASD-KM-051 | Kopierte Inhalte MÜSSEN Lizenz und Urheberrecht beachten. |
| SASD-KM-052 | Kritisches Wissen SOLLTE nicht ausschließlich von einem veränderlichen externen Link abhängen. |
| SASD-KM-053 | Veraltete Referenzen MÜSSEN bei relevanten Reviews aktualisiert oder gekennzeichnet werden. |

### 3.7 Prompts und KI-Arbeitswissen

| ID | Anforderung |
|---|---|
| SASD-KM-060 | Wiederverwendbare oder entscheidungsrelevante Prompts SOLLTEN versioniert und mit Zweck, Eingaben und erwarteter Prüfung dokumentiert werden. |
| SASD-KM-061 | Ein Prompt DARF NICHT als Ersatz für die fachliche Regel oder Entscheidung dienen. |
| SASD-KM-062 | Ergebnisse aus KI-Systemen MÜSSEN vor Übernahme in die Source of Truth geprüft werden. |
| SASD-KM-063 | Flüchtige Prompts ohne langfristigen Nutzen MÜSSEN nicht vollständig archiviert werden. |

### 3.8 Übergabe und Onboarding

| ID | Anforderung |
|---|---|
| SASD-KM-070 | Recommended- und Production-Projekte MÜSSEN einen Einstiegspfad für neue Entwickler oder Betreiber bereitstellen. |
| SASD-KM-071 | Production-Projekte MÜSSEN kritische Verantwortlichkeiten, Zugänge, Systeme, Eskalationen und Wiederherstellungswissen übergabefähig dokumentieren. |
| SASD-KM-072 | Eine Übergabe MUSS offene Risiken, technische Schulden und bekannte Einschränkungen benennen. |
| SASD-KM-073 | Ein Projekt SOLLTE regelmäßig prüfen, ob eine fachkundige fremde Person den Einstieg mit der vorhandenen Dokumentation bewältigen kann. |

### 3.9 Aktualität und Archivierung

| ID | Anforderung |
|---|---|
| SASD-KM-080 | Wissen MUSS aktualisiert werden, wenn eine Änderung seine Richtigkeit oder Anwendbarkeit beeinflusst. |
| SASD-KM-081 | Dokumente SOLLTEN einen Owner oder einen erkennbaren Pflegekontext besitzen. |
| SASD-KM-082 | Veraltetes Wissen MUSS aktualisiert, als historisch gekennzeichnet oder archiviert werden. |
| SASD-KM-083 | Historische Entscheidungen und Lessons Learned SOLLTEN erhalten bleiben, wenn sie spätere Entwicklungen erklären. |
| SASD-KM-084 | Archivierung MUSS Sicherheits-, Datenschutz- und Aufbewahrungsanforderungen berücksichtigen. |

## 4. Empfohlene Wissensstruktur

```text
docs/
├── README.md
├── architecture/
│   └── decisions/
├── operations/
├── troubleshooting/
├── lessons-learned/
├── glossary.md
└── references.md
```

Die konkrete Struktur darf kompakter sein.

## 5. Zuordnung zu Qualitätsstufen

| Maßnahme | Minimum | Recommended | Production |
|---|---|---|---|
| Source of Truth | MUSS | MUSS | MUSS |
| wesentliche Entscheidungen | SOLLTE | MUSS | MUSS |
| Glossar | KANN | bei Domänenbegriffen SOLLTE | bei komplexer Domäne MUSS |
| Troubleshooting | KANN | SOLLTE | MUSS |
| Runbooks | KANN | bei Betrieb SOLLTE | MUSS |
| Lessons Learned | KANN | SOLLTE | nach Vorfällen und großen Releases MUSS |
| Übergabedokumentation | KANN | MUSS | MUSS und geprüft |
| Promptbibliothek | KANN | bei KI-Nutzung SOLLTE | bei wiederholbarer KI-Nutzung MUSS |

## 6. Verantwortlichkeiten

Jede beteiligte Person überführt wesentliches Wissen in die Source of Truth. Maintainer organisieren Auffindbarkeit und Pflege. Projektverantwortliche stellen Übergabefähigkeit sicher.

## 7. Nachweise und Prüfkriterien

Geeignete Nachweise sind ADR-Verzeichnis, Glossar, Runbooks, Troubleshooting, Lessons Learned, Onboarding-Anleitung, Prompt-Metadaten und dokumentierte Übergabeprüfung.

## 8. Ausnahmen und Abweichungen

Kleine Projekte dürfen Wissensbereiche zusammenfassen. Kritisches Wissen DARF dennoch nicht ausschließlich in unzugänglichen persönlichen Notizen verbleiben.

## 9. Verwandte Dokumente

- [Dokumentationsstandard](DOCUMENTATION.md)
- [Architekturstandard](ARCHITECTURE.md)
- [Wartungsstandard](MAINTENANCE.md)
- [KI-gestützte Entwicklung](AI-ASSISTED-DEVELOPMENT.md)
- [ADR-Template](../../templates/architecture-decisions/ADR-TEMPLATE.md)
