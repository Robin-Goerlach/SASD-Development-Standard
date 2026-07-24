---
title: "Lebenszyklus von Standarddokumenten"
document-id: SASD-GOV-002
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
depends-on: [SASD-GOV-001, SASD-GOV-003, SASD-GOV-004, SASD-GOV-005]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Lebenszyklus von Standarddokumenten

## 1. Zweck

Dieses Dokument definiert Statuswerte, Übergänge, Prüfschritte und Freigaben für Dokumente des SASD Development Standard.

## 2. Statusmodell

```text
Planned -> Draft -> Proposed -> Approved -> Deprecated -> Retired
             ^          |
             |----------|
```

| Status | Bedeutung | Normative Wirkung |
|---|---|---|
| `Planned` | Dokumentrolle vorgesehen | keine |
| `Draft` | aktiver Arbeitsentwurf | keine |
| `Proposed` | vollständiger Freigabekandidat | Pilot Alignment |
| `Approved` | fachlich freigegeben | verbindlich innerhalb veröffentlichter Bezugsfassung |
| `Deprecated` | noch vorhanden, aber zur Ablösung vorgesehen | eingeschränkt mit Übergangsregel |
| `Retired` | außer Kraft | keine |

## 3. Normative Anforderungen

| Anforderungs-ID | Normative Anforderung |
|---|---|
| `SASD-GOV-REQ-100` | Jedes Standarddokument MUSS genau einen zulässigen Status besitzen. |
| `SASD-GOV-REQ-101` | Ein Planned-Dokument DARF NICHT verbindliche Anforderungen für Anwender setzen. |
| `SASD-GOV-REQ-102` | Ein Draft-Dokument KANN für Entwicklung und Review genutzt werden, ist aber nicht verbindlich. |
| `SASD-GOV-REQ-103` | Ein Proposed-Dokument MUSS fachlich vollständig genug für Pilotierung und Freigabereview sein. |
| `SASD-GOV-REQ-104` | Ein Proposed-Dokument KANN für Pilot Alignment verwendet werden, DARF aber NICHT als Grundlage einer stabilen formalen Alignment-Aussage dienen. |
| `SASD-GOV-REQ-105` | Ein Approved-Dokument MUSS einen dokumentierten Freigabenachweis besitzen. |
| `SASD-GOV-REQ-106` | Dokumente ohne Approved-Status DÜRFEN NICHT verbindlicher Bestandteil eines stabil veröffentlichten Standards sein. |
| `SASD-GOV-REQ-107` | Ein Deprecated-Dokument MUSS einen vorgesehenen Ersatz oder eine begründete Auslaufentscheidung nennen. |
| `SASD-GOV-REQ-108` | Ein Retired-Dokument DARF NICHT mehr als anwendbare normative Quelle verwendet werden. |
| `SASD-GOV-REQ-109` | Der Übergang Planned zu Draft MUSS einen verantwortlichen Owner und einen initialen Geltungsbereich voraussetzen. |
| `SASD-GOV-REQ-110` | Der Übergang Draft zu Proposed MUSS vollständige Metadaten, stabile IDs, geschlossene interne Platzhalter und erfolgreiche Basisvalidatoren voraussetzen. |
| `SASD-GOV-REQ-111` | Der Übergang Proposed zu Approved MUSS einen Review gegen dokumentierte Freigabekriterien voraussetzen. |
| `SASD-GOV-REQ-112` | Ein Approved-Dokument MUSS mindestens gegen Widersprüche, Anwendbarkeit, Proportionalität, Nachweisbarkeit und Abhängigkeiten geprüft worden sein. |
| `SASD-GOV-REQ-113` | Ein Approved-Dokument MUSS die freigebende Person, das Datum, die Version und den geprüften Commit nennen. |
| `SASD-GOV-REQ-114` | Eine Person KANN als alleiniger Maintainer freigeben, MUSS dann aber einen zeitlich getrennten Selbstreview dokumentieren. |
| `SASD-GOV-REQ-115` | Für sicherheitskritische oder rechtlich relevante Inhalte SOLLTE zusätzliche fachkundige Prüfung eingeholt werden. |
| `SASD-GOV-REQ-116` | Eine Änderung an einem Approved-Dokument MUSS nach ihrem Änderungsgrad erneut geprüft werden. |
| `SASD-GOV-REQ-117` | Redaktionelle Änderungen an Approved-Dokumenten KÖNNEN ohne vollständigen Neufreigabeprozess erfolgen, MÜSSEN aber nachvollziehbar protokolliert werden. |
| `SASD-GOV-REQ-118` | Normative Bedeutungsänderungen an Approved-Dokumenten MÜSSEN den Status mindestens auf Proposed zurücksetzen oder in einer neuen Dokumentversion als Proposed geführt werden. |
| `SASD-GOV-REQ-119` | Eine Statusänderung MUSS im Changelog oder Freigabeprotokoll nachvollziehbar sein. |
| `SASD-GOV-REQ-120` | Abhängige Dokumente MÜSSEN bei einer relevanten Status- oder Bedeutungsänderung auf Auswirkungen geprüft werden. |
| `SASD-GOV-REQ-121` | Ein Dokument DARF NICHT Approved sein, wenn eine normative Abhängigkeit nur Planned oder Draft ist. |
| `SASD-GOV-REQ-122` | Eine Proposed-Abhängigkeit KANN für eine koordinierte Freigabe akzeptiert werden, wenn beide Dokumente gemeinsam geprüft und freigegeben werden. |
| `SASD-GOV-REQ-123` | Die autoritative Fassung MUSS vor einer Übersetzung freigegeben werden oder die Übersetzung MUSS ausdrücklich als vorläufig bezeichnet werden. |
| `SASD-GOV-REQ-124` | Deprecated-Dokumente MÜSSEN mindestens eine Übergangsfrist oder ein Auslaufkriterium nennen. |
| `SASD-GOV-REQ-125` | Retired-Dokumente SOLLTEN aus aktiver Navigation entfernt, aber zur historischen Nachvollziehbarkeit erhalten werden. |
| `SASD-GOV-REQ-126` | Dokumentdateien SOLLTEN nicht allein wegen einer Statusänderung umbenannt werden. |
| `SASD-GOV-REQ-127` | Dokument-IDs MÜSSEN über Statusübergänge hinweg stabil bleiben. |
| `SASD-GOV-REQ-128` | Ein Freigabereview MUSS offene Blocker ausschließen. |
| `SASD-GOV-REQ-129` | Offene Major-Befunde MÜSSEN behoben, als genehmigte Ausnahme dokumentiert oder ausdrücklich aus dem Freigabeumfang entfernt werden. |
| `SASD-GOV-REQ-130` | Minor-Befunde KÖNNEN nach Freigabe offen bleiben, wenn sie keinen Widerspruch oder falsche Anwendung erzeugen. |
| `SASD-GOV-REQ-131` | Ein Freigabenachweis MUSS zwischen geprüft, genehmigt und veröffentlicht unterscheiden. |
| `SASD-GOV-REQ-132` | Die Veröffentlichung eines Tags DARF NICHT automatisch als fachliche Dokumentfreigabe interpretiert werden. |
| `SASD-GOV-REQ-133` | Eine fachliche Freigabe DARF NICHT automatisch als Veröffentlichung interpretiert werden. |

