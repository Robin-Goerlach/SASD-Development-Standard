---
prompt-id: "SASD-PROMPT-REVIEW-009"
title: "Foundation und Governance prüfen"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "review"
language: "de"
summary: "Prüft Vision, Scope, Dokumentlebenszyklus, Versionierung, Ausnahmen und Freigabereife."
variables: ["standard_version", "source_material", "evidence", "constraints", "output_language"]
tags: ["governance", "foundation", "approval", "versioning"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core"]
last-reviewed: "2026-07-25"
---

# Foundation und Governance prüfen
## Zweck

Prüfe Foundation und Governance des SASD Development Standard **{{standard_version}}** als vorsichtiger Maintainer.

## Eingaben

- zu prüfende Dokumente: {{source_material}}
- vorhandene Review- und Validierungsnachweise: {{evidence}}
- Randbedingungen und geplanter Freigabeumfang: {{constraints}}

## Arbeitsauftrag

1. Prüfe Vision, Scope, Zielgruppen und Leitprinzipien.
2. Identifiziere Konflikte zwischen Prinzipien und normativen Regeln.
3. Prüfe Dokumenteigentümer, Abhängigkeiten, IDs und Vorrangregeln.
4. Bewerte normative Sprache, Testbarkeit und Nachweisbarkeit.
5. Prüfe Lebenszyklus, Approval, Versionierung, Änderungen und Ausnahmen.
6. Bewerte Alignment-Semantik und Praktikabilität für Einzelentwickler.
7. Trenne Reviewreife, Maintainer-Freigabe, CI-Verifikation und Veröffentlichung.

## Qualitätsregeln

- Vollständigkeit oder maschinelle Validität allein rechtfertigt kein Approved.
- Historische Freigabemanifeste dürfen nicht stillschweigend verändert werden.
- Blocker, Major, Minor und Observation getrennt klassifizieren.
- Fehlende externe Evidenz offen lassen.

## Ausgabeformat

Liefere in {{output_language}}: Scope, Blocker, Major/Minor Findings, Abhängigkeitsbefunde, Proportionalität, Freigabeempfehlung und benötigte Nachweise.
