---
title: "Repository-CI-Aktivierungsrecord"
document-id: SASD-REF-CI-003
document-type: informative
status: Draft
version: 0.10.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Recommended, Production]
applies-to-profiles: [Core]
depends-on: [SASD-REF-CI-001, SASD-REF-CI-002, SASD-REF-PILOT-002]
---

# Repository-CI-Aktivierungsrecord

## Status

```text
Repository boundary repaired: Pending remote commit evidence
Local quality gates:           Prepared and previously tested
Green Ubuntu run:              Pending
Green Windows run:             Pending
Green SASD merge gate:         Pending
Evidence JSON:                 Pending
Ruleset created:               No
Ruleset active:                No
Activation complete:           No
```

## Geprüfte Revision

- Commit SHA: Pending
- Branch: `main`
- Push date: Pending
- Workflow run ID: Pending
- Workflow run URL: Pending
- Workflow conclusion: Pending

## Jobnachweise

| Erwarteter Job | Ergebnis | URL |
|---|---|---|
| `Validate (ubuntu-latest)` | Pending | Pending |
| `Validate (windows-latest)` | Pending | Pending |
| `SASD merge gate` | Pending | Pending |

## Rulesetnachweis

- Ruleset name: `Protect main with SASD merge gate`
- Ruleset ID: Pending
- Enforcement: Pending
- Target: `branch`
- Default-Branch-Bedingung vorhanden: Pending
- Required check `SASD merge gate`: Pending
- Strict status-check policy: Pending
- Force pushes blocked: Pending
- Branch deletion blocked: Pending

## Evidenz

Der maschinenlesbare Nachweis wird nach erfolgreicher Remote-Prüfung geschrieben:

```text
docs/50-reference-implementations/repository-self-hosting/CI-ACTIVATION-EVIDENCE.json
```

## Offene Schritte

1. Repository-Boundary-Repair committen und pushen.
2. GitHub-Actions-Lauf für exakt diesen Commit abwarten.
3. Remote-Evidenz mit `capture-ci-activation.py` erfassen.
4. Ruleset-Plan prüfen.
5. Ruleset aktivieren.
6. Ruleset zurücklesen und Record aktualisieren.
7. Aktivierungsrecord in einem getrennten Nachweiscommit speichern.

## Aussagegrenze

Dieser Record bleibt bis zum Remote-Nachweis auf `Pending`. Die vorbereiteten
Skripte und Regeln sind kein Erfolgsnachweis.
