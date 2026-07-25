---
title: "Prozesslandkarte Version 1.0"
document-id: SASD-REF-PROC-001
document-type: informative
status: Draft
version: 0.9.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-PROC-001, SASD-PROC-002, SASD-PROC-003, SASD-PROC-004, SASD-PROC-005, SASD-PROC-006, SASD-PROC-007]
---

# Prozesslandkarte Version 1.0

## Zweck

Diese Landkarte zeigt das Zusammenspiel der operativen Prozesse. Die Abläufe sind iterativ und dürfen je nach Projekt zusammengeführt werden.

```mermaid
flowchart TD
    A[Idee oder bestehendes Projekt] --> B[Projektklassifikation]
    B --> C{Neu oder bestehend?}
    C -->|Neu| D[Projektinitialisierung]
    C -->|Bestehend| E[Legacy-Assessment und Migration]
    D --> F[Entwicklung und Meilensteine]
    E --> F
    F --> G[Architekturentscheidungen]
    F --> H[Reviews]
    G --> F
    H --> F
    F --> I[Releaseprozess]
    I --> J[Betrieb und Wartung]
    J --> B
    J --> K{Weiterführen?}
    K -->|Ja| F
    K -->|Nein| L[Projektarchivierung]
```

## Prozessverantwortung

| Prozess | Primäre Entscheidung | Typische Nachweise |
|---|---|---|
| Projektklassifikation | Welche Stufe und Profile gelten? | Klassifikationsnachweis, Risikomerkmale |
| Projektinitialisierung | Ist das Projekt bereit für den ersten Meilenstein? | Projektbrief, Readiness Gate |
| ADR-Prozess | Welche langfristige technische Option wird gewählt? | ADR, ADR-Index, Folgemaßnahmen |
| Reviewprozess | Ist ein Artefakt oder Änderungsstand ausreichend geprüft? | Findings, Verifikation, Freigabe |
| Legacy-Migration | Wie wird ein bestehendes Projekt sicher angeglichen? | Assessment, Backlog, Wellenplan |
| Releaseprozess | Darf der geprüfte Stand veröffentlicht werden? | Artefakte, Release Record, Verifikation |
| Projektarchivierung | Ist die Stilllegung vollständig und verantwortbar? | Archivierungsnachweis, Restpflichten |

## Skalierung

Einzelentwickler dürfen Rollen kombinieren und Artefakte zusammenführen. Nicht zusammengeführt werden dürfen jedoch:

- Entscheidung und ihre Begründung,
- offenes Risiko und genehmigte Ausnahme,
- geprüfter Stand und später veränderter Stand,
- Releaseartefakt und nicht geprüfter lokaler Build,
- Archivierungsstatus und weiterhin aktive Restpflichten.

## Pilotanwendung

Für die ersten SASD-Pilotprojekte empfiehlt sich folgende Reihenfolge:

1. bestehendes Projekt klassifizieren,
2. Legacy-Assessment erstellen,
3. einen kleinen Migrationsmeilenstein planen,
4. ADRs für strukturelle Änderungen schreiben,
5. Änderung reviewen,
6. Releaseprozess anwenden,
7. Erfahrungen im Reviewnachweis festhalten.
