---
title: "Release-Candidate-Blockerregister 1.0.0-rc.1"
document-id: SASD-REF-RC-003
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
depends-on: [SASD-REF-RC-001, SASD-REF-PILOT-007, SASD-REF-CI-003]
---

# Release-Candidate-Blockerregister 1.0.0-rc.1

## Statusmodell

| Status | Bedeutung |
|---|---|
| Open | Bedingung ist nicht erfüllt und blockiert die Veröffentlichung. |
| Evidence Pending | Umsetzung kann vorhanden sein, aber der notwendige Nachweis fehlt. |
| Decision Required | Maintainer muss eine ausdrückliche, dokumentierte Entscheidung treffen. |
| Closed | Bedingung ist erfüllt und nachgewiesen. |
| Accepted for RC | Befristete Releaseentscheidung erlaubt den RC; stabile Version bleibt gegebenenfalls blockiert. |

## Aktuelle Blocker

| ID | Kategorie | Bedingung | Status | Erforderlicher Nachweis | RC-Wirkung |
|---|---|---|---|---|---|
| RC-BLK-001 | Remote CI | Ubuntu, Windows und `SASD merge gate` müssen für exakt den vorgesehenen Commit erfolgreich sein. | Evidence Pending | CI-Aktivierungsevidenz oder Release-Record-Link auf erfolgreichen Lauf | Blocker |
| RC-BLK-002 | Pilotierung | Mindestens ein Pilotdurchlauf muss praktisch ausgeführt und technisch mit `Passed` verifiziert sein. | Open | Pilotmanifest, Zielcommit, Build-/Test-/Laufzeitnachweise | Blocker |
| RC-BLK-003 | Branch Governance | Das geplante Ruleset muss aktiviert oder seine Verschiebung ausdrücklich bewertet sein. | Decision Required | Ruleset-Evidenz oder befristete Maintainer-Entscheidung | Blocker bis Entscheidung |
| RC-BLK-004 | Artefakte | Source- und Markdown-Archive müssen aus einem sauberen Checkout erzeugt und unabhängig geprüft werden. | Open | Release-Candidate-Manifest, SHA256SUMS und Verifikationsbericht | Blocker |
| RC-BLK-005 | Release Record | Commit, Tag, Workflow-Lauf, Artefakte, Known Issues und Maintainer-Entscheidung müssen vollständig sein. | Open | ausgefüllter Release Record | Blocker |
| RC-BLK-006 | Tag/Publikation | Annotierter Tag und GitHub Pre-release dürfen erst nach Abschluss der vorherigen Gates erstellt werden. | Open | Tag- und GitHub-Release-URL | Veröffentlichungsschritt |

## Nicht als RC-Blocker eingestuft

| Thema | Begründung |
|---|---|
| Word- und PDF-Ausgabe | Für die stabile Version 1.0 erforderlich; im RC muss der Publikationspfad vorbereitet und anschließend praktisch geprüft werden. |
| vollständige technische Verifikation aller drei Piloten | Für Version 1.0 sollen alle Baselines bestätigt und Erkenntnisse konsolidiert werden; der erste RC verlangt mindestens einen verifizierten praktischen Durchlauf. |
| englische normative Ausgabe | Nach Stabilisierung vorgesehen, aber nicht Bestandteil des deutschen Version-1.0-RC-Umfangs. |
| spätere Fachprofile | ausdrücklich außerhalb des Version-1.0-Scopes. |

## Änderungsregel

Der Status dieses Registers darf nur geändert werden, wenn der zugehörige Nachweis im Repository oder im Release Record referenziert wird. Ein vorbereiteter Workflow, Test oder Skript ist kein erfolgreicher Ausführungsnachweis.
