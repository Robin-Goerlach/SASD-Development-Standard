---
title: "Inhaltsarchitektur für SASD Development Standard Version 1.0"
document-id: SASD-FND-005
document-type: normative
status: Proposed
version: 0.1.0
standard-version: "1.0"
language: de
authoritative: true
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-FND-001, SASD-FND-002, SASD-FND-003, SASD-GOV-001, SASD-GOV-002, SASD-GOV-003]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Inhaltsarchitektur für Version 1.0

## 1. Zweck

Dieses Dokument definiert die verbindliche Informations- und Dokumentarchitektur des **SASD Development Standard Version 1.0**. Es legt fest:

- aus welchen Dokumentgruppen der Standard besteht,
- welche Rolle und Verbindlichkeit diese Gruppen besitzen,
- welche Dokumente für Version 1.0 vorgesehen sind,
- wie Kernstandard, Profile, Qualitätsstufen und Prozesse zusammenwirken,
- welche Metadaten normative Dokumente tragen,
- welche Abhängigkeiten und Vorrangregeln gelten,
- wie Übersetzungen und Publikationsformate behandelt werden,
- und anhand welcher Kriterien die Inhaltsarchitektur als vollständig gilt.

Die detaillierte Liste aller Dokumente, Dokument-IDs, Zwecke, Abhängigkeiten und geplanten Reifegrade befindet sich im [Dokumentkatalog](DOCUMENT-CATALOG.md).

## 2. Geltungsbereich

Diese Inhaltsarchitektur gilt für:

1. den technologieunabhängigen Kernstandard,
2. die für Version 1.0 vorgesehenen Profile C#/.NET und Desktop,
3. die Projekt- und Governance-Prozesse,
4. Vorlagen, Checklisten, Prompts und Tooling,
5. Referenzimplementierungen und Pilotmigrationen,
6. aus Markdown erzeugte Word- und PDF-Publikationen.

Detaillierte Profile für Linux, Datenbanken, Container, Kubernetes, Web-APIs und erweiterte Sicherheit sind Teil der langfristigen Produktvision, aber nicht notwendiger Bestandteil der Fertigstellung von Version 1.0.

## 3. Architekturgrundsätze

### 3.1 Eine normative Quelle

Die Markdown-Dateien im Repository sind die verbindliche **Source of Truth**. Word-, PDF- und andere Ausgaben werden aus diesen Quellen erzeugt und DARF NICHT parallel als eigenständige normative Fassung gepflegt werden.

### 3.2 Trennung von Regel, Erklärung und Hilfsmittel

Verbindliche Anforderungen, erklärende Inhalte und operative Hilfsmittel MÜSSEN unterscheidbar sein. Eine Checkliste, ein Prompt oder ein Beispiel DARF NICHT unbemerkt neue Anforderungen einführen.

### 3.3 Technologieunabhängiger Kern

Allgemeine Anforderungen werden im Kernstandard definiert. Technologie- oder projektspezifische Regeln gehören in Profile. Dadurch bleibt der Kern auf Software-, Infrastruktur- und andere technische Projekte anwendbar.

### 3.4 Angemessene Skalierung

Die Qualitätsstufen **SASD Minimum**, **SASD Recommended** und **SASD Production** bestimmen die erforderliche Tiefe der Umsetzung. Die Qualitätsstufe verändert nicht die Bedeutung einer Anforderung, sondern entscheidet, ob und in welchem Umfang sie für ein Projekt gilt.

### 3.5 Nachvollziehbare Abweichungen

Profile und Projekte dürfen den Kernstandard nicht stillschweigend abschwächen. Notwendige Abweichungen werden nach dem Governance-Dokument `EXCEPTIONS.md` dokumentiert.

### 3.6 Schrittweise Reife

Vor Version 1.0 dürfen Dokumente in unterschiedlichen Reifegraden vorliegen. Nur Dokumente mit Status **Approved** sind verbindlicher Bestandteil einer veröffentlichten Standardversion.

