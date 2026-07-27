---
prompt-id: "SASD-PROMPT-REVIEW-012"
title: "Updatepaket und Ziel-Repository prüfen"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "review"
language: "de"
summary: "Prüft Repository-Identität, Overlay-Sicherheit, Löschungen, Rollback und verbleibende Nachweise."
variables: ["project_name", "repository_url", "source_material", "evidence", "constraints", "output_language"]
tags: ["update-package", "repository-boundary", "rollback", "routing"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# Updatepaket und Ziel-Repository prüfen
## Zweck

Prüfe das Updatepaket **{{project_name}}** vor dem Einspielen in **{{repository_url}}**.

## Eingaben

- Paketmanifest, Dateibaum und Anwendungshinweise: {{source_material}}
- Prüfsummen und bisherige Validierung: {{evidence}}
- Randbedingungen: {{constraints}}

## Arbeitsauftrag

1. Bestimme das exakte kanonische Ziel-Repository.
2. Prüfe Marker, Remote und Repository-Identität.
3. Unterscheide neue, ersetzte und zu löschende Dateien.
4. Bewerte, ob reines ZIP-Entpacken ausreicht oder ein Skript/Patch nötig ist.
5. Nenne mögliche Überschreibungen und Fremdprojekt-Marker.
6. Definiere Vorher-/Nachher-Prüfungen und genaue Rollback-Schritte.
7. Trenne statische Paketprüfung von Build, Test, CI und Laufzeit.

## Qualitätsregeln

- Anwendung ablehnen, wenn das Ziel nicht eindeutig belegt ist.
- ZIP-Extraktion kann committed Dateien nicht löschen.
- Keine Erfolgsaussage aus Test- oder Workflowquellcode ableiten.
- Prüfsumme, Zielpfad und Baseline müssen zusammenpassen.

## Ausgabeformat

Liefere in {{output_language}}: Zielentscheidung, Dateioperationen, Risiken, sichere Anwendungsschritte, Validierungsbefehle, Rollback und offene Nachweise.
