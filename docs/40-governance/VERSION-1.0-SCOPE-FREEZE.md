---
title: "Scope Freeze für Version 1.0"
document-id: SASD-REF-RC-007
document-type: informative
status: Draft
version: 0.1.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-08-05
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-FND-002, SASD-FND-007, SASD-REF-BASELINE-007, SASD-REF-RC-001, SASD-REF-RC-002]
normative-keywords: []
---
# Scope Freeze für Version 1.0

## 1. Zweck

Dieses Dokument hält den operativen Umfang für den Weg von der freigegebenen normativen Baseline `0.9.0` über `1.0.0-rc.1` bis zur stabilen Version `1.0.0` fest.

Es verändert den Approved Scope in [`SASD-FND-002`](../00-foundation/SCOPE.md) und die Approved Akzeptanzkriterien in [`SASD-FND-007`](../00-foundation/VERSION-1.0-ACCEPTANCE-CRITERIA.md) nicht. Bei einem Widerspruch haben diese normativen Dokumente Vorrang.

Der Scope Freeze verhindert, dass die Veröffentlichung durch zusätzliche Profile, neue Governance-Modelle oder nicht releasekritische Werkzeuge immer weiter verschoben wird.

## 2. Verbindliche Produktbasis von Version 1.0

Version 1.0 veröffentlicht die bereits freigegebene Produktbasis:

- sieben Foundation-Dokumente,
- sieben Governance-Dokumente,
- dreizehn Core-Dokumente,
- acht Dokumente des C#/.NET-Profils,
- vier Dokumente des Desktopprofils,
- sieben operative Prozessdokumente,
- die zugehörigen Vorlagen, Checklisten, Prompts, Beispiele und Prüfwerkzeuge,
- die dokumentierten Referenzpilot-Baselines für Small, Medium und Large.

Die normative Baseline umfasst damit insgesamt **46 Approved Dokumente**. Core, C#/.NET, Desktop und operative Prozesse enthalten zusammen **1.345 normative Anforderungen**.

## 3. Zulässige Arbeiten vor `1.0.0-rc.1`

Vor dem ersten Release Candidate werden nur Arbeiten aufgenommen, die mindestens einem der folgenden Zwecke dienen:

1. einen dokumentierten Releaseblocker schließen,
2. einen fachlichen Widerspruch oder nachweisbaren Fehler korrigieren,
3. Security-, Datenschutz-, Lizenz- oder Datenverlustrisiken beseitigen,
4. den Einstieg so weit verbessern, dass ein fremder Entwickler den Standard anwenden kann,
5. reproduzierbare Releaseartefakte, Evidenz oder Verifikation ermöglichen,
6. notwendige Pilotbefunde mit direkter Wirkung auf Version 1.0 einarbeiten,
7. Repository-Grenze, Navigation oder Source-of-Truth-Beziehungen konsistent halten.

Nicht releasekritische Verbesserungen werden einer späteren Version zugeordnet.

## 4. Bedingungen für `1.0.0-rc.1`

Der Release Candidate setzt mindestens voraus:

- alle erforderlichen normativen Dokumente bleiben Approved,
- die vollständigen lokalen Quality Gates sind grün,
- Ubuntu, Windows und `SASD merge gate` wurden für exakt denselben vorgesehenen Releasecommit erfolgreich nachgewiesen,
- mindestens ein Pilotdurchlauf wurde im Ziel-Repository praktisch ausgeführt und technisch mit `Passed` verifiziert,
- das geplante `main`-Ruleset ist aktiviert oder seine Verschiebung wurde ausdrücklich und befristet entschieden,
- Source- und Markdown-Archive wurden aus einem sauberen Checkout deterministisch erzeugt und unabhängig verifiziert,
- Release Record, Release Notes, Known Issues, Manifest und Prüfsummen sind vollständig,
- die Maintainer-Entscheidung referenziert den exakten Commit und die unveränderten Artefakte.

Die generierte [`Release-Candidate-Readiness`](VERSION-1.0-RELEASE-CANDIDATE-READINESS.md) und das [`Blockerregister`](VERSION-1.0-RELEASE-CANDIDATE-BLOCKERS.md) liefern den aktuellen technischen Nachweis.

