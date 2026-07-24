---
title: "Repository- und GitHub-Standard"
document-id: SASD-CORE-005
document-type: normative
status: Draft
version: 0.2.0
standard-version: "1.0"
language: de
authoritative: true
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core]
depends-on: [SASD-FND-003, SASD-GOV-001, SASD-CORE-004, SASD-CORE-006, SASD-CORE-008, SASD-CORE-010]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Repository- und GitHub-Standard

## 1. Zweck

Dieses Dokument definiert technologieunabhängige Regeln für Repository-Struktur, Git-Nutzung, Metadaten, Zusammenarbeit, Releases und Archivierung. GitHub-spezifische Funktionen werden empfohlen, der Kern bleibt auf andere Git-Plattformen übertragbar.

## 2. Geltungsbereich

Der Standard gilt für einzelne Repositories und für Repository-Sammlungen eines größeren Produkts. Monorepo und mehrere Repositories sind zulässig, wenn Ownership, Versionierung und Abhängigkeiten verständlich bleiben.

## 3. Normative Anforderungen

### 3.1 Repository-Identität

| ID | Anforderung |
|---|---|
| SASD-REP-001 | Ein Repository MUSS einen eindeutigen, stabilen und verständlichen Namen besitzen. |
| SASD-REP-002 | Beschreibung, Zweck, Status und primäre Technologie oder Projektart MÜSSEN im README oder in den Repository-Metadaten erkennbar sein. |
| SASD-REP-003 | Ein öffentliches Repository MUSS Lizenz, Sicherheitskontakt und Wartungsstatus auffindbar machen. |
| SASD-REP-004 | Forks, Mirrors, archivierte Kopien und kanonische Repositories MÜSSEN unterscheidbar sein. |
| SASD-REP-005 | Der kanonische Standort eines Projekts MUSS benannt werden, wenn mehrere gleichartige Kopien existieren. |

### 3.2 Grundstruktur

Die folgende Struktur ist der bevorzugte Ausgangspunkt und darf projektspezifisch angepasst werden:

```text
.
├── src/          # produktive Quellen oder Hauptartefakte
├── tests/        # automatisierte und unterstützende Tests
├── docs/         # weiterführende Dokumentation
├── artefacts/    # ausgewählte erzeugte oder veröffentlichte Artefakte
├── tooling/      # lokale Skripte und Prüfwerkzeuge
├── .github/      # GitHub-spezifische Vorlagen und Workflows
├── README.md
├── LICENSE
├── CHANGELOG.md
└── .gitignore
```

| ID | Anforderung |
|---|---|
| SASD-REP-010 | Produktive Quellen, Tests, Dokumentation und erzeugte Artefakte MÜSSEN unterscheidbar sein. |
| SASD-REP-011 | Repository-Struktur SOLLTE der Größe des Projekts entsprechen und DARF nicht allein aus formalen Gründen unnötig tief oder fragmentiert werden. |
| SASD-REP-012 | Build- und Laufzeitausgaben MÜSSEN standardmäßig von der Versionskontrolle ausgeschlossen werden, sofern sie keine bewusst versionierten Releaseartefakte sind. |
| SASD-REP-013 | Große Binärdateien SOLLTEN nur versioniert werden, wenn ihr Nutzen, ihre Herkunft und ihre Aktualisierung geregelt sind. |
| SASD-REP-014 | Fremdmaterial MUSS hinsichtlich Lizenz, Herkunft und Integrität nachvollziehbar sein. |

### 3.3 Root-Dateien

| ID | Anforderung |
|---|---|
| SASD-REP-020 | Jedes Repository MUSS ein `README.md` oder eine gleichwertige Einstiegsdatei besitzen. |
| SASD-REP-021 | Ein verteiltes oder öffentliches Projekt MUSS eine Lizenzdatei oder einen eindeutigen Rechtehinweis besitzen. |
| SASD-REP-022 | Eine geeignete Ignore-Datei MUSS Buildausgaben, lokale Einstellungen, temporäre Dateien und Geheimnisse ausschließen. |
| SASD-REP-023 | Recommended- und Production-Projekte MÜSSEN eine nachvollziehbare Änderungs- oder Releasehistorie führen. |
| SASD-REP-024 | Sicherheitsrelevante Projekte und öffentliche Repositories SOLLTEN eine `SECURITY.md` oder gleichwertige Meldeanleitung besitzen. |
| SASD-REP-025 | Projekte mit externen Beiträgen SOLLTEN `CONTRIBUTING.md`, Verhaltensregeln und Reviewhinweise bereitstellen. |

