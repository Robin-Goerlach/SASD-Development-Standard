---
title: "Pilot 01 Evidenzzuordnung – SASD TaskHost Local"
document-id: SASD-REF-PILOT-108
document-type: informative
status: Draft
version: 0.9.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-08-06
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

## 3. Verifizierte Remote-Baseline vom 2026-08-06

| Evidenz-ID | Klasse | Nachweis | Ergebnis | Einschränkung |
|---|---|---|---|---|
| P01-EV-301 | V | Standardcommit `d80baf0cccf66b5c940cfd7f05e399c83f880e1a`, Zielcommit `2404feb0904b22274972b5803520e6d86a70047d`, `dotnet --info` | Passed | bestätigt Umgebung und unveränderliche Identität, nicht den Pilotabschluss |
| P01-EV-302 | V | `dotnet restore` und Release-Build | Passed | Wave-01-Integration und Produkttests fehlen weiterhin |
| P01-EV-307 | V | GitHub Actions Run `31100169566` auf Windows mit Commit- und Artefaktidentität | Passed | Workflow liegt im Standard-Repository und prüft den externen Zielcommit |
| P01-EV-309 | V | NuGet-Audit und `dotnet publish`; Windows-Publish-Artefakt erzeugt | Passed | kein Headless-Self-Check und kein manueller Smoke-Test |

Vollständiger Nachweis: [REMOTE-BASELINE-EVIDENCE-2026-08-06.md](REMOTE-BASELINE-EVIDENCE-2026-08-06.md)

## 4. Noch erforderliche verifizierte Nachweise

| Evidenz-ID | Klasse | Geplanter Nachweis | Zugeordnete Gaps |
|---|---|---|---|
| P01-EV-303 | V | erfolgreicher Testlauf mit allen angemessenen Wave-01-Tests | 001, 002, 009 |
| P01-EV-304 | V | Start mit frischer Datenbank | 001 |
| P01-EV-305 | V | Start mit gesicherter Testkopie einer bestehenden Datenbank | 001, 009 |
| P01-EV-306 | V | Fehlerfall und Diagnosepfad praktisch geprüft | 010 |
| P01-EV-308 | O/V | committed LICENSE, Security- und Alignment-Dokumente | 006, 007, 008 |

## 5. Repräsentative Standardzuordnung

## 4. Repräsentative Standardzuordnung

| Standardbereich | Aktuelle Evidenz | Vorläufige Bewertung |
|---|---|---|
| Scope und Nicht-Ziele | Baseline-Dokumente | stark |
| Architektur | einfache Schichtung, bewusst unverändert | proportional |
| Repository und Build | exakter Remote-Checkout, Restore, Release-Build und Publish bestanden | Remote Baseline Passed; Wave-01-Integration offen |
| Tests | im gepinnten Baseline-Commit kein Testprojekt vorhanden | NotAvailable; praktische Testvalidierung offen |
| Security und Datenschutz | NuGet-Audit bestanden; weitere Security- und Alignment-Arbeiten vorbereitet | Baseline teilweise verifiziert |
| Persistenz und Datenintegrität | Build bestätigt; Datenbankstart, Migration und Fehlerpfade nicht praktisch geprüft | blockiert bis Laufzeitverifikation |
| Releases | noch kein Releaseziel dieser Welle | offen für Wave 02 |
| Wartung und Wissen | umfangreiche Pilot- und Projektdokumentation | gut, praktische Nachweise offen |

## 6. Aktualisierungsregel

Nach dem Ziel-Commit werden Artefaktnachweise nicht gelöscht, sondern durch verifizierte Evidenz ergänzt. Öffentliche Beobachtungen und vorbereitete Artefakte werden nicht rückwirkend als lokal verifiziert umklassifiziert.
