---
title: "Evidenzmodell für Pilotbewertungen"
document-id: SASD-REF-PILOT-002
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
depends-on: [SASD-CORE-004, SASD-CORE-007, SASD-GOV-007, SASD-PROC-004]
---

# Evidenzmodell für Pilotbewertungen

## 1. Zweck

Pilotbewertungen müssen zwischen direkt geprüften Tatsachen, vorbereiteten Artefakten, öffentlich beobachtbaren Merkmalen, Projektaussagen und Annahmen unterscheiden. Dieses Modell verhindert, dass eine Repository-Übersicht oder ein erzeugtes Updatepaket fälschlich als vollständiger technischer Audit dargestellt wird.

## 2. Evidenzklassen

| Code | Klasse | Bedeutung | Typisches Beispiel |
|---|---|---|---|
| `V` | Verified locally | lokal gebaut, ausgeführt, getestet oder direkt inspiziert | erfolgreicher `dotnet test`- und Startlauf |
| `A` | Prepared artifact | Inhalt eines erzeugten Patches, ZIPs oder Overlays wurde statisch geprüft, aber noch nicht als Zielstand ausgeführt | Updatepaket enthält Testprojekt und CI-Datei |
| `O` | Observed publicly | im öffentlichen Repository direkt sichtbar | vorhandene Solution, README oder Projektdatei |
| `R` | Reported by project | in Projektdokumentation angegeben, aber nicht unabhängig geprüft | README meldet bekannten Laufzeitfehler |
| `I` | Inferred | begründete Schlussfolgerung aus mehreren Indizien | Datenintegrität ist wegen SQLite-Nutzung relevant |
| `U` | Unknown | noch nicht geprüft oder keine ausreichende Evidenz | tatsächliche Wiederherstellbarkeit eines Backups |

## 3. Vertrauensregeln

- `V` besitzt den höchsten technischen Nachweiswert für die konkret geprüfte Umgebung und den konkret identifizierten Stand.
- `A` bestätigt den Inhalt und die statische Konsistenz eines vorbereiteten Artefakts, nicht dessen Merge, Build, Laufzeitverhalten oder CI-Erfolg.
- `O` bestätigt Existenz oder Inhalt im beobachteten Repository, nicht automatisch Funktion oder Aktualität.
- `R` ist ein wertvoller Projektbefund, muss für Abschlussentscheidungen jedoch möglichst verifiziert werden.
- `I` muss Begründung und Unsicherheit nennen.
- `U` darf nicht als erfüllt oder nicht anwendbar behandelt werden.

## 4. Identität des geprüften Stands

Technische Verifikation muss mindestens enthalten:

- Ziel-Repository,
- Branch oder Tag,
- vollständige Commit-ID,
- Datum und Umgebung,
- ausgeführte Befehle,
- Exitcodes oder Ergebnisnachweise,
- relevante Artefakt-Hashes,
- bekannte Einschränkungen.

Ohne unveränderliche Commit-ID darf eine Verifikation nur als Arbeitsnachweis, nicht als dauerhafter Referenznachweis verwendet werden.

## 5. Artefaktnachweise

Ein vorbereitetes Overlay oder ZIP sollte erfassen:

- Dateiname und SHA-256,
- vorgesehene Ziel-Repository- und Baseline-Information,
- Anzahl neuer oder geänderter Dateien,
- statische Prüfungen,
- nicht ausgeführte Prüfungen,
- manuell zu bestätigende Entscheidungen,
- Rückfall- und Einspielhinweise.

## 6. Quellenaufnahme

Eine Evidenzreferenz sollte enthalten:

- Evidenz-ID,
- Klasse,
- Quelle oder Befehl,
- Beobachtungsdatum,
- betroffene Aussage,
- Ergebnis,
- Einschränkungen,
- optional Commit, Tag oder Artefakt-Hash.

## 7. Aktualität

Repository-Beobachtungen können nach späteren Commits veralten. Pilotdokumente nennen deshalb das Beobachtungsdatum und sollten vor jeder Wellenfreigabe gegen den aktuellen Zielstand aktualisiert werden.

## 8. Keine Scheingenauigkeit

Ein unvollständiger öffentlicher Snapshot oder ein nicht ausgeführtes Updatepaket darf nicht in Prozentwerte umgerechnet werden, die eine vollständige Anforderungsprüfung vortäuschen. Für frühe Piloten sind qualitative Zustände und priorisierte Lücken aussagekräftiger als eine künstliche Compliance-Quote.
