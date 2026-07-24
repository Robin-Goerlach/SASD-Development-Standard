---
title: "Pilot 01 – SASD TaskHost Local"
document-id: SASD-REF-PILOT-101
document-type: informative
status: Draft
version: 0.7.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-REF-PILOT-001, SASD-REF-PILOT-002, SASD-PROC-005]
---

# Pilot 01 – SASD TaskHost Local

## Status

```text
Pilot ID:       SASD-PILOT-001
Kategorie:      kleines C#/.NET-Desktopprojekt
Qualitätsstufe: SASD Recommended
Profile:        Core + DotNet + Desktop
Pilotstatus:    Wave 01 vorbereitet
Ziel-Repository: https://github.com/Robin-Goerlach/SASD-TaskHost-Local
```

Dieses Paket dokumentiert Auswahl, Baseline Assessment und die erste begrenzte Migrationswelle. Es nimmt keine Änderungen am Ziel-Repository vor und behauptet deshalb noch keine abgeschlossene Umsetzung.

## Dokumente

1. [Pilot Charter](PILOT-CHARTER.md)
2. [Projektklassifikation](PROJECT-CLASSIFICATION.md)
3. [Baseline Assessment](BASELINE-ASSESSMENT.md)
4. [Gap Register](GAP-REGISTER.md)
5. [Migrationsplan](MIGRATION-PLAN.md)
6. [Wave-01-Plan](WAVE-01-PLAN.md)
7. [Evidenzzuordnung](EVIDENCE-MAP.md)
8. [Entscheidungslog](DECISION-LOG.md)
9. [Pilotreview](PILOT-REVIEW.md)
10. [`pilot.json`](pilot.json)

## Warum dieses Projekt?

TaskHost Local ist klein genug für einen überschaubaren Pilotdurchlauf, besitzt aber reale Persistenz, private Nutzerdaten, einen dokumentierten Laufzeitblocker, eine WinForms-Oberfläche und einen langfristigen Nutzungszweck. Damit prüft es, ob der Standard pragmatisch hilft, ohne einen modularen Monolithen oder eine Clean-Architecture-Solution künstlich zu erzwingen.

## Nächster Schritt

Wave 01 wird im Ziel-Repository technisch ausgeführt. Danach werden Build-, Test-, Laufzeit- und Reviewnachweise hier ergänzt und die Pilotbewertung aktualisiert.
