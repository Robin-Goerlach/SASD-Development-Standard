---
title: "Pilot 01 Migrationsplan – SASD TaskHost Local"
document-id: SASD-REF-PILOT-106
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
depends-on: [SASD-REF-PILOT-105, SASD-PROC-005, SASD-PROC-004]
---

# Migrationsplan – SASD TaskHost Local

## 1. Strategie

Die Migration erfolgt in kleinen, rückfallfähigen Wellen. Der bestehende fachliche Scope und die einfache Architektur bleiben erhalten. Jede Welle muss eigenständig baubar und prüfbar sein.

## 2. Wellenübersicht

| Welle | Ziel | Hauptinhalt | Nicht enthalten |
|---|---|---|---|
| Wave 00 | Baseline sichern | Branch/Tag, lokale Toolchain, Datenkopie, Reproduktion des Fehlers | Produktänderungen |
| Wave 01 | Startfähigkeit und Engineering-Basis | SQLite-Blocker, Regressionstest, Buildbasis, CI, Lizenz, Security, Alignment | UI-Neuentwurf, Installer |
| Wave 02 | Daten- und Releasevertrauen | Backup/Restore, Logging, Packaging, Release-Smoke-Test, Screenshot | Cloud, Synchronisierung |
| Wave 03 | optionale Produktverbesserungen | UX, Tastatur, Detailbereich, zusätzliche Tests | Architekturumbau ohne Nutzen |

## 3. Wave 00 – Baseline

Vor Änderungen:

- aktuellen `main`-Stand sichern,
- lokale Datenbank und Backups außerhalb des Repositories sichern,
- SDK- und Visual-Studio-Version protokollieren,
- `dotnet restore` und `dotnet build -c Release` ausführen,
- Startfehler mit Stacktrace und Datenbankzustand erfassen,
- vorhandenen manuellen Testplan einmal durchführen, soweit der Start möglich ist.

## 4. Wave 01 – Stabilisierung

[Der detaillierte Plan](WAVE-01-PLAN.md) ist verbindliche Arbeitsgrundlage des Piloten. Die Welle soll möglichst in kleinen Commits ausgeführt werden:

1. Baseline und Fehlerreproduktion,
2. Datenbankfehler und Regressionstest,
3. Build-/SDK-/Analyzer-Basis,
4. CI,
5. Lizenz, Security und Alignment,
6. abschließender Selbstreview.

## 5. Wave 02 – Vertrauensbildung

- Backup mit echtem Restore-Szenario prüfen,
- Datenbankfehler und korrupte Datei kontrolliert behandeln,
- Logging- und Supportpfade dokumentieren,
- portable oder installierbare Veröffentlichung definieren,
- Release Record und Smoke Test durchführen,
- README und Screenshot auf den tatsächlichen Stand bringen.

## 6. Rückfallstrategie

- jede Welle beginnt auf sauberem, reproduzierbarem Commit,
- Datenbankänderungen erhalten Sicherung und Rückweg,
- Strukturänderungen werden getrennt von Fehlerkorrekturen committed,
- bei Regression wird auf den letzten geprüften Commit zurückgegangen,
- bestehende Nutzerdaten werden nicht als Testdaten verwendet.

## 7. Abschluss des Piloten

Der Pilot wird erst geschlossen, wenn mindestens Wave 01 technisch ausgeführt, nachgewiesen und retrospektiv bewertet wurde. Wave 02 kann danach als reguläre Projektarbeit fortgeführt werden.
