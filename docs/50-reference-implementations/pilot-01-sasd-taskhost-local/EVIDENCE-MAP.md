---
title: "Pilot 01 Evidenzzuordnung – SASD TaskHost Local"
document-id: SASD-REF-PILOT-108
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
depends-on: [SASD-REF-PILOT-002, SASD-REF-PILOT-104, SASD-GOV-007]
---

# Evidenzzuordnung – SASD TaskHost Local

## 1. Öffentliche Baseline-Quellen

| Evidenz-ID | Klasse | Quelle | Beobachtung |
|---|---|---|---|
| P01-EV-001 | O | öffentliches Ziel-Repository am 2026-07-24 | Repository, README, WinForms-Projekt, docs, Changelog und Solution sichtbar |
| P01-EV-002 | O | `TaskHostLocal.sln` | ein Produktionsprojekt in der Baseline-Solution |
| P01-EV-003 | O | Baseline-Projektdatei | .NET 8 Windows, WinForms, Nullable und Microsoft.Data.Sqlite |
| P01-EV-004 | O | Baseline-Quellstruktur | Forms, Models, Services, Repositories und Database sichtbar |
| P01-EV-005 | O | Baseline-`docs/` | Anforderungen, Design, Datenmodell, Roadmap, Known Issues, Tests und ADRs dokumentiert |
| P01-EV-006 | R | README Projektstatus | Build erfolgreich, Startfehler `SQLite Error 1: near "=": syntax error` gemeldet |
| P01-EV-007 | R | README Datenschutz | keine Telemetrie/Netzwerkkommunikation; Datenbank und Backups nicht ins Repository |
| P01-EV-008 | O | Baseline-Root | keine LICENSE, zentrale Buildbasis, CI oder Testsolution sichtbar |

## 2. Vorbereitetes Wave-01-Artefakt

| Evidenz-ID | Klasse | Quelle | Beobachtung | Einschränkung |
|---|---|---|---|---|
| P01-EV-201 | A | `SASD-TaskHost-Local-Wave-01-Update.zip` | Overlay mit 36 Dateien vorbereitet | noch nicht als Ziel-Commit nachgewiesen |
| P01-EV-202 | A | SHA-256 `61a199...72d7` | Artefaktidentität dokumentiert | Hash bestätigt Inhalt, nicht Funktion |
| P01-EV-203 | A | `TaskHostLocal.Tests/` | elf Testmethoden für Datenbank, Repositories und Backup vorbereitet | Tests nicht mit `dotnet test` ausgeführt |
| P01-EV-204 | A | Database- und Diagnostics-Dateien | robuste Initialisierung und Startup-Diagnose vorbereitet | WinForms-Start nicht geprüft |
| P01-EV-205 | A | Build-/Paketdateien | SDK-, Build- und Paketbasis vorbereitet | Restore und Build offen |
| P01-EV-206 | A | `.github/workflows/ci.yml` | Windows-CI mit Build, Test und Audit vorbereitet | kein Workflow-Lauf vorhanden |
| P01-EV-207 | A | LICENSE, SECURITY, Alignment und ADR | Governance-Nachweise vorbereitet | Eigentümerprüfung und Commit offen |
| P01-EV-208 | A | statischer Wave-Validator | Struktur-, XML-, SQLite- und ZIP-Prüfungen bestanden | ersetzt Compiler und Laufzeit nicht |

## 3. Noch erforderliche verifizierte Nachweise

| Evidenz-ID | Klasse | Geplanter Nachweis | Zugeordnete Gaps |
|---|---|---|---|
| P01-EV-301 | V | Baseline- und Ziel-Commit, `dotnet --info` | 003, 004 |
| P01-EV-302 | V | erfolgreicher Restore- und Release-Build | 003, 004, 013 |
| P01-EV-303 | V | erfolgreicher Testlauf mit allen Wave-01-Tests | 001, 002, 009 |
| P01-EV-304 | V | Start mit frischer Datenbank | 001 |
| P01-EV-305 | V | Start mit gesicherter Testkopie einer bestehenden Datenbank | 001, 009 |
| P01-EV-306 | V | Fehlerfall und Diagnosepfad praktisch geprüft | 010 |
| P01-EV-307 | V | erfolgreicher Windows-CI-Lauf mit Commit- und Run-ID | 005, 013 |
| P01-EV-308 | O/V | committed LICENSE, Security- und Alignment-Dokumente | 006, 007, 008 |

## 4. Repräsentative Standardzuordnung

| Standardbereich | Aktuelle Evidenz | Vorläufige Bewertung |
|---|---|---|
| Scope und Nicht-Ziele | Baseline-Dokumente | stark |
| Architektur | einfache Schichtung, bewusst unverändert | proportional |
| Repository und Build | Artefakt vorbereitet, Verifikation offen | Artifact Prepared |
| Tests | Testprojekt vorbereitet, Lauf offen | Artifact Prepared |
| Security und Datenschutz | Security- und Auditbasis vorbereitet | Artifact Prepared |
| Persistenz und Datenintegrität | robuster Code und Tests vorbereitet; Laufzeit offen | blockiert bis Verifikation |
| Releases | noch kein Releaseziel dieser Welle | offen für Wave 02 |
| Wartung und Wissen | umfangreiche Pilot- und Projektdokumentation | gut, praktische Nachweise offen |

## 5. Aktualisierungsregel

Nach dem Ziel-Commit werden Artefaktnachweise nicht gelöscht, sondern durch verifizierte Evidenz ergänzt. Öffentliche Beobachtungen und vorbereitete Artefakte werden nicht rückwirkend als lokal verifiziert umklassifiziert.
