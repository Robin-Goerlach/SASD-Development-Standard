---
title: "Pilot 01 Projektklassifikation – SASD TaskHost Local"
document-id: SASD-REF-PILOT-103
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
depends-on: [SASD-REF-PILOT-102, SASD-PROC-002, SASD-CORE-006]
---

# Projektklassifikation – SASD TaskHost Local

## 1. Ergebnis

| Dimension | Einstufung | Begründung |
|---|---|---|
| Projektgröße | **Small** | eine Solution mit einem WinForms-Produktprojekt, lokaler Scope, begrenzte Integrationen |
| Lebenszyklus | **langfristig gepflegtes Produkt im MVP-Stadium** | soll kurzfristig nutzbar und später weiterentwickelbar sein |
| Qualitätsstufe | **SASD Recommended** | öffentliche Codebasis, dauerhafte lokale Nutzung, private Aufgaben und Datenpersistenz |
| Risikoklasse | **moderat** | keine Netzwerkkommunikation, aber Integritäts- und Verlustfolgen bei SQLite-Daten |
| Profile | **Core + DotNet + Desktop** | C#/.NET-8-WinForms-Anwendung mit lokaler Persistenz |
| Migrationsmodus | **Legacy-Migration in kleinen Wellen** | bestehender Code und Dokumentation sind vorhanden; kein Rewrite erforderlich |

## 2. Projekttyp

TaskHost Local ist eine lokale Windows-Aufgabenverwaltung mit WinForms und SQLite. Der MVP ist offline-only und besitzt bewusst keine Cloud-, Login- oder Collaboration-Funktionen.

## 3. Schutzbedarf

| Schutzziel | Bewertung | Begründung |
|---|---|---|
| Vertraulichkeit | mittel | Aufgaben und Notizen können private oder geschäftliche Informationen enthalten |
| Integrität | mittel bis hoch | fehlerhafte Datenbankoperationen können Aufgaben oder Listen beschädigen |
| Verfügbarkeit | mittel | Ausfall ist nicht geschäftskritisch, beeinträchtigt aber den persönlichen Arbeitsablauf |
| Wiederherstellbarkeit | hoch relevant | lokale Einzelkopie macht Backup und Restore wichtig |

## 4. Qualitätsstufenentscheidung

**Minimum** wäre zu schwach, weil das Werkzeug dauerhaft genutzt werden soll und persistente Nutzerdaten verarbeitet. **Production** wäre derzeit unverhältnismäßig, da kein externer Service, keine Verfügbarkeitszusage und keine Mehrbenutzerumgebung bestehen.

Recommended bedeutet hier ausdrücklich nicht:

- mehrere Produktionsprojekte,
- komplexe Dependency-Injection-Infrastruktur,
- Domain-Driven Design,
- vollständige Testabdeckung,
- Enterprise-Deployment.

Es bedeutet:

- reproduzierbarer Build,
- stabiler Start und Datenzugriff,
- angemessene automatisierte Tests,
- nachvollziehbare Dokumentation,
- gesicherte Daten- und Releasegrundlagen,
- wartbare einfache Architektur.

## 5. Neubewertungsauslöser

Die Klassifikation wird neu geprüft, wenn:

- Synchronisierung oder Netzwerkkommunikation hinzukommt,
- mehrere Benutzer oder Geräte unterstützt werden,
- personenbezogene Daten Dritter verarbeitet werden,
- TaskHost Local geschäftskritisch eingesetzt wird,
- ein automatisches Update- oder Cloud-Backend eingeführt wird.
