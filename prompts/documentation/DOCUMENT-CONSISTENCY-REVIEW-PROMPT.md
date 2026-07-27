---
prompt-id: "SASD-PROMPT-DOC-002"
title: "Dokumentkonsistenz prüfen"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "documentation"
language: "de"
summary: "Prüft Widersprüche, veraltete Aussagen, Links, Versionen und Zuständigkeiten in Projektdokumenten."
variables: ["project_name", "existing_documentation", "current_state", "requirements", "evidence", "output_language"]
tags: ["documentation-review", "consistency", "links", "versioning"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# Dokumentkonsistenz prüfen
## Zweck

Prüfe die Dokumentation von **{{project_name}}** auf Konsistenz und Aktualität.

## Eingaben

- Dokumente: {{existing_documentation}}
- bestätigter Ist-Zustand: {{current_state}}
- Anforderungen: {{requirements}}
- Nachweise: {{evidence}}

## Arbeitsauftrag

1. Vergleiche Vision, README, Anforderungen, Architektur, Roadmap, Changelog, Security, Tests und Releaseunterlagen.
2. Identifiziere widersprüchliche Versions-, Status-, Lizenz-, Technologie- und Funktionsaussagen.
3. Prüfe Links, Dokument-IDs, Verantwortlichkeiten und Source-of-Truth-Regeln.
4. Kennzeichne historische Dokumente und veraltete Pläne.
5. Schlage konkrete Korrekturen mit Vorrangregeln vor.

## Qualitätsregeln

- Historische Nachweise nicht stillschweigend überschreiben.
- Freigabemanifeste und Prüfsummen berücksichtigen.
- Eine aktuellere Datei ist nicht automatisch autoritativ.
- Fehlende Evidenz als Unsicherheit dokumentieren.

## Ausgabeformat

Liefere in {{output_language}}: Dokumentinventar, Konfliktmatrix, veraltete Aussagen, Linkfehler, Source-of-Truth-Empfehlung und priorisierten Korrekturplan.
