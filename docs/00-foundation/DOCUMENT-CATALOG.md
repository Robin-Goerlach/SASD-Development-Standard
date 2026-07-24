---
title: "Dokumentkatalog für Version 1.0"
document-id: SASD-FND-006
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
depends-on: [SASD-FND-005, SASD-GOV-002, SASD-GOV-003]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Dokumentkatalog für Version 1.0

## 1. Zweck

Dieser Katalog ist das verbindliche Inventar der für SASD Development Standard Version 1.0 vorgesehenen Dokumentrollen. Er verhindert Doppelzuständigkeiten und macht Bearbeitungsstand, Zweck und Abhängigkeiten sichtbar.

Ein Eintrag mit Status **Planned** bedeutet, dass die Dokumentrolle beschlossen, der Inhalt aber noch nicht ausgearbeitet ist. Nur **Approved**-Dokumente sind verbindlich.

## 2. Katalog

| Dokument-ID | Pfad | Typ | Aktueller Zielstatus | Zweck | Zielgruppe | Wesentliche Abhängigkeiten |
|---|---|---|---|---|---|---|
| SASD-FND-001 | `docs/00-foundation/PROJECT-CHARTER.md` | Normativ | Approved | Mandat, Vision, Mission und Produktmodell | Alle Beteiligten | — |
| SASD-FND-002 | `docs/00-foundation/SCOPE.md` | Normativ | Approved | Grenzt Version 1.0 ein und definiert Erfolgskriterien | Maintainer, Anwender | SASD-FND-001 |
| SASD-FND-003 | `docs/00-foundation/PRINCIPLES.md` | Normativ | Approved | Technologieunabhängige Leitprinzipien | Alle Beteiligten | SASD-FND-001 |
| SASD-FND-004 | `docs/00-foundation/GLOSSARY.md` | Normativ | Approved | Verbindliche Begriffe und Definitionen | Alle Beteiligten | SASD-FND-001 |
| SASD-FND-005 | `docs/00-foundation/CONTENT-ARCHITECTURE.md` | Normativ | Approved | Struktur, Hierarchie und Dokumentrollen von Version 1.0 | Maintainer, Autoren | FND-001 bis FND-004, GOV-001 bis GOV-003 |
| SASD-FND-006 | `docs/00-foundation/DOCUMENT-CATALOG.md` | Normativ | Approved | Vollständiges Inventar der Dokumente für Version 1.0 | Maintainer, Autoren | SASD-FND-005 |
| SASD-FND-007 | `docs/00-foundation/VERSION-1.0-ACCEPTANCE-CRITERIA.md` | Normativ | Approved | Freigabe- und Fertigstellungskriterien für Version 1.0 | Maintainer, Reviewer | SASD-FND-002, SASD-FND-005 |
| SASD-CORE-001 | `docs/10-core-standard/PROJECT-LIFECYCLE.md` | Normativ | Proposed | Projektphasen von Idee bis Archivierung | Projektverantwortliche | SASD-FND-002, SASD-FND-003, SASD-CORE-006 |
| SASD-CORE-002 | `docs/10-core-standard/REQUIREMENTS.md` | Normativ | Proposed | Anforderungen, Scope, Nachverfolgbarkeit und Änderungen | Projektverantwortliche, Entwickler | SASD-CORE-001, SASD-CORE-006 |
| SASD-CORE-003 | `docs/10-core-standard/ARCHITECTURE.md` | Normativ | Proposed | Architektur, Modularisierung, Abhängigkeiten und Entscheidungen | Entwickler, Architekten | SASD-CORE-002, SASD-CORE-006, SASD-CORE-008 |
| SASD-CORE-004 | `docs/10-core-standard/DOCUMENTATION.md` | Normativ | Proposed | Dokumentarten, Pflege und Mindestinhalte | Alle Projektbeteiligten | SASD-CORE-001, SASD-CORE-006 |
| SASD-CORE-005 | `docs/10-core-standard/REPOSITORY.md` | Normativ | Proposed | Repository-Aufbau, Git und Plattformkonventionen | Maintainer, Entwickler | SASD-CORE-004, SASD-CORE-006, SASD-CORE-008, SASD-CORE-010 |
| SASD-CORE-006 | `docs/10-core-standard/QUALITY-LEVELS.md` | Normativ | Proposed | Minimum, Recommended und Production | Alle Projektbeteiligten | SASD-FND-002, SASD-GOV-006, SASD-GOV-007 |
| SASD-CORE-007 | `docs/10-core-standard/QUALITY.md` | Normativ | Proposed | Qualitätsziele, Reviews, statische Analyse und Definition of Done | Entwickler, Reviewer | SASD-CORE-002, SASD-CORE-003, SASD-CORE-006, SASD-CORE-009 |
| SASD-CORE-008 | `docs/10-core-standard/SECURITY.md` | Normativ | Proposed | Sicherheitsgrundlagen, Datenschutz und Supply Chain | Alle Projektbeteiligten | SASD-CORE-002, SASD-CORE-003, SASD-CORE-006, SASD-CORE-007 |
| SASD-CORE-009 | `docs/10-core-standard/TESTING.md` | Normativ | Proposed | Teststrategie, Testarten und Nachweise | Entwickler, Tester | SASD-CORE-002, SASD-CORE-006, SASD-CORE-007, SASD-CORE-008 |
| SASD-CORE-010 | `docs/10-core-standard/RELEASES.md` | Normativ | Proposed | Versionierung, Releasequalität und Veröffentlichungen | Maintainer | SASD-CORE-005, SASD-CORE-007, SASD-CORE-008, SASD-CORE-009 |
| SASD-CORE-011 | `docs/10-core-standard/MAINTENANCE.md` | Normativ | Proposed | Betrieb, Wartung, Updates, Backups und Archivierung | Maintainer, Betreiber | SASD-CORE-006, SASD-CORE-008, SASD-CORE-009, SASD-CORE-010, SASD-CORE-012 |
| SASD-CORE-012 | `docs/10-core-standard/KNOWLEDGE-MANAGEMENT.md` | Normativ | Proposed | ADRs, Lessons Learned, Übergaben und Wissenssicherung | Alle Projektbeteiligten | SASD-CORE-003, SASD-CORE-004, SASD-CORE-006, SASD-CORE-011 |
| SASD-CORE-013 | `docs/10-core-standard/AI-ASSISTED-DEVELOPMENT.md` | Normativ | Proposed | Verantwortungsvolle KI-Nutzung und Ergebnisprüfung | Entwickler, Reviewer | SASD-CORE-002, SASD-CORE-004, SASD-CORE-006 bis SASD-CORE-009, SASD-CORE-012 |
| SASD-PROF-DOTNET-001 | `docs/20-profiles/dotnet/DOTNET-PROFILE.md` | Normativ | Proposed | Geltungsbereich und Anwendung des .NET-Profils | C#/.NET-Entwickler | SASD-CORE-* |
| SASD-PROF-DOTNET-002 | `docs/20-profiles/dotnet/SOLUTION-STRUCTURE.md` | Normativ | Proposed | Solution-, Projekt- und Abhängigkeitsstruktur | C#/.NET-Entwickler | DOTNET-001, CORE-003 |
| SASD-PROF-DOTNET-003 | `docs/20-profiles/dotnet/CODING-STANDARD.md` | Normativ | Proposed | C#-Konventionen, Kommentare und Analyzer | C#/.NET-Entwickler | DOTNET-001, CORE-007 |
| SASD-PROF-DOTNET-004 | `docs/20-profiles/dotnet/ERROR-HANDLING.md` | Normativ | Proposed | Fehlerbehandlung, Exceptions und Result-Modelle | C#/.NET-Entwickler | DOTNET-003, CORE-008 |
| SASD-PROF-DOTNET-005 | `docs/20-profiles/dotnet/LOGGING.md` | Normativ | Proposed | Strukturiertes Logging und Diagnose | C#/.NET-Entwickler | DOTNET-004 |
| SASD-PROF-DOTNET-006 | `docs/20-profiles/dotnet/CONFIGURATION.md` | Normativ | Proposed | Konfiguration, Optionen, Umgebungen und Secrets | C#/.NET-Entwickler | CORE-008 |
| SASD-PROF-DOTNET-007 | `docs/20-profiles/dotnet/PERSISTENCE.md` | Normativ | Proposed | Persistenz, Migrationen und Datenintegrität | C#/.NET-Entwickler | DOTNET-002, CORE-003 |
| SASD-PROF-DOTNET-008 | `docs/20-profiles/dotnet/DOTNET-TESTING.md` | Normativ | Proposed | Teststruktur und .NET-Testwerkzeuge | C#/.NET-Entwickler | CORE-009, DOTNET-002 |
| SASD-PROF-DESKTOP-001 | `docs/20-profiles/desktop/DESKTOP-PROFILE.md` | Normativ | Proposed | Geltungsbereich des Desktopprofils | Desktopentwickler | SASD-PROF-DOTNET-001 |
| SASD-PROF-DESKTOP-002 | `docs/20-profiles/desktop/UI-ARCHITECTURE.md` | Normativ | Proposed | UI-Schichten, Zuständigkeiten und Navigation | Desktopentwickler | DESKTOP-001, CORE-003 |
| SASD-PROF-DESKTOP-003 | `docs/20-profiles/desktop/USER-EXPERIENCE.md` | Normativ | Proposed | Bedienbarkeit, Barrierefreiheit und konsistente Interaktion | Desktopentwickler | DESKTOP-001 |
| SASD-PROF-DESKTOP-004 | `docs/20-profiles/desktop/APPLICATION-LIFECYCLE.md` | Normativ | Proposed | Start, Shutdown, Single Instance, Updates und Diagnose | Desktopentwickler | DESKTOP-001, DOTNET-004 bis 006 |
| SASD-PROC-001 | `docs/30-processes/NEW-PROJECT.md` | Normativ | Proposed | Wiederholbarer Start eines neuen Projekts | Projektverantwortliche | CORE-001, CORE-002 |
| SASD-PROC-002 | `docs/30-processes/PROJECT-CLASSIFICATION.md` | Normativ | Proposed | Auswahl von Qualitätsstufe und Profilen | Projektverantwortliche | CORE-006 |
| SASD-PROC-003 | `docs/30-processes/ARCHITECTURE-DECISION-PROCESS.md` | Normativ | Proposed | Erstellen, Prüfen und Pflegen von ADRs | Entwickler, Architekten | CORE-003, CORE-012 |
| SASD-PROC-004 | `docs/30-processes/REVIEW-PROCESS.md` | Normativ | Proposed | Dokument-, Code- und Projektprüfung | Reviewer, Entwickler | CORE-007 |
| SASD-PROC-005 | `docs/30-processes/LEGACY-MIGRATION.md` | Normativ | Proposed | Schrittweise Migration bestehender Projekte | Maintainer | PROC-002, GOV-007 |
| SASD-PROC-006 | `docs/30-processes/RELEASE-PROCESS.md` | Normativ | Proposed | Vorbereitung, Freigabe und Veröffentlichung | Maintainer | CORE-010 |
| SASD-PROC-007 | `docs/30-processes/PROJECT-ARCHIVAL.md` | Normativ | Proposed | Geordnete Stilllegung und Archivierung | Maintainer | CORE-011 |
| SASD-GOV-001 | `docs/40-governance/NORMATIVE-LANGUAGE.md` | Normativ | Approved | Verbindliche Schlüsselwörter und Interpretation | Alle Autoren und Anwender | SASD-FND-004 |
| SASD-GOV-002 | `docs/40-governance/DOCUMENT-LIFECYCLE.md` | Normativ | Approved | Statusmodell und Freigabekriterien | Maintainer, Reviewer | GOV-001, GOV-003 |
| SASD-GOV-003 | `docs/40-governance/DOCUMENT-METADATA.md` | Normativ | Approved | Front-Matter, Dokument-IDs und Versionen | Autoren, Tooling | GOV-001, GOV-002 |
| SASD-GOV-004 | `docs/40-governance/VERSIONING.md` | Normativ | Approved | Versionierung des Standards und seiner Dokumente | Maintainer | GOV-002, GOV-003 |
| SASD-GOV-005 | `docs/40-governance/CHANGE-PROCESS.md` | Normativ | Approved | Änderungsvorschläge, Bewertung und Entscheidung | Maintainer, Beitragende | GOV-004 |
| SASD-GOV-006 | `docs/40-governance/EXCEPTIONS.md` | Normativ | Approved | Ausnahmen, Risiken und Ablaufdaten | Projektverantwortliche | GOV-001 |
| SASD-GOV-007 | `docs/40-governance/COMPLIANCE.md` | Normativ | Approved | Anwendung, Nachweise und Compliance-Erklärung | Projektverantwortliche, Reviewer | CORE-006, GOV-006 |
| SASD-REF-001 | `docs/50-reference-implementations/README.md` | Informativ | Proposed | Einstieg, Pilotkategorien und aktive Referenzprojekte | Maintainer, Anwender | SASD-GOV-007, SASD-PROC-005 |
| SASD-REF-002 | `docs/10-core-standard/CORE-RESPONSIBILITY-MAP.md` | Informativ | Draft | Zuständigkeitsgrenzen und zulässige Querschnittsregeln des Core | Autoren, Reviewer | SASD-CORE-* |
| SASD-REF-003 | `docs/10-core-standard/SOLO-DEVELOPER-GUIDE.md` | Informativ | Draft | Pragmatische Anwendung durch Einzelentwickler | Einzelentwickler, kleine Teams | SASD-CORE-006, SASD-GOV-007 |
| SASD-REF-004 | `docs/10-core-standard/CORE-STANDARD-REVIEW-0.3.0.md` | Informativ | Draft | Reviewnachweis für den Übergang Draft zu Proposed | Maintainer, Reviewer | SASD-CORE-*, SASD-GOV-006, SASD-GOV-007 |
| SASD-REF-005 | `docs/10-core-standard/CORE-REQUIREMENTS-INDEX.md` | Informativ, erzeugt | Draft | Navigationsindex aller Core-Anforderungen | Anwender, Tooling | SASD-CORE-* |
| SASD-REF-DOTNET-001 | `docs/20-profiles/dotnet/DOTNET-REFERENCE-BASELINE.md` | Informativ | Draft | Primärquellen und technische Baseline des .NET-Profils | .NET-Anwender, Reviewer | SASD-PROF-DOTNET-001 |
| SASD-REF-DOTNET-002 | `docs/20-profiles/dotnet/DOTNET-PROJECT-SIZING-GUIDE.md` | Informativ | Draft | Proportionale Projektstrukturen für kleine bis komplexe Lösungen | Einzelentwickler, Architekten | DOTNET-001, DOTNET-002 |
| SASD-REF-DOTNET-003 | `docs/20-profiles/dotnet/DOTNET-PROFILE-REVIEW-0.4.0.md` | Informativ | Draft | Reviewnachweis für Proposed 0.4.0 | Maintainer, Reviewer | DOTNET-001 bis DOTNET-008 |
| SASD-REF-DOTNET-004 | `docs/20-profiles/dotnet/DOTNET-REQUIREMENTS-INDEX.md` | Informativ, erzeugt | Draft | Index aller .NET-Profilanforderungen | Anwender, Tooling | SASD-PROF-DOTNET-* |
| SASD-REF-DOTNET-005 | `docs/20-profiles/dotnet/DOTNET-QUALITY-LEVEL-MATRIX.md` | Informativ | Draft | Konsolidierte Qualitätsstufensicht des .NET-Profils | Anwender, Reviewer | DOTNET-001 bis DOTNET-008 |
| SASD-REF-DESKTOP-001 | `docs/20-profiles/desktop/DESKTOP-REFERENCE-BASELINE.md` | Informativ | Draft | Primärquellen und technische Basis des Desktopprofils | Desktopentwickler, Reviewer | DESKTOP-001 |
| SASD-REF-DESKTOP-002 | `docs/20-profiles/desktop/WINDOWS-FORMS-GUIDANCE.md` | Informativ | Draft | Pragmatische Umsetzung mit WinForms | WinForms-Entwickler | DESKTOP-001 bis DESKTOP-004 |
| SASD-REF-DESKTOP-003 | `docs/20-profiles/desktop/WPF-GUIDANCE.md` | Informativ | Draft | Pragmatische Umsetzung mit WPF | WPF-Entwickler | DESKTOP-001 bis DESKTOP-004 |
| SASD-REF-DESKTOP-004 | `docs/20-profiles/desktop/DESKTOP-PROJECT-SIZING-GUIDE.md` | Informativ | Draft | Proportionale Desktop-Projektmodelle | Einzelentwickler, Architekten | DESKTOP-001, DESKTOP-002 |
| SASD-REF-DESKTOP-005 | `docs/20-profiles/desktop/DESKTOP-PROFILE-REVIEW-0.5.0.md` | Informativ | Draft | Reviewnachweis für Proposed 0.5.0 | Maintainer, Reviewer | DESKTOP-001 bis DESKTOP-004 |
| SASD-REF-DESKTOP-006 | `docs/20-profiles/desktop/DESKTOP-REQUIREMENTS-INDEX.md` | Informativ, erzeugt | Draft | Index aller Desktopanforderungen | Anwender, Tooling | SASD-PROF-DESKTOP-* |
| SASD-REF-DESKTOP-007 | `docs/20-profiles/desktop/DESKTOP-QUALITY-LEVEL-MATRIX.md` | Informativ | Draft | Konsolidierte Qualitätsstufensicht des Desktopprofils | Anwender, Reviewer | DESKTOP-001 bis DESKTOP-004 |
| SASD-REF-006 | `docs/10-core-standard/CORE-QUALITY-LEVEL-MATRIX.md` | Informativ, erzeugt | Draft | Vergleich aller Qualitätsstufentabellen | Anwender, Reviewer | SASD-CORE-* |

