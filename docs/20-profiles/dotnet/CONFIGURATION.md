---
title: "Konfiguration und Secrets in .NET"
document-id: SASD-PROF-DOTNET-006
document-type: normative
status: Proposed
version: 0.4.0
standard-version: "1.0"
language: de
authoritative: true
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [DotNet]
depends-on: [SASD-PROF-DOTNET-001, SASD-CORE-006, SASD-CORE-008, SASD-CORE-011]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Konfiguration und Secrets in .NET

## 1. Zweck

Dieses Dokument definiert Konfigurationsquellen, typisierte Optionen, Validierung, Umgebungen, Pfade, lokale Dateien, Feature Flags und Secret-Behandlung für .NET-Projekte.

## 2. Geltungsbereich

Die Regeln gelten für Konfiguration, die das Verhalten einer Anwendung ohne Neukompilierung verändert. Fachliche Benutzerdaten und persistente Anwendungsdaten fallen zusätzlich unter den Persistenzstandard.

## 3. Normative Anforderungen

| ID | Anforderung |
|---|---|
| SASD-DOTNET-REQ-501 | Konfiguration MUSS von ausführbarem Code und fest eingebetteten Geheimnissen getrennt sein. |
| SASD-DOTNET-REQ-502 | Ein Projekt MUSS seine unterstützten Konfigurationsquellen und deren Vorrangreihenfolge dokumentieren. |
| SASD-DOTNET-REQ-503 | Konfigurationswerte SOLLTEN über typisierte Optionsklassen oder gleichwertige validierbare Modelle konsumiert werden. |
| SASD-DOTNET-REQ-504 | Optionsklassen SOLLTEN einen klaren Abschnittsnamen, eine eindeutige Verantwortung und nachvollziehbare Standardwerte besitzen. |
| SASD-DOTNET-REQ-505 | Kritische Optionen MÜSSEN spätestens beim Anwendungsstart validiert werden. |
| SASD-DOTNET-REQ-506 | Ungültige Konfiguration DARF NICHT unbemerkt durch riskante oder zufällige Standardwerte ersetzt werden. |
| SASD-DOTNET-REQ-507 | Standardwerte MÜSSEN sicher, dokumentiert und für die vorgesehene Umgebung geeignet sein. |
| SASD-DOTNET-REQ-508 | Umgebungsspezifische Konfigurationsdateien DÜRFEN NICHT produktive Geheimnisse enthalten. |
| SASD-DOTNET-REQ-509 | Passwörter, Tokens, private Schlüssel und andere Secrets DÜRFEN NICHT in Quellcode, regulären Konfigurationsdateien oder Beispielwerten committed werden. |
| SASD-DOTNET-REQ-510 | Entwicklungssecrets SOLLTEN über User Secrets, Umgebungsvariablen oder einen lokalen Secret Store verwaltet werden. |
| SASD-DOTNET-REQ-511 | Production-Secrets MÜSSEN aus einem dafür vorgesehenen Secret-Management- oder Plattformmechanismus bezogen werden. |
| SASD-DOTNET-REQ-512 | Secretwerte DÜRFEN NICHT in Exceptions, Logs, Diagnoseansichten oder Support-Bundles erscheinen. |
| SASD-DOTNET-REQ-513 | Secretrotation und der Umgang mit kompromittierten Werten MÜSSEN für Production dokumentiert sein. |
| SASD-DOTNET-REQ-514 | Datei- und Verzeichnispfade MÜSSEN über Plattform-APIs zusammengesetzt und DÜRFEN NICHT durch unsichere Zeichenkettenverkettung erzeugt werden. |
| SASD-DOTNET-REQ-515 | Benutzerspezifische veränderliche Daten SOLLTEN in den vom Betriebssystem vorgesehenen Benutzerverzeichnissen gespeichert werden. |
| SASD-DOTNET-REQ-516 | Maschinenweite veränderliche Daten MÜSSEN an einem geeigneten, berechtigungsgeschützten Ort liegen. |
| SASD-DOTNET-REQ-517 | Das Installationsverzeichnis SOLLTE nicht als regulärer Speicherort für veränderliche Benutzerdaten verwendet werden. |
| SASD-DOTNET-REQ-518 | Ein portabler Modus MUSS ausdrücklich aktiviert, dokumentiert und hinsichtlich Schreibrechten, Backup und Geheimnissen bewertet werden. |
| SASD-DOTNET-REQ-519 | Konfigurationsdateien MÜSSEN eine definierte Kodierung und ein robustes Verhalten bei fehlenden, beschädigten oder teilweise geschriebenen Dateien besitzen. |
| SASD-DOTNET-REQ-520 | Schreibvorgänge an wichtige lokale Konfiguration SOLLTEN atomar oder mit geeigneter Wiederherstellung erfolgen. |
| SASD-DOTNET-REQ-521 | Konfigurationsschemaänderungen MÜSSEN versioniert oder anderweitig migrationsfähig sein, wenn bestehende Installationen betroffen sind. |
| SASD-DOTNET-REQ-522 | Unbekannte Konfigurationswerte SOLLTEN nicht stillschweigend verloren gehen, wenn Dateien von mehreren Versionen bearbeitet werden können. |
| SASD-DOTNET-REQ-523 | Dynamisch neu ladbare Konfiguration SOLLTE nur verwendet werden, wenn Thread-Sicherheit, Gültigkeit und Fehlerverhalten definiert sind. |
| SASD-DOTNET-REQ-524 | Änderungen an sicherheits- oder betriebsrelevanter Konfiguration SOLLTEN nachvollziehbar protokolliert werden, ohne Werte offenzulegen. |
| SASD-DOTNET-REQ-525 | Feature Flags MÜSSEN Eigentümer, Zweck, Standardwert und Entfernungskriterium besitzen. |
| SASD-DOTNET-REQ-526 | Abgelaufene oder dauerhaft aktivierte temporäre Feature Flags SOLLTEN entfernt werden. |
| SASD-DOTNET-REQ-527 | Konfiguration für Tests MUSS von realer Production-Konfiguration getrennt sein. |
| SASD-DOTNET-REQ-528 | Beispielkonfigurationen MÜSSEN syntaktisch gültig und frei von realen Geheimnissen oder personenbezogenen Daten sein. |
| SASD-DOTNET-REQ-529 | Konfigurationsquellen und Optionsvalidierung MÜSSEN automatisiert oder durch reproduzierbare Starttests geprüft werden. |
| SASD-DOTNET-REQ-530 | Berechtigungen für Konfigurations- und Secretdateien MÜSSEN dem Schutzbedarf entsprechen. |

