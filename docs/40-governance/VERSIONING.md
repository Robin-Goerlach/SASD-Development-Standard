---
title: "Versionierung und Veröffentlichung des Standards"
document-id: SASD-GOV-004
document-type: normative
status: Approved
version: 0.8.0
standard-version: "1.0"
language: de
authoritative: true
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
approved-on: 2026-07-24
approval-record: SASD-REF-GOV-005
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-GOV-002, SASD-GOV-003, SASD-GOV-005]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Versionierung und Veröffentlichung des Standards

## 1. Zweck

Dieses Dokument definiert Versionen, Tags, Releases, Dokumentversionen und Publikationsartefakte.

## 2. Versionsmodell

| Fassung | Bedeutung |
|---|---|
| `0.x.y` | Entwicklung vor dem ersten stabilen Standard |
| `1.0.0-rc.N` | Release Candidate |
| `1.0.0` | erste stabile Fassung |
| `MAJOR.MINOR.PATCH` | spätere stabile Fassungen |

## 3. Änderungswirkung

| Änderung | Typische Versionswirkung |
|---|---|
| Rechtschreibung, Format, defekter Link | Patch oder unveröffentlichte Korrektur |
| kompatible Präzisierung ohne neue Pflicht | Patch |
| neue kompatible Anforderung oder neues Profil | Minor |
| Entfernung oder inkompatible Bedeutungsänderung | Major |
| dringende Security Correction | begründeter Patch oder Minor |

## 4. Normative Anforderungen

