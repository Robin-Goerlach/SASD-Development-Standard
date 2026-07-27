---
prompt-id: "SASD-PROMPT-RESEARCH-001"
title: "Bestehende Lösungen analysieren"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "research"
language: "de"
summary: "Analysiert vergleichbare Produkte und trennt Funktionsideen von belastbaren Anforderungen."
variables: ["project_name", "project_description", "target_users", "constraints", "source_material", "output_language"]
tags: ["research", "competition", "feature-analysis", "market"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# Bestehende Lösungen analysieren
## Zweck

Analysiere bestehende Lösungen, die für **{{project_name}}** relevant sind.

## Eingaben

- Projektidee: {{project_description}}
- Zielgruppen: {{target_users}}
- Randbedingungen: {{constraints}}
- bekannte Quellen oder Produkte: {{source_material}}

## Arbeitsauftrag

1. Identifiziere direkte, indirekte und nichtsoftwarebasierte Alternativen.
2. Vergleiche Zielgruppe, Kernnutzen, Funktionsumfang, Betriebsmodell, Datenhaltung, Erweiterbarkeit, Sicherheit, Lizenz und Kostenmodell.
3. Trenne beobachtete Funktionen von Marketingaussagen und eigenen Schlussfolgerungen.
4. Leite Chancen, Risiken und bewusst nicht zu übernehmende Komplexität ab.
5. Erzeuge keine Kopie fremder Produkte, sondern begründete Produktentscheidungen.

## Qualitätsregeln

- Nutze aktuelle Primärquellen, sofern Recherche erlaubt ist.
- Zitiere belastbare Aussagen.
- Kennzeichne unbestätigte oder zeitabhängige Informationen.
- Bewerte Funktionen nach Nutzerproblem und Wartungsaufwand, nicht nach Anzahl.

## Ausgabeformat

Erzeuge in {{output_language}} eine Vergleichsmatrix, Kernmuster, Differenzierungsmöglichkeiten, Funktionskandidaten, Anti-Features, Risiken und empfohlene Validierungsschritte.
