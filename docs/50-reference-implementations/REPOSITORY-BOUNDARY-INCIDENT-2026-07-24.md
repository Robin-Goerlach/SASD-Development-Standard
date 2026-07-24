---
title: "Repository-Grenzvorfall vom 24. Juli 2026"
document-id: SASD-REF-PILOT-006
document-type: informative
status: Draft
version: 0.9.1
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-REF-PILOT-002, SASD-REF-PILOT-004]
---

# Repository-Grenzvorfall vom 24. Juli 2026

## Zusammenfassung

Zwei für `Robin-Goerlach/SASD-TaskHost-Local` bestimmte ZIP-Updates wurden in das
Repository `Robin-Goerlach/SASD-Development-Standard` entpackt und dort committed.
Zusätzlich enthielt der ursprüngliche Starter-Export einen verschachtelten Ordner
`SASD-Development-Standard/`.

Der erste Lauf der neuen Repository-CI am Commit `3ea1a88` scheiterte deshalb auf
Ubuntu und Windows. Der Workflow selbst funktionierte: Beide Jobs erzeugten
Evidenzartefakte und meldeten die Inhaltsfehler korrekt.

## Auswirkungen

Im Standard-Repository befanden sich danach unter anderem:

- eine TaskHost-Local-Solution,
- WinForms- und Testprojekte,
- TaskHost-spezifische Build- und Verifikationsskripte,
- TaskHost-Projektdokumente außerhalb des Referenzpilotbereichs,
- ein zweiter GitHub-Actions-Workflow für TaskHost Local,
- ein verschachteltes Abbild des Starter-Repositories.

Diese Dateien verletzten die Repository-Grenze. Die Metadatenprüfung interpretierte
TaskHost-Projektdokumente außerdem fälschlich als Standarddokumente.

## Ursache

Die Updatepakete waren als dateibasiertes Overlay aufgebaut. Ein ZIP-Overlay kann
Dateien ergänzen und ersetzen, aber keine bereits committed Fremddateien entfernen.
Die Zielangabe war in der Begleitdokumentation vorhanden, wurde beim manuellen
Entpacken jedoch nicht technisch erzwungen.

## Korrektur

Das Reparaturpaket:

1. entfernt ausschließlich die bekannten TaskHost- und Nested-Repository-Pfade,
2. stellt die `.gitignore` des Standard-Repositories wieder her,
3. führt `REPOSITORY-IDENTITY.json` als maschinenlesbare Identität ein,
4. ergänzt einen blockierenden Repository-Grenzvalidator,
5. aktualisiert das deterministische Repository-Manifest,
6. führt anschließend die vollständigen Quality Gates aus.

## Vorbeugende Maßnahmen

Künftige Updatepakete sollten mindestens enthalten:

- kanonisches Ziel-Repository,
- erwartete Repository-Marker,
- erforderlichen Vorgängerstand,
- Paket-ID und SHA-256,
- Liste der hinzugefügten, geänderten und zu entfernenden Pfade,
- ein Anwendungsskript mit Repository-Identitätsprüfung,
- eine ausdrückliche Aussage, ob das Paket Löschoperationen benötigt.

Direktes Entpacken ohne Anwendungsskript ist nur für rein additive Pakete zulässig.

## Evidenz

- Fehlgeschlagener CI-Lauf: `https://github.com/Robin-Goerlach/SASD-Development-Standard/actions/runs/30116801087`
- Betroffener Commit laut GitHub: `3ea1a88`
- Workflow-Ergebnis: Failure auf Ubuntu, Windows und `SASD merge gate`
- Erzeugte CI-Artefakte: Linux- und Windows-Quality-Gate-Evidenz

## Status

- Fremdinhalte identifiziert: **Ja**
- Reproduzierbare lokale Fehleranalyse: **Ja**
- Reparaturpaket vorbereitet: **Ja**
- Reparatur in GitHub committed: **Ausstehend**
- Erneuter grüner CI-Lauf: **Ausstehend**
- Branch-Regel aktiviert: **Nein**