### 3.4 Branches und Hauptlinie

| ID | Anforderung |
|---|---|
| SASD-REP-030 | Ein Repository MUSS eine benannte kanonische Hauptlinie besitzen, üblicherweise `main`. |
| SASD-REP-031 | Die Hauptlinie SOLLTE in einem buildbaren oder anderweitig konsistenten Zustand gehalten werden. |
| SASD-REP-032 | Branch-Strategie MUSS zur Projektgröße passen. Ein komplexes Flow-Modell DARF nicht ohne erkennbaren Nutzen eingeführt werden. |
| SASD-REP-033 | Kurzlebige Feature- oder Fix-Branches SOLLTEN zeitnah integriert oder geschlossen werden. |
| SASD-REP-034 | Direkte Änderungen an geschützten Production-Repositories SOLLTEN durch Reviews und automatisierte Prüfungen kontrolliert werden. |

### 3.5 Commits

| ID | Anforderung |
|---|---|
| SASD-REP-040 | Commits MÜSSEN eine verständliche, handlungsorientierte Nachricht besitzen. |
| SASD-REP-041 | Ein Commit SOLLTE eine kohärente Änderung darstellen und nicht unnötig unabhängige Themen vermischen. |
| SASD-REP-042 | Geheimnisse und produktive Zugangsdaten DÜRFEN NICHT committed werden. Ein späteres Löschen ersetzt nicht die Rotation kompromittierter Zugangsdaten. |
| SASD-REP-043 | Automatisch erzeugte Massenänderungen SOLLTEN von fachlichen Änderungen getrennt werden. |
| SASD-REP-044 | Rewriting veröffentlichter Historie SOLLTE vermieden werden, wenn andere Nutzer oder Systeme darauf angewiesen sein können. |
| SASD-REP-045 | Ein konsistentes Commit-Konventionsmodell, beispielsweise Conventional Commits, KANN verwendet werden und SOLLTE automatisiert geprüft werden, wenn Releases daraus abgeleitet werden. |

### 3.6 Reviews und Pull Requests

| ID | Anforderung |
|---|---|
| SASD-REP-050 | Änderungen mit hohem Risiko SOLLTEN über einen nachvollziehbaren Reviewprozess integriert werden. |
| SASD-REP-051 | Pull Requests oder gleichwertige Änderungsnachweise SOLLTEN Zweck, Auswirkungen, Tests, Dokumentationsänderungen und offene Risiken benennen. |
| SASD-REP-052 | Production-Änderungen an sicherheits-, daten- oder betriebsrelevanten Bereichen MÜSSEN geprüft oder durch eine dokumentierte strukturierte Selbstprüfung freigegeben werden. |
| SASD-REP-053 | Fehlgeschlagene Pflichtprüfungen DÜRFEN NICHT ohne dokumentierte Ausnahme umgangen werden. |
| SASD-REP-054 | Reviewkommentare und Entscheidungen SOLLTEN sachlich, begründet und auf das Projektziel bezogen sein. |

### 3.7 Issues, Roadmap und Nachverfolgung

| ID | Anforderung |
|---|---|
| SASD-REP-060 | Offene Fehler, Risiken und geplante Arbeiten MÜSSEN in einem auffindbaren System nachverfolgbar sein. |
| SASD-REP-061 | GitHub Issues, lokale Markdown-Dateien oder andere Systeme sind zulässig, sofern die Source of Truth eindeutig ist. |
| SASD-REP-062 | Kritische Sicherheitsprobleme DÜRFEN NICHT unnötig öffentlich offengelegt werden, bevor ein koordinierter Umgang möglich ist. |
| SASD-REP-063 | Geschlossene oder verworfene Arbeiten SOLLTEN mit einer erkennbaren Entscheidung enden. |

### 3.8 Tags, Releases und Artefakte

