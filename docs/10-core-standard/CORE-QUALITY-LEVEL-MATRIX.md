---
title: "Konsolidierte Qualitätsstufenmatrix"
document-id: SASD-REF-006
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
generated: true
---

# Konsolidierte Qualitätsstufenmatrix

> Automatisch erzeugte, nicht normative Vergleichsansicht. Maßgeblich bleiben die jeweiligen Core-Dokumente. Aktualisierung: `python tooling/generate-core-quality-matrix.py`.

Die Übersicht konsolidiert **110** Maßnahmen aus den Qualitätsstufentabellen.

## [Qualitätsstufen und Anwendbarkeit](QUALITY-LEVELS.md)

| Maßnahme oder Artefakt | Minimum | Recommended | Production |
|---|---|---|---|
| Lebensdauer | kurz oder experimentell | längerfristig gepflegt | langfristig oder vertraglich zugesichert |
| Nutzerkreis | Entwickler selbst oder kleiner Lernkreis | mehrere Nutzer oder Open Source | externe Kunden, Öffentlichkeit oder operative Teams |
| Ausfallauswirkung | gering und leicht behebbar | spürbar, aber beherrschbar | erheblich, geschäfts- oder sicherheitskritisch |
| Daten | keine oder unkritische Testdaten | reguläre Projektdaten | sensible, personenbezogene oder geschäftskritische Daten |
| Betrieb | lokal und gelegentlich | regelmäßig genutzt | produktiv, automatisiert oder dauerhaft verfügbar |
| Wiederherstellung | erneute Erstellung vertretbar | Backup oder dokumentierte Wiederherstellung | getestete Wiederherstellung und definierte Ziele |
| Nachweisbedarf | gering | nachvollziehbar für Dritte | auditierbar oder vertraglich relevant |
| Projektziel und Scope | MUSS | MUSS | MUSS |
| README und Nutzung | MUSS | MUSS | MUSS |
| Anforderungen | kompakt MUSS | strukturiert MUSS | nachvollziehbar und freigegeben MUSS |
| Architektur | einfache Übersicht SOLLTE | dokumentiert MUSS | geprüft und entscheidungsbasiert MUSS |
| Tests | kritische Nutzung MUSS geprüft werden | risikobasierte Teststrategie MUSS | automatisierte und dokumentierte Freigaben MÜSSEN vorhanden sein |
| Sicherheit | Baseline MUSS | Risikoanalyse MUSS | Bedrohungsmodell und belastbare Nachweise MÜSSEN vorhanden sein |
| Releases | nachvollziehbarer Stand MUSS | versioniert und dokumentiert MUSS | reproduzierbar, prüfbar und rückrollbar MUSS |
| Wartung | Zuständigkeit MUSS | Wartungsplan SOLLTE | Betriebs-, Update- und Wiederherstellungsplan MUSS |
| Wissensmanagement | wesentliche Hinweise MUSS | ADRs und Übergabewissen SOLLTEN vorhanden sein | vollständige Betriebs- und Entscheidungsnachweise MÜSSEN vorhanden sein |
| Automatisierung | KANN | SOLLTE | für wiederholbare Prüfungen MUSS sie soweit technisch möglich eingesetzt werden |

## [Projektlebenszyklus](PROJECT-LIFECYCLE.md)

| Maßnahme oder Artefakt | Minimum | Recommended | Production |
|---|---|---|---|
| Startentscheidung | kompakter Projektauftrag | dokumentierter Projektauftrag | geprüfter Auftrag mit Risiko- und Betriebsbetrachtung |
| Umsetzungsstart | Ziel und nächster Meilenstein | Anforderungen und Architekturgrundlage | freigegebene Anforderungen, Architektur und Risikomaßnahmen |
| Releasefreigabe | Nutzung geprüft | definierte DoD und Testnachweise | formale Freigabe, Security-, Betriebs- und Recovery-Nachweise |
| Wartungsübergang | Zuständigkeit benannt | Wartungs- und Updateweg dokumentiert | Betriebsmodell, Monitoring, Backup und Incident-Verfahren geprüft |
| Archivierung | Status und Nutzungshinweis | Migrations- und Archivhinweis | kontrollierter EOL-Prozess und Datenbehandlung |

## [Anforderungsmanagement](REQUIREMENTS.md)

| Maßnahme oder Artefakt | Minimum | Recommended | Production |
|---|---|---|---|
| Problem, Ziel, Scope | kompakt MUSS | strukturiert MUSS | geprüft und freigegeben MUSS |
| Nicht-Ziele | SOLLTE | MUSS | MUSS |
| stabile Kennungen | KANN | wesentliche Anforderungen MUSS | alle freigaberelevanten Anforderungen MUSS |
| Akzeptanzkriterien | für kritische Nutzung MUSS | für wesentliche Anforderungen MUSS | vollständig und nachvollziehbar MUSS |
| Traceability | KANN | Anforderung zu Nachweis MUSS | bidirektional MUSS |
| formale Änderungsbewertung | KANN | wesentliche Änderungen SOLLTE | wesentliche Änderungen MUSS |

