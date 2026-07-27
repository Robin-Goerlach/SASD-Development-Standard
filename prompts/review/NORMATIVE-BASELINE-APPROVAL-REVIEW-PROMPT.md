---
prompt-id: "SASD-PROMPT-REVIEW-010"
title: "Normative Baseline freigabereif prüfen"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "review"
language: "de"
summary: "Prüft ein normatives Dokumentbündel auf Vollständigkeit, Zyklen, Doppelungen und Freigabereife."
variables: ["standard_version", "source_material", "evidence", "constraints", "output_language"]
tags: ["normative-baseline", "approval", "dependencies", "consistency"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# Normative Baseline freigabereif prüfen
## Zweck

Prüfe die normative Baseline des SASD Development Standard **{{standard_version}}** als ein zusammenhängendes Freigabebündel.

## Eingaben

- enthaltene Dokumente und Anforderungen: {{source_material}}
- Review-, Pilot- und CI-Nachweise: {{evidence}}
- Freigabegrenzen und Randbedingungen: {{constraints}}

## Arbeitsauftrag

1. Prüfe Vollständigkeit und eindeutigen Freigabeumfang.
2. Identifiziere Widersprüche und doppelte Pflichten über alle Ebenen.
3. Prüfe Abhängigkeitsrichtung, Zyklen und nicht freigegebene externe Abhängigkeiten.
4. Bewerte Proportionalität für Minimum, Recommended und Production.
5. Prüfe Praktikabilität für Einzelentwickler und kleine Teams.
6. Prüfe Trennung von Core, Profilen und Prozessen.
7. Bewerte Traceability, Evidenz-, Ausnahme- und Releasefolgen.
8. Formuliere eine ausdrückliche Freigabeempfehlung.

## Qualitätsregeln

- Testcode, Workflowdateien und generierte Manifeste sind keine Ausführungsnachweise.
- Reviewabschluss, Maintainer-Approval, CI und Release bleiben getrennte Zustände.
- Kein Dokument darf durch Freigabe eines abhängigen, noch instabilen Dokuments indirekt verändert werden.

## Ausgabeformat

Erzeuge in {{output_language}}: Bündelscope, Blocker, Major/Minor Findings, Abhängigkeitsgraph, Proportionalitätsbewertung, Bedingungen und Freigabeempfehlung.
