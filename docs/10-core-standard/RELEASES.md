---
title: "Release-Standard"
document-id: SASD-CORE-010
document-type: normative
status: Proposed
version: 0.3.0
standard-version: "1.0"
language: de
authoritative: true
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core]
depends-on: [SASD-FND-003, SASD-GOV-001, SASD-GOV-004, SASD-CORE-005, SASD-CORE-006, SASD-CORE-007, SASD-CORE-008, SASD-CORE-009]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Release-Standard

## 1. Zweck

Dieses Dokument definiert Versionierung, Freigabekriterien, Release Notes, Artefakte, Rückverfolgbarkeit, Migration, Rollback und Veröffentlichung.

## 2. Geltungsbereich

Ein Release ist ein identifizierbarer, für Nutzung oder Verteilung freigegebener Projektstand. Das kann eine Anwendung, Bibliothek, Infrastrukturdefinition, Dokumentation, Datenmigration oder ein anderes technisches Produkt sein.

## 3. Normative Anforderungen

### 3.1 Releaseidentität und Versionierung

| ID | Anforderung |
|---|---|
| SASD-REL-001 | Jedes Release MUSS eindeutig identifizierbar und auf einen unveränderlichen Quellstand zurückführbar sein. |
| SASD-REL-002 | Das Versionsschema MUSS dokumentiert und konsistent angewendet werden. |
| SASD-REL-003 | Semantic Versioning SOLLTE verwendet werden, wenn das Projekt einen definierten öffentlichen Vertrag oder eine öffentliche API besitzt. |
| SASD-REL-004 | Vorabversionen MÜSSEN als Alpha, Beta, Preview, Release Candidate oder gleichwertig erkennbar sein. |
| SASD-REL-005 | Eine einmal veröffentlichte Versionsnummer DARF NICHT für inhaltlich veränderte Artefakte wiederverwendet werden. |

### 3.2 Releaseumfang

| ID | Anforderung |
|---|---|
| SASD-REL-010 | Der Umfang eines Releases MUSS vor der Freigabe erkennbar sein. |
| SASD-REL-011 | Enthaltene Änderungen MÜSSEN auf Anforderungen, Fehler, Wartungsarbeiten oder technische Entscheidungen zurückführbar sein. |
| SASD-REL-012 | Nicht abgeschlossene oder bewusst verschobene Inhalte MÜSSEN vom Releaseumfang unterscheidbar sein. |
| SASD-REL-013 | Unbeabsichtigte Entwicklungs-, Test- oder Debugartefakte DÜRFEN NICHT im Release enthalten sein. |

### 3.3 Freigabekriterien

| ID | Anforderung |
|---|---|
| SASD-REL-020 | Ein Release MUSS die für seine Qualitätsstufe geltende Definition of Done erfüllen. |
| SASD-REL-021 | Pflichtbuilds, Tests, Dokumentations- und Sicherheitsprüfungen MÜSSEN erfolgreich sein oder eine genehmigte Ausnahme besitzen. |
| SASD-REL-022 | Bekannte Defekte und Einschränkungen MÜSSEN hinsichtlich Auswirkung und Vertretbarkeit bewertet werden. |
| SASD-REL-023 | Production-Releases MÜSSEN eine ausdrückliche, nachvollziehbare Freigabe besitzen. |
| SASD-REL-024 | Ein Release DARF NICHT freigegeben werden, wenn erforderliche Migration, Backup oder Rückfallmaßnahmen ungeklärt sind. |

### 3.4 Release Notes und Changelog

| ID | Anforderung |
|---|---|
| SASD-REL-030 | Jedes extern verteilte oder längerfristig genutzte Release MUSS Änderungen für Nutzer und Betreiber verständlich beschreiben. |
| SASD-REL-031 | Breaking Changes, Sicherheitsänderungen, Migrationen, bekannte Probleme und erforderliche Handlungen MÜSSEN hervorgehoben werden. |
| SASD-REL-032 | Ein Changelog SOLLTE einen Unreleased-Bereich und versionierte Einträge besitzen. |
| SASD-REL-033 | Commit-Historie allein SOLLTE NICHT als nutzerorientierte Releasebeschreibung verwendet werden. |
| SASD-REL-034 | Sicherheitsrelevante Details MÜSSEN so kommuniziert werden, dass Nutzer handeln können, ohne unnötig Missbrauch zu erleichtern. |

### 3.5 Reproduzierbarkeit und Artefakte

| ID | Anforderung |
|---|---|
| SASD-REL-040 | Recommended- und Production-Releases MÜSSEN aus dokumentierten Quellen und Schritten reproduzierbar erzeugbar sein. |
| SASD-REL-041 | Buildwerkzeuge, Abhängigkeiten und relevante Konfiguration MÜSSEN versioniert oder anderweitig nachvollziehbar festgelegt sein. |
| SASD-REL-042 | Production-Artefakte MÜSSEN automatisiert oder durch einen kontrollierten, protokollierten Prozess erzeugt werden. |
| SASD-REL-043 | Releaseartefakte SOLLTEN Prüfsummen besitzen, wenn sie als Dateien verteilt werden. |
| SASD-REL-044 | Signaturen oder Provenance-Nachweise SOLLTEN für sicherheitsrelevante oder extern verteilte Production-Artefakte verwendet werden. |
| SASD-REL-045 | Der veröffentlichte Quellstand, die erzeugten Artefakte und Release Notes MÜSSEN dieselbe Version repräsentieren. |