| SASD-REF-PROC-001 | `docs/30-processes/PROCESS-MAP.md` | Informativ | Draft | Zusammenspiel und Verantwortungsgrenzen der operativen Prozesse | Anwender, Maintainer | SASD-PROC-001 bis SASD-PROC-007 |
| SASD-REF-PROC-002 | `docs/30-processes/PROCESS-REVIEW-0.6.0.md` | Informativ | Draft | Reviewnachweis für Proposed 0.6.0 | Maintainer, Reviewer | SASD-PROC-001 bis SASD-PROC-007 |
| SASD-REF-PROC-003 | `docs/30-processes/PROCESS-REQUIREMENTS-INDEX.md` | Informativ, erzeugt | Draft | Index aller operativen Prozessanforderungen | Anwender, Tooling | SASD-PROC-001 bis SASD-PROC-007 |
| SASD-REF-PROC-004 | `docs/30-processes/PROCESS-QUALITY-LEVEL-MATRIX.md` | Informativ, erzeugt | Draft | Qualitätsstufensicht der operativen Prozesse | Anwender, Reviewer | SASD-PROC-001 bis SASD-PROC-007 |

| SASD-REF-PILOT-001 | `docs/50-reference-implementations/PILOT-PROGRAM.md` | Informativ | Proposed | Pilotlebenszyklus, Auswahl, Mindestartefakte und Standardfeedback | Maintainer, Reviewer | SASD-PROC-002, SASD-PROC-004, SASD-PROC-005 |
| SASD-REF-PILOT-002 | `docs/50-reference-implementations/PILOT-EVIDENCE-MODEL.md` | Informativ | Proposed | Evidenzklassen und Vertrauensregeln für Pilotbewertungen | Reviewer, Anwender | SASD-GOV-007, SASD-PROC-004 |
| SASD-REF-PILOT-003 | `docs/50-reference-implementations/PILOT-PORTFOLIO.md` | Informativ, erzeugt | Draft | Maschinenlesbar erzeugte Übersicht der Piloten | Maintainer, Anwender | SASD-REF-PILOT-001, SASD-REF-PILOT-002 |
| SASD-REF-PILOT-101 | `docs/50-reference-implementations/pilot-01-sasd-taskhost-local/README.md` | Informativ | Draft | Einstieg in Pilot 01 | Maintainer, Anwender | SASD-REF-PILOT-001, SASD-PROC-005 |
| SASD-REF-PILOT-102 | `docs/50-reference-implementations/pilot-01-sasd-taskhost-local/PILOT-CHARTER.md` | Informativ | Draft | Ziel, Scope und Erfolgskriterien von Pilot 01 | Maintainer, Reviewer | SASD-PROC-002, SASD-PROC-005 |
| SASD-REF-PILOT-103 | `docs/50-reference-implementations/pilot-01-sasd-taskhost-local/PROJECT-CLASSIFICATION.md` | Informativ | Draft | Klassifikation des kleinen WinForms-/SQLite-Projekts | Maintainer, Reviewer | SASD-CORE-006, SASD-PROC-002 |
| SASD-REF-PILOT-104 | `docs/50-reference-implementations/pilot-01-sasd-taskhost-local/BASELINE-ASSESSMENT.md` | Informativ | Draft | Evidenzbasiertes öffentliches Ausgangsassessment | Maintainer, Reviewer | SASD-PROC-005, SASD-REF-PILOT-002 |
| SASD-REF-PILOT-105 | `docs/50-reference-implementations/pilot-01-sasd-taskhost-local/GAP-REGISTER.md` | Informativ | Draft | Priorisierte Lücken und Nachweise | Maintainer, Entwickler | SASD-GOV-006, SASD-GOV-007 |
| SASD-REF-PILOT-106 | `docs/50-reference-implementations/pilot-01-sasd-taskhost-local/MIGRATION-PLAN.md` | Informativ | Draft | Wellenbasierter Migrationsplan | Maintainer, Entwickler | SASD-PROC-005 |
| SASD-REF-PILOT-107 | `docs/50-reference-implementations/pilot-01-sasd-taskhost-local/WAVE-01-PLAN.md` | Informativ | Draft | Ausführbarer Plan für Stabilisierung und Engineering-Basis | Entwickler, Reviewer | SASD-PROC-004, SASD-PROF-DOTNET-008, SASD-PROF-DESKTOP-004 |
| SASD-REF-PILOT-108 | `docs/50-reference-implementations/pilot-01-sasd-taskhost-local/EVIDENCE-MAP.md` | Informativ | Draft | Quellen und geplante lokale Nachweise | Reviewer, Maintainer | SASD-GOV-007, SASD-REF-PILOT-002 |
| SASD-REF-PILOT-109 | `docs/50-reference-implementations/pilot-01-sasd-taskhost-local/DECISION-LOG.md` | Informativ | Draft | Pilotentscheidungen und Overengineering-Grenzen | Maintainer, Reviewer | SASD-PROC-003 |
| SASD-REF-PILOT-110 | `docs/50-reference-implementations/pilot-01-sasd-taskhost-local/PILOT-REVIEW.md` | Informativ | Draft | Review der Pilotvorbereitung | Maintainer, Reviewer | SASD-PROC-004 |

