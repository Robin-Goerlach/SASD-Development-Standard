---
title: "Freigabereife der normativen Baseline 0.9.0"
document-id: SASD-REF-BASELINE-002
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
depends-on: [SASD-REF-BASELINE-001, SASD-REF-BASELINE-003, SASD-REF-BASELINE-004, SASD-REF-BASELINE-005, SASD-GOV-002, SASD-GOV-004, SASD-GOV-005, SASD-GOV-007]
normative-keywords: []
---
# Freigabereife der normativen Baseline 0.9.0

## 1. Zweck

Dieses Dokument hält den abgeschlossenen Übergang vom integrierten Review zur formalen
Maintainer-Freigabe fest. Es bleibt als historischer Readiness-Nachweis erhalten.

## 2. Gesamtstatus

```text
Reviewstatus:                 Abgeschlossen
Technische Baselineprüfung:   Bestanden
Bündelstatus:                 Approved 0.9.0
Formale Maintainer-Freigabe:  Erteilt
Approval Record:              SASD-REF-BASELINE-007
Approval Manifest:            SASD-REF-BASELINE-008
Release Candidate:            Noch nicht freigegeben
Version 1.0.0:                Noch nicht veröffentlicht
```

## 3. Freigabebündel

| Bereich | Dokumente | Anforderungen | Freigabestatus |
|---|---:|---:|---|
| Core Standard | 13 | 545 | Approved 0.9.0 |
| C#/.NET-Profil | 8 | 277 | Approved 0.9.0 |
| Desktopprofil | 4 | 215 | Approved 0.9.0 |
| Operative Prozesse | 7 | 308 | Approved 0.9.0 |
| **Gesamt** | **32** | **1.345** | **Approved 0.9.0** |

## 4. Erfüllte Freigabekriterien

- [x] Alle Dokumente besitzen vollständige normative Metadaten.
- [x] Dokument-IDs und Anforderungs-IDs sind eindeutig.
- [x] Alle externen normativen Abhängigkeiten zeigen auf freigegebene Dokumente.
- [x] Der bündelinterne Abhängigkeitsgraph ist azyklisch.
- [x] Es bestehen keine wortgleichen Doppelanforderungen.
- [x] Es bestehen keine offenen TODO-, TBD- oder FIXME-Marker.
- [x] Qualitätsstufen, Nachweise und Ausnahmen sind behandelt.
- [x] Core, Profile und Prozesse besitzen abgegrenzte Verantwortlichkeiten.
- [x] Das Bündel wurde bewusst durch den Maintainer freigegeben.
- [x] Approval Record und SHA-256-Manifest wurden erzeugt.

## 5. Dokumentierte Release-Auflagen

Die Freigabe der Dokumente ist von ihrer Veröffentlichung als Release getrennt. Vor einem
Release Candidate MÜSSEN zusätzlich erfüllt oder ausdrücklich neu entschieden werden:

1. Ubuntu-, Windows- und `SASD merge gate`-Prüfung für den Approval-Commit,
2. Abschluss oder dokumentierte Release-Ausnahme für TaskHost Local Wave 01,
3. Bewertung der Repository-Ruleset-Aktivierung,
4. vollständiger Release-Readiness- und Publikationslauf.

Diese Auflagen ändern den Dokumentstatus nicht rückwirkend. Ein fehlgeschlagener Validator,
ein nachträglich entdeckter Blocker oder eine normative Korrektur MUSS jedoch über den
Change-Prozess behandelt werden.

## 6. Entscheidung

Die Baseline wurde als **Approved 0.9.0 mit dokumentierten Release-Auflagen** freigegeben.
Sie ist noch kein Release Candidate und keine stabile Version 1.0.0.