| Anforderungs-ID | Normative Anforderung |
|---|---|
| `SASD-GOV-REQ-300` | Veröffentlichte Gesamtstände des Standards MÜSSEN Semantic Versioning in der Form MAJOR.MINOR.PATCH verwenden. |
| `SASD-GOV-REQ-301` | Entwicklungsstände vor der ersten stabilen Version MÜSSEN eine Version kleiner als 1.0.0 verwenden. |
| `SASD-GOV-REQ-302` | Release Candidates MÜSSEN als Vorabversion in der Form 1.0.0-rc.N gekennzeichnet werden. |
| `SASD-GOV-REQ-303` | Ein stabiler Standardrelease MUSS ausschließlich Approved-Dokumente als normative Basis enthalten. |
| `SASD-GOV-REQ-304` | Jeder veröffentlichte Standardstand MUSS einem eindeutigen annotierten Git-Tag zugeordnet sein. |
| `SASD-GOV-REQ-305` | Ein Tag MUSS exakt den freigegebenen Commit referenzieren. |
| `SASD-GOV-REQ-306` | Ein veröffentlichter Tag DARF NICHT nachträglich auf einen anderen Commit verschoben werden. |
| `SASD-GOV-REQ-307` | Jeder GitHub Release MUSS die Standardversion, das Datum und den Status nennen. |
| `SASD-GOV-REQ-308` | Release Notes MÜSSEN normative Änderungen, Migrationen, bekannte Einschränkungen und betroffene Profile zusammenfassen. |
| `SASD-GOV-REQ-309` | Ein Patch-Release DARF NICHT absichtlich eine inkompatible normative Änderung enthalten. |
| `SASD-GOV-REQ-310` | Ein Minor-Release KANN kompatible neue Profile, Prozesse, Vorlagen oder Anforderungen ergänzen. |
| `SASD-GOV-REQ-311` | Ein Major-Release MUSS verwendet werden, wenn bestehende korrekte Anwendungen des Standards durch normative Änderungen inkompatibel werden. |
| `SASD-GOV-REQ-312` | Eine redaktionelle Korrektur KANN in einem Patch-Release veröffentlicht werden. |
| `SASD-GOV-REQ-313` | Eine kompatible Klarstellung KANN in einem Patch-Release erfolgen, wenn sie keine neue Pflicht erzeugt. |
| `SASD-GOV-REQ-314` | Eine neue verbindliche Pflicht MUSS mindestens als Minor-Release behandelt werden, sofern sie nicht ausschließlich eine bereits erklärte Sicherheitslücke schließt. |
| `SASD-GOV-REQ-315` | Eine strengere Sicherheitsanforderung KANN ausnahmsweise in einem Patch-Release erfolgen, MUSS dann aber deutlich als Security Correction gekennzeichnet werden. |
| `SASD-GOV-REQ-316` | Dokumentversionen MÜSSEN unabhängig von der Gesamtstandardversion geführt werden. |
| `SASD-GOV-REQ-317` | Ein Standardrelease MUSS eine Manifestliste der enthaltenen normativen Dokumentversionen besitzen. |
| `SASD-GOV-REQ-318` | Die autoritative Sprachfassung MUSS im Release eindeutig benannt werden. |
| `SASD-GOV-REQ-319` | Word- und PDF-Ausgaben MÜSSEN aus dem freigegebenen Quellstand erzeugt werden. |
| `SASD-GOV-REQ-320` | Publikationsartefakte MÜSSEN die Standardversion und den Quellcommit erkennen lassen. |
| `SASD-GOV-REQ-321` | Veröffentlichte Binär- oder Publikationsartefakte SOLLTEN mit SHA-256-Prüfsummen versehen werden. |
| `SASD-GOV-REQ-322` | Ein Release Candidate MUSS dieselben wesentlichen Validierungen wie der geplante stabile Release durchlaufen. |
| `SASD-GOV-REQ-323` | Ein stabiler Release DARF NICHT erstellt werden, solange Release-Blocker offen sind. |
| `SASD-GOV-REQ-324` | Known Issues MÜSSEN vor Veröffentlichung bewertet und in Release Notes oder Begleitdokumenten sichtbar gemacht werden. |
| `SASD-GOV-REQ-325` | Nicht normative Repositoryänderungen KÖNNEN zwischen Standardreleases auf main erfolgen, sofern sie keine veröffentlichte normative Bedeutung verändern. |
| `SASD-GOV-REQ-326` | Die Hauptbranch MUSS den aktuellen Entwicklungsstand und nicht zwingend den letzten stabilen Release abbilden. |
| `SASD-GOV-REQ-327` | Verbraucher MÜSSEN für reproduzierbare Assessments eine veröffentlichte Version, einen Tag oder einen Commit referenzieren. |
| `SASD-GOV-REQ-328` | Ein Release MUSS ein Standard Release Record besitzen. |
| `SASD-GOV-REQ-329` | Das Release Record MUSS Validatorergebnisse, Freigaben, Artefakte und offene Ausnahmen dokumentieren. |
| `SASD-GOV-REQ-330` | Zurückgezogene Releases MÜSSEN sichtbar als withdrawn oder superseded gekennzeichnet werden und DÜRFEN nicht stillschweigend gelöscht werden. |
| `SASD-GOV-REQ-331` | Ein korrigierender Folgerelease SOLLTE einem zurückgezogenen Release zeitnah folgen. |
| `SASD-GOV-REQ-332` | Die Versionspolitik MUSS im Repository öffentlich auffindbar sein. |
| `SASD-GOV-REQ-333` | Release-Bezeichnungen DÜRFEN NICHT eine Stabilität behaupten, die der Dokumentstatus nicht trägt. |
| `SASD-GOV-REQ-334` | Ein Draft Snapshot KANN ohne GitHub Release verteilt werden, MUSS aber eindeutig als nicht stabil gekennzeichnet sein. |
| `SASD-GOV-REQ-335` | Ein Pre-1.0-Release SOLLTE besonders auf mögliche inkompatible Änderungen hinweisen. |

## 5. Releasebestandteile

Ein stabiler Release umfasst mindestens:

- annotierten Git-Tag,
- GitHub Release mit Release Notes,
- Changelog-Eintrag,
- Standard Release Record,
- Manifest der normativen Dokumentversionen,
- Validatorergebnisse,
- bekannte Einschränkungen,
- erzeugte Publikationsartefakte, sofern für die Fassung vorgesehen.

## 6. Dokument- und Gesamtversion

Die Dokumentversion beschreibt die Entwicklung eines einzelnen Dokuments. Die Standardversion beschreibt eine freigegebene Zusammenstellung. Ein Dokument `0.8.0` kann daher in einem späteren Standardrelease `1.0.0` enthalten sein.

## 7. Verwandte Dokumente

- [Änderungsprozess](CHANGE-PROCESS.md)
- [Dokumentlebenszyklus](DOCUMENT-LIFECYCLE.md)
- [Version-1.0-Akzeptanzkriterien](../00-foundation/VERSION-1.0-ACCEPTANCE-CRITERIA.md)
- [Standard Release Record Template](../../templates/documents/STANDARD-RELEASE-RECORD-TEMPLATE.md)
