---
title: "Pilotprogramm für Version 1.0"
document-id: SASD-REF-PILOT-001
document-type: informative
status: Proposed
version: 0.8.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-FND-002, SASD-GOV-007, SASD-PROC-002, SASD-PROC-004, SASD-PROC-005]
---

# Pilotprogramm für Version 1.0

## 1. Zweck

Das Pilotprogramm prüft, ob Core Standard, Profile, Prozesse, Vorlagen und Tooling an realen Projekten verständlich, proportional und praktisch anwendbar sind. Es soll nicht nur bestätigen, dass Dokumente vollständig wirken, sondern konkrete Reibung, Doppelarbeit und fehlende Regeln sichtbar machen.

## 2. Pilotkategorien

| Kategorie | Zweck | Erwartete Beispieleigenschaften |
|---|---|---|
| Kleines Projekt | Prüft Pragmatismus und Vermeidung von Overengineering | ein Produktprojekt, begrenzter Scope, lokale Nutzung |
| Mittleres Projekt | Prüft vollständige Recommended-Anwendung | mehrere fachliche Bereiche, aktive Pflege, Tests und Releases |
| Komplexeres Projekt | Prüft Abhängigkeiten, Schichten und umfangreiche Nachweise | mehrere Projekte/Module, Persistenz, Erweiterbarkeit, höhere Risiken |

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
| Umsetzung | `Not Started` | keine Zieländerung vorbereitet |
| Umsetzung | `Artifact Prepared` | Patch, Overlay oder Commit-Inhalt wurde erstellt und statisch geprüft, aber noch nicht als Zielstand nachgewiesen |
| Umsetzung | `Committed` | Änderungen sind einem unveränderlichen Ziel-Commit zugeordnet |
| Umsetzung | `Verified` | der committed Zielstand wurde mit den vorgesehenen Befehlen und Laufzeittests geprüft |
| Verifikation | `Pending` | erforderliche Nachweise fehlen |
| Verifikation | `Partial` | ein Teil der Nachweise liegt vor; Freigabekriterien sind noch offen |
| Verifikation | `Passed` | alle definierten Akzeptanzkriterien sind nachgewiesen |
| Verifikation | `Failed` | mindestens ein Blocker oder Akzeptanzkriterium ist fehlgeschlagen |

`Artifact Prepared` ist kein Synonym für „implementiert“, „behoben“, „baubar“ oder „lauffähig“. Diese Aussagen benötigen mindestens einen identifizierten Ziel-Commit und passende Verifikation.

## 5. Mindestartefakte

Jeder Pilot enthält:

- Pilot Charter,
- Projektklassifikation,
- Baseline Assessment,
- Gap Register,
- Migrationsplan,
- mindestens einen detaillierten Wellenplan,
- Evidenzzuordnung,
- Entscheidungslog,
- Implementierungsreview für vorbereitete oder committed Änderungen,
- Verifikationsplan und Verifikationsrecord,
- Wellen- oder Pilotreview,
- Standardfeedback,
- Retrospektive nach Abschluss.

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
- Ein erzeugtes ZIP, Patchset oder Overlay belegt seinen Inhalt, nicht dessen erfolgreiche Integration.
- Ein historischer Fehler darf nicht als behoben bezeichnet werden, wenn er weder reproduziert noch durch einen passenden Regressionstest eindeutig abgedeckt wurde.
- Vorbereitete CI-Konfiguration belegt keinen erfolgreichen CI-Lauf.
- Pilotfeedback darf zu Änderungen am Standard führen.
- Eine Pilotbewertung gegen Proposed-Dokumente ist Pilot Alignment, keine formale Compliance-Aussage.

## 8. Verifikationsgate zwischen Wellen

Eine Folgewelle mit neuen Produkt- oder Architekturänderungen SOLLTE erst beginnen, wenn die vorherige Welle mindestens:

1. einem Ziel-Commit zugeordnet,
2. gebaut und getestet,
3. in der vorgesehenen Laufzeitumgebung geprüft,
4. hinsichtlich Datenmigration und Rückfallweg bewertet,
5. im Gap Register und Evidenzmodell aktualisiert wurde.

Abweichungen von diesem Gate müssen Risiko, Begründung und Rückfallstrategie nennen.

## 9. Ergebnisse für den Standard

Nach jeder Welle wird bewertet:

1. Welche Regeln waren eindeutig und hilfreich?
2. Welche Regeln waren zu streng, zu schwach oder doppelt?
3. Welche Vorlagen haben Zeit gespart?
4. Welche Nachweise fehlten?
5. Welche Regeln sollten geändert, verschoben oder ergänzt werden?
6. War die gewählte Qualitätsstufe angemessen?
7. Wurde unnötige Architektur vermieden?
8. Wurden vorbereitete Artefakte klar von verifizierten Zielzuständen getrennt?