| ID | Anforderung |
|---|---|
| SASD-REP-070 | Veröffentlichte Versionen MÜSSEN auf einen unveränderlichen Commit oder gleichwertigen Quellstand zurückführbar sein. |
| SASD-REP-071 | Tags für Releases MÜSSEN eindeutig und konsistent benannt werden. |
| SASD-REP-072 | Releaseartefakte MÜSSEN zur dokumentierten Version passen. |
| SASD-REP-073 | Production-Artefakte SOLLTEN automatisiert aus dem freigegebenen Quellstand erzeugt werden. |
| SASD-REP-074 | Prüfsummen, Signaturen oder Provenance-Nachweise SOLLTEN für extern verteilte oder sicherheitsrelevante Artefakte bereitgestellt werden. |

### 3.9 Plattformkonfiguration

| ID | Anforderung |
|---|---|
| SASD-REP-080 | Repository-Beschreibung, Topics oder Tags und Website-Verweis SOLLTEN gepflegt werden. |
| SASD-REP-081 | Branch Protection, Required Reviews und Required Checks SOLLTEN dem Risiko und der Teamgröße entsprechen. |
| SASD-REP-082 | Automatisierte Abhängigkeits- und Sicherheitsmeldungen SOLLTEN aktiviert werden, wenn die Plattform sie anbietet und sie sinnvoll ausgewertet werden können. |
| SASD-REP-083 | Workflow-Berechtigungen MÜSSEN nach dem Prinzip geringstmöglicher Rechte konfiguriert werden. |
| SASD-REP-084 | Drittanbieter-Actions oder Plugins MÜSSEN hinsichtlich Herkunft, Berechtigungen und Versionierung geprüft werden. |

### 3.10 Archivierung

| ID | Anforderung |
|---|---|
| SASD-REP-090 | Ein archiviertes Repository MUSS seinen Status im README sichtbar machen. |
| SASD-REP-091 | Letzte unterstützte Version, Nachfolgeprojekt und bekannte Sicherheitsrisiken SOLLTEN genannt werden. |
| SASD-REP-092 | Vor Archivierung MÜSSEN offene Geheimnisse, aktive Tokens, Deployments und unnötige Automatisierungen deaktiviert oder entfernt werden. |
| SASD-REP-093 | Historische Tags und Releases SOLLTEN erhalten bleiben, sofern keine Sicherheits- oder Rechtsgründe dagegensprechen. |

## 4. Zuordnung zu Qualitätsstufen

| Bereich | Minimum | Recommended | Production |
|---|---|---|---|
| README, Lizenzstatus, Ignore-Regeln | MUSS | MUSS | MUSS |
| strukturierte Verzeichnisse | angemessen SOLLTE | MUSS | MUSS |
| Issues / Roadmap | einfache Liste SOLLTE | MUSS | MUSS |
| Reviewprozess | KANN | risikobasiert SOLLTE | MUSS für wesentliche Änderungen |
| CI-Prüfungen | KANN | SOLLTE | MUSS soweit automatisierbar |
| Branch Protection | KANN | SOLLTE bei mehreren Beteiligten | MUSS für kritische Hauptlinie |
| Release-Tags | bei Releases MUSS | MUSS | MUSS |
| Provenance / Signatur / Prüfsumme | KANN | bei externer Verteilung SOLLTE | MUSS oder begründete Alternative |

## 5. Verantwortlichkeiten

Maintainer pflegen Hauptlinie, Metadaten, Releases und Plattformkonfiguration. Beitragende erstellen nachvollziehbare Änderungen. Reviewer prüfen Inhalt, Risiken und Nachweise.

## 6. Nachweise und Prüfkriterien

Geeignete Nachweise sind Repository-Dateibaum, Plattform-Einstellungen, Commit-Historie, Pull Requests, CI-Protokolle, Tags, Releases und Security-Konfiguration.

## 7. Ausnahmen und Abweichungen

Ein privates Einpersonenprojekt darf auf Pull Requests oder Issues verzichten, wenn Änderungen, offene Arbeiten und Selbstprüfungen anderweitig nachvollziehbar bleiben.

## 8. Verwandte Dokumente

- [Dokumentationsstandard](DOCUMENTATION.md)
- [Release-Standard](RELEASES.md)
- [Sicherheitsstandard](SECURITY.md)
- [Repository-Metadaten-Template](../../templates/repositories/REPOSITORY-METADATA-TEMPLATE.md)
