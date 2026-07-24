---
title: "Lebenszyklus von Standarddokumenten"
document-id: SASD-GOV-002
document-type: normative
status: Proposed
version: 0.1.0
standard-version: "1.0"
language: de
authoritative: true
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-GOV-001, SASD-GOV-003, SASD-GOV-004, SASD-GOV-005]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Lebenszyklus von Standarddokumenten

## 1. Zweck

Dieses Dokument definiert die zulässigen Statuswerte, Übergänge und Freigabekriterien für Dokumente des SASD Development Standard.

## 2. Statusmodell

```text
Planned -> Draft -> Proposed -> Approved -> Deprecated -> Retired
            ^          |
            |----------|
```

### Planned

Das Dokument ist im Dokumentkatalog vorgesehen, wurde aber noch nicht fachlich ausgearbeitet. Ein Planned-Dokument enthält keine verbindlichen Anforderungen.

### Draft

Das Dokument wird aktiv erarbeitet. Struktur, Inhalt und Anforderungen können sich grundlegend ändern. Draft-Inhalte sind nicht verbindlich.

### Proposed

Das Dokument ist inhaltlich vollständig genug für eine gezielte Prüfung. Es ist ein Freigabekandidat, aber noch nicht verbindlich.

### Approved

Das Dokument ist für die angegebene Standardversion freigegeben. Nur Approved-Dokumente können verbindliche Anforderungen einer veröffentlichten Standardversion enthalten.

### Deprecated

Das Dokument oder ein wesentlicher Teil davon ist noch referenzierbar, soll aber nicht mehr für neue Projekte verwendet werden. Eine Nachfolge oder ein Migrationsweg MUSS benannt sein.

### Retired

Das Dokument ist nicht mehr Bestandteil des aktiven Standards. Es bleibt nur aus Gründen der Nachvollziehbarkeit erhalten oder wird in einen Archivbereich verschoben.

## 3. Zulässige Übergänge

| Von | Nach | Mindestbedingung |
|---|---|---|
| Planned | Draft | Zweck, Dokument-ID und Owner festgelegt |
| Draft | Proposed | vorgesehene Inhalte vollständig, Abhängigkeiten benannt, Selbstprüfung durchgeführt |
| Proposed | Approved | Review abgeschlossen, Widersprüche geklärt, Freigabekriterien erfüllt |
| Proposed | Draft | wesentliche Überarbeitung erforderlich |
| Approved | Draft | neue Hauptüberarbeitung für eine zukünftige Version; bestehende Approved-Fassung bleibt über Tag nachvollziehbar |
| Approved | Deprecated | Nachfolge oder Ablösegrund dokumentiert |
| Deprecated | Retired | aktive Standardversionen verweisen nicht mehr darauf |

Direkte Übergänge dürfen nur erfolgen, wenn keine Nachvollziehbarkeit verloren geht.

## 4. Freigabekriterien für Proposed

Ein Draft kann Proposed werden, wenn:

- Zweck und Geltungsbereich eindeutig sind,
- Metadaten vollständig sind,
- normative und informative Aussagen getrennt sind,
- Abhängigkeiten und verwandte Dokumente benannt sind,
- keine bekannten internen Widersprüche bestehen,
- offene Punkte ausdrücklich markiert sind,
- die Dokumentstruktur angemessen vollständig ist.

## 5. Freigabekriterien für Approved

Ein Proposed-Dokument kann Approved werden, wenn:

1. der Inhalt fachlich geprüft wurde,
2. alle MUSS-Anforderungen verständlich und prinzipiell prüfbar sind,
3. Auswirkungen auf andere Dokumente berücksichtigt wurden,
4. Terminologie mit dem Glossar übereinstimmt,
5. notwendige Vorlagen, Checklisten oder Nachweise vorhanden oder geplant sind,
6. wesentliche offene Punkte gelöst wurden,
7. die Freigabe im Commit, Changelog oder Release nachvollziehbar ist.

## 6. Freigabeverantwortung

Solange das Projekt durch einen einzelnen Maintainer geführt wird, kann dieselbe Person Autor, Reviewer und Freigabeverantwortlicher sein. In diesem Fall SOLLTE die Selbstprüfung mit der Dokument-Review-Checkliste nachvollziehbar erfolgen.

Bei mehreren Mitwirkenden SOLLTE mindestens eine zweite Person normative Proposed-Dokumente prüfen.

## 7. Änderungen an Approved-Dokumenten

Redaktionelle Korrekturen ohne Bedeutungsänderung können innerhalb einer Patch-Version erfolgen.

Änderungen, die Pflichten, Verbote, Geltungsbereiche oder Compliance verändern, MÜSSEN:

- über den Änderungsprozess bewertet werden,
- eine neue Dokumentversion erhalten,
- im Changelog erscheinen,
- hinsichtlich Migration und Rückwärtskompatibilität geprüft werden.

## 8. Archivierung

Retired-Dokumente SOLLTEN nicht gelöscht werden, wenn sie Teil einer veröffentlichten Standardversion waren. Git-Tags und Releases bleiben die primäre historische Referenz.
