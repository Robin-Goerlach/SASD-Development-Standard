---
title: "SASD Prompt Package Specification"
document-id: SASD-REF-PROMPT-001
document-type: informative
status: Draft
version: 0.13.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-25
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core]
depends-on: [SASD-CORE-013, SASD-GOV-003, SASD-GOV-004]
---

# SASD Prompt Package Specification

## Zweck

Die Spezifikation definiert ein portables, versionierbares Austauschformat für SASD-Prompts. Sie ist ein unterstützendes Artefakt und erweitert die freigegebene normative Baseline nicht.

## Paketstruktur

```text
prompts/packages/<package-id>/
├── manifest.json
├── catalog.json
├── categories.json
├── variables.json
├── workflow.json
├── CATALOG.md
└── README.md
```

Die Promptquellen bleiben als Markdown-Dateien in den fachlichen Kategorieordnern. Das Paket referenziert sie relativ zum Repository.

## Promptidentität

Jeder Prompt besitzt:

- eine unveränderliche `prompt-id`,
- eine semantische Promptversion,
- einen Status,
- eine Kategorie,
- deklarierte Variablen,
- Tags, Profile und Qualitätsstufen,
- eine Zusammenfassung,
- eine SHA-256-Prüfsumme im generierten Katalog.

Eine Umbenennung der Datei darf die `prompt-id` nicht verändern. Eine inhaltlich inkompatible Änderung benötigt eine neue Major-Version oder eine neue Prompt-ID.

## Variablen

Platzhalter verwenden ausschließlich die Form `{{variable_name}}`. Variablennamen bestehen aus Kleinbuchstaben, Ziffern und Unterstrichen. Jede verwendete Variable muss im Prompt-Frontmatter und in `variables.json` deklariert sein.

Sensitive Variablen kennzeichnen nur den möglichen Inhalt. Das Paket speichert niemals konkrete Secrets, Zugangsdaten oder private Nutzerdaten.

## Statusmodell

| Status | Bedeutung |
|---|---|
| Draft | in Bearbeitung; grundlegende Änderungen möglich |
| Candidate | vollständig geprüft, aber noch vor der stabilen Paketausgabe |
| Stable | für eine veröffentlichte Paketversion freigegeben |
| Deprecated | noch lesbar, aber durch einen Nachfolger ersetzt |
| Retired | nicht mehr Bestandteil aktiver Pakete |

## Kompatibilität

Das Format ist absichtlich unabhängig vom internen Persistenzmodell des SASD Prompt Managers. Ein Importadapter muss:

1. eine konkrete Prompt-Manager-Version nennen,
2. IDs, Versionen, Text, Variablen, Kategorien und Tags verlustfrei abbilden,
3. Import- und Export-Roundtrip testen,
4. Konflikt- und Mergeverhalten dokumentieren,
5. keine internen Felder erfinden.

## Deterministischer Paketbau

Der Builder verwendet stabile Pfadreihenfolge, feste ZIP-Zeitstempel, UTF-8, sichere relative Pfade und SHA-256-Prüfsummen. Ein identischer Repository-Stand muss ein bytegleiches Paket erzeugen.

## Importadapter

Der [Importadapter-Plan](PROMPT-MANAGER-IMPORT-ADAPTER-PLAN.md), die [Mapping-Vorlage](../templates/documents/PROMPT-MANAGER-IMPORT-MAPPING-TEMPLATE.md) und die [Roundtrip-Checkliste](../checklists/development/PROMPT-MANAGER-IMPORT-ROUNDTRIP-CHECKLIST.md) definieren die Voraussetzungen für eine spätere direkte Prompt-Manager-Kompatibilität.
