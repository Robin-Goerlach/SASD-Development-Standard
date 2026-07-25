---
title: "Integrierter Review der normativen Baseline 0.9.0"
document-id: SASD-REF-BASELINE-001
document-type: informative
status: Approved
version: 0.9.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
approved-on: 2026-07-24
approval-record: SASD-REF-BASELINE-007
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-GOV-001, SASD-GOV-002, SASD-GOV-003, SASD-GOV-004, SASD-GOV-005, SASD-GOV-006, SASD-GOV-007, SASD-REF-BASELINE-003, SASD-REF-BASELINE-004, SASD-REF-BASELINE-005]
normative-keywords: []
---

# Integrierter Review der normativen Baseline 0.9.0

## 1. Reviewziel

Der Review führt die bislang getrennt entwickelten Bereiche Core Standard, C#/.NET-Profil,
Desktopprofil und operative Prozesse zu einem gemeinsam prüfbaren Freigabebündel zusammen.
Er prüft nicht nur einzelne Dokumente, sondern insbesondere ihr Zusammenspiel.

Das Freigabebündel trägt die Kennung:

```text
SASD-NORMATIVE-BASELINE-0.9.0
```

## 2. Umfang

Geprüft wurden:

- 13 Core-Dokumente,
- 8 C#/.NET-Profildokumente,
- 4 Desktop-Profildokumente,
- 7 operative Prozessdokumente,
- insgesamt 32 normative Dokumente,
- insgesamt 1.345 einzeln referenzierbare normative Anforderungen,
- direkte Dokumentabhängigkeiten,
- Qualitätsstufenzuordnungen,
- Profil- und Prozessgrenzen,
- Nachweis-, Ausnahme- und Reviewregeln,
- Praxistauglichkeit für Einzelentwickler und kleine Teams.

Foundation und Governance waren nicht Gegenstand einer erneuten fachlichen Freigabe. Ihre
bereits freigegebene Version 0.8.0 wurde als organisatorische Grundlage verwendet.

## 3. Reviewmethodik

Der Review kombinierte:

1. Metadaten- und Linkprüfung,
2. Prüfung eindeutiger Dokument- und Anforderungs-IDs,
3. Prüfung auf wortgleiche Doppelanforderungen,
4. Prüfung auf offene `TODO`-, `TBD`- und `FIXME`-Marker,
5. Prüfung aller externen Abhängigkeiten auf `Approved`-Status,
6. Zyklusprüfung des normativen Abhängigkeitsgraphen,
7. Prüfung einheitlicher Pflichtabschnitte,
8. Gegenprüfung der Zuständigkeiten zwischen Core, Profilen und Prozessen,
9. Prüfung der Skalierung über Minimum, Recommended und Production,
10. Prüfung, ob kleine Projekte ohne unnötige Schichten oder Rollenmodelle auskommen.

## 4. Geschlossene Befunde

### 4.1 Zirkuläre Core-Abhängigkeiten

Der bisherige Metadatengraph enthielt drei Zyklen. Die fachlichen Texte waren dadurch nicht
widersprüchlich, aber eine eindeutige Lesereihenfolge und spätere Freigabereihenfolge waren
nicht möglich.

Geschlossen wurden:

| Zyklus | Korrektur |
|---|---|
| Architektur ↔ Security | Architektur benötigt Anforderungen und Qualitätsstufen; Security konkretisiert anschließend die Architektur- und Schutzanforderungen. |
| Qualität ↔ Testing | Qualität definiert Qualitätssteuerung; Testing liefert den zugehörigen Verifikationsmechanismus. |
| Repository ↔ Releases | Repository definiert Quell- und Nachweisstruktur; Releases verwenden diese Struktur. |
| Wartung ↔ Wissensmanagement | Wissensmanagement definiert die Wissensbasis; Wartung nutzt diese Basis über den Lebenszyklus. |

Die normativen Aussagen wurden nicht abgeschwächt. Korrigiert wurde ausschließlich die
formale Richtung der Dokumentabhängigkeiten.