## [Architekturstandard](ARCHITECTURE.md)

| Maßnahme oder Artefakt | Minimum | Recommended | Production |
|---|---|---|---|
| Systemübersicht | einfache Beschreibung MUSS | Kontextdiagramm oder gleichwertig MUSS | geprüfter Kontext mit Vertrauensgrenzen MUSS |
| Komponenten | wichtigste Bereiche SOLLTE | Verantwortlichkeiten und Abhängigkeiten MUSS | zusätzlich Laufzeit- und Ausfallverhalten MUSS |
| ADRs | für kritische Entscheidungen SOLLTE | wesentliche Entscheidungen MUSS | wesentliche und sicherheitsrelevante Entscheidungen MUSS |
| Datenflüsse | bei Relevanz SOLLTE | externe und sensible Flüsse MUSS | vollständige kritische Flüsse und Aufbewahrung MUSS |
| Deployment | Nutzungsschritte MUSS | Deployment-Sicht MUSS | Betriebs-, Monitoring- und Recovery-Sicht MUSS |
| Architekturreview | KANN | vor großen Meilensteinen SOLLTE | vor Releases und wesentlichen Änderungen MUSS |

## [Dokumentationsstandard](DOCUMENTATION.md)

| Maßnahme oder Artefakt | Minimum | Recommended | Production |
|---|---|---|---|
| README | MUSS | MUSS | MUSS |
| Lizenzstatus | MUSS bei Verteilung | MUSS | MUSS |
| Projektziel, Scope, Nicht-Ziele | kompakt MUSS | MUSS | MUSS |
| Roadmap oder Wartungsstatus | SOLLTE | MUSS | MUSS |
| Changelog / Releasehistorie | SOLLTE bei Releases | MUSS | MUSS |
| Anforderungen | kompakt MUSS | strukturiert MUSS | freigegeben und traceable MUSS |
| Architektur | SOLLTE | MUSS | MUSS einschließlich Betrieb und Risiken |
| Teststrategie | Prüfschritte MUSS | MUSS | MUSS mit Nachweisen |
| Security-Dokumentation | Baseline MUSS | MUSS | MUSS einschließlich Incident und Threat Model |
| Installations-/Deployment-Doku | bei Relevanz MUSS | MUSS | MUSS |
| Betriebs- und Recovery-Doku | KANN | bei Betrieb SOLLTE | MUSS |
| Contributing / Code of Conduct | KANN | bei Beiträgen SOLLTE | bei externer Zusammenarbeit MUSS |
| ADRs | kritische Entscheidungen SOLLTE | MUSS | MUSS |

## [Repository- und GitHub-Standard](REPOSITORY.md)

| Maßnahme oder Artefakt | Minimum | Recommended | Production |
|---|---|---|---|
| README, Lizenzstatus, Ignore-Regeln | MUSS | MUSS | MUSS |
| strukturierte Verzeichnisse | angemessen SOLLTE | MUSS | MUSS |
| Issues / Roadmap | einfache Liste SOLLTE | MUSS | MUSS |
| Reviewprozess | KANN | risikobasiert SOLLTE | MUSS für wesentliche Änderungen |
| CI-Prüfungen | KANN | SOLLTE | MUSS soweit automatisierbar |
| Branch Protection | KANN | SOLLTE bei mehreren Beteiligten | MUSS für kritische Hauptlinie |
| Release-Tags | bei Releases MUSS | MUSS | MUSS |
| Provenance / Signatur / Prüfsumme | KANN | bei externer Verteilung SOLLTE | MUSS oder begründete Alternative |

## [Qualitätsstandard](QUALITY.md)

| Maßnahme oder Artefakt | Minimum | Recommended | Production |
|---|---|---|---|
| Qualitätsziele | kritische Ziele SOLLTE | MUSS | MUSS mit Nachweisen |
| Definition of Done | kompakt MUSS | MUSS | MUSS und releasegebunden |
| Formatierung / Linting | KANN | SOLLTE | MUSS für relevante Artefakte |
| statische Analyse | KANN | SOLLTE | MUSS |
| Review | risikobasiert KANN | wesentliche Änderungen SOLLTE | wesentliche Änderungen MUSS |
| technische Schulden | kritische Lücken MUSS | MUSS | MUSS mit Frist/Risiko |
| Beobachtbarkeit | Fehlerausgabe MUSS | strukturierte Diagnose SOLLTE | Monitoring und Diagnose MUSS |

## [Sicherheitsstandard](SECURITY.md)

| Maßnahme oder Artefakt | Minimum | Recommended | Production |
|---|---|---|---|
| Security Baseline | MUSS | MUSS | MUSS |
| Risikoanalyse | kompakt SOLLTE | MUSS | MUSS |
| Threat Model | KANN | bei erhöhtem Risiko SOLLTE | MUSS |
| Secret Management | MUSS | MUSS | MUSS mit Rotation |
| Dependency Scanning | KANN | SOLLTE | MUSS |
| SBOM | KANN | bei Verteilung SOLLTE | MUSS soweit möglich |
| Security Review | kritische Bereiche SOLLTE | vor Releases SOLLTE | vor wesentlichen Releases MUSS |
| Incident-Verfahren | KANN | bei Betrieb SOLLTE | MUSS |
| Restore-Test | KANN | regelmäßig SOLLTE | regelmäßig MUSS |