## 4. Dokumentklassen

### 4.1 Normative Dokumente

Normative Dokumente enthalten Anforderungen, Definitionen oder verbindliche Prozesse. Sie verwenden die Schlüsselwörter aus `NORMATIVE-LANGUAGE.md`.

Beispiele:

- Kernstandard,
- Profile,
- Governance-Regeln,
- verbindliche Prozessdefinitionen,
- Scope und Grundprinzipien.

Ein normatives Dokument MUSS die Metadaten aus `DOCUMENT-METADATA.md` enthalten.

### 4.2 Informative Dokumente

Informative Dokumente erklären Hintergründe, begründen Entscheidungen oder zeigen Beispiele. Sie dürfen normative Inhalte zusammenfassen, aber DARF NICHT die verbindliche Quelle einer Anforderung sein.

Beispiele:

- Referenzimplementierungen,
- Erläuterungen,
- Tutorials,
- Lessons Learned,
- FAQ,
- Migrationsbeispiele.

### 4.3 Unterstützende Artefakte

Unterstützende Artefakte helfen bei der praktischen Anwendung des Standards.

Dazu gehören:

- Vorlagen,
- Checklisten,
- Prompt-Pakete,
- Konfigurationsdateien,
- Skripte,
- GitHub Workflows,
- Generatoren und Validatoren.

Unterstützende Artefakte können normativ geforderte Nachweise erzeugen oder prüfen, sind aber selbst nur dann normativ, wenn ein Approved-Dokument dies ausdrücklich festlegt.

## 5. Hierarchie des Standards

Ein Projekt wendet den Standard in folgender Zusammensetzung an:

```text
veröffentlichte Standardversion
+ technologieunabhängiger Kernstandard
+ ausgewählte Technologie- und Projektprofile
+ gewählte Qualitätsstufe
+ Projektklassifikation
+ dokumentierte und genehmigte Abweichungen
```

### 5.1 Kernstandard

Der Kernstandard gilt grundsätzlich für alle Projekte, sofern eine Anforderung nicht ausdrücklich auf bestimmte Projektarten oder Qualitätsstufen beschränkt ist.

### 5.2 Profile

Profile konkretisieren den Kernstandard für eine Technologie, Plattform oder Projektart.

Ein Profil:

- MUSS auf relevante Kernanforderungen verweisen,
- KANN Anforderungen präzisieren oder verschärfen,
- DARF Kernanforderungen nicht stillschweigend widersprechen,
- MUSS einen ausdrücklichen Vorranghinweis enthalten, falls eine fachlich notwendige Sonderregel besteht.

Für Version 1.0 sind verbindlich vorgesehen:

- C#/.NET-Profil,
- Desktopanwendungsprofil.

### 5.3 Qualitätsstufen

Die Qualitätsstufe bestimmt, welche Anforderungen für ein Projekt mindestens anzuwenden sind.

| Qualitätsstufe | Typischer Einsatz |
|---|---|
| SASD Minimum | kleine Werkzeuge, Lernprojekte, Experimente und Prototypen |
| SASD Recommended | gepflegte Anwendungen, öffentliche Repositories und reguläre SASD-Projekte |
| SASD Production | geschäftskritische, sicherheitssensitive, kundennahe oder operative Systeme |

Ein Projekt MUSS genau eine primäre Qualitätsstufe benennen. Es KANN einzelne Bereiche freiwillig auf einer höheren Stufe umsetzen.

### 5.4 Prozesse

Prozessdokumente beschreiben wiederholbare Abläufe, beispielsweise Projektinitialisierung, Review, Migration oder Release.

Ein Prozessdokument:

- MUSS Startbedingungen, Schritte, Ergebnisse und Abschlusskriterien benennen,
- SOLLTE Rollen oder Verantwortlichkeiten nennen,
- DARF keine versteckten Anforderungen erzeugen,
- MUSS auf die zugrunde liegenden normativen Dokumente verweisen.

