---
prompt-id: "SASD-PROMPT-DEBUG-002"
title: "Buildfehler analysieren"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "debugging"
language: "de"
summary: "Analysiert Restore-, Compiler-, Analyzer-, Test- und Packagingfehler reproduzierbar."
variables: ["project_name", "repository_tree", "logs_and_errors", "environment", "constraints", "source_material", "output_language"]
tags: ["build", "restore", "compiler", "ci"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: [".NET"]
last-reviewed: "2026-07-25"
---

# Buildfehler analysieren
## Zweck

Analysiere den Buildfehler von **{{project_name}}**.

## Eingaben

- Repository-Struktur: {{repository_tree}}
- vollständige Buildausgabe: {{logs_and_errors}}
- Umgebung und SDKs: {{environment}}
- Randbedingungen: {{constraints}}
- relevante Projektdateien: {{source_material}}

## Arbeitsauftrag

1. Identifiziere den ersten ursächlichen Fehler, nicht nur Folgefehler.
2. Trenne Restore, SDK-Auswahl, Projektkonfiguration, Compiler, Analyzer, Tests und Packaging.
3. Prüfe `global.json`, Target Frameworks, Paketquellen, zentrale Paketversionen und Plattformabhängigkeiten.
4. Vergleiche lokalen und CI-Kontext.
5. Formuliere minimale Korrekturen und Verifikationsbefehle.
6. Benenne Warnungen, die später zu Fehlern eskalieren können.

## Qualitätsregeln

- Keine Paket- oder SDK-Version raten, wenn aktuelle Primärquellen erforderlich sind.
- Keine Warnungen global deaktivieren, um Symptome zu verbergen.
- Buildartefakte und Caches nur kontrolliert löschen.
- Reproduzierbarkeit vor Optimierung.

## Ausgabeformat

Erzeuge in {{output_language}}: Fehlerkette, Ursache, betroffene Dateien, minimalen Patchplan, Befehle, erwartete Ergebnisse, CI-Auswirkungen und Restunsicherheit.
