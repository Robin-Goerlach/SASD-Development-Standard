---
prompt-id: "SASD-PROMPT-INIT-001"
title: "SASD-Projektinitialisierung"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "project-initiation"
language: "de"
summary: "Initialisiert ein neues technisches Projekt mit Vision, Scope, Klassifikation, Risiken und erstem Milestone."
variables: ["project_name", "project_description", "project_context", "target_users", "stakeholders", "goals", "constraints", "non_goals", "quality_level", "profiles", "output_language"]
tags: ["project-initiation", "scope", "roadmap", "risk"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# SASD-Projektinitialisierung
## Zweck

Initialisiere **{{project_name}}** als nachvollziehbares Projekt nach dem SASD Development Standard.

## Eingaben

- Projektbeschreibung: {{project_description}}
- Kontext: {{project_context}}
- Zielgruppen: {{target_users}}
- Stakeholder: {{stakeholders}}
- Ziele: {{goals}}
- Randbedingungen: {{constraints}}
- bekannte Nicht-Ziele: {{non_goals}}
- vorläufige Qualitätsstufe: {{quality_level}}
- vorläufige Profile: {{profiles}}

## Arbeitsauftrag

1. Formuliere Problem, Produktvision und erwarteten Nutzen.
2. Trenne Ziele, messbare Ergebnisse, Scope und Nicht-Ziele.
3. Klassifiziere Größe, Lebensdauer, Risiken, Qualitätsstufe und Profile.
4. Benenne Annahmen, offene Fragen, Abhängigkeiten und Entscheidungsbedarf.
5. Leite die erforderlichen Startdokumente und die angemessene Repository-Struktur ab.
6. Skizziere eine proportionale Anfangsarchitektur ohne unnötige Schichten oder Frameworks.
7. Definiere einen begrenzten ersten Milestone mit Akzeptanzkriterien, Risiken und Abbruchbedingungen.

## Qualitätsregeln

- Erfinde keine geschäftlichen Fakten.
- Kennzeichne Annahmen und Unsicherheiten ausdrücklich.
- Trenne Muss-Anforderungen von Ideen und späteren Optionen.
- Bevorzuge die kleinste tragfähige Lösung.
- Berücksichtige Sicherheit, Datenschutz, Betrieb und Wiederherstellung von Anfang an.

## Ausgabeformat

Erzeuge in {{output_language}}: Executive Summary, Klassifikation, Vision, Ziele, Scope, Nicht-Ziele, Stakeholder, Risiken, Dokumentbedarf, Architekturstartpunkt, Milestone 1 und offene Entscheidungen.
