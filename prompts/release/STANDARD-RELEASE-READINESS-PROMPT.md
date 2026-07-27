---
prompt-id: "SASD-PROMPT-RELEASE-002"
title: "Standardrelease bewerten"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "release"
language: "de"
summary: "Bewertet ein SASD-Standardrelease gegen Freigaben, Tags, Validatoren, Piloten und Publikationsartefakte."
variables: ["standard_version", "repository_url", "release_version", "evidence", "source_material", "output_language"]
tags: ["standard-release", "governance", "approval", "publication"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# Standardrelease bewerten
## Zweck

Bewerte das geplante SASD Development Standard Release **{{release_version}}**.

## Eingaben

- Standardversion: {{standard_version}}
- Repository: {{repository_url}}
- Freigabe- und CI-Nachweise: {{evidence}}
- Releaseunterlagen und Artefakte: {{source_material}}

## Arbeitsauftrag

Verlange Evidenz für Approved normative Dokumente und Approval Records, unveränderlichen Tag und Commit, erfolgreiche Validatoren aus sauberem Checkout, aktuelle generierte Indizes, Pilot- und Kompatibilitätsnachweise, Known Issues und Ausnahmen, Release Notes, Changelog, Publikationsartefakte und Prüfsummen.

## Qualitätsregeln

- Vorbereitung, Approval, CI, Tag und Veröffentlichung getrennt bewerten.
- Keine stabile Freigabe bei offenen blockierenden Akzeptanzkriterien.
- Historische Freigabemanifeste nicht durch aktuelle Dateien ersetzen.
- Befristete Entscheidungen mit Ablauf und Wirkung sichtbar machen.

## Ausgabeformat

Erzeuge in {{output_language}}: Ready / Conditionally Ready / Not Ready, Blocker, Major Findings, fehlende Evidenz, Ausnahmen und exakte Behebungsschritte.
