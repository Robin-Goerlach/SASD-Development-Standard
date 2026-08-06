---
title: "Referenzimplementierungskatalog"
document-id: SASD-REF-PILOT-008
document-type: informative
status: Draft
version: 0.1.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-08-06
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-REF-PILOT-001, SASD-REF-PILOT-002, SASD-REF-PILOT-003]
---

# Referenzimplementierungskatalog

Dieser Katalog verbindet den SASD Development Standard mit öffentlich erreichbaren Referenzprojekten. Der vollständige Produktquellcode verbleibt im jeweiligen Ziel-Repository. Dieses Repository versioniert Auswahl, Einordnung, den festgehaltenen Ziel-Commit und die zugehörige Evidenz.

## C# / .NET

### SASD TaskHost Local

| Merkmal | Wert |
|---|---|
| Pilot | `SASD-PILOT-001` |
| Repository | [Robin-Goerlach/SASD-TaskHost-Local](https://github.com/Robin-Goerlach/SASD-TaskHost-Local) |
| Standardprofile | Core, DotNet, Desktop |
| Qualitätsstufe | Recommended |
| Plattform | Windows, .NET 8, Windows Forms, SQLite |
| Beobachteter Branch | `main` |
| Gepinnter Ziel-Commit | `2404feb0904b22274972b5803520e6d86a70047d` |
| Aktueller Nachweisumfang | exakter Remote-Checkout, Restore, Build, verfügbare Tests, NuGet-Audit und Publish |
| Noch offen | Wave-01-Integration im Ziel-Repository, verpflichtende Tests, Headless-Self-Check, manueller Windows-Smoke-Test und Pilotabschluss |

Der gepinnte Commit ist eine unveränderliche Baseline für den Remote-Nachweis. Ein erfolgreicher Baseline-Workflow bedeutet noch nicht, dass Wave 01 oder der Pilot abgeschlossen ist.

## Java

Für Version 1.0 ist noch keine Java-Referenzimplementierung registriert oder technisch verifiziert. Eine spätere Java-Anwendung soll als eigenständiges öffentliches Repository aufgenommen werden, nicht als Quellcodekopie innerhalb des Standard-Repositorys.

## Weitere Technologien

Weitere Referenzimplementierungen können nach demselben Modell ergänzt werden:

1. eigenständiges Ziel-Repository,
2. eindeutige Pilot-ID,
3. festgehaltener Ziel-Commit,
4. profil- und qualitätsstufengerechte Prüfungen,
5. getrennte Baseline-, Implementierungs-, Verifikations- und Abschlusszustände.
