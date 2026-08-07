---
title: "Pilotprogramm für Version 1.0"
document-id: SASD-REF-PILOT-001
document-type: informative
status: Proposed
version: 0.12.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-08-07
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-FND-002, SASD-GOV-007, SASD-PROC-002, SASD-PROC-004, SASD-PROC-005]
---

# Pilotprogramm für Version 1.0

## 1. Zweck

Das Pilotprogramm prüft, ob Core Standard, Profile, Prozesse, Vorlagen und Tooling an realen Projekten verständlich, proportional und praktisch anwendbar sind. Es soll nicht nur bestätigen, dass Dokumente vollständig wirken, sondern konkrete Reibung, Doppelarbeit und fehlende Regeln sichtbar machen.

## 2. Pilotportfolio für Version 1.0

| Pilot | Größenklasse | Repräsentierter Projekttyp | Ziel |
|---|---|---|---|
| Pilot 01 – SASD TaskHost Local | Small | kleines lokales WinForms-/SQLite-Werkzeug | Pragmatismus und Vermeidung von Overengineering |
| Pilot 02 – SASD Prompt Manager | Medium | langfristig gepflegte geschichtete Desktopanwendung | vollständige Recommended-Anwendung mit fachlicher Breite |
| Pilot 03 – SASD Mail Workbench | Large / Complex | modulare, persistente und erweiterbare C#/.NET-Plattform | Abhängigkeiten, Security, Recovery und umfangreiche Nachweise |

Die drei Piloten bilden die in `SASD-FND-007` verlangten Größenklassen ab. Eine Baseline-Bewertung erfüllt die Kategorie „bewertet“, ist aber keine Aussage, dass das Projekt gebaut, migriert oder technisch verifiziert wurde.

## 3. Pilotlebenszyklus

```text
Candidate
  -> Selected
  -> Baseline Assessed
  -> Wave Planned
  -> In Execution
  -> Wave Validated
  -> Pilot Closed
```

Ein Pilot darf mehrere Migrationswellen besitzen. Der Lebenszyklusstatus bezieht sich auf den Gesamtfortschritt. Zusätzlich werden Umsetzungs- und Verifikationszustand getrennt erfasst.

## 4. Umsetzungs- und Verifikationszustände

| Dimension | Zustand | Bedeutung |
|---|---|---|
| Umsetzung | `Not Started` | Baseline und Maßnahmen sind dokumentiert; im Ziel-Repository wurde noch keine Änderung vorbereitet. |
| Umsetzung | `Artifact Prepared` | Patch, Overlay oder Commit-Inhalt wurde erstellt und statisch geprüft, aber noch nicht als Zielstand nachgewiesen. |
| Umsetzung | `Committed` | Änderungen sind einem unveränderlichen Ziel-Commit zugeordnet. |
| Umsetzung | `Verified` | der committed Zielstand wurde mit den vorgesehenen Befehlen und Laufzeittests geprüft. |
| Verifikation | `Pending` | erforderliche Nachweise fehlen. |
| Verifikation | `Partial` | ein Teil der Nachweise liegt vor; Freigabekriterien sind noch offen. |
| Verifikation | `Passed` | alle definierten Akzeptanzkriterien sind nachgewiesen. |
| Verifikation | `Failed` | mindestens ein Blocker oder Akzeptanzkriterium ist fehlgeschlagen. |

`Baseline Assessed` und `Not Started` dürfen gemeinsam verwendet werden: Das Projekt wurde dann bewertet, aber noch nicht verändert. `Artifact Prepared` ist kein Synonym für „implementiert“, „behoben“, „baubar“ oder „lauffähig“.

## 5. Mindestartefakte

Jeder Pilot enthält mindestens:

- Pilot Charter,
- Projektklassifikation,
- Baseline Assessment,
- Gap Register,
- Migrationsplan,
- mindestens einen detaillierten Wellenplan,
- Evidenzzuordnung,
- Entscheidungslog,
- Pilotreview,
- initiale oder abschließende Lessons Learned.

Für vorbereitete oder committed Änderungen kommen Implementierungsreview, Verifikationsplan und Verifikationsrecord hinzu.

## 6. Auswahlkriterien

Ein Projekt eignet sich besonders, wenn:

- ein realer Wartungs- oder Nutzungsbedarf besteht,
- Scope und Risiken überschaubar genug für einen Pilotdurchlauf sind,
- vorhandene Stärken und Schwächen sichtbar sind,
- Änderungen in kleinen Wellen möglich sind,
- das Projekt typische SASD-Entscheidungen repräsentiert,
- Ergebnisse öffentlich oder intern nachvollziehbar dokumentiert werden können.

