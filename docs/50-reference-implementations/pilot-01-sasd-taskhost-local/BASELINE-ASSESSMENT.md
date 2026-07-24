---
title: "Pilot 01 Baseline Assessment – SASD TaskHost Local"
document-id: SASD-REF-PILOT-104
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
depends-on: [SASD-REF-PILOT-002, SASD-REF-PILOT-103, SASD-PROC-005]
---

# Baseline Assessment – SASD TaskHost Local

## 1. Bewertungsstand

```text
Beobachtungsdatum: 2026-07-24
Quelle: öffentliches GitHub-Repository auf Branch main
Lokaler Build: nicht in diesem Arbeitsschritt durchgeführt
Lokaler Laufzeittest: nicht in diesem Arbeitsschritt durchgeführt
Bewertungsart: öffentliches Baseline Assessment mit expliziten Unsicherheiten
```

## 2. Beobachtete Stärken

| Evidenz | Stärke | Bewertung |
|---|---|---|
| O | MVP-Ziel und Nicht-Ziele sind klar beschrieben. | verhindert Scope Creep |
| O | Restore-, Build- und Run-Befehle sind im README dokumentiert. | gute Ausgangsbasis für Reproduzierbarkeit |
| O | Die Solution enthält bewusst nur ein Produktprojekt. | proportional für Small-Projekt |
| O | Ordner für Forms, Models, Services, Repositories und Database machen Verantwortlichkeiten sichtbar. | einfache, nachvollziehbare Schichtung |
| O | SQL soll laut Architekturregel nicht im Formularcode liegen. | sinnvolle Abhängigkeitsgrenze |
| O | Nullable Reference Types und Implicit Usings sind aktiviert. | gute .NET-Basis |
| O | SQLite-Daten liegen außerhalb des Programmverzeichnisses im Benutzerprofil. | Updates benötigen keine Schreibrechte im Installationsordner |
| O | Lastenheft, Pflichtenheft, UI-Konzept, technisches Design, Datenmodell, Roadmap, Known Issues, manueller Testplan und ADR-Verzeichnis sind vorhanden. | ungewöhnlich gute Dokumentationsbasis für ein kleines Projekt |
| O | `CHANGELOG.md` ist vorhanden. | Änderungshistorie vorbereitet |
| R | Keine Netzwerkkommunikation und keine Telemetrie sind für den MVP vorgesehen. | reduziert Angriffsfläche und Datenschutzrisiko |
| R | `.db`- und Backup-Dateien sollen nicht in das Repository gelangen. | sinnvolle Datenschutzregel |

## 3. Blocker und wesentliche Lücken

| Evidenz | Befund | Auswirkung |
|---|---|---|
| R | README dokumentiert `SQLite Error 1: near "=": syntax error` beim Start. | verhindert nutzbare Baseline und hat höchste Priorität |
| O | Kein automatisiertes Testprojekt ist in der Solution sichtbar. | Datenbankinitialisierung und Repositories besitzen keinen erkennbaren Regressionsschutz |
| O | Keine `.editorconfig`, `Directory.Build.props` oder `global.json` sind im Root-Snapshot sichtbar. | Toolchain- und Codequalitätsregeln sind nicht zentralisiert oder gepinnt |
| O | Keine `.github`-CI-Struktur ist im Root-Snapshot sichtbar. | Build und Tests werden nicht automatisch reproduziert |
| O/R | Lizenz ist laut README offen; keine `LICENSE`-Datei ist sichtbar. | Weiterverwendung und Beitragssituation sind rechtlich unklar |
| O | Keine `SECURITY.md` ist im Root-Snapshot sichtbar. | Meldung von Sicherheits- oder Datenproblemen ist nicht geregelt |
| U | Restore-Fähigkeit der Backup-Funktion ist nicht nachgewiesen. | Backup kann ohne Restore-Test Scheinsicherheit erzeugen |
| U | Logging-, Crash- und Diagnoseverhalten wurden nicht lokal geprüft. | Supportfähigkeit ist unbekannt |
| U | Der aktuelle NuGet-Paketstand und bekannte Schwachstellen wurden nicht geprüft. | Supply-Chain-Risiko bleibt offen |
| U | Installer, portable Veröffentlichung und Release-Smoke-Test sind nicht nachgewiesen. | noch keine belastbare Veröffentlichung |

## 4. Proportionalitätsbewertung

Die bestehende Ein-Projekt-Struktur ist für den aktuellen Scope grundsätzlich angemessen. Der Standard liefert keinen Grund, Domain, Application und Infrastructure als separate Assemblies einzuführen. Ein zusätzliches Testprojekt ist jedoch sinnvoll, weil Datenbankinitialisierung und Persistenz die kritischsten technischen Risiken bilden.

## 5. Unsicherheiten

Vor Ausführung von Wave 01 müssen lokal geprüft werden:

- tatsächlicher Buildstatus unter Windows,
- genauer Auslöser des SQLite-Fehlers,
- aktuelle Datenbankschemata und Migrationslogik,
- Verhalten bei bestehender, leerer und beschädigter Datenbank,
- Backup- und Restore-Ablauf,
- verwendete .NET-SDK-Version,
- Paketabhängigkeiten und verfügbare Updates,
- UI-Start, Shutdown und Fehlerdialoge.

## 6. Baseline-Ergebnis

```text
Pilot Alignment: Assessment in Progress
Technische Nutzbarkeit: Blockiert durch gemeldeten Startfehler
Architektur: für Small-Projekt grundsätzlich proportional
Dokumentation: stark, aber technische Nachweise fehlen
Empfehlung: Wave 01 ausführen; kein Architektur-Refactoring vor Stabilisierung
```
