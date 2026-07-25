---
title: "Pilot-Readiness für Version 1.0"
document-id: SASD-REF-PILOT-007
document-type: informative
status: Draft
version: 0.11.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-25
applies-to-quality-levels: [Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-FND-007, SASD-REF-PILOT-001, SASD-REF-PILOT-002, SASD-REF-PILOT-003]
---

# Pilot-Readiness für Version 1.0

Diese Datei wird deterministisch aus den Pilotmanifesten erzeugt.

## Abdeckung

| Erforderliche Kategorie | Pilot | Bewertungszustand | Technischer Zustand |
|---|---|---|---|
| kleines Werkzeug | Pilot 01 – SASD TaskHost Local | In Execution | Artefakt vorbereitet; technische Verifikation ausstehend |
| mittlere Desktopanwendung | Pilot 02 – SASD Prompt Manager | Baseline Assessed | Umsetzung nicht begonnen |
| komplexere geschichtete Anwendung | Pilot 03 – SASD Mail Workbench | Baseline Assessed | Umsetzung nicht begonnen |

## Zusammenfassung

- registrierte Piloten: **3**
- mindestens als Baseline bewertet: **3**
- technisch mit `Passed` verifiziert: **0**
- abgedeckte Größenklassen: **Small, Medium, Large**

## Bewertung

Die strukturelle Größenabdeckung aus `SASD-FND-007` ist hergestellt, wenn Small, Medium und Large vorhanden sind. Dies ist ein Portfolio- und Dokumentationsnachweis, kein Build-, Test-, Laufzeit- oder CI-Nachweis der Ziel-Repositories.

## Release-Bedeutung

Für einen Release Candidate ist mindestens ein praktisch ausgeführter und überprüfter Pilotdurchlauf weiterhin erforderlich. Für die stabile Version 1.0 sollen alle drei Baselines gegen konkrete Commits bestätigt und die wesentlichen Erkenntnisse konsolidiert werden.

## Offene Pilot-Blocker

1. TaskHost Local Wave 01 im Ziel-Repository committen und verifizieren.
2. Prompt Manager Baseline in einem lokalen Clone bestätigen und Wave 01 ausführen.
3. Mail Workbench Baseline in einem lokalen Clone bestätigen und Wave 01 ausführen.
4. gemeinsame Lessons Learned und Standardänderungsbedarf konsolidieren.
