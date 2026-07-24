---
title: "Referenzimplementierungen"
document-id: SASD-REF-001
document-type: informative
status: Proposed
version: 0.8.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-GOV-007, SASD-PROC-005]
---

# Referenzimplementierungen

Dieses Verzeichnis dokumentiert die praktische Erprobung des SASD Development Standard an realen SASD-Projekten. Der Quellcode der Pilotprojekte verbleibt in den jeweiligen Projekt-Repositories; hier werden Auswahl, Klassifikation, Ausgangslage, Migrationswellen, Nachweise und Erkenntnisse versioniert.

## Pilotprogramm

1. [Pilotprogramm](PILOT-PROGRAM.md)
2. [Evidenzmodell](PILOT-EVIDENCE-MODEL.md)
3. [Pilotportfolio](PILOT-PORTFOLIO.md)
4. [Feedbacklog](PILOT-FEEDBACK-LOG.md)
5. [Feedbackübersicht](PILOT-FEEDBACK-SUMMARY.md)

## Aktive Piloten

| Pilot | Kategorie | Zielstufe | Status | Umsetzung | Verifikation | Nächster Schritt |
|---|---|---|---|---|---|---|
| [Pilot 01 – SASD TaskHost Local](pilot-01-sasd-taskhost-local/README.md) | kleines C#/.NET-WinForms-Werkzeug | Recommended | In Execution | Artifact Prepared | Pending | kontrollierte Wave-01-Verifikation |

## Für Version 1.0 vorgesehene Kategorien

1. kleines C#/.NET-Werkzeug,
2. mittlere gepflegte Desktopanwendung,
3. komplexere geschichtete C#/.NET-Anwendung.

## Wichtige Abgrenzung

Die Referenzdokumentation ist informativ. Sie zeigt Anwendung und Feedback, ersetzt aber weder normative Dokumente noch Nachweise im Ziel-Repository. Ein statisch geprüftes Overlay ist ein wertvolles Artefakt, aber noch keine verifizierte Referenzimplementierung.