### 3.6 Abhängigkeiten und SBOM

| ID | Anforderung |
|---|---|
| SASD-REL-050 | Releaseabhängigkeiten MÜSSEN hinsichtlich bekannter kritischer Schwachstellen und Lizenzrisiken geprüft werden. |
| SASD-REL-051 | Production-Releases MÜSSEN soweit technisch möglich eine SBOM oder gleichwertige Komponentenliste bereitstellen. |
| SASD-REL-052 | Die SBOM MUSS zum veröffentlichten Artefakt und nicht nur zu einem beliebigen Entwicklungsstand passen. |
| SASD-REL-053 | Drittanbieterartefakte MÜSSEN Herkunft und Version erkennen lassen. |

### 3.7 Migration und Kompatibilität

| ID | Anforderung |
|---|---|
| SASD-REL-060 | Änderungen an Daten, Konfigurationen, Schnittstellen oder Betriebsumgebungen MÜSSEN auf Migrationsbedarf geprüft werden. |
| SASD-REL-061 | Notwendige Migrationsschritte MÜSSEN vor dem Release dokumentiert und entsprechend dem Risiko getestet werden. |
| SASD-REL-062 | Breaking Changes MÜSSEN eindeutig gekennzeichnet werden. |
| SASD-REL-063 | Datenmigrationen SOLLTEN idempotent, wiederaufnehmbar oder anderweitig gegen Teilfehler abgesichert sein. |
| SASD-REL-064 | Ein Rückweg MUSS definiert sein, wenn eine Migration nicht sicher rückgängig gemacht werden kann. |

### 3.8 Deployment, Rollback und Einführung

| ID | Anforderung |
|---|---|
| SASD-REL-070 | Deployment-Schritte MÜSSEN für Recommended und Production dokumentiert sein. |
| SASD-REL-071 | Production-Releases MÜSSEN einen Rollback-, Recovery- oder Schadensbegrenzungsplan besitzen. |
| SASD-REL-072 | Rollback-Pläne MÜSSEN Daten- und Schemaänderungen berücksichtigen. |
| SASD-REL-073 | Kritische Releases SOLLTEN schrittweise, beobachtbar oder mit begrenztem Nutzerkreis eingeführt werden. |
| SASD-REL-074 | Nach der Einführung MUSS geprüft werden, ob der erwartete Betriebszustand erreicht wurde. |

### 3.9 Veröffentlichung und Aufbewahrung

| ID | Anforderung |
|---|---|
| SASD-REL-080 | Offizielle Veröffentlichungsorte MÜSSEN benannt werden. |
| SASD-REL-081 | Veraltete oder unsichere Releases MÜSSEN als solche gekennzeichnet oder zurückgezogen werden. |
| SASD-REL-082 | Production-Releases und zugehörige Nachweise MÜSSEN für einen angemessenen Zeitraum aufbewahrt werden. |
| SASD-REL-083 | Ein Release MUSS Supportstatus oder Wartungserwartung erkennen lassen, wenn mehrere Versionen parallel existieren. |

## 4. Releaseklassen

| Klasse | Zweck | Typische Kennzeichnung |
|---|---|---|
| Development Build | interne Prüfung | Commit-ID oder Buildnummer |
| Alpha / Preview | frühe Funktionsprüfung | `-alpha`, `-preview` |
| Beta | breitere Prüfung, noch nicht stabil | `-beta` |
| Release Candidate | geplanter Inhalt vollständig | `-rc.N` |
| Stable | freigegebene reguläre Version | `vMAJOR.MINOR.PATCH` |
| Hotfix | dringende kompatible Korrektur | Patch-Version |

## 5. Zuordnung zu Qualitätsstufen

| Maßnahme | Minimum | Recommended | Production |
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

## 6. Verantwortlichkeiten

Maintainer erstellen Releasekandidaten, Versionen und Notes. Projektverantwortliche genehmigen Scope und Restrisiko. Entwickler und Reviewer liefern Prüf- und Migrationsnachweise. Betreiber bestätigen Deployment und Recovery.

## 7. Nachweise und Prüfkriterien

Geeignete Nachweise sind Release-Checkliste, Tag, Commit-ID, Buildprotokoll, Testergebnisse, SBOM, Prüfsumme, Signatur, Release Notes, Deployment- und Rollbackbericht.

## 8. Ausnahmen und Abweichungen

Manuelle Releases sind zulässig, wenn der Prozess dokumentiert, reproduzierbar und entsprechend der Qualitätsstufe geprüft ist. Production-Abweichungen benötigen eine Risiko- und Wiederholbarkeitsbewertung.

## 9. Verwandte Dokumente

- [Versionierung](../40-governance/VERSIONING.md)
- [Repository- und GitHub-Standard](REPOSITORY.md)
- [Teststandard](TESTING.md)
- [Wartungsstandard](MAINTENANCE.md)
- [Release-Checkliste](../../checklists/releases/RELEASE-CHECKLIST.md)
