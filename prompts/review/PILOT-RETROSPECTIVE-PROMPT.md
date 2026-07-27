---
prompt-id: "SASD-PROMPT-REVIEW-008"
title: "Pilotretrospektive durchführen"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "review"
language: "de"
summary: "Bewertet Zielprojekt und Standard getrennt und leitet konkrete Verbesserungen ab."
variables: ["project_name", "pilot_wave_plan", "evidence", "current_state", "constraints", "output_language"]
tags: ["pilot", "retrospective", "lessons-learned", "standard-change"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# Pilotretrospektive durchführen
## Zweck

Bewerte die abgeschlossene Pilotwelle von **{{project_name}}** aus Projekt- und Standardsicht.

## Eingaben

- Wellenplan: {{pilot_wave_plan}}
- Nachweise: {{evidence}}
- Ergebniszustand: {{current_state}}
- Randbedingungen und Aufwand: {{constraints}}

## Arbeitsauftrag

1. Bewerte Stabilität, Wartbarkeit, Sicherheit, Tests, Dokumentation und Aufwand im Zielprojekt.
2. Bewerte Verständlichkeit, Proportionalität, Doppelungen, fehlende Regeln und Hilfsmittel des Standards.
3. Trenne nachgewiesene Ergebnisse, offene Punkte, Ausnahmen und Änderungsvorschläge.
4. Prüfe ausdrücklich, ob Overengineering vermieden wurde.
5. Leite konkrete Änderungen an Regeln, Vorlagen, Checklisten oder Prompts ab.

## Qualitätsregeln

- Keine positive Retrospektive ohne Abgleich mit Akzeptanzkriterien.
- Aufwand und Nutzen getrennt bewerten.
- Ein lokales Projektproblem nicht vorschnell zur allgemeinen Standardregel machen.
- Änderungsvorschläge benötigen Beispiel, Wirkung und Rückwärtskompatibilität.

## Ausgabeformat

Erzeuge in {{output_language}}: Projektergebnis, Standardfeedback, bewährte Praktiken, Probleme, Overengineering-Bewertung, Änderungsvorschläge und nächste Pilotmaßnahmen.
