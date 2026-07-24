---
title: "Repository-CI-Recovery und Aktivierung"
document-id: SASD-REF-CI-001
document-type: informative
status: Proposed
version: 0.10.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Recommended, Production]
applies-to-profiles: [Core]
depends-on: [SASD-GOV-002, SASD-GOV-005, SASD-GOV-007, SASD-PROC-004, SASD-REF-PILOT-002]
---

# Repository-CI-Recovery und Aktivierung

## 1. Zweck

Dieses Verfahren schließt die erste Repository-CI-Einführung kontrolliert ab.
Es verhindert, dass ein lokal erfolgreicher Lauf, eine vorhandene Workflowdatei
oder ein laufender GitHub-Job als aktivierte und wirksame Branch-Regel ausgegeben
wird.

## 2. Ausgangslage

Der erste Remote-Lauf hat eine echte Repository-Grenzverletzung erkannt. Deshalb
wird die Aktivierung in getrennten Nachweisschritten durchgeführt:

```text
Boundary Repair
  -> Local Quality Gates
  -> Repair Commit
  -> Green GitHub Run for exact commit
  -> Evidence Capture
  -> Ruleset Plan Review
  -> Ruleset Activation
  -> Ruleset Read-Back
  -> Activation Record
```

## 3. Voraussetzungen

Vor der Remote-Verifikation müssen folgende Bedingungen erfüllt sein:

- `REPOSITORY-IDENTITY.json` ist vorhanden.
- `python tooling/validate-repository-boundary.py` ist erfolgreich.
- `python tooling/run-quality-gates.py` ist erfolgreich.
- Die bekannten TaskHost-Local-Fremdpfade sind entfernt.
- Das Arbeitsverzeichnis enthält nur beabsichtigte Änderungen.
- Der Repair-Commit ist nach `origin/main` gepusht.

## 4. Remote-Verifikation

Nach dem Push wird für die exakte Commit-SHA geprüft:

- Workflow: `SASD Quality Gates`,
- Ubuntu-Matrixjob: erfolgreich,
- Windows-Matrixjob: erfolgreich,
- Aggregatcheck: `SASD merge gate` erfolgreich,
- Workflowstatus: abgeschlossen,
- Workflow-Conclusio: `success`,
- Commit-SHA des Runs: identisch mit der geprüften Revision.

Der Befehl lautet:

```bash
python tooling/capture-ci-activation.py --verify-only
```

Nach einem erfolgreichen Lauf kann ein maschinenlesbarer Nachweis geschrieben
werden:

```bash
python tooling/capture-ci-activation.py --write
```

## 5. Ruleset-Aktivierung

Das vorgesehene Ruleset liegt unter:

```text
.github/rulesets/main-merge-gate.json
```

Es schützt den Default Branch durch:

- Verbot der Branch-Löschung,
- Verbot von Force Pushes,
- erforderlichen Check `SASD merge gate`,
- Prüfung gegen den aktuellen Stand des Zielbranches.

Vor der Aktivierung zeigt folgender Befehl ausschließlich den Plan:

```bash
python tooling/manage-main-ruleset.py --plan
```

Die Aktivierung ist absichtlich nur mit einer zusätzlichen Bestätigung möglich:

```bash
python tooling/manage-main-ruleset.py \
  --activate \
  --confirm-switch-to-pull-requests
```

Nach der Aktivierung sollen Änderungen normalerweise über Branch und Pull Request
laufen. Ein direkter Push nach `main` besitzt keinen bereits erfolgreichen Check
und ist daher nicht der normale Arbeitsweg.

## 6. Nachweis und Abschluss

Nach Aktivierung wird der Remote-Zustand erneut gelesen:

```bash
python tooling/capture-ci-activation.py --write --require-active-ruleset
```

Erst dann dürfen folgende Aussagen im Aktivierungsrecord auf `Yes` oder `Passed`
gesetzt werden:

- Green Ubuntu run,
- Green Windows run,
- Green `SASD merge gate`,
- Active ruleset,
- required status check present,
- force-push protection present,
- deletion protection present.

## 7. Rückfallweg

Falls das Ruleset den Arbeitsablauf unerwartet blockiert:

```bash
python tooling/manage-main-ruleset.py --disable
```

Das Deaktivieren ist eine administrative Maßnahme und muss im Aktivierungsrecord
mit Grund und Zeitpunkt dokumentiert werden.

## 8. Nicht durch dieses Verfahren bewiesen

Auch eine vollständig aktivierte Repository-CI beweist nicht:

- fachliche Freigabe der Proposed Core- oder Profildokumente,
- Abschluss von Pilot 01,
- Veröffentlichung eines Release Candidate,
- Konformität fremder SASD-Repositories,
- stabile Version 1.0.
