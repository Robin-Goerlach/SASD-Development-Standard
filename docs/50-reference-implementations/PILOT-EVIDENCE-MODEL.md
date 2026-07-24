---
title: "Evidenzmodell für Pilotbewertungen"
document-id: SASD-REF-PILOT-002
document-type: informative
status: Proposed
version: 0.7.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-CORE-004, SASD-CORE-007, SASD-GOV-007, SASD-PROC-004]
---

# Evidenzmodell für Pilotbewertungen

## 1. Zweck

Pilotbewertungen müssen zwischen direkt geprüften Tatsachen, öffentlich beobachtbaren Merkmalen, Projektaussagen und Annahmen unterscheiden. Dieses Modell verhindert, dass eine Repository-Übersicht fälschlich als vollständiger technischer Audit dargestellt wird.

## 2. Evidenzklassen

| Code | Klasse | Bedeutung | Typisches Beispiel |
|---|---|---|---|
| `V` | Verified locally | lokal gebaut, ausgeführt, getestet oder direkt inspiziert | erfolgreicher `dotnet test`-Lauf |
| `O` | Observed publicly | im öffentlichen Repository direkt sichtbar | vorhandene Solution, README oder Projektdatei |
| `R` | Reported by project | in Projektdokumentation angegeben, aber nicht unabhängig geprüft | README meldet bekannten Laufzeitfehler |
| `I` | Inferred | begründete Schlussfolgerung aus mehreren Indizien | Datenintegrität ist wegen SQLite-Nutzung relevant |
| `U` | Unknown | noch nicht geprüft oder keine ausreichende Evidenz | tatsächliche Wiederherstellbarkeit eines Backups |

## 3. Vertrauensregeln

- `V` besitzt den höchsten technischen Nachweiswert.
- `O` bestätigt Existenz oder Inhalt, nicht automatisch Funktion oder Aktualität.
- `R` ist ein wertvoller Projektbefund, muss für Abschlussentscheidungen jedoch möglichst verifiziert werden.
- `I` muss Begründung und Unsicherheit nennen.
- `U` darf nicht als erfüllt oder nicht anwendbar behandelt werden.

## 4. Quellenaufnahme

Eine Evidenzreferenz sollte enthalten:

- Evidenz-ID,
- Klasse,
- Quelle oder Befehl,
- Beobachtungsdatum,
- betroffene Aussage,
- Ergebnis,
- Einschränkungen,
- optional Commit, Tag oder Artefakt-Hash.

## 5. Aktualität

Repository-Beobachtungen können nach späteren Commits veralten. Pilotdokumente nennen deshalb das Beobachtungsdatum und sollten vor jeder Wellenfreigabe gegen den aktuellen Zielstand aktualisiert werden.

## 6. Keine Scheingenauigkeit

Ein unvollständiger öffentlicher Snapshot darf nicht in Prozentwerte umgerechnet werden, die eine vollständige Anforderungsprüfung vortäuschen. Für frühe Piloten sind qualitative Zustände und priorisierte Lücken aussagekräftiger als eine künstliche Compliance-Quote.
