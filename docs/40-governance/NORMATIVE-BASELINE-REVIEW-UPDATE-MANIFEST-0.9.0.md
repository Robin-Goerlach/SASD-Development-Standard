---
title: "Updatepaket für den integrierten normativen Review 0.9.0"
document-id: SASD-REF-BASELINE-006
document-type: informative
status: Approved
version: 0.9.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
approved-on: 2026-07-24
approval-record: SASD-REF-BASELINE-007
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-REF-BASELINE-001, SASD-REF-BASELINE-002, SASD-REF-BASELINE-003, SASD-REF-BASELINE-004, SASD-REF-BASELINE-005]
normative-keywords: []
---

# Updatepaket für den integrierten normativen Review 0.9.0

## Ziel-Repository

```text
Robin-Goerlach/SASD-Development-Standard
```

## Voraussetzung

Das Paket setzt den bereinigten Repository-Zustand mit folgenden Bestandteilen voraus:

- freigegebene Foundation und Governance 0.8.0,
- Repository-Identitäts- und Boundary-Prüfung,
- Repository Quality Gates,
- CI-Recovery- und Ruleset-Aktivierungswerkzeuge.

Vor dem Commit SOLLTE ausgeführt werden:

```bash
python tooling/validate-repository-boundary.py
```

## Enthaltener Stand

- 32 normative Dokumente als einheitliches Proposed-0.9.0-Bündel,
- 1.345 unverändert referenzierbare Anforderungen,
- aufgelöste formale Abhängigkeitszyklen,
- integrierter Review- und Freigabereifebericht,
- deterministische Abhängigkeitskarte und Reviewmanifest,
- bündelweiter Validator und Quality-Gate-Integration,
- aktualisierte Navigation, Roadmap und Statusdarstellung.

## Aussagegrenze

```text
Integrated review completed: Yes
Local quality gates:         Passed in package preparation
Maintainer approval:         No
Remote CI for target commit: Pending
Normative documents Approved: No
Release candidate:           No
Version 1.0.0:               No
```

## Anwendung

Dieses ZIP ist ein rein additives beziehungsweise dateiersetzendes Overlay. Es löscht keine
Repository-Dateien und enthält keinen zusätzlichen äußeren Repository-Ordner.

Nach dem Entpacken:

```bash
python tooling/run-quality-gates.py
git status
git add .
git commit
git push
```

Die formale Freigabe erfolgt ausschließlich in einem späteren, getrennten Approval-Commit.