### 5.5 Governance

Governance-Dokumente regeln die Entwicklung und Anwendung des Standards selbst. Dazu gehören normative Sprache, Dokumentstatus, Metadaten, Versionierung, Änderungen, Ausnahmen und Compliance.

## 6. Vorrang- und Konfliktregeln

Bei Widersprüchen gilt folgende Reihenfolge:

1. eine ausdrücklich genehmigte, projektbezogene Abweichung,
2. eine ausdrücklich als vorrangig gekennzeichnete Spezialregel eines anwendbaren Profils,
3. der technologieunabhängige Kernstandard,
4. normative Prozess- und Governance-Dokumente,
5. informative Dokumente und Referenzimplementierungen,
6. Vorlagen, Checklisten, Prompts und Tooling.

Diese Reihenfolge bedeutet nicht, dass eine Abweichung allgemein gültige Regeln ersetzt. Sie gilt ausschließlich für das dokumentierte Projekt und den genehmigten Umfang.

Wird ein Widerspruch entdeckt, MUSS er dokumentiert und durch eine Änderung des Standards oder eine ausdrückliche Abweichung aufgelöst werden.

## 7. Repository- und Dokumentgruppen

| Pfad | Rolle | Charakter | Bestandteil von Version 1.0 |
|---|---|---|---|
| `docs/00-foundation` | Mandat, Scope, Prinzipien, Begriffe und Inhaltsarchitektur | überwiegend normativ | ja |
| `docs/10-core-standard` | technologieunabhängige Anforderungen | normativ | ja |
| `docs/20-profiles/dotnet` | C#/.NET-Konkretisierung | normativ | ja |
| `docs/20-profiles/desktop` | Desktopanwendungs-Konkretisierung | normativ | ja |
| `docs/20-profiles/*` weitere | vorbereitete spätere Fachprofile | informativ/geplant | nein |
| `docs/30-processes` | wiederholbare Arbeitsabläufe | normativ und anleitend | ja |
| `docs/40-governance` | Pflege, Versionierung, Ausnahmen und Compliance | normativ | ja |
| `docs/50-reference-implementations` | Pilotprojekte, Beispiele und Erkenntnisse | informativ | ja, mindestens drei Piloten |
| `templates` | wiederverwendbare Vorlagen | unterstützend | ja |
| `checklists` | operative Prüf- und Arbeitslisten | unterstützend | ja |
| `prompts` | standardisierte KI-Arbeitsanweisungen | unterstützend | ja |
| `tooling` | Erzeugung und Prüfung | unterstützend | ja, Basistooling |
| `examples` | kurze, isolierte Anwendungsbeispiele | informativ | optional |
| `artefacts` | erzeugte Veröffentlichungen | abgeleitet | ja für Release 1.0 |
| `.github` | Zusammenarbeit und Automatisierung | unterstützend | ja |

## 8. Verbindliche Dokumentstruktur für Version 1.0

### 8.1 Foundation

Die Foundation definiert Identität, Grenzen und Struktur des Standards:

- `PROJECT-CHARTER.md`
- `SCOPE.md`
- `PRINCIPLES.md`
- `GLOSSARY.md`
- `CONTENT-ARCHITECTURE.md`
- `DOCUMENT-CATALOG.md`
- `VERSION-1.0-ACCEPTANCE-CRITERIA.md`

### 8.2 Core Standard

Der Core Standard enthält technologieunabhängige Anforderungen:

- `PROJECT-LIFECYCLE.md`
- `REQUIREMENTS.md`
- `ARCHITECTURE.md`
- `DOCUMENTATION.md`
- `REPOSITORY.md`
- `QUALITY-LEVELS.md`
- `QUALITY.md`
- `SECURITY.md`
- `TESTING.md`
- `RELEASES.md`
- `MAINTENANCE.md`
- `KNOWLEDGE-MANAGEMENT.md`
- `AI-ASSISTED-DEVELOPMENT.md`

