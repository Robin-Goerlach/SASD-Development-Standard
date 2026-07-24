---
title: "Pilot 01 Evidenzzuordnung – SASD TaskHost Local"
document-id: SASD-REF-PILOT-108
document-type: informative
status: Draft
version: 0.7.0
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

## 1. Öffentliche Quellen

| Evidenz-ID | Klasse | Quelle | Beobachtung |
|---|---|---|---|
| P01-EV-001 | O | `https://github.com/Robin-Goerlach/SASD-TaskHost-Local` | Repository, README, fünf Commits, WinForms-Projekt, docs, Changelog und Solution sichtbar |
| P01-EV-002 | O | `TaskHostLocal.sln` | ein Produktionsprojekt in der Solution |
| P01-EV-003 | O | `TaskHostLocal.WinForms.csproj` | .NET 8 Windows, WinForms, Nullable, Microsoft.Data.Sqlite 8.0.0 |
| P01-EV-004 | O | `TaskHostLocal.WinForms/` | Forms, Models, Services, Repositories und Database sichtbar |
| P01-EV-005 | O | `docs/` | Anforderungen, Design, Datenmodell, Roadmap, Known Issues, Tests und ADRs dokumentiert |
| P01-EV-006 | R | README Projektstatus | Build erfolgreich, Startfehler `SQLite Error 1: near "=": syntax error` gemeldet |
| P01-EV-007 | R | README Datenschutz | keine Telemetrie/Netzwerkkommunikation; Datenbank und Backups nicht ins Repository |
| P01-EV-008 | O | Root-Snapshot | keine LICENSE, `.editorconfig`, `Directory.Build.props`, `global.json`, `.github` oder Testsolution sichtbar |

## 2. Nachweise, die Wave 01 erzeugen muss

| Evidenz-ID | Klasse | Geplanter Nachweis | Zugeordnete Gaps |
|---|---|---|---|
| P01-EV-101 | V | `dotnet --info`, Restore- und Buildprotokoll | 003, 004 |
| P01-EV-102 | V | reproduzierter SQL-Fehler mit Stacktrace und Testdaten | 001 |
| P01-EV-103 | V | erfolgreicher Start nach Korrektur | 001 |
| P01-EV-104 | V | automatisierter DB-Initialisierungstest | 001, 002 |
| P01-EV-105 | V | erfolgreicher Windows-CI-Lauf | 005 |
| P01-EV-106 | O/V | LICENSE- und Security-Datei plus Entscheidung | 006, 007 |
| P01-EV-107 | O | SASD-Alignment-Dokument im Ziel-Repository | 008 |
| P01-EV-108 | V | Paket- und Schwachstellenreview | 013 |

## 3. Repräsentative Standardzuordnung

| Standardbereich | Aktuelle Evidenz | Vorläufige Bewertung |
|---|---|---|
| Scope und Nicht-Ziele | README und Projektdokumente | stark |
| Architektur | einfache Schichtung und Design-Dokumente | grundsätzlich passend |
| Repository und Build | Solution und Buildbefehle, aber Toolchain nicht gepinnt | teilweise |
| Tests | manueller Testplan, kein Testprojekt sichtbar | offen/major |
| Security und Datenschutz | gute lokale Prinzipien, kein Security-Meldeweg | teilweise |
| Persistenz und Datenintegrität | Datenmodell dokumentiert, Startblocker vorhanden | blockiert |
| Releases | Changelog und Tag-Hinweis, kein belastbares Release nachgewiesen | offen |
| Wartung und Wissen | Roadmap, Known Issues und ADRs vorhanden | gut mit Nachweislücken |

## 4. Aktualisierungsregel

Nach jedem Ziel-Repository-Commit werden Evidenzen mit Commit-ID, Befehl und Ergebnis ergänzt. Öffentliche Beobachtungen werden nicht rückwirkend als lokal verifiziert umklassifiziert.
