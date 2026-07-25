---
title: "Pilot 03 Projektklassifikation – SASD Mail Workbench"
document-id: SASD-REF-PILOT-303
document-type: informative
status: Draft
version: 0.11.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-25
applies-to-quality-levels: [Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-REF-PILOT-302, SASD-PROC-002, SASD-CORE-006]
---

# Projektklassifikation – SASD Mail Workbench

## 1. Ergebnis

| Dimension | Einstufung | Begründung |
|---|---|---|
| Projektgröße | **Large / Complex** | sechs sichtbare Produktionsprojekte, fünf Testprojekte, Persistenz, Recovery, Extension Model und umfangreiche Dokumentation |
| Lebenszyklus | **langfristiges Plattformprodukt im technischen Fundamentstadium** | aktuelle Version 0.3.1 schafft Basis vor Mailprotokollen und UI |
| Qualitätsstufe | **Recommended im aktuellen Entwicklungsstand** | noch kein produktiver Mailboxbetrieb; anspruchsvolle Build-, Test- und Security-Regeln bleiben erforderlich |
| Zielstufe vor realer Nutzung | **Production** | reale Mails, Zugangsdaten, Anhänge und personenbezogene Daten erhöhen Schutz- und Betriebsanforderungen |
| Risikoklasse | **hoch** | untrusted Inhalte, Datenschutz, Datenintegrität, potenzielle Credentials und komplexe Recovery-Fälle |
| Profile | **Core + DotNet; Desktop teilweise** | Desktopprofil wird mit fertiger UI vollständig anwendbar; Lifecycle- und Packaging-Regeln sind bereits relevant |
| Migrationsmodus | **Review und Härtung in Wellen** | Architekturgrundlage wird validiert, nicht neu erfunden |

## 2. Schutzbedarf

| Schutzziel | Bewertung | Begründung |
|---|---|---|
| Vertraulichkeit | hoch | Mailinhalte und künftige Zugangsdaten sind personenbezogen und vertraulich |
| Integrität | sehr hoch | bytegenaue Archivierung und Deduplizierung sind Kerneigenschaften |
| Verfügbarkeit | mittel bis hoch | lokale Analyse und Wiederanlauf müssen zuverlässig funktionieren |
| Wiederherstellbarkeit | sehr hoch | Staging, Katalog und Roharchive müssen konsistent rekonstruierbar sein |

## 3. Profilanwendbarkeit

Das Desktopprofil ist derzeit nur teilweise anwendbar, weil die README den sichtbaren Stand ausdrücklich als technische Grundlage ohne fertige GUI beschreibt. UI-spezifische Anforderungen werden nicht als Lücke bewertet, solange sie einem späteren Meilenstein zugeordnet sind.