## 5. Zusätzliche Bedingungen für die stabile Version `1.0.0`

Nach Veröffentlichung des Release Candidate werden zusätzlich abgeschlossen:

- praktischer Review des veröffentlichten Release Candidate,
- Entscheidung, ob ein weiterer Release Candidate erforderlich ist,
- Bestätigung der drei Pilotbaselines gegen konkrete Ziel-Repository-Commits,
- Konsolidierung der wesentlichen Lessons Learned und Abweichungen,
- Erzeugung von Word- und PDF-Publikationen aus demselben freigegebenen Markdown-Quellstand,
- visueller Review von Inhaltsverzeichnis, Tabellen, Seitenumbrüchen und Links,
- dokumentierte SHA-256-Prüfsummen der Publikationsartefakte,
- finaler Release Record und Veröffentlichung des Tags `v1.0.0`.

Eine vollständige technische Migration aller drei Piloten ist nicht automatisch Voraussetzung für `1.0.0`. Der konkrete Mindestnachweis ergibt sich aus den Approved Akzeptanzkriterien, der Pilot-Readiness und einer dokumentierten Releaseentscheidung.

## 6. Bewusst nicht releaseblockierend für Version 1.0

Folgende Arbeiten können nützlich sein, blockieren Version 1.0 aber nicht, sofern kein konkreter Fehler oder fehlender Akzeptanznachweis daraus entsteht:

- zusätzliche optionale Dokumentvorlagen oder Checklisten,
- vollständige technische Verifikation aller drei Pilotwellen,
- direkter Prompt-Manager-Importadapter und Roundtrip-Nachweis,
- weitere Beispielprojekte,
- vollständige Publikationsautomatisierung,
- zusätzliche Metriken oder Dashboards,
- englische normative Ausgabe.

## 7. Bewusst verschobene Themen

Nicht Bestandteil des Version-1.0-Umfangs sind insbesondere:

- vollständiges Linux-Administrationsprofil,
- umfassendes Datenbankprofil,
- vollständiges Container-, Docker- oder Kubernetes-Profil,
- vollständiges Web-API-Profil,
- erweitertes Security-Fachprofil,
- unternehmensweites Governance-Modell für große Organisationen,
- formale Zertifizierung oder externe Konformitätsbestätigung,
- vollständiger automatischer Compliance-Auditor,
- inkompatible Änderung der normativen Sprache oder Dokumenthierarchie,
- Aufteilung des Produktes in mehrere Repositories als Voraussetzung für Version 1.0.

Diese Themen werden nur dann einer späteren Version zugeordnet, wenn Nutzen, Aufwand, Kompatibilität und Migrationswirkung getrennt bewertet wurden.

## 8. Änderungsbudget bis Version 1.0

Neue umfangreiche Themen werden vor Version 1.0 grundsätzlich vertagt. Eine Aufnahme in den Releaseumfang benötigt mindestens:

- ein konkret beschriebenes Problem,
- eine Begründung, warum die Arbeit nicht bis Version 1.1 oder später warten kann,
- eine Auswirkungsanalyse auf Standard, Profile, Prozesse, Vorlagen, Tooling und Piloten,
- eine eindeutige Maintainer-Entscheidung,
- einen überprüfbaren Abschlussnachweis.

## 9. Geplanter Versionsschnitt

- **Version 1.0:** stabiler Kern, erste Profile, operative Prozesse, Releaseevidenz und veröffentlichbare Dokumentation.
- **Version 1.1:** leichterer Einstieg, gefilterte Anwendungssichten, bessere Solo-Developer- und Adoption-Guidance.
- **Version 1.2:** stärkere Pilot- und Betriebsevidenz, mehr Automation und praktisch bestätigte Integrationen.
- **Version 2.0:** nur bei tatsächlich notwendigen inkompatiblen Änderungen mit dokumentierter Migration.

Die detaillierte Planung steht in der Repository-[`ROADMAP.md`](../../ROADMAP.md).
