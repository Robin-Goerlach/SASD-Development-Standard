---
prompt-id: "SASD-PROMPT-REVIEW-005"
title: "Legacy-Projekt für SASD-Migration prüfen"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "review"
language: "de"
summary: "Plant eine schrittweise, risikoarme Migration eines bestehenden Projekts."
variables: ["project_name", "repository_url", "current_state", "target_state", "evidence", "constraints", "quality_level", "profiles", "output_language"]
tags: ["legacy", "migration", "stabilization", "waves"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# Legacy-Projekt für SASD-Migration prüfen
## Zweck

Prüfe **{{project_name}}** auf eine schrittweise Migration zum SASD Development Standard.

## Eingaben

- Repository: {{repository_url}}
- Ist-Zustand: {{current_state}}
- Zielzustand: {{target_state}}
- Nachweise: {{evidence}}
- Randbedingungen: {{constraints}}
- Qualitätsstufe und Profile: {{quality_level}} / {{profiles}}

## Arbeitsauftrag

Priorisiere: Sicherung und reproduzierbaren Ist-Zustand, Secrets und kritische Risiken, Build/Start/Charakterisierungstests, Nutzer/Daten/Integrationen, risikobasierte Standardabweichungen, kleine reversible Wellen und erst danach strukturelle Modernisierung.

## Qualitätsregeln

- Keine pauschale Neuentwicklung empfehlen.
- Trenne sofortige Stabilisierung, verpflichtende Lücken, sinnvolle Verbesserungen, Aufschub, nicht anwendbar und Ausnahme.
- Funktionsfähigkeit vor kosmetischer Vereinheitlichung.
- Jede Welle benötigt Rollback und Abschlusskriterien.

## Ausgabeformat

Liefere in {{output_language}}: Assessment, Prioritäten, Gap Register, Migrationswellen, Risiken, Rollback, Nachweise, Stop-Kriterien und nächste Entscheidung.