## 7. Grundsätze

- Der Pilot darf funktionierende Software nicht für kosmetische Einheitlichkeit gefährden.
- Strukturänderungen benötigen einen konkreten Nutzen.
- Nicht geprüfte Behauptungen werden als unbestätigt gekennzeichnet.
- Ein öffentlicher Repository-Snapshot ersetzt keinen lokalen Build- und Laufzeittest.
- Eine Baseline-Bewertung belegt Auswahl und Analyse, nicht technische Funktionsfähigkeit.
- Ein erzeugtes ZIP, Patchset oder Overlay belegt seinen Inhalt, nicht dessen erfolgreiche Integration.
- Ein historischer Fehler darf nicht als behoben bezeichnet werden, wenn er weder reproduziert noch durch einen passenden Regressionstest eindeutig abgedeckt wurde.
- Vorbereitete CI-Konfiguration belegt keinen erfolgreichen CI-Lauf.
- Profile dürfen abhängig vom Projektstand nur teilweise anwendbar sein; diese Begrenzung muss sichtbar sein.
- Pilotfeedback darf zu Änderungen am Standard führen.
- Reibung wird zunächst beobachtet und gebündelt; nicht jede einzelne Irritation rechtfertigt eine spontane Normänderung.

## 8. Verifikationsgate zwischen Wellen

Eine Folgewelle mit neuen Produkt- oder Architekturänderungen SOLLTE erst beginnen, wenn die vorherige Welle mindestens:

1. einem Ziel-Commit zugeordnet,
2. gebaut und getestet,
3. in der vorgesehenen Laufzeitumgebung geprüft,
4. hinsichtlich Datenmigration und Rückfallweg bewertet,
5. im Gap Register und Evidenzmodell aktualisiert wurde.

## 9. Usability- und Reibungsbeobachtung

Die Piloten prüfen nicht nur technische Konformität und Evidenz, sondern auch, wie sich SASD in echter Produktarbeit anfühlt. Diese Beobachtung ist eine eigene Sicht und verändert den Umsetzungs- oder Verifikationsstatus eines Piloten nicht.

Nach Möglichkeit werden pro Pilot oder Welle leichtgewichtig erfasst:

- Zeit bis zur ersten produktiven Produktarbeit,
- initialer SASD-Zusatz- und Dokumentationsaufwand,
- unnötige Doppelpflege,
- häufiges Nachschlagen und Schwierigkeiten beim Finden der richtigen Vorgabe,
- Regeln, Vorlagen oder Checklisten mit erkennbarem Nutzen,
- Tooling- und Quality-Gate-Reibung,
- konkrete Fehler oder Fehlentscheidungen, die SASD verhindert oder früher sichtbar gemacht hat,
- Aufwand für Build, Tests und Releases im Verhältnis zum Projektrisiko.

Dafür steht die [Pilot Friction Log Vorlage](../../templates/documents/PILOT-FRICTION-LOG-TEMPLATE.md) zur Verfügung. Sie ist bewusst kein neues Pflichtartefakt: gleichwertige Notizen sind ausreichend, sofern die Beobachtungen später in Retrospektive, Feedback oder Gap-Bewertung nachvollziehbar zusammengeführt werden können.

Einzelne Reibungsmomente werden nicht sofort durch Standardänderungen beantwortet. Wiederkehrende Beobachtungen werden nach der Welle gebündelt und mindestens als Standardfehler, Klarstellungsbedarf, projektspezifische Ausnahme, zukünftige Verbesserung oder verworfenes Feedback klassifiziert.

## 10. Ergebnisse für den Standard

Nach jeder Baseline und jeder Welle wird bewertet:

1. Welche Regeln waren eindeutig und hilfreich?
2. Welche Regeln waren zu streng, zu schwach oder doppelt?
3. Welche Vorlagen haben Zeit gespart?
4. Welche Nachweise fehlten?
5. Welche Regeln sollten geändert, verschoben oder ergänzt werden?
6. War die gewählte Qualitätsstufe angemessen?
7. Wurde unnötige Architektur vermieden?
8. Wurden Beobachtung, Artefakt, Commit und Verifikation klar getrennt?
9. Wo entstand messbare oder wiederkehrende Reibung?
10. Welchen konkreten Aufwand hat SASD reduziert oder welchen Fehler verhindert?
