---
title: "Version 1.0 Spezifikationsbaseline und Validierungsübergabe"
document-id: SASD-REF-RC-008
document-type: informative
status: Draft
version: 0.1.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-08-06
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-FND-007, SASD-REF-RC-001, SASD-REF-RC-003, SASD-REF-PILOT-007]
---

# Version 1.0 Spezifikationsbaseline und Validierungsübergabe

## 1. Maintainer-Entscheidung

> **Die Theorie ist vollständig genug, um praktisch angewendet und bewertet zu werden. Ihre Praxistauglichkeit ist noch nicht abschließend bestätigt.**

Der SASD Development Standard wird nach Abschluss der laufenden Dokumentationskonsolidierung als **Version 1.0 Specification Candidate** behandelt. Dieser Zustand ist eine stabile Arbeits- und Bewertungsgrundlage, aber weder ein Release Candidate noch die stabile Version `1.0.0`.

Die endgültige Freigabe von Version 1.0 bleibt ausgesetzt, bis Referenzprodukte den eingefrorenen Standard praktisch angewendet haben, die dabei entstandene Evidenz ausgewertet wurde und notwendige Korrekturen in einen abschließend geprüften Standardstand eingeflossen sind.

## 2. Erreichter theoretischer Stand

Die Spezifikationsbaseline umfasst:

- 46 freigegebene normative Dokumente,
- die freigegebene Foundation- und Governance-Basis `0.8.0`,
- die integrierte normative Baseline `0.9.0` mit 1.345 Anforderungen,
- Core-, C#/.NET- und Desktopprofil,
- sieben operative Prozesse,
- Vorlagen, Checklisten, Prompts und Validatoren,
- dokumentierte Small-, Medium- und Large-Pilotbaselines,
- einen verbindlichen Scope Freeze für Version 1.0,
- plattformübergreifend erfolgreiche Repository-Quality-Gates,
- eine reproduzierbare technische Remote-Baseline für SASD TaskHost Local.

Diese Nachweise bestätigen, dass der Standard konsistent genug ist, um als Arbeitsgrundlage in realen Projekten eingesetzt zu werden. Sie bestätigen noch nicht seine vollständige Praxistauglichkeit.

## 3. Statusmodell

| Bereich | Zustand | Bedeutung |
|---|---|---|
| Normative Dokumentation | Approved | Die bindenden Inhalte sind formal freigegeben. |
| Spezifikationsbaseline | Established | Die Theorie ist für praktische Anwendung und Bewertung vollständig genug. |
| Repository-Validierung | Passed | Die automatisierten lokalen und plattformübergreifenden Standardprüfungen sind reproduzierbar. |
| TaskHost-Remote-Baseline | Passed | Exakter Checkout, Restore, Build, NuGet-Audit und Publish sind für einen festgelegten Zielcommit nachgewiesen. |
| Praktische Referenzvalidierung | Pending | Der Standard wurde noch nicht vollständig durch mindestens ein Referenzprodukt angewendet und bewertet. |
| Release Candidate | Paused | Die RC-Vorbereitung wird erst nach ausreichender praktischer Evidenz fortgesetzt. |
| Stable `1.0.0` | Not approved | Eine stabile Freigabe wäre zum aktuellen Zeitpunkt eine nicht belegte Behauptung. |

## 4. Abgrenzung der TaskHost-Baseline

Der erfolgreiche Remote-Baseline-Lauf für SASD TaskHost Local bestätigt:

- öffentlich erreichbares Ziel-Repository,
- unveränderlichen Zielcommit,
- Windows-Ausführung in GitHub Actions,
- `dotnet restore`,
- `dotnet build`,
- NuGet-Audit,
- `dotnet publish` und ein erzeugtes Windows-Artefakt.

Er bestätigt ausdrücklich nicht:

- die Integration des vorbereiteten Wave-01-Artefakts,
- vorhandene und erfolgreich ausgeführte automatisierte Produkttests,
- einen Headless-Laufzeit-Self-Check,
- einen manuellen Windows-Smoke-Test,
- den vollständigen Abschluss des Piloten,
- die abschließende Praxistauglichkeit des Standards.