## 4. Freigabekriterien Proposed zu Approved

Ein Freigabereview bewertet mindestens:

1. Zweck und Geltungsbereich,
2. eindeutige Zuständigkeit,
3. Widerspruchsfreiheit,
4. Verhältnismäßigkeit für Einzelentwickler und kleine Teams,
5. Anwendbarkeit der Qualitätsstufen,
6. Prüfbarkeit und mögliche Nachweise,
7. Abhängigkeiten und Vorrangregeln,
8. Sicherheit, Datenschutz und rechtliche Auswirkungen,
9. Vorlagen, Checklisten, Prompts und Tooling,
10. offene Befunde und genehmigte Ausnahmen.

## 5. Freigabeverantwortung

Vor Version 1.0 ist der benannte Maintainer die Freigabeinstanz. Ein dokumentierter Selbstreview ist zulässig, sofern Erarbeitung und abschließende Prüfung zeitlich oder methodisch getrennt werden. Externe Zertifizierung wird nicht behauptet.

## 6. Freigabenachweis

Der Nachweis verwendet die Vorlage [Document Approval Record](../../templates/documents/DOCUMENT-APPROVAL-RECORD-TEMPLATE.md) und referenziert den geprüften Commit.

## 7. Verwandte Dokumente

- [Dokumentmetadaten](DOCUMENT-METADATA.md)
- [Änderungsprozess](CHANGE-PROCESS.md)
- [Versionierung](VERSIONING.md)
- [Approval Readiness 0.8.0](APPROVAL-READINESS-0.8.0.md)
