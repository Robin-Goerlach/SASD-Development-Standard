---
title: "Pilot 01 Vorbereitungsreview – SASD TaskHost Local"
document-id: SASD-REF-PILOT-110
document-type: informative
status: Draft
version: 0.7.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-REF-PILOT-107, SASD-PROC-004]
---

# Pilot 01 Vorbereitungsreview – SASD TaskHost Local

## 1. Reviewumfang

Dieses Review bewertet die Pilotvorbereitung, nicht die technische Ausführung. Die Ziel-Repository-Änderungen, Buildläufe und Tests stehen noch aus.

## 2. Ergebnis

```text
Pilotstatus: Wave 01 vorbereitet
Reviewstatus: Ready for execution with known unknowns
Formale Alignment-Aussage: nicht möglich
Technische Abschlussaussage: nicht möglich
```

## 3. Positive Befunde

- Der Pilot besitzt einen klar begrenzten Scope.
- Blocker, Major-Gaps und spätere Verbesserungen sind getrennt.
- Die bestehende einfache Architektur wird nicht pauschal verworfen.
- Die erste Welle verbindet Fehlerbehebung mit Regressionstest.
- Evidenzklassen verhindern Scheingenauigkeit.
- Daten- und Rückfallrisiken werden vor kosmetischen Änderungen behandelt.

## 4. Offene Reviewpunkte vor Ausführung

- tatsächliche lokale SDK-Version,
- genauer SQL-Fehler und betroffene Datenbankzustände,
- vorhandene ADR-Inhalte,
- aktueller Paket- und Schwachstellenstand,
- konkrete Lizenzentscheidung,
- Verfügbarkeit einer anonymisierten oder frisch erzeugten Testdatenbank.

## 5. Feedback an den Standard aus der Vorbereitung

1. Die Trennung von Projektgröße und Qualitätsstufe ist für diesen Piloten notwendig und verständlich.
2. Der Standard muss ausdrücklich erlauben, dass ein Small-Projekt nicht unter `src/` verschoben und nicht in mehrere Assemblies zerlegt wird.
3. Pilotbewertungen benötigen eine verbindliche Evidenzsprache; diese wurde mit dem Pilot-Evidenzmodell ergänzt.
4. Ein Referenzpilot braucht einen maschinenlesbaren Status, damit Portfolio und Tooling später automatisiert werden können.
5. Die Definition einer Referenzimplementierung muss technische Ausführung verlangen; Dokumentplanung allein reicht nicht.

## 6. Reviewentscheidung

**Go für Wave 01**, sofern vor Codeänderungen eine lokale Baseline und Datensicherung erstellt werden. Nach Ausführung ist dieses Dokument durch ein Wellenreview mit tatsächlichen Befunden zu ergänzen.