| SASD-REF-PILOT-004 | `docs/50-reference-implementations/PILOT-FEEDBACK-LOG.md` | Informativ | Draft | Konsolidiertes Feedback aus Piloten | Maintainer, Reviewer | SASD-REF-PILOT-001, SASD-REF-PILOT-002 |
| SASD-REF-PILOT-005 | `docs/50-reference-implementations/PILOT-FEEDBACK-SUMMARY.md` | Informativ, erzeugt | Draft | Statusübersicht des Pilotfeedbacks | Maintainer, Anwender | SASD-REF-PILOT-004 |
| SASD-REF-PILOT-111 | `docs/50-reference-implementations/pilot-01-sasd-taskhost-local/WAVE-01-IMPLEMENTATION-REVIEW.md` | Informativ | Draft | Statisches Review des Wave-01-Updateartefakts | Maintainer, Reviewer | SASD-REF-PILOT-002, SASD-REF-PILOT-107 |
| SASD-REF-PILOT-112 | `docs/50-reference-implementations/pilot-01-sasd-taskhost-local/WAVE-01-VERIFICATION-PLAN.md` | Informativ | Draft | Kontrollierter Build-, Test-, Start-, Daten- und CI-Nachweis | Entwickler, Reviewer | SASD-REF-PILOT-107, SASD-REF-PILOT-111 |
| SASD-REF-PILOT-113 | `docs/50-reference-implementations/pilot-01-sasd-taskhost-local/INTERIM-RETROSPECTIVE.md` | Informativ | Draft | Vorläufige Erkenntnisse vor technischer Verifikation | Maintainer, Reviewer | SASD-REF-PILOT-111, SASD-REF-PILOT-004 |