### 8.3 C#/.NET-Profil

- `DOTNET-PROFILE.md`
- `SOLUTION-STRUCTURE.md`
- `CODING-STANDARD.md`
- `ERROR-HANDLING.md`
- `LOGGING.md`
- `CONFIGURATION.md`
- `PERSISTENCE.md`
- `DOTNET-TESTING.md`

### 8.4 Desktopprofil

- `DESKTOP-PROFILE.md`
- `UI-ARCHITECTURE.md`
- `USER-EXPERIENCE.md`
- `APPLICATION-LIFECYCLE.md`

### 8.5 Prozesse

- `NEW-PROJECT.md`
- `PROJECT-CLASSIFICATION.md`
- `ARCHITECTURE-DECISION-PROCESS.md`
- `REVIEW-PROCESS.md`
- `LEGACY-MIGRATION.md`
- `RELEASE-PROCESS.md`
- `PROJECT-ARCHIVAL.md`

### 8.6 Governance

- `NORMATIVE-LANGUAGE.md`
- `DOCUMENT-LIFECYCLE.md`
- `DOCUMENT-METADATA.md`
- `VERSIONING.md`
- `CHANGE-PROCESS.md`
- `EXCEPTIONS.md`
- `COMPLIANCE.md`

### 8.7 Referenzimplementierungen

Version 1.0 MUSS Erfahrungen aus mindestens drei Pilotkategorien dokumentieren:

1. kleines C#/.NET-Werkzeug,
2. mittlere gepflegte Desktopanwendung,
3. komplexere, geschichtete C#/.NET-Anwendung.

Der Quellcode der Pilotprojekte verbleibt in den jeweiligen Projekt-Repositories. Dieses Repository dokumentiert Auswahl, angewendete Profile, Qualitätsstufe, Abweichungen und Lessons Learned.

## 9. Dokumentmetadaten

Normative Dokumente MÜSSEN YAML-Front-Matter verwenden. Das verbindliche Schema steht in `DOCUMENT-METADATA.md`.

Mindestens erforderlich sind:

- Titel,
- Dokument-ID,
- Dokumenttyp,
- Status,
- Dokumentversion,
- Zielversion des Standards,
- Sprache,
- Kennzeichnung der autoritativen Fassung,
- verantwortliche Rolle,
- Datum der letzten inhaltlichen Änderung,
- anwendbare Qualitätsstufen,
- anwendbare Profile,
- Dokumentabhängigkeiten.

## 10. Standardaufbau normativer Dokumente

Ein normatives Dokument SOLLTE folgende Abschnitte besitzen, soweit sie für den Inhalt sinnvoll sind:

1. Zweck,
2. Geltungsbereich,
3. Begriffe und Abgrenzungen,
4. normative Anforderungen,
5. Zuordnung zu Qualitätsstufen,
6. Verantwortlichkeiten,
7. erforderliche Nachweise,
8. zulässige Abweichungen,
9. Prüfkriterien,
10. verwandte Dokumente.

Kurze Foundation- oder Governance-Dokumente dürfen davon abweichen, wenn Zweck und Anforderungen dennoch eindeutig bleiben.

## 11. Anforderungskennzeichnungen

Ab dem Kernstandard SOLLTEN normative Anforderungen stabile Kennzeichnungen erhalten.

Beispiel:

```text
SASD-DOC-REQ-001
SASD-SEC-REQ-014
SASD-DOTNET-REQ-023
```

Eine Kennzeichnung:

- MUSS innerhalb eines Dokuments eindeutig sein,
- SOLLTE nach Veröffentlichung nicht wiederverwendet werden,
- DARF bei redaktionellen Änderungen unverändert bleiben,
- MUSS bei inhaltlicher Ersetzung nachvollziehbar als ersetzt oder entfernt markiert werden.

