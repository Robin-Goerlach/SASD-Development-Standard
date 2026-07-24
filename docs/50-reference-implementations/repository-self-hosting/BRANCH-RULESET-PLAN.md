---
title: "Branch-Ruleset-Plan für main"
document-id: SASD-REF-CI-002
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
depends-on: [SASD-GOV-004, SASD-GOV-005, SASD-PROC-004, SASD-REF-CI-001]
---

# Branch-Ruleset-Plan für `main`

## 1. Ziel

Der Default Branch soll vor versehentlichen, nicht geprüften und nicht
rückverfolgbaren Änderungen geschützt werden, ohne für die aktuelle
Solo-Maintainer-Phase unnötige Teamprozesse vorzutäuschen.

## 2. Gewählte Regeln

| Regel | Einstellung | Begründung |
|---|---|---|
| Ziel | Default Branch | unabhängig von einer späteren Umbenennung |
| Löschung | verboten | schützt den kanonischen Branch |
| Force Push | verboten | erhält die nachvollziehbare Historie |
| Statuscheck | `SASD merge gate` | bündelt Ubuntu- und Windows-Validierung |
| Strict Policy | aktiviert | prüft gegen den aktuellen Zielbranch |
| Externe Approval-Anzahl | keine | derzeit kein zweiter Maintainer |
| Merge Queue | keine | für das aktuelle Änderungsvolumen unverhältnismäßig |
| Bypass Actors | keine im Baseline-Payload | Ausnahmen sollen bewusst administrativ erfolgen |

## 3. Auswirkung auf den Arbeitsablauf

Nach der Aktivierung ist der vorgesehene Ablauf:

```text
Arbeitsbranch erstellen
  -> Änderungen committen
  -> Branch pushen
  -> Pull Request öffnen
  -> SASD Quality Gates abwarten
  -> Ergebnisse prüfen
  -> Pull Request mergen
```

Die Regel „Require a pull request before merging“ wird nicht zusätzlich gesetzt.
Der erforderliche Statuscheck verhindert dennoch den normalen ungeprüften Push
nach `main`, weil der Check erst für einen anderen Ref beziehungsweise Pull
Request erfolgreich ausgeführt werden kann.

## 4. Aktivierungsgrenze

Das Ruleset darf erst aktiviert werden, wenn für die aktuelle `main`-Commit-SHA
alle drei erwarteten Jobs erfolgreich nachgewiesen wurden:

- `Validate (ubuntu-latest)`,
- `Validate (windows-latest)`,
- `SASD merge gate`.

## 5. Verwaltungsrechte

Die API-Aktivierung benötigt ein Token mit Repository-Berechtigung
`Administration: write`. Das Token wird nicht im Repository gespeichert. Das
Tool verwendet zuerst `GITHUB_TOKEN` oder `GH_TOKEN` und kann optional den
GitHub-CLI-Login über `gh auth token` verwenden.

## 6. Änderungsregel

Eine Änderung des Checknamens, der Branchbedingungen, des Enforcement-Status
oder der Schutzregeln muss zusammen mit Workflow, Aktivierungsrecord und
CI-Policy-Validator geprüft werden.