| SASD-REF-GOV-001 | `docs/40-governance/GOVERNANCE-RESPONSIBILITY-MAP.md` | Informativ | Draft | Primäre Zuständigkeiten der Governance-Dokumente | Maintainer, Reviewer | SASD-GOV-001 bis SASD-GOV-007 |
| SASD-REF-GOV-002 | `docs/40-governance/FOUNDATION-GOVERNANCE-REVIEW-0.8.0.md` | Informativ | Draft | Reviewnachweis für Foundation und Governance vor der Freigabe 0.8.0 | Maintainer, Reviewer | SASD-FND-*, SASD-GOV-* |
| SASD-REF-GOV-003 | `docs/40-governance/APPROVAL-READINESS-0.8.0.md` | Informativ | Draft | Historischer Nachweis der Freigabereife vor der Maintainer-Entscheidung | Maintainer | SASD-GOV-002, SASD-FND-007 |
| SASD-REF-GOV-004 | `docs/40-governance/GOVERNANCE-REQUIREMENTS-INDEX.md` | Informativ, erzeugt | Draft | Index aller Governance-Anforderungen | Anwender, Tooling | SASD-GOV-001 bis SASD-GOV-007 |
| SASD-REF-GOV-005 | `docs/40-governance/FOUNDATION-GOVERNANCE-APPROVAL-0.8.0.md` | Informativ | Approved | Formale Maintainer-Freigabe der Foundation- und Governance-Baseline | Maintainer, Anwender | SASD-FND-001 bis SASD-FND-007, SASD-GOV-001 bis SASD-GOV-007 |
| SASD-REF-GOV-006 | `docs/40-governance/FOUNDATION-GOVERNANCE-APPROVAL-MANIFEST-0.8.0.md` | Informativ, erzeugt | Approved | Hashmanifest der 14 freigegebenen Dokumente | Maintainer, Tooling | SASD-REF-GOV-005 |
| SASD-REF-GOV-007 | `docs/40-governance/FOUNDATION-GOVERNANCE-APPROVAL-CHECKLIST-0.8.0.md` | Informativ | Approved | Ausgefüllte Freigabecheckliste und Reviewnachweis | Maintainer, Reviewer | SASD-REF-GOV-002, SASD-REF-GOV-003, SASD-REF-GOV-005 |