## 12. Sprache und Übersetzungen

Bis zur Stabilisierung von Version 1.0 ist Deutsch die autoritative Sprache der normativen Entwürfe.

Eine englische Übersetzung:

- MUSS aus der deutschen Source of Truth abgeleitet werden,
- MUSS die zugrunde liegende Dokumentversion nennen,
- DARF keine zusätzlichen Anforderungen enthalten,
- MUSS bei inhaltlichen Abweichungen als nicht autoritativ gekennzeichnet werden,
- SOLLTE erst nach Stabilisierung der Terminologie vollständig gepflegt werden.

Eine spätere zweisprachig autoritative Veröffentlichung erfordert einen eigenen Governance-Beschluss.

## 13. Word-, PDF- und andere Publikationen

Veröffentlichungsartefakte werden unter `artefacts/publications` erzeugt.

Sie:

- MÜSSEN die zugrunde liegende Standardversion nennen,
- MÜSSEN auf die Repository-Quelle verweisen,
- SOLLTEN Erzeugungsdatum und Commit oder Tag enthalten,
- DÜRFEN NICHT als separat gepflegte normative Quelle verwendet werden.

## 14. Änderungs- und Freigabemodell

Dokumente durchlaufen den in `DOCUMENT-LIFECYCLE.md` definierten Lebenszyklus:

```text
Planned -> Draft -> Proposed -> Approved -> Deprecated -> Retired
```

Für ein öffentliches Release des Standards gilt:

- alle für das Release erforderlichen normativen Dokumente MÜSSEN Approved sein,
- bekannte Widersprüche MÜSSEN gelöst oder ausdrücklich dokumentiert sein,
- Änderungen MÜSSEN im Changelog nachvollziehbar sein,
- abgeleitete Artefakte MÜSSEN aus dem markierten Repository-Stand erzeugt werden.

## 15. Abgrenzung von Version 1.0

Nicht erforderlich für die Fertigstellung von Version 1.0 sind:

- vollständige Linux-, Datenbank-, Container- oder Kubernetes-Profile,
- umfassende Team- und Unternehmensgovernance,
- formale Zertifizierung durch Dritte,
- ein vollständiger universeller Compliance-Auditor,
- detaillierte Regeln für Großunternehmen,
- vollständige Toolunterstützung für jede Anforderung.

Diese Themen können vorbereitet oder informativ erwähnt werden, dürfen aber die Freigabe von Version 1.0 nicht blockieren.

## 16. Akzeptanzkriterien dieser Inhaltsarchitektur

Die Inhaltsarchitektur ist freigabefähig, wenn:

1. jede für Version 1.0 erforderliche Dokumentrolle benannt ist,
2. jedes normative Dokument eine stabile Dokument-ID besitzt,
3. normative, informative und unterstützende Inhalte getrennt sind,
4. Kernstandard, Profile, Qualitätsstufen und Prozesse eindeutig zusammenwirken,
5. Vorrang- und Konfliktregeln dokumentiert sind,
6. Dokumentstatus und Metadaten definiert sind,
7. Übersetzungen und abgeleitete Publikationen geregelt sind,
8. der Dokumentkatalog keine ungeklärten Doppelzuständigkeiten enthält,
9. ausgeschlossene Themen klar abgegrenzt sind,
10. README, Roadmap und Dokumentkatalog auf diese Architektur verweisen.

## 17. Nächster Schritt nach Freigabe

Nach Freigabe dieser Inhaltsarchitektur werden die Dokumente des Kernstandards in der Reihenfolge ausgearbeitet, die in `ROADMAP.md` und `DOCUMENT-CATALOG.md` festgelegt ist. Einzelne Coding- oder Technologieentscheidungen werden erst im passenden Profil normativ festgelegt.
