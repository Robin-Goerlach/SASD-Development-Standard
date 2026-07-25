---
title: "Release-Candidate-Readiness 1.0.0-rc.1"
document-id: SASD-REF-RC-002
document-type: informative
status: Draft
version: 0.12.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-25
applies-to-quality-levels: [Recommended, Production]
applies-to-profiles: [Core]
depends-on: [SASD-REF-RC-001, SASD-REF-RC-003, SASD-REF-PILOT-007, SASD-REF-CI-003]
---

# Release-Candidate-Readiness 1.0.0-rc.1

Diese Datei wird deterministisch aus dem Repository-Zustand erzeugt.

## Ergebnis

- Release Candidate technisch veröffentlichungsbereit: **Nein**
- blockierende offene Checks: **3**
- Approved normative Dokumente: **46/46**
- Pilotbaselines: **3/3**
- technisch verifizierte Piloten: **0**

## Checks

| ID | Bedingung | Blockierend | Ergebnis | Detail |
|---|---|---:|---:|---|
| `RC-RDY-001` | All normative documents are Approved | Ja | PASS | 46/46 Approved |
| `RC-RDY-002` | Small, Medium and Large pilot baselines are documented | Ja | PASS | sizes={'Small': 1, 'Medium': 1, 'Large': 1}, assessed=3 |
| `RC-RDY-003` | At least one pilot is technically verified | Ja | OPEN | verified=0 |
| `RC-RDY-004` | Exact-commit cross-platform GitHub Actions evidence exists | Ja | OPEN | commit=pending, workflow=pending |
| `RC-RDY-005` | Governed main ruleset is active | Ja | OPEN | pending or incomplete |
| `RC-RDY-006` | Release-candidate documents and tools are present | Ja | PASS | complete |
| `RC-RDY-007` | Word and PDF publication artefacts exist | Nein | OPEN | required for stable 1.0.0, not for initial RC publication |

## Interpretation

Ein `PASS` bestätigt nur den konkret beschriebenen Nachweis. Das Vorhandensein von
Skripten, Testcode, Workflowdateien oder Vorlagen ersetzt keinen erfolgreichen Lauf.
Diese Readiness-Datei erteilt keine Maintainer-Freigabe, erstellt keinen Tag und
veröffentlicht keinen GitHub Release.

## Aktuell blockierende Checks

- `RC-RDY-003`
- `RC-RDY-004`
- `RC-RDY-005`

## Erneute Erzeugung

```bash
python tooling/generate-release-candidate-readiness.py --write
python tooling/generate-release-candidate-readiness.py --check
python tooling/generate-release-candidate-readiness.py --require-ready
```