## 5. Regeln während der praktischen Validierung

1. Die freigegebene normative Baseline bleibt der feste Ausgangsmaßstab.
2. Neue große Themen, Profile oder Umstrukturierungen bleiben außerhalb des Version-1.0-Scopes.
3. Referenzprodukte verbleiben in eigenständigen Repositories und werden über exakte Commits referenziert.
4. Erfahrungen werden zunächst als Evidenz, Gap, Abweichung, Ausnahme oder Feedback erfasst.
5. Der Standard wird während der Referenzentwicklung nur für nachgewiesene Fehler, Sicherheitsprobleme oder zwingende Klarstellungen geändert.
6. Praktische Schwierigkeiten führen nicht automatisch zu einer Normänderung; zunächst ist zwischen Standardfehler, projektspezifischer Ausnahme und fehlender Projektreife zu unterscheiden.
7. Jede spätere Änderung bleibt über den regulären Änderungs- und Freigabeprozess nachvollziehbar.

## 6. Praktische Validierungsphase

Die Referenzprodukte sollen den Specification Candidate in getrennten Arbeitssträngen anwenden. Die derzeit vorgesehenen Projekte sind:

- SASD TaskHost Local als kleines C#/.NET-Desktopprojekt,
- SASD Prompt Manager als mittleres Projekt,
- SASD Mail Workbench als großes beziehungsweise komplexes Projekt.

Für jedes Projekt werden mindestens festgehalten:

- angewendete Standardversion und Profile,
- exakter Zielcommit,
- gewählte Qualitätsstufe,
- umgesetzte Anforderungen und begründete Nichtanwendbarkeit,
- Build-, Test-, Sicherheits-, Laufzeit- und Releaseevidenz im angemessenen Umfang,
- Abweichungen, Ausnahmen und unnötige Belastungen,
- Lessons Learned und konkrete Änderungsvorschläge.

## 7. Wiederaufnahme der Release-Candidate-Phase

Die RC-Vorbereitung wird erst wieder aufgenommen, wenn mindestens:

1. ein Referenzprodukt den Standard praktisch und nachvollziehbar angewendet hat,
2. die für dieses Projekt angemessenen Build-, Test-, Laufzeit- und Releaseprüfungen erfolgreich nachgewiesen sind,
3. die daraus entstandenen Gaps, Abweichungen und Lessons Learned bewertet wurden,
4. erforderliche Standardkorrekturen umgesetzt und erneut freigegeben wurden,
5. die Quality Gates für den dann vorgesehenen RC-Commit erfolgreich sind,
6. die Branch-Governance entschieden und die Releaseartefakte reproduzierbar geprüft werden können.

Die bestehenden RC-Blocker bleiben bis dahin offen. Sie werden weder umbenannt noch durch eine pauschale Ausnahme als erledigt behandelt.

## 8. Nichtaussagen

Der Specification Candidate ist nicht:

- ein veröffentlichter Release Candidate,
- die stabile Version `1.0.0`,
- eine Zertifizierung,
- ein Nachweis, dass alle Referenzprodukte fertig sind,
- ein Nachweis, dass jede Anforderung in jedem Projekt praktikabel ist,
- eine Freigabe, praktische Evidenz durch Dokumentation zu ersetzen.

## 9. Verwandte Nachweise

- [Projektstatus](../../PROJECT-STATUS.md)
- [Roadmap](../../ROADMAP.md)
- [Version-1.0-Scope-Freeze](VERSION-1.0-SCOPE-FREEZE.md)
- [Release-Candidate-Plan](VERSION-1.0-RELEASE-CANDIDATE-PLAN.md)
- [Release-Candidate-Blockerregister](VERSION-1.0-RELEASE-CANDIDATE-BLOCKERS.md)
- [Version-1.0-Pilot-Readiness](../50-reference-implementations/VERSION-1.0-PILOT-READINESS.md)
- [TaskHost-Remote-Baseline-Evidenz](../50-reference-implementations/pilot-01-sasd-taskhost-local/REMOTE-BASELINE-EVIDENCE-2026-08-06.md)
