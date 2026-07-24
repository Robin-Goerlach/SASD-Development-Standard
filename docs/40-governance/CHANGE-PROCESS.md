---
title: "Änderungsprozess"
document-id: SASD-GOV-005
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
depends-on: [SASD-FND-003, SASD-FND-005, SASD-GOV-002, SASD-GOV-004]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Änderungsprozess

## 1. Zweck

Dieses Dokument definiert, wie der Standard kontrolliert korrigiert, erweitert, verschärft, vereinfacht oder zurückgenommen wird.

## 2. Änderungsarten

| Typ | Beschreibung | Beispiel |
|---|---|---|
| `editorial` | keine Bedeutungsänderung | Rechtschreibung, Format |
| `clarification` | präzisiert bestehende Absicht | Bedingung eindeutiger formulieren |
| `additive` | ergänzt kompatiblen Inhalt | neues optionales Profil |
| `breaking` | ändert bestehende korrekte Anwendung | Anforderung entfernen oder umdeuten |
| `security` | schließt Sicherheitsrisiko | unsichere Praxis verbieten |
| `emergency` | dringende Sofortkorrektur | fehlerhafte Releaseanweisung zurückziehen |

## 3. Normative Anforderungen

| Anforderungs-ID | Normative Anforderung |
|---|---|
| `SASD-GOV-REQ-400` | Jede normative Bedeutungsänderung MUSS nachvollziehbar beantragt oder protokolliert werden. |
| `SASD-GOV-REQ-401` | Ein Änderungsvorschlag MUSS Problem, Ziel, betroffene Dokumente und vorgeschlagene Lösung beschreiben. |
| `SASD-GOV-REQ-402` | Ein Änderungsvorschlag MUSS betroffene Anforderungs-IDs nennen, sofern diese existieren. |
| `SASD-GOV-REQ-403` | Ein Änderungsvorschlag MUSS Auswirkungen auf bestehende Projekte und Assessments bewerten. |
| `SASD-GOV-REQ-404` | Ein Änderungsvorschlag MUSS Auswirkungen auf Profile, Prozesse, Vorlagen, Checklisten, Prompts und Tooling prüfen. |
| `SASD-GOV-REQ-405` | Ein Änderungsvorschlag SOLLTE mindestens eine verworfene Alternative oder begründen, warum keine Alternative sinnvoll war. |
| `SASD-GOV-REQ-406` | Eine Änderung MUSS als editorial, clarification, additive, breaking, security oder emergency klassifiziert werden. |
| `SASD-GOV-REQ-407` | Editorial Changes DÜRFEN NICHT die normative Bedeutung verändern. |
| `SASD-GOV-REQ-408` | Clarifications DÜRFEN NICHT eine neue unabhängige Pflicht erzeugen. |
| `SASD-GOV-REQ-409` | Additive Changes MÜSSEN ihre Anwendbarkeit und Versionswirkung nennen. |
| `SASD-GOV-REQ-410` | Breaking Changes MÜSSEN eine Migrationsstrategie oder explizite Nicht-Migrationsentscheidung enthalten. |
| `SASD-GOV-REQ-411` | Security Changes MÜSSEN Risiko, Dringlichkeit und gegebenenfalls eingeschränkte Offenlegung berücksichtigen. |
| `SASD-GOV-REQ-412` | Emergency Changes MÜSSEN nachträglich vollständig dokumentiert und reviewed werden. |
| `SASD-GOV-REQ-413` | Normative Änderungen MÜSSEN gegen die Projektcharta und Grundprinzipien geprüft werden. |
| `SASD-GOV-REQ-414` | Eine Änderung DARF NICHT die definierte Dokumentzuständigkeit ohne Anpassung der Inhaltsarchitektur verschieben. |
| `SASD-GOV-REQ-415` | Neue normative Dokumentrollen MÜSSEN in Inhaltsarchitektur und Dokumentkatalog aufgenommen werden. |
| `SASD-GOV-REQ-416` | Entfernte normative Dokumentrollen MÜSSEN über Deprecated oder eine ausdrücklich begründete Vorab-1.0-Entscheidung behandelt werden. |
| `SASD-GOV-REQ-417` | Anforderungs-IDs gelöschter Anforderungen DÜRFEN NICHT wiederverwendet werden. |
| `SASD-GOV-REQ-418` | Ersetzte Anforderungen SOLLTEN auf Nachfolger oder Migrationshinweis verweisen. |
| `SASD-GOV-REQ-419` | Jede normative Änderung MUSS mindestens eine fachliche Prüfung erhalten. |
| `SASD-GOV-REQ-420` | Ein Solo-Maintainer KANN die Prüfung selbst durchführen, MUSS dabei aber Erstellungs- und Reviewmodus nachvollziehbar trennen. |
| `SASD-GOV-REQ-421` | Änderungen mit Security-, Datenschutz-, Lizenz- oder Rechtswirkung SOLLTEN fachkundig geprüft werden. |
| `SASD-GOV-REQ-422` | Validatoren MÜSSEN nach einer Änderung erfolgreich laufen, bevor sie Proposed oder Approved wird. |
| `SASD-GOV-REQ-423` | Abgeleitete Indizes und Matrizen MÜSSEN nach relevanten Änderungen neu erzeugt werden. |
| `SASD-GOV-REQ-424` | Interne Links MÜSSEN nach Strukturänderungen geprüft werden. |
| `SASD-GOV-REQ-425` | Der Changelog MUSS relevante normative Änderungen in verständlicher Form nennen. |
| `SASD-GOV-REQ-426` | Commit-Nachrichten SOLLTEN Art und Gegenstand der Änderung erkennen lassen. |
| `SASD-GOV-REQ-427` | Vor Version 1.0 KÖNNEN kleine redaktionelle Änderungen direkt auf main erfolgen. |
| `SASD-GOV-REQ-428` | Vor Version 1.0 SOLLTEN größere normative Änderungen als eigenständiger Commit oder Pull Request isoliert werden. |
| `SASD-GOV-REQ-429` | Nach Version 1.0 MÜSSEN normative Änderungen einen dokumentierten Change Record oder Pull Request besitzen. |
| `SASD-GOV-REQ-430` | Eine abgelehnte Änderung MUSS mit einer kurzen Begründung dokumentiert werden, wenn sie eine wiederkehrende Grundsatzfrage betrifft. |
| `SASD-GOV-REQ-431` | Eine vertagte Änderung MUSS einen Auslöser oder geplanten Neubewertungszeitpunkt nennen. |
| `SASD-GOV-REQ-432` | Pilotfeedback KANN einen Änderungsvorschlag auslösen, MUSS aber Evidenz und Kontext des Piloten nennen. |
| `SASD-GOV-REQ-433` | Ein einzelner Pilotbefund SOLLTE nicht ohne Prüfung der Übertragbarkeit verallgemeinert werden. |
| `SASD-GOV-REQ-434` | Eine Änderung MUSS auf unnötige Bürokratie und Overengineering geprüft werden. |
| `SASD-GOV-REQ-435` | Eine neue Pflicht SOLLTE einen erwarteten Qualitäts- oder Risikonutzen benennen. |
| `SASD-GOV-REQ-436` | Eine neue Pflicht MUSS ein angemessenes Nachweisniveau ermöglichen. |
| `SASD-GOV-REQ-437` | Änderungen DÜRFEN NICHT eine externe Zertifizierung oder Rechtskonformität behaupten, die nicht tatsächlich geprüft wurde. |
| `SASD-GOV-REQ-438` | Die finale Entscheidung MUSS Accepted, Rejected, Deferred oder Withdrawn lauten. |
| `SASD-GOV-REQ-439` | Eine angenommene Änderung MUSS eine verantwortliche Person und Zielversion besitzen. |

## 4. Prozessablauf

```text
Erfassen -> Klassifizieren -> Auswirkungen analysieren -> Review -> Entscheidung
-> Umsetzung -> Validatoren -> Dokumentstatus/Version -> Changelog -> Veröffentlichung
```

## 5. Vereinfachter Weg für kleine Änderungen

Eine rein redaktionelle Vorab-1.0-Änderung kann über Commit und Changelog erfolgen. Sobald normative Bedeutung, Status, IDs, Anwendbarkeit oder Versionswirkung betroffen sind, wird die Vorlage [Standard Change Proposal](../../templates/documents/STANDARD-CHANGE-PROPOSAL-TEMPLATE.md) verwendet.

## 6. Entscheidungsstatus

- `Accepted`
- `Rejected`
- `Deferred`
- `Withdrawn`

## 7. Verwandte Dokumente

- [Versionierung](VERSIONING.md)
- [Dokumentlebenszyklus](DOCUMENT-LIFECYCLE.md)
- [Pilot Feedback Log](../50-reference-implementations/PILOT-FEEDBACK-LOG.md)
