---
title: "Pilot 02 Charter – SASD Prompt Manager"
document-id: SASD-REF-PILOT-202
document-type: informative
status: Draft
version: 0.11.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-25
applies-to-quality-levels: [Recommended]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-REF-PILOT-001, SASD-PROC-002, SASD-PROC-005]
---

# Pilot 02 Charter – SASD Prompt Manager

## 1. Pilotziel

Der Pilot soll zeigen, ob der Standard eine bereits umfangreiche, geschichtete Desktopanwendung vereinheitlichen kann, ohne funktionierende fachliche Strukturen unnötig umzubauen. Gleichzeitig wird geprüft, ob Recommended-Anforderungen für Tests, Datenintegrität, Security, Dokumentation und CI bei einer mittelgroßen Einzelentwickleranwendung handhabbar bleiben.

## 2. Validierungsfragen

- Ist die Einstufung Medium / Recommended angemessen?
- Sind App, Application, Domain und Infrastructure sinnvoll getrennt oder existieren unnötige Abhängigkeiten?
- Reicht das vorhandene Testmodell für fachliche und persistente Risiken?
- Wie werden Prompts mit möglichen Secrets, Import/Export und Backups sicher behandelt?
- Welche Standarddateien und Nachweise fehlen trotz guter Projektstruktur?
- Lässt sich die Migration in einer begrenzten Welle durchführen, ohne UI- oder Datenmodell-Redesign?

## 3. In Scope für Wave 01

- lokaler Baseline-Clone mit vollständiger Commit-ID,
- reproduzierbarer Restore-, Build- und Testlauf,
- Projekt- und Abhängigkeitsinventar,
- CI- und Paketmanagement-Basis,
- Security Policy und Secret-/Prompt-Risikobewertung,
- Persistenz-, Import/Export- und Backup-Verifikation,
- Testlücken in Application, Infrastructure und UI-nahem Verhalten,
- SASD-Alignment- und Abweichungsnachweis.

## 4. Out of Scope

- Wechsel von WinForms zu WPF, Avalonia oder MAUI,
- direkte KI-Provider-Integration,
- RAG, Agenten oder Workflow-Engine,
- Mehrbenutzer- oder Cloudbetrieb,
- vollständiger UI-Neuentwurf,
- pauschale Aufteilung in weitere Projekte,
- Migration des gesamten Datenmodells ohne belegten Fehler.

## 5. Erfolgskriterien

- Baseline-Commit und Toolchain sind dokumentiert.
- Restore, Release-Build und bestehende Tests laufen reproduzierbar.
- CI prüft Build und Tests auf Windows.
- relevante Datenpfade, Backup und Restore sind praktisch geprüft.
- Secret-/Prompt-Risiken und Security-Kontaktweg sind dokumentiert.
- priorisierte Testlücken besitzen mindestens einen umsetzbaren Plan.
- keine Architekturänderung erfolgt ohne dokumentierten Nutzen.