## 3. Unterstützende Artefakte für Version 1.0

Zusätzlich zu den Dokumenten werden mindestens folgende Artefaktgruppen benötigt:

| Bereich | Mindestinhalt für Version 1.0 |
|---|---|
| `templates/documents` | README-, Roadmap-, Compliance-, normatives und informatives Dokumenttemplate |
| `templates/architecture-decisions` | ADR-Template |
| `templates/repositories` | Repository-Metadaten und Grundstruktur |
| `checklists/project-initiation` | Projektstart-Checkliste |
| `checklists/development` | Milestone- und Dokument-Review-Checkliste |
| `checklists/security` | Security-Baseline |
| `checklists/releases` | Release-Checkliste |
| `prompts` | Initialisierung, Architektur, Entwicklung, Review, Debugging und Release |
| `tooling` | mindestens Metadaten- und Linkprüfung sowie Basiskonfigurationen für .NET |
| `.github` | Issue- und Pull-Request-Vorlagen; CI erst nach Freigabe der zu prüfenden Regeln |
| `artefacts/publications` | Word- und PDF-Ausgabe der veröffentlichten Version 1.0 |

## 4. Bearbeitungsreihenfolge

Die empfohlene Reihenfolge lautet:

1. Foundation und Governance freigeben,
2. Qualitätsstufen und Projektklassifikation definieren,
3. Projektlebenszyklus, Anforderungen und Dokumentation ausarbeiten,
4. Architektur, Qualität, Sicherheit und Tests definieren,
5. Repository-, Release- und Wartungsregeln ergänzen,
6. C#/.NET-Profil erstellen,
7. Desktopprofil erstellen,
8. Vorlagen, Checklisten, Prompts und Tooling angleichen,
9. Pilotprojekte durchführen,
10. Release Candidate und Version 1.0 veröffentlichen.

## 5. Änderungsregel

Neue normative Dokumentrollen oder die Zusammenlegung bestehender Rollen MÜSSEN über den Änderungsprozess bewertet und in diesem Katalog sowie in `CONTENT-ARCHITECTURE.md` nachvollzogen werden.
