---
title: "Dokumentkatalog für Version 1.0"
document-id: SASD-FND-006
document-type: normative
status: Proposed
version: 0.3.0
standard-version: "1.0"
language: de
authoritative: true
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
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
| SASD-FND-001 | `docs/00-foundation/PROJECT-CHARTER.md` | Normativ | Proposed | Mandat, Vision, Mission und Produktmodell | Alle Beteiligten | — |
| SASD-FND-002 | `docs/00-foundation/SCOPE.md` | Normativ | Proposed | Grenzt Version 1.0 ein und definiert Erfolgskriterien | Maintainer, Anwender | SASD-FND-001 |
| SASD-FND-003 | `docs/00-foundation/PRINCIPLES.md` | Normativ | Proposed | Technologieunabhängige Leitprinzipien | Alle Beteiligten | SASD-FND-001 |
| SASD-FND-004 | `docs/00-foundation/GLOSSARY.md` | Normativ | Draft | Verbindliche Begriffe und Definitionen | Alle Beteiligten | SASD-FND-001 |
| SASD-FND-005 | `docs/00-foundation/CONTENT-ARCHITECTURE.md` | Normativ | Proposed | Struktur, Hierarchie und Dokumentrollen von Version 1.0 | Maintainer, Autoren | FND-001 bis FND-004, GOV-001 bis GOV-003 |
| SASD-FND-006 | `docs/00-foundation/DOCUMENT-CATALOG.md` | Normativ | Proposed | Vollständiges Inventar der Dokumente für Version 1.0 | Maintainer, Autoren | SASD-FND-005 |
| SASD-FND-007 | `docs/00-foundation/VERSION-1.0-ACCEPTANCE-CRITERIA.md` | Normativ | Draft | Freigabe- und Fertigstellungskriterien für Version 1.0 | Maintainer, Reviewer | SASD-FND-002, SASD-FND-005 |
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
| SASD-PROF-DOTNET-001 | `docs/20-profiles/dotnet/DOTNET-PROFILE.md` | Normativ | Planned | Geltungsbereich und Anwendung des .NET-Profils | C#/.NET-Entwickler | SASD-CORE-* |
| SASD-PROF-DOTNET-002 | `docs/20-profiles/dotnet/SOLUTION-STRUCTURE.md` | Normativ | Planned | Solution-, Projekt- und Abhängigkeitsstruktur | C#/.NET-Entwickler | DOTNET-001, CORE-003 |
| SASD-PROF-DOTNET-003 | `docs/20-profiles/dotnet/CODING-STANDARD.md` | Normativ | Planned | C#-Konventionen, Kommentare und Analyzer | C#/.NET-Entwickler | DOTNET-001, CORE-007 |
| SASD-PROF-DOTNET-004 | `docs/20-profiles/dotnet/ERROR-HANDLING.md` | Normativ | Planned | Fehlerbehandlung, Exceptions und Result-Modelle | C#/.NET-Entwickler | DOTNET-003, CORE-008 |
| SASD-PROF-DOTNET-005 | `docs/20-profiles/dotnet/LOGGING.md` | Normativ | Planned | Strukturiertes Logging und Diagnose | C#/.NET-Entwickler | DOTNET-004 |
| SASD-PROF-DOTNET-006 | `docs/20-profiles/dotnet/CONFIGURATION.md` | Normativ | Planned | Konfiguration, Optionen, Umgebungen und Secrets | C#/.NET-Entwickler | CORE-008 |
| SASD-PROF-DOTNET-007 | `docs/20-profiles/dotnet/PERSISTENCE.md` | Normativ | Planned | Persistenz, Migrationen und Datenintegrität | C#/.NET-Entwickler | DOTNET-002, CORE-003 |
| SASD-PROF-DOTNET-008 | `docs/20-profiles/dotnet/DOTNET-TESTING.md` | Normativ | Planned | Teststruktur und .NET-Testwerkzeuge | C#/.NET-Entwickler | CORE-009, DOTNET-002 |
| SASD-PROF-DESKTOP-001 | `docs/20-profiles/desktop/DESKTOP-PROFILE.md` | Normativ | Planned | Geltungsbereich des Desktopprofils | Desktopentwickler | SASD-PROF-DOTNET-001 |
| SASD-PROF-DESKTOP-002 | `docs/20-profiles/desktop/UI-ARCHITECTURE.md` | Normativ | Planned | UI-Schichten, Zuständigkeiten und Navigation | Desktopentwickler | DESKTOP-001, CORE-003 |
| SASD-PROF-DESKTOP-003 | `docs/20-profiles/desktop/USER-EXPERIENCE.md` | Normativ | Planned | Bedienbarkeit, Barrierefreiheit und konsistente Interaktion | Desktopentwickler | DESKTOP-001 |
| SASD-PROF-DESKTOP-004 | `docs/20-profiles/desktop/APPLICATION-LIFECYCLE.md` | Normativ | Planned | Start, Shutdown, Single Instance, Updates und Diagnose | Desktopentwickler | DESKTOP-001, DOTNET-004 bis 006 |
| SASD-PROC-001 | `docs/30-processes/NEW-PROJECT.md` | Normativ | Planned | Wiederholbarer Start eines neuen Projekts | Projektverantwortliche | CORE-001, CORE-002 |
| SASD-PROC-002 | `docs/30-processes/PROJECT-CLASSIFICATION.md` | Normativ | Planned | Auswahl von Qualitätsstufe und Profilen | Projektverantwortliche | CORE-006 |
| SASD-PROC-003 | `docs/30-processes/ARCHITECTURE-DECISION-PROCESS.md` | Normativ | Planned | Erstellen, Prüfen und Pflegen von ADRs | Entwickler, Architekten | CORE-003, CORE-012 |
| SASD-PROC-004 | `docs/30-processes/REVIEW-PROCESS.md` | Normativ | Planned | Dokument-, Code- und Projektprüfung | Reviewer, Entwickler | CORE-007 |
| SASD-PROC-005 | `docs/30-processes/LEGACY-MIGRATION.md` | Normativ | Planned | Schrittweise Migration bestehender Projekte | Maintainer | PROC-002, GOV-007 |
| SASD-PROC-006 | `docs/30-processes/RELEASE-PROCESS.md` | Normativ | Planned | Vorbereitung, Freigabe und Veröffentlichung | Maintainer | CORE-010 |
| SASD-PROC-007 | `docs/30-processes/PROJECT-ARCHIVAL.md` | Normativ | Planned | Geordnete Stilllegung und Archivierung | Maintainer | CORE-011 |
| SASD-GOV-001 | `docs/40-governance/NORMATIVE-LANGUAGE.md` | Normativ | Proposed | Verbindliche Schlüsselwörter und Interpretation | Alle Autoren und Anwender | SASD-FND-004 |
| SASD-GOV-002 | `docs/40-governance/DOCUMENT-LIFECYCLE.md` | Normativ | Proposed | Statusmodell und Freigabekriterien | Maintainer, Reviewer | GOV-001, GOV-003 |
| SASD-GOV-003 | `docs/40-governance/DOCUMENT-METADATA.md` | Normativ | Proposed | Front-Matter, Dokument-IDs und Versionen | Autoren, Tooling | GOV-001, GOV-002 |
| SASD-GOV-004 | `docs/40-governance/VERSIONING.md` | Normativ | Draft | Versionierung des Standards und seiner Dokumente | Maintainer | GOV-002, GOV-003 |
| SASD-GOV-005 | `docs/40-governance/CHANGE-PROCESS.md` | Normativ | Draft | Änderungsvorschläge, Bewertung und Entscheidung | Maintainer, Beitragende | GOV-004 |
| SASD-GOV-006 | `docs/40-governance/EXCEPTIONS.md` | Normativ | Draft | Ausnahmen, Risiken und Ablaufdaten | Projektverantwortliche | GOV-001 |
| SASD-GOV-007 | `docs/40-governance/COMPLIANCE.md` | Normativ | Draft | Anwendung, Nachweise und Compliance-Erklärung | Projektverantwortliche, Reviewer | CORE-006, GOV-006 |
| SASD-REF-001 | `docs/50-reference-implementations/README.md` | Informativ | Draft | Auswahl und Dokumentation der Pilotprojekte | Maintainer, Anwender | SASD-GOV-007 |
| SASD-REF-002 | `docs/10-core-standard/CORE-RESPONSIBILITY-MAP.md` | Informativ | Draft | Zuständigkeitsgrenzen und zulässige Querschnittsregeln des Core | Autoren, Reviewer | SASD-CORE-* |
| SASD-REF-003 | `docs/10-core-standard/SOLO-DEVELOPER-GUIDE.md` | Informativ | Draft | Pragmatische Anwendung durch Einzelentwickler | Einzelentwickler, kleine Teams | SASD-CORE-006, SASD-GOV-007 |
| SASD-REF-004 | `docs/10-core-standard/CORE-STANDARD-REVIEW-0.3.0.md` | Informativ | Draft | Reviewnachweis für den Übergang Draft zu Proposed | Maintainer, Reviewer | SASD-CORE-*, SASD-GOV-006, SASD-GOV-007 |
| SASD-REF-005 | `docs/10-core-standard/CORE-REQUIREMENTS-INDEX.md` | Informativ, erzeugt | Draft | Navigationsindex aller Core-Anforderungen | Anwender, Tooling | SASD-CORE-* |
| SASD-REF-006 | `docs/10-core-standard/CORE-QUALITY-LEVEL-MATRIX.md` | Informativ, erzeugt | Draft | Vergleich aller Qualitätsstufentabellen | Anwender, Reviewer | SASD-CORE-* |

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