### 4.2 Uneinheitliche Dokumentversionen

Die vier Bereiche waren historisch als Proposed 0.3.0 bis 0.6.0 geführt. Für den integrierten
Review wurden alle 32 Dokumente auf **Proposed 0.9.0** vereinheitlicht. Die früheren Review-
Dokumente bleiben als historische Entwicklungsnachweise erhalten.

### 4.3 Fehlende bündelweite Prüfung

Die bisherigen Validatoren prüften Core, Profile und Prozesse jeweils getrennt. Neu ist eine
bündelweite Prüfung, die bereichsübergreifende Doppelanforderungen, ungültige externe
Abhängigkeiten und Abhängigkeitszyklen erkennt.

## 5. Bestätigte Architekturentscheidungen

### 5.1 Core vor Profilen

Der Core bleibt technologieunabhängig. Profile dürfen ihn konkretisieren und verschärfen,
aber keine widersprechende Parallelregel etablieren.

### 5.2 Profile bleiben proportional

Das C#/.NET- und das Desktopprofil verlangen nicht pauschal:

- Clean Architecture,
- mehrere Produktionsassemblies,
- Dependency Injection,
- Generic Host,
- MVVM oder MVP,
- Repository- und Unit-of-Work-Abstraktionen.

Solche Strukturen werden nur eingesetzt, wenn Komplexität, Lebensdauer, Testbarkeit oder
Risiko einen nachvollziehbaren Nutzen erzeugen.

### 5.3 Prozesse erzeugen Nachweise, keine Parallelstandards

Die operativen Prozesse beschreiben, wann und wie Ergebnisse erzeugt, geprüft, freigegeben
oder archiviert werden. Die fachlichen Qualitätsanforderungen verbleiben in Core und Profilen.

### 5.4 Einzelentwickler dürfen Rollen kombinieren

Eine Person darf mehrere Rollen übernehmen. Rollenbündelung hebt jedoch Dokumentation,
zeitlich getrennten Selbstreview, Risikobewertung und nachvollziehbare Freigabe nicht auf.

## 6. Reviewresultat

| Prüfaspekt | Ergebnis |
|---|---:|
| Dokumente im Bündel | 32 |
| Normative Anforderungen | 1.345 |
| Doppelte Anforderungs-IDs | 0 |
| Wortgleiche Doppelanforderungen | 0 |
| Unbekannte Dokumentabhängigkeiten | 0 |
| Nicht freigegebene externe Abhängigkeiten | 0 |
| Verbleibende Abhängigkeitszyklen | 0 |
| Offene TODO/TBD/FIXME-Marker | 0 |
| Technische Reviewfehler | 0 |

## 7. Noch offene Freigabebedingungen

Der integrierte Review ist abgeschlossen. Die formale Freigabe der 32 Dokumente bleibt dennoch
getrennt und ist noch nicht erfolgt.

Vor dem Approval-Commit sind mindestens zu bestätigen:

1. bewusste Maintainer-Freigabe des gesamten Bündels,
2. erfolgreicher lokaler Quality-Gate-Lauf auf dem vorgesehenen Inhalt,
3. erfolgreicher Ubuntu- und Windows-CI-Lauf für den vorgesehenen Freigabe-Commit,
4. dokumentierte Entscheidung, ob die noch ausstehende TaskHost-Verifikation als Blocker oder
   als zeitlich begrenzte Pilotauflage behandelt wird,
5. Erzeugung eines eigenen Approval Records und Approval Manifests nach der Statusänderung.

## 8. Schlussfolgerung

Die 32 Dokumente sind als **integrierte Proposed-Baseline 0.9.0** technisch und strukturell
freigabereif. Sie werden durch diesen Review nicht automatisch zu `Approved`.

Der nächste zulässige normative Schritt ist ein eigener Approval-Commit. Ein Release Candidate
oder Version 1.0.0 darf daraus erst entstehen, wenn zusätzlich die Releasekriterien und die
noch offenen Pilot- und CI-Nachweise bewertet wurden.
