---
title: "Pilot 02 Projektklassifikation – SASD Prompt Manager"
document-id: SASD-REF-PILOT-203
document-type: informative
status: Draft
version: 0.11.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-25
applies-to-quality-levels: [Recommended]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-REF-PILOT-202, SASD-PROC-002, SASD-CORE-006]
---

# Projektklassifikation – SASD Prompt Manager

## 1. Ergebnis

| Dimension | Einstufung | Begründung |
|---|---|---|
| Projektgröße | **Medium** | vier Produktionsprojekte, mehrere fachliche Bereiche, lokale Persistenz, Import/Export, Backup und umfangreiche Bedienoberfläche |
| Lebenszyklus | **langfristig gepflegtes Produkt** | soll als zentrale Prompt Engineering Workbench weiterentwickelt und praktisch genutzt werden |
| Qualitätsstufe | **SASD Recommended** | öffentliche Codebasis, dauerhafte lokale Daten und sicherheitsrelevante Promptinhalte; noch kein geschäftskritischer Mehrbenutzerdienst |
| Risikoklasse | **moderat bis erhöht** | Prompts können API-Schlüssel, Passwörter, interne Informationen oder Kundendaten enthalten |
| Profile | **Core + DotNet + Desktop** | C#/.NET-Desktopanwendung mit Schichtenmodell und lokaler Datenverwaltung |
| Migrationsmodus | **kontrollierte Bestandsmigration** | vorhandene Struktur und Tests werden ergänzt, nicht ersetzt |

## 2. Schutzbedarf

| Schutzziel | Bewertung | Begründung |
|---|---|---|
| Vertraulichkeit | hoch relevant | Prompttexte können Secrets oder vertraulichen Projektkontext enthalten |
| Integrität | hoch | Verlust oder falsche Versionierung kann zentrale Arbeitsartefakte beschädigen |
| Verfügbarkeit | mittel | Ausfall stört Arbeitsabläufe, ist aber derzeit kein 24/7-Service |
| Wiederherstellbarkeit | hoch | lokale Einzelplatzdaten erfordern nachgewiesene Backups und Imports |

## 3. Neubewertungsauslöser

Production ist neu zu prüfen, wenn Teamnutzung, Cloud-Synchronisierung, direkte Provideranbindung, zentrale Unternehmensdaten oder geschäftskritische Automatisierungen hinzukommen.