## 4. Empfohlene Vorrangreihenfolge

Ein Projekt kann folgende Reihenfolge verwenden und MUSS Abweichungen dokumentieren:

```text
harte sichere Defaults
  < gemeinsame Konfigurationsdatei
  < umgebungsspezifische Konfiguration
  < lokaler Secret Store / Secret Provider
  < Umgebungsvariablen
  < Kommandozeilenargumente
```

Nicht jede Anwendung benötigt alle Quellen.

## 5. Zuordnung zu Qualitätsstufen

| Bereich | Minimum | Recommended | Production |
|---|---|---|---|
| Quellen und Vorrang | dokumentiert MUSS | MUSS | MUSS |
| typisierte Optionen | SOLLTE | MUSS | MUSS |
| Startvalidierung | kritische Werte MUSS | MUSS | MUSS |
| Secret Store | bei Secrets MUSS | MUSS | zentraler Production-Mechanismus MUSS |
| Schema/Migration | bei langlebiger Konfiguration SOLLTE | MUSS | rückwärts- oder migrationsfähig MUSS |
| atomare Schreibweise | bei kritischer Datei SOLLTE | MUSS | MUSS |
| Berechtigungen | MUSS | MUSS | geprüft MUSS |
| Feature-Flag-Lifecycle | KANN | SOLLTE | MUSS bei Verwendung |

## 6. Verantwortlichkeiten

Entwickler definieren Optionsmodelle und Validierung. Betreiber stellen Production-Werte und Secrets bereit. Security-Verantwortliche prüfen Speicherorte und Berechtigungen. Maintainer dokumentieren Pfade, Defaults und Migrationen.

## 7. Nachweise und Prüfkriterien

Nachweise sind Optionsklassen, Validierungsregeln, Starttests, Beispielkonfiguration, Secret-Dokumentation, Pfadkonzept, Dateiberechtigungen und Migrationstests.

## 8. Ausnahmen und Abweichungen

Framework- oder Plattformkonfiguration darf abweichen, wenn Vorrang, Validierung, Schutz und Betriebsverhalten gleichwertig dokumentiert sind.

## 9. Verwandte Dokumente

- [Core Security](../../10-core-standard/SECURITY.md)
- [Logging](LOGGING.md)
- [Persistence](PERSISTENCE.md)
