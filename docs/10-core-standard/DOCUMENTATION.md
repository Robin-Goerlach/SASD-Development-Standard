---
title: "Dokumentationsstandard"
document-id: SASD-CORE-004
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
depends-on: [SASD-FND-003, SASD-GOV-001, SASD-GOV-003, SASD-CORE-001, SASD-CORE-006]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Dokumentationsstandard

## 1. Zweck

Dieses Dokument definiert Mindestinhalte, Qualitätskriterien, Verantwortlichkeiten und Pflegeanforderungen für Projektdokumentation.

## 2. Geltungsbereich

Dokumentation umfasst alle Informationen, die zum Verstehen, Erstellen, Testen, Verwenden, Betreiben, Warten, Migrieren und Archivieren eines Projekts benötigt werden. Form und Umfang richten sich nach Qualitätsstufe, Projektrisiko und Zielgruppe.

## 3. Grundsätze

- Dokumentation ist Teil des Produkts.
- Die verbindliche Quelle muss eindeutig sein.
- Informationen sollen dort stehen, wo Leser sie erwarten.
- Doppelte Inhalte sollen vermieden oder klar als abgeleitet gekennzeichnet werden.
- Dokumentation muss mit dem tatsächlichen Projektstand übereinstimmen.
- Erzeugte Dokumente dürfen ihre Quelle nicht ersetzen.

## 4. Normative Anforderungen

### 4.1 Source of Truth und Ablage

| ID | Anforderung |
|---|---|
| SASD-DOC-001 | Jedes Projekt MUSS eine eindeutige Source of Truth für seine Dokumentation benennen. |
| SASD-DOC-002 | Dokumentation SOLLTE gemeinsam mit dem Projekt versioniert werden, wenn sie den jeweiligen Projektstand beschreibt. |
| SASD-DOC-003 | Parallel gepflegte, inhaltlich gleichwertige Fassungen DÜRFEN NICHT ohne festgelegten Synchronisationsprozess als gleichermaßen verbindlich gelten. |
| SASD-DOC-004 | Erzeugte Word-, PDF-, HTML- oder andere Publikationen MÜSSEN als abgeleitete Artefakte erkennbar sein. |
| SASD-DOC-005 | Geheimnisse, produktive Zugangsdaten und unnötige personenbezogene Daten DÜRFEN NICHT in Dokumentation oder Beispielen enthalten sein. |

### 4.2 Auffindbarkeit und Navigation

| ID | Anforderung |
|---|---|
| SASD-DOC-010 | Das Root-README MUSS Zweck, Status, Einstieg, Nutzung oder Buildweg sowie weiterführende Dokumentation auffindbar machen. |
| SASD-DOC-011 | Dokumente MÜSSEN über README, Dokumentationsindex oder nachvollziehbare Verzeichnisstruktur erreichbar sein. |
| SASD-DOC-012 | Dateinamen SOLLTEN stabil, eindeutig und sprechend sein. |
| SASD-DOC-013 | Relative Links SOLLTEN innerhalb des Repositories verwendet und automatisiert geprüft werden. |
| SASD-DOC-014 | Veraltete Dokumente MÜSSEN als veraltet gekennzeichnet, aktualisiert oder archiviert werden. |

### 4.3 Zielgruppen und Schreibqualität

| ID | Anforderung |
|---|---|
| SASD-DOC-020 | Ein Dokument MUSS seinen Zweck und seine primäre Zielgruppe erkennen lassen. |
| SASD-DOC-021 | Anweisungen MÜSSEN Voraussetzungen, Schritte und erwartete Ergebnisse enthalten, soweit dies für eine reproduzierbare Durchführung erforderlich ist. |
| SASD-DOC-022 | Begriffe und Abkürzungen SOLLTEN konsistent verwendet und bei Bedarf im Glossar erklärt werden. |
| SASD-DOC-023 | Beispiele MÜSSEN als Beispiele erkennbar sein und DÜRFEN NICHT unbeabsichtigt neue normative Regeln einführen. |
| SASD-DOC-024 | Aussagen über unterstützte Versionen, Plattformen oder Betriebsbedingungen MÜSSEN überprüfbar und aktuell sein. |

### 4.4 Pflege und Aktualisierung

| ID | Anforderung |
|---|---|
| SASD-DOC-030 | Dokumentation MUSS im selben Änderungsvorgang aktualisiert werden, wenn Verhalten, Konfiguration, Schnittstellen, Installation, Sicherheit oder Betrieb geändert werden. |
| SASD-DOC-031 | Jedes wesentliche Dokument MUSS einen verantwortlichen Owner besitzen oder eindeutig einem Projektverantwortlichen zugeordnet sein. |
| SASD-DOC-032 | Recommended- und Production-Projekte SOLLTEN Dokumentation zu Meilensteinen oder Releases systematisch prüfen. |
| SASD-DOC-033 | Production-Dokumentation MUSS vor einem Release auf sicherheits-, betriebs- und migrationsrelevante Aktualität geprüft werden. |
| SASD-DOC-034 | Bekannte Dokumentationslücken MÜSSEN nachverfolgbar sein. |

