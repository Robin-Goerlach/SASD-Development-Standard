---
prompt-id: "SASD-PROMPT-REVIEW-004"
title: "Security Review durchführen"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "review"
language: "de"
summary: "Prüft Schutzbedarf, Angriffsflächen, Secrets, Abhängigkeiten, Daten und Wiederherstellung."
variables: ["project_name", "repository_tree", "architecture_context", "security_context", "quality_level", "evidence", "source_material", "output_language"]
tags: ["security-review", "secrets", "supply-chain", "privacy"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# Security Review durchführen
## Zweck

Führe ein risikobasiertes Security Review für **{{project_name}}** durch.

## Eingaben

- Repository und Struktur: {{repository_tree}}
- Architektur: {{architecture_context}}
- Schutzbedarf: {{security_context}}
- Qualitätsstufe: {{quality_level}}
- vorhandene Sicherheitsnachweise: {{evidence}}
- relevante Dateien und Quellen: {{source_material}}

## Arbeitsauftrag

Prüfe Assets, Vertrauensgrenzen, Eingaben, Authentisierung, Autorisierung, Secrets, Kryptographie, Konfiguration, Datenpfade, Logging, Datenschutz, Abhängigkeiten, Buildkette, Updates, Backup, Restore und Incident Response. Ordne Befunde konkreten Anforderungen und realistischen Angriffsszenarien zu.

## Qualitätsregeln

- Keine Exploitbehauptung ohne reproduzierbare Evidenz.
- Keine sensitiven Werte in der Ausgabe wiedergeben.
- Schweregrad aus Auswirkung und Ausnutzbarkeit ableiten.
- Defensive, proportionale Maßnahmen bevorzugen.
- Rechtliche Beratung nicht vortäuschen.

## Ausgabeformat

Erzeuge in {{output_language}}: Scope, Schutzbedarf, Angriffsfläche, Befunde mit Evidenz, Risikobewertung, Sofortmaßnahmen, strukturelle Maßnahmen, Tests, Restrisiken und verantwortliche Offenlegungshinweise.
