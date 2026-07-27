---
prompt-id: "SASD-PROMPT-ARCH-004"
title: "Bedrohungsmodell erstellen"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "architecture"
language: "de"
summary: "Erstellt ein proportioniertes Bedrohungsmodell mit Assets, Grenzen, Szenarien und Maßnahmen."
variables: ["project_name", "architecture_context", "security_context", "target_users", "source_material", "quality_level", "output_language"]
tags: ["security", "threat-model", "trust-boundaries", "risk"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# Bedrohungsmodell erstellen
## Zweck

Erstelle ein proportioniertes Bedrohungsmodell für **{{project_name}}**.

## Eingaben

- Architektur: {{architecture_context}}
- Schutzbedarf und Daten: {{security_context}}
- Nutzer und Rollen: {{target_users}}
- bestehende Sicherheitsinformationen: {{source_material}}
- Qualitätsstufe: {{quality_level}}

## Arbeitsauftrag

1. Identifiziere Assets, Angreiferziele, Eintrittspunkte und Vertrauensgrenzen.
2. Beschreibe relevante Datenflüsse und privilegierte Operationen.
3. Entwickle realistische Missbrauchs- und Fehlerszenarien.
4. Bewerte Wahrscheinlichkeit, Auswirkung und vorhandene Kontrollen.
5. Leite präventive, detektive und wiederherstellende Maßnahmen ab.
6. Ordne Maßnahmen Anforderungen, Architektur, Tests und Betrieb zu.

## Qualitätsregeln

- Keine Sicherheitsgarantien ohne Evidenz.
- Risiken durch Fehlbedienung, Datenverlust und Lieferkette berücksichtigen.
- Keine generische Checkliste ohne Projektbezug.
- Restrisiken und akzeptierte Risiken sichtbar halten.

## Ausgabeformat

Erzeuge in {{output_language}}: Systemübersicht, Assetliste, Vertrauensgrenzen, Bedrohungsszenarien, Risikomatrix, Maßnahmen, Tests, Restrisiken und Reviewauslöser.
