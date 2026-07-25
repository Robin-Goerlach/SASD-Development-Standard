---
title: "Normative Baseline Approval Record 0.9.0"
document-id: SASD-REF-BASELINE-007
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
depends-on: [SASD-REF-BASELINE-001, SASD-REF-BASELINE-002, SASD-REF-BASELINE-003, SASD-REF-BASELINE-004, SASD-REF-BASELINE-005, SASD-GOV-002, SASD-GOV-004, SASD-GOV-005, SASD-GOV-007]
normative-keywords: []
---

# Normative Baseline Approval Record 0.9.0

## 1. Entscheidung

```text
Integrated review:            Completed
Local technical validation:   Passed
Maintainer decision:          Approved with release conditions
Normative documents:          32
Normative requirements:       1,345
Publication performed:        No
Release candidate:            No
Stable Version 1.0.0:         No
```

Der Maintainer **Robin Görlach** (`Robin-Goerlach`) genehmigt am **24. Juli 2026** die
normative Baseline `0.9.0` für die weitere Entwicklung von SASD Development Standard
Version 1.0.

Die Freigabe umfasst den technologieunabhängigen Core Standard, das C#/.NET-Profil, das
Desktopprofil sowie die operativen Prozesse. Sie macht diese Dokumente innerhalb des
freigegebenen Repository-Entwicklungsstands verbindlich. Sie ist noch kein GitHub Release,
kein Release Candidate, keine stabile Version 1.0.0 und keine externe Zertifizierung.

## 2. Commit- und Inhaltsidentität

Der Approval-Commit wird mit der empfohlenen Commit-Message
`docs: approve normative baseline 0.9.0` eingespielt.

Da die konkrete Commit-SHA erst durch den Commit entsteht, wird keine erfundene SHA in dieses
Paket geschrieben. Der Approval-Commit ist nach dem Commit dauerhaft auflösbar mit:

```bash
git log --diff-filter=A --format=%H -- \
  docs/40-governance/NORMATIVE-BASELINE-APPROVAL-0.9.0.md
```

Der geprüfte Baseline-Stand ist der Parent dieses Approval-Commits. Die freigegebenen
Dateiinhalte werden zusätzlich durch das
[Approval Manifest](NORMATIVE-BASELINE-APPROVAL-MANIFEST-0.9.0.md) mit SHA-256-Prüfsummen
identifiziert. Der aktuelle Lifecycle-Status wird zusätzlich im
[Status Register](NORMATIVE-BASELINE-STATUS-REGISTER-0.9.0.md) dokumentiert, ohne den
historischen Dokumentkatalog 0.8.0 rückwirkend zu verändern.

## 3. Freigegebener Umfang

| Bereich | Dokumente | Anforderungen | Dokumentversion | Status |
|---|---:|---:|---:|---|
| Core Standard | 13 | 545 | 0.9.0 | Approved |
| C#/.NET-Profil | 8 | 277 | 0.9.0 | Approved |
| Desktopprofil | 4 | 215 | 0.9.0 | Approved |
| Operative Prozesse | 7 | 308 | 0.9.0 | Approved |
| **Gesamt** | **32** | **1.345** | **0.9.0** | **Approved** |

Nicht Bestandteil dieser Freigabe sind:

- Veröffentlichung eines Tags oder GitHub Releases,
- Release Candidate `1.0.0-rc.1`,
- stabile Version `1.0.0`,
- Abschluss des TaskHost-Local-Piloten,
- Aktivierung eines GitHub-Rulesets,
- spätere Linux-, Datenbank-, Container- oder Security-Fachprofile.

## 4. Reviewumfang und Ergebnis

| Prüfkriterium | Ergebnis | Nachweis |
|---|---|---|
| Vollständigkeit | Passed | 32 Dokumente und 1.345 Anforderungen |
| Widerspruchsfreiheit | Passed | integrierter Review 0.9.0 |
| Abhängigkeiten | Passed | azyklische Dependency Map |
| Eindeutigkeit | Passed | Dokument- und Anforderungsvalidatoren |
| Proportionalität | Passed | Qualitätsstufen und Solo-Developer-Guidance |
| Nachweisbarkeit | Passed | stabile IDs, Evidence-Regeln und Manifest |
| Offene Platzhalter | None | bündelweiter Validator |
| Wortgleiche Doppelanforderungen | None | bündelweiter Validator |
| Blocker | None | Approval Checklist 0.9.0 |
| Major-Befunde | None | Approval Checklist 0.9.0 |

## 5. Befunde, Ausnahmen und Auflagen

### Blocker

Keine inhaltlichen Freigabeblocker.

### Major

Keine offenen Major-Befunde.

### Genehmigte normative Ausnahmen

Keine.

### Release-Auflagen

Die Dokumentfreigabe erfolgt mit folgenden Auflagen für den Release Candidate:

1. Der Approval-Commit MUSS in GitHub Actions unter Ubuntu und Windows erfolgreich geprüft
   werden.
2. Der Statuscheck `SASD merge gate` MUSS für den Approval-Commit erfolgreich sein.
3. TaskHost Local Wave 01 MUSS verifiziert oder durch eine getrennte, begründete
   Release-Entscheidung als nicht blockierend eingestuft werden.
4. Offene Repository-CI- und Ruleset-Nachweise MÜSSEN vor dem Release Candidate bewertet
   werden.
5. Publikationsartefakte, Release Record und Release Notes MÜSSEN separat erzeugt werden.

Eine Release-Auflage ist keine stillschweigende Ausnahme von einer normativen Anforderung.
Sie begrenzt ausschließlich den Übergang zum Release Candidate.

## 6. Freigabeerklärung

Ich bestätige, dass das aufgeführte Bündel gegen die dokumentierten Freigabekriterien geprüft
wurde. Ich genehmige die 32 normativen Dokumente als Baseline `0.9.0` für SASD Development
Standard Version 1.0 mit den in Abschnitt 5 genannten Release-Auflagen.

- **Name:** Robin Görlach
- **Repository identity:** `Robin-Goerlach/SASD-Development-Standard`
- **Rolle:** SASD Development Standard Maintainer
- **Datum:** 24. Juli 2026
- **Entscheidung:** Approved with documented release conditions
- **Veröffentlichung:** noch nicht erfolgt

## 7. Änderungswirkung

Nach dieser Freigabe gilt:

- normative Bedeutungsänderungen setzen das betroffene Dokument mindestens auf `Proposed`
  zurück oder werden als neue Proposed-Dokumentversion geführt,
- redaktionelle Korrekturen bleiben nachvollziehbar,
- ein fehlgeschlagener Approval-Commit-Validator MUSS vor dem Release Candidate behoben
  werden,
- spätere Releases referenzieren die freigegebenen Dokumentversionen und das Approval
  Manifest,
- die Freigabe kann nur über einen dokumentierten Change-, Deprecation- oder
  Ablöseprozess ersetzt werden.
