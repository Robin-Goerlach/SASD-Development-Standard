---
prompt-id: "SASD-PROMPT-DEBUG-003"
title: "Laufzeitvorfall reproduzieren"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "debugging"
language: "de"
summary: "Plant eine sichere Reproduktion eines Laufzeitfehlers mit Daten-, Umgebungs- und Rollbackschutz."
variables: ["project_name", "issue_description", "environment", "logs_and_errors", "security_context", "reproduction_steps", "output_language"]
tags: ["runtime", "incident", "recovery", "diagnostics"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core", ".NET", "Desktop"]
last-reviewed: "2026-07-25"
---

# Laufzeitvorfall reproduzieren
## Zweck

Plane eine sichere Reproduktion des Laufzeitvorfalls in **{{project_name}}**.

## Eingaben

- Vorfall: {{issue_description}}
- Umgebung: {{environment}}
- Logs: {{logs_and_errors}}
- Schutzbedarf: {{security_context}}
- bekannte Schritte: {{reproduction_steps}}

## Arbeitsauftrag

1. Erhalte Originaldaten und Beweise unverändert.
2. Erstelle eine anonymisierte oder synthetische Reproduktionsumgebung.
3. Dokumentiere Versionen, Konfiguration, Datenzustand und Zeitablauf.
4. Definiere Beobachtungspunkte, Logs und Abbruchbedingungen.
5. Prüfe frische Daten, bestehende Daten, Fehlerpfad und Wiederherstellung.
6. Leite nach erfolgreicher Reproduktion Charakterisierungs- und Regressionstests ab.

## Qualitätsregeln

- Keine sensiblen Produktivdaten in unsichere Umgebungen kopieren.
- Keine Wiederherstellungsbehauptung ohne Restore-Test.
- Logausgaben vor Weitergabe auf Secrets und personenbezogene Daten prüfen.
- Den ursprünglichen Vorfall und eine nur ähnliche Beobachtung unterscheiden.

## Ausgabeformat

Liefere in {{output_language}}: Sicherheitsvorkehrungen, Reproduktionsmatrix, Datensätze, Schritte, Beobachtungen, Abbruchregeln, Beweissicherung, Tests und Abschlusskriterien.