### 4.5 Pflichtdokumente und bedingte Dokumente

| ID | Anforderung |
|---|---|
| SASD-DOC-040 | Jedes Projekt MUSS mindestens README, Lizenzstatus, Qualitätsstufe, Build- oder Nutzungshinweise und bekannte wesentliche Einschränkungen dokumentieren. |
| SASD-DOC-041 | Ein öffentlich verteiltes Projekt MUSS eine Lizenz oder einen ausdrücklichen Hinweis auf fehlende Nutzungsrechte enthalten. |
| SASD-DOC-042 | Recommended- und Production-Projekte MÜSSEN Roadmap oder Wartungsstatus, Changelog oder Releasehistorie, Anforderungen, Architektur, Testansatz und Sicherheitskontakt oder Sicherheitsrichtlinie dokumentieren. |
| SASD-DOC-043 | Production-Projekte MÜSSEN zusätzlich Betriebs-, Backup-, Wiederherstellungs-, Incident-, Migrations- und End-of-Life-Informationen bereitstellen, soweit anwendbar. |
| SASD-DOC-044 | API-, Datenbank-, Deployment-, Benutzer- oder Administratorendokumentation MUSS vorhanden sein, wenn das Projekt entsprechende Schnittstellen, Datenstrukturen oder Betriebsaufgaben besitzt. |

### 4.6 Code- und Konfigurationsdokumentation

| ID | Anforderung |
|---|---|
| SASD-DOC-050 | Öffentliche Schnittstellen und nicht offensichtliche Verträge SOLLTEN in technologiegeeigneter Form dokumentiert werden. |
| SASD-DOC-051 | Kommentare SOLLTEN Gründe, Randbedingungen und nicht offensichtliche Konsequenzen erklären, nicht lediglich den Code wiederholen. |
| SASD-DOC-052 | Temporäre Workarounds, Sicherheitsannahmen und Kompatibilitätsgrenzen MÜSSEN sichtbar und nachverfolgbar sein. |
| SASD-DOC-053 | Konfigurationsoptionen MÜSSEN Bedeutung, erlaubte Werte, Standardverhalten und Sicherheitsauswirkungen erklären, wenn diese nicht offensichtlich sind. |
| SASD-DOC-054 | Beispielkonfigurationen DÜRFEN NICHT so gestaltet sein, dass unsichere Werte unbeabsichtigt als empfohlener Produktivstandard erscheinen. |

### 4.7 Übersetzungen

| ID | Anforderung |
|---|---|
| SASD-DOC-060 | Bei mehreren Sprachfassungen MUSS die autoritative Fassung eindeutig benannt werden. |
| SASD-DOC-061 | Übersetzungen MÜSSEN auf die Version der Ausgangsfassung verweisen. |
| SASD-DOC-062 | Eine veraltete Übersetzung MUSS als solche erkennbar sein und DARF NICHT denselben Aktualitätsstatus vortäuschen. |

### 4.8 Barrierefreiheit und Formate

| ID | Anforderung |
|---|---|
| SASD-DOC-070 | Dokumente SOLLTEN mit klarer Überschriftenhierarchie, verständlichen Linktexten, beschrifteten Tabellen und Alternativtexten für informative Bilder erstellt werden. |
| SASD-DOC-071 | Wesentliche Informationen DÜRFEN NICHT ausschließlich durch Farbe oder visuelle Position vermittelt werden. |
| SASD-DOC-072 | Publikationsformate SOLLTEN Textsuche, Kopieren und maschinelle Verarbeitung ermöglichen, soweit dies praktisch möglich ist. |

## 5. Dokumentmatrix je Qualitätsstufe

| Dokument oder Inhalt | Minimum | Recommended | Production |
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

## 6. Verantwortlichkeiten

Autoren aktualisieren betroffene Dokumentation. Reviewer prüfen Verständlichkeit, Konsistenz und Sicherheitsrisiken. Maintainer stellen Navigation, Versionierung und Archivierung sicher.

## 7. Nachweise und Prüfkriterien

Geeignete Nachweise sind Dokumentationsindex, automatisierte Linkprüfung, Review-Checkliste, Änderungsdiff, Publikationsprotokoll und dokumentierte Owner.

## 8. Ausnahmen und Abweichungen

Ein kleines Projekt darf mehrere Dokumentrollen in README oder einer Projektübersicht zusammenfassen. Die zusammengeführte Form MUSS weiterhin alle anwendbaren Inhalte auffindbar machen.

## 9. Verwandte Dokumente

- [Repository- und GitHub-Standard](REPOSITORY.md)
- [Wissensmanagement](KNOWLEDGE-MANAGEMENT.md)
- [Dokumentmetadaten](../40-governance/DOCUMENT-METADATA.md)
- [README-Template](../../templates/documents/README-TEMPLATE.md)
