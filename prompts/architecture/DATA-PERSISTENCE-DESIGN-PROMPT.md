---
prompt-id: "SASD-PROMPT-ARCH-003"
title: "Daten- und Persistenzkonzept entwerfen"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "architecture"
language: "de"
summary: "Entwirft Datenmodell, Speicherstrategie, Migration, Backup und Wiederherstellung."
variables: ["project_name", "requirements", "architecture_context", "security_context", "constraints", "quality_level", "output_language"]
tags: ["data", "persistence", "migration", "backup"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core", ".NET"]
last-reviewed: "2026-07-25"
---

# Daten- und Persistenzkonzept entwerfen
## Zweck

Erstelle ein Daten- und Persistenzkonzept für **{{project_name}}**.

## Eingaben

- Anforderungen: {{requirements}}
- Architekturkontext: {{architecture_context}}
- Schutzbedarf: {{security_context}}
- Randbedingungen: {{constraints}}
- Qualitätsstufe: {{quality_level}}

## Arbeitsauftrag

1. Identifiziere fachliche Daten, Eigentümer, Lebenszyklus und Beziehungen.
2. Trenne dauerhafte Daten, Konfiguration, Cache, Logs und temporäre Artefakte.
3. Bewerte Speicheroptionen nach Konsistenz, Portabilität, Betrieb und Wiederherstellung.
4. Definiere Schema, Versionierung, Migration, Transaktionen und Konkurrenzverhalten.
5. Plane Backup, Restore, Export, Löschung und Datenschutz.
6. Leite Integrations- und Migrationstests ab.

## Qualitätsregeln

- Keine Repository-Abstraktion ohne konkreten Test-, Austausch- oder Fachnutzen.
- Datenverlust- und Rückwärtskompatibilitätsrisiken explizit behandeln.
- Geheimnisse dürfen nicht in normale Konfigurations- oder Exportdateien gelangen.
- Migrationen müssen wiederholbar und nachweisbar sein.

## Ausgabeformat

Liefere in {{output_language}}: Dateninventar, Modell, Speicherentscheidung, Dateipfade, Migration, Backup/Restore, Security, Tests und offene ADRs.
