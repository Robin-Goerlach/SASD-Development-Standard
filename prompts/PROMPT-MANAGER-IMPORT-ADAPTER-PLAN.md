---
title: "Importadapter-Plan für den SASD Prompt Manager"
document-id: SASD-REF-PROMPT-005
document-type: informative
status: Draft
version: 0.13.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-25
applies-to-quality-levels: [Recommended, Production]
applies-to-profiles: [Core]
depends-on: [SASD-REF-PROMPT-001, SASD-REF-PROMPT-003, SASD-REF-PROMPT-004]
---

# Importadapter-Plan für den SASD Prompt Manager

## Zweck

Dieses Dokument beschreibt den kontrollierten Übergang vom kanonischen SASD-Promptpaket zu einem konkreten Importformat des SASD Prompt Managers. Es behauptet keine Kompatibilität mit einer nicht geprüften Anwendungsversion.

## Ausgangsregel

Das Paketformat `sasd-prompt-package/1.0` ist die hersteller- und persistenzunabhängige Source of Truth. Ein Adapter darf erst als kompatibel bezeichnet werden, wenn er gegen eine exakte Prompt-Manager-Version oder Commit-SHA implementiert und per Import-/Export-Roundtrip geprüft wurde.

## Erforderliche Adapterinformationen

Ein Adapter muss dokumentieren:

- Prompt-Manager-Version und Commit-SHA,
- unterstützte Paketformatversion,
- Zuordnung von Prompt-ID, Titel, Version, Status, Text, Kategorie, Tags und Variablen,
- Umgang mit unbekannten oder nicht unterstützten Feldern,
- Konfliktstrategie bei bereits vorhandenen IDs,
- Merge-, Replace-, Skip- und Dry-run-Verhalten,
- Transaktions- oder Rollbackverhalten,
- Protokollierung ohne Secrets,
- Import- und Exportgrenzen.

## Vorgesehener Ablauf

1. Exakten Prompt-Manager-Quellstand sichern und dessen Import-/Exportmodell dokumentieren.
2. Feldzuordnung mit der Import-Mapping-Vorlage erstellen.
3. Adapter zunächst nur als Dry-run implementieren.
4. Validierung vor jeder Schreiboperation durchführen.
5. Import in einer isolierten Testdatenbank ausführen.
6. Erneut exportieren und semantisch mit dem Quellpaket vergleichen.
7. Konflikt-, Wiederholungs-, Abbruch- und Backupfälle testen.
8. Kompatibilität nur für den tatsächlich geprüften Versionsbereich freigeben.

## Mindestakzeptanzkriterien

- Alle 39 Prompt-IDs bleiben unverändert erhalten.
- Prompttexte werden verlustfrei und in UTF-8 übertragen.
- Alle 35 Variablen werden mit Pflicht-, Default- und Sensitive-Eigenschaften abgebildet oder eine Abweichung wird blockierend gemeldet.
- Kategorien, Tags, Profile, Qualitätsstufen und Status werden nachvollziehbar übertragen.
- Ein zweiter Import ist idempotent oder erzeugt einen kontrollierten Konfliktbericht.
- Ein Export nach dem Import lässt sich semantisch gegen das Ausgangspaket vergleichen.
- Vor Schreiboperationen existieren Backup und Dry-run-Bericht.
- Konkrete Secrets oder Testzugangsdaten erscheinen weder in Paket noch Log.

## Freigabegrenze

Solange diese Kriterien nicht für eine konkrete Anwendungsversion nachgewiesen sind, bleibt in `manifest.json`:

```json
"prompt_manager_direct_import": false
```