## [Teststandard](TESTING.md)

| Maßnahme oder Artefakt | Minimum | Recommended | Production |
|---|---|---|---|
| dokumentierter Testansatz | kompakt MUSS | MUSS | MUSS |
| automatisierte Tests | kritische Logik SOLLTE | wesentliche Logik MUSS | umfassend risikobasiert MUSS |
| Integrationstests | bei relevanten Integrationen SOLLTE | MUSS | MUSS |
| manuelle Releaseprüfung | bei Bedarf MUSS | reproduzierbar MUSS | protokolliert MUSS |
| Security-Tests | Baseline SOLLTE | risikobasiert MUSS | Bedrohungsmodell-basiert MUSS |
| Upgrade/Recovery-Tests | KANN | bei Betrieb SOLLTE | MUSS |
| CI-Integration | KANN | SOLLTE | MUSS |
| Testnachweise | Ergebnis SOLLTE | MUSS | releasebezogen MUSS |

## [Release-Standard](RELEASES.md)

| Maßnahme oder Artefakt | Minimum | Recommended | Production |
|---|---|---|---|
| eindeutige Version / Commit | MUSS | MUSS | MUSS |
| Release Notes | bei Verteilung SOLLTE | MUSS | MUSS |
| Changelog | SOLLTE | MUSS | MUSS |
| automatisierter Build | KANN | SOLLTE | MUSS soweit möglich |
| Freigabecheckliste | kompakt SOLLTE | MUSS | MUSS mit Nachweisen |
| Prüfsumme | KANN | bei Dateiverteilung SOLLTE | MUSS |
| Signatur / Provenance | KANN | bei hohem Risiko SOLLTE | SOLLTE oder begründete Alternative |
| SBOM | KANN | bei Verteilung SOLLTE | MUSS soweit möglich |
| Rollback / Recovery | KANN | bei Betrieb SOLLTE | MUSS |

## [Wartungsstandard](MAINTENANCE.md)

| Maßnahme oder Artefakt | Minimum | Recommended | Production |
|---|---|---|---|
| Maintainer/Status | MUSS | MUSS | MUSS |
| Updateprüfung | bei Bedarf SOLLTE | regelmäßig MUSS | geplant und risikobasiert MUSS |
| Diagnose | grundlegende Fehlerausgabe MUSS | strukturierte Diagnose SOLLTE | Monitoring und Alerting MUSS |
| Backup | bei nicht reproduzierbaren Daten MUSS | MUSS | MUSS mit Schutz und Zielen |
| Restore-Test | KANN | regelmäßig SOLLTE | regelmäßig MUSS |
| Incident-Prozess | KANN | bei Betrieb SOLLTE | MUSS |
| EOL-Plan | bei Einstellung MUSS | MUSS | MUSS mit Migration und Kommunikation |

## [Wissensmanagement](KNOWLEDGE-MANAGEMENT.md)

| Maßnahme oder Artefakt | Minimum | Recommended | Production |
|---|---|---|---|
| Source of Truth | MUSS | MUSS | MUSS |
| wesentliche Entscheidungen | SOLLTE | MUSS | MUSS |
| Glossar | KANN | bei Domänenbegriffen SOLLTE | bei komplexer Domäne MUSS |
| Troubleshooting | KANN | SOLLTE | MUSS |
| Runbooks | KANN | bei Betrieb SOLLTE | MUSS |
| Lessons Learned | KANN | SOLLTE | nach Vorfällen und großen Releases MUSS |
| Übergabedokumentation | KANN | MUSS | MUSS und geprüft |
| Promptbibliothek | KANN | bei KI-Nutzung SOLLTE | bei wiederholbarer KI-Nutzung MUSS |

## [KI-gestützte Entwicklung](AI-ASSISTED-DEVELOPMENT.md)

| Maßnahme oder Artefakt | Minimum | Recommended | Production |
|---|---|---|---|
| menschliche Verantwortung | MUSS | MUSS | MUSS |
| fachliche Prüfung | risikobasiert MUSS | MUSS | vertieft MUSS |
| Promptversionierung | KANN | für Wiederverwendung SOLLTE | für kritische Abläufe MUSS |
| Werkzeug-/Kontextdokumentation | KANN | bei wichtigen Ergebnissen SOLLTE | bei kritischen Ergebnissen MUSS |
| Schutz sensibler Daten | MUSS | MUSS | MUSS mit freigegebener Umgebung |
| Agentenberechtigungen | minimal MUSS | kontrolliert MUSS | minimal, protokolliert und freigegeben MUSS |
| unabhängiger Review | KANN | bei hohem Risiko SOLLTE | bei kritischen Änderungen MUSS |
