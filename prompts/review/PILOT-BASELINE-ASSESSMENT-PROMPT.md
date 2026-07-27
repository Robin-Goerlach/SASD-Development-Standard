---
prompt-id: "SASD-PROMPT-REVIEW-006"
title: "Pilot-Baseline bewerten"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "review"
language: "de"
summary: "Erstellt eine evidenzbasierte Ausgangsbewertung für einen Referenzpiloten."
variables: ["project_name", "repository_url", "repository_tree", "current_state", "quality_level", "profiles", "evidence", "output_language"]
tags: ["pilot", "baseline", "evidence", "gaps"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core", ".NET", "Desktop"]
last-reviewed: "2026-07-25"
---

# Pilot-Baseline bewerten
## Zweck

Bewerte **{{project_name}}** als Pilot für den SASD Development Standard.

## Eingaben

- Repository: {{repository_url}}
- Struktur: {{repository_tree}}
- berichteter Ist-Zustand: {{current_state}}
- Qualitätsstufe: {{quality_level}}
- Profile: {{profiles}}
- Nachweise: {{evidence}}

## Arbeitsauftrag

Unterscheide lokal verifiziert, öffentlich beobachtet, vom Projekt berichtet, abgeleitet, vorbereitet und unbekannt. Erstelle Projektklassifikation, Stärken, Blocker/Major/Minor/Observation, Risiken für Daten/Security/Build/Tests/Releases, proportionale Bewertung, priorisierte Migrationswellen und benötigte lokale Nachweise.

## Qualitätsregeln

- Keine erfolgreichen Builds, Tests oder Alignment behaupten, wenn direkte Evidenz fehlt.
- Beobachtungsdatum, Branch und Commit nennen, soweit bekannt.
- Keine komplexe Zielarchitektur nur zur Erfüllung eines Musters.
- Unsicherheit sichtbar halten.

## Ausgabeformat

Erzeuge in {{output_language}}: Baseline Assessment, Evidenzklassen, Gap Register, erste Wellen, Verifikationsplan, offene Fragen und Pilotentscheidung.
