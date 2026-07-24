---
title: "Persistenz in .NET"
document-id: SASD-PROF-DOTNET-007
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
depends-on: [SASD-PROF-DOTNET-001, SASD-PROF-DOTNET-002, SASD-PROF-DOTNET-006, SASD-CORE-003, SASD-CORE-006, SASD-CORE-008, SASD-CORE-011]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Persistenz in .NET

## 1. Zweck

Dieses Dokument definiert sichere und wartbare Persistenz für relationale Datenbanken, lokale Datenbanken, Dateien und andere dauerhafte Speicher. Es behandelt Datenzugriff, Transaktionen, Migrationen, Integrität, Nebenläufigkeit, Backup und Tests.

## 2. Geltungsbereich

Die Regeln gelten, sobald eine .NET-Anwendung Daten über ihren Prozesslebenszyklus hinaus speichert oder fremde persistente Daten verändert.

## 3. Normative Anforderungen

| ID | Anforderung |
|---|---|
| SASD-DOTNET-REQ-601 | Die Persistenztechnologie MUSS anhand von Datenmenge, Nebenläufigkeit, Integrität, Betrieb, Portabilität und Wiederherstellungsbedarf ausgewählt werden. |
| SASD-DOTNET-REQ-602 | Ein Projekt DARF NICHT allein aus Konventionsgründen eine komplexe Datenzugriffsschicht einführen. |
| SASD-DOTNET-REQ-603 | Persistenzdetails SOLLTEN von fachlicher Logik getrennt sein, wenn Technologieaustausch, Tests oder mehrere Datenquellen einen realen Nutzen haben. |
| SASD-DOTNET-REQ-604 | Datenmodelle, Persistenzmodelle und Transportmodelle SOLLTEN getrennt werden, wenn ihre Lebenszyklen oder Verträge unterschiedlich sind. |
| SASD-DOTNET-REQ-605 | Verbindungszeichenfolgen und Zugangsdaten MÜSSEN nach dem Konfigurations- und Secretstandard behandelt werden. |
| SASD-DOTNET-REQ-606 | Datenbankzugriffe MÜSSEN parametrisierte Abfragen oder sichere Frameworkmechanismen verwenden. |
| SASD-DOTNET-REQ-607 | Dynamisch zusammengesetztes SQL MUSS Eingaben sicher behandeln und SOLLTE auf klar begrenzte Fälle beschränkt werden. |
| SASD-DOTNET-REQ-608 | Verbindungen, Commands, Reader und Transaktionen MÜSSEN deterministisch freigegeben werden. |
| SASD-DOTNET-REQ-609 | Asynchrone Datenzugriffe SOLLTEN Cancellation Tokens unterstützen, wenn Provider und Operation dies erlauben. |
| SASD-DOTNET-REQ-610 | Transaktionsgrenzen MÜSSEN fachlich oder technisch nachvollziehbar sein. |
| SASD-DOTNET-REQ-611 | Eine Transaktion DARF NICHT länger als für den konsistenten Vorgang erforderlich gehalten werden. |
| SASD-DOTNET-REQ-612 | Mehrschrittige Schreibvorgänge MÜSSEN atomar, kompensierbar oder als bewusst eventual-consistent dokumentiert sein. |
| SASD-DOTNET-REQ-613 | Schemaänderungen MÜSSEN versioniert und reproduzierbar sein. |
| SASD-DOTNET-REQ-614 | Migrationen MÜSSEN in definierter Reihenfolge ausgeführt und gegen den erwarteten Ausgangsstand geprüft werden. |
| SASD-DOTNET-REQ-615 | Destruktive Migrationen MÜSSEN Datenverlust, Backup und Rollback oder Vorwärtskorrektur ausdrücklich behandeln. |
| SASD-DOTNET-REQ-616 | Production-Migrationen MÜSSEN vor Freigabe mit repräsentativen Daten oder einem geeigneten Testverfahren geprüft werden. |
| SASD-DOTNET-REQ-617 | Eine Anwendung MUSS erkennen können, ob das Persistenzschema mit ihrer Version kompatibel ist. |
| SASD-DOTNET-REQ-618 | Automatische Migration beim Anwendungsstart SOLLTE nur verwendet werden, wenn Rechte, Parallelstart, Ausfall und Wiederherstellung beherrscht sind. |
| SASD-DOTNET-REQ-619 | Lokale Datenbanken und Dateien MÜSSEN in geeigneten Anwendungsdatenverzeichnissen liegen und DÜRFEN NICHT unbeabsichtigt im Installations- oder Repositoryverzeichnis erzeugt werden. |
| SASD-DOTNET-REQ-620 | Persistente Schreibvorgänge MÜSSEN Fehler, Teilwrites, Speichermangel und Prozessabbruch angemessen berücksichtigen. |
| SASD-DOTNET-REQ-621 | Wichtige Dateien SOLLTEN atomar ersetzt, mit Journalmechanismen geschützt oder anderweitig wiederherstellbar geschrieben werden. |
| SASD-DOTNET-REQ-622 | Datenintegritätsbedingungen MÜSSEN möglichst nahe an der verantwortlichen Daten- oder Domänengrenze durchgesetzt werden. |
| SASD-DOTNET-REQ-623 | Eindeutigkeit, Fremdschlüssel, Nullfähigkeit und Längenbeschränkungen MÜSSEN zwischen Code und Schema konsistent sein. |
| SASD-DOTNET-REQ-624 | Nebenläufigkeitskonflikte MÜSSEN erkannt und mit einer dokumentierten Strategie behandelt werden, wenn mehrere Schreiber möglich sind. |
| SASD-DOTNET-REQ-625 | IDs MÜSSEN stabil, kollisionssicher und für Verteilung oder Synchronisation geeignet sein, sofern diese Anforderungen bestehen. |
| SASD-DOTNET-REQ-626 | Zeitwerte MÜSSEN mit eindeutigem UTC-/Offset- oder fachlichem Zeitzonenmodell gespeichert werden. |
| SASD-DOTNET-REQ-627 | Verschlüsselung ruhender Daten MUSS ein Bedrohungsmodell, Schlüsselmanagement und Wiederherstellung berücksichtigen und DARF NICHT nur durch obskure Dateiformate simuliert werden. |
| SASD-DOTNET-REQ-628 | Backups MÜSSEN konsistent zur Persistenztechnologie erstellt werden und SOLLTEN vor riskanten Migrationen automatisch oder prozessual ausgelöst werden. |
| SASD-DOTNET-REQ-629 | Wiederherstellung MUSS für Recommended- und Production-Projekte dokumentiert und risikobasiert getestet werden. |
| SASD-DOTNET-REQ-630 | Datenexporte MÜSSEN Formatversion, Kodierung, Datenschutz und Fehlerbehandlung definieren. |
| SASD-DOTNET-REQ-631 | Datenimporte MÜSSEN Eingaben validieren und DÜRFEN bestehende Daten nicht ohne Bestätigung, Transaktion oder Wiederherstellungsweg zerstören. |
| SASD-DOTNET-REQ-632 | Aufbewahrung, Löschung und Archivierung MÜSSEN für personenbezogene oder betriebsrelevante Daten definiert sein. |
| SASD-DOTNET-REQ-633 | Persistenzoperationen SOLLTEN relevante Dauer-, Fehler- und Kapazitätsinformationen beobachtbar machen, ohne sensible Inhalte zu protokollieren. |
| SASD-DOTNET-REQ-634 | Persistenztests MÜSSEN die tatsächlich eingesetzte Technologie für migrations-, query- oder providerabhängiges Verhalten angemessen einbeziehen. |
| SASD-DOTNET-REQ-635 | In-Memory-Provider DÜRFEN NICHT als alleiniger Nachweis für provider- oder SQL-spezifisches Verhalten verwendet werden. |
| SASD-DOTNET-REQ-636 | Testdaten MÜSSEN isoliert, reproduzierbar und frei von realen produktiven Geheimnissen oder personenbezogenen Daten sein. |

## 4. Architekturentscheidung

Die Wahl zwischen direktem Providerzugriff, ORM, Repository, Unit of Work, Dateispeicher oder externem Dienst ist eine Architekturentscheidung. Abstraktionen MÜSSEN einen konkreten Nutzen besitzen und dürfen keine Fähigkeiten des Providers unbemerkt verbergen.

## 5. Zuordnung zu Qualitätsstufen

| Bereich | Minimum | Recommended | Production |
|---|---|---|---|
| Technologieentscheidung | kurz begründet MUSS | dokumentiert MUSS | geprüft MUSS |
| Schema/Migration | bei Schema MUSS | reproduzierbar MUSS | getestet und freigegeben MUSS |
| Transaktionen | bei Mehrschrittwrite MUSS | MUSS | MUSS mit Fehler- und Retrystrategie |
| Backup | bei wertvollen Daten SOLLTE | MUSS | automatisiert und getestet MUSS |
| Restore | dokumentiert SOLLTE | getestet SOLLTE | regelmäßig getestet MUSS |
| Concurrency | bei mehreren Schreibern MUSS | MUSS | Last- und Konflikttests SOLLTEN |
| Verschlüsselung | risikobasiert | risikobasiert MUSS | Bedrohungsmodell und Schlüsselmanagement MUSS |
| Provider-Integrationstests | bei providerspezifischem Verhalten SOLLTE | MUSS | MUSS |

## 6. Verantwortlichkeiten

Entwickler definieren Datenverträge, Transaktionen und Migrationen. Betreiber verantworten Production-Zugänge, Backup, Restore und Kapazität. Security-Verantwortliche prüfen Datenklassifikation und Schlüsselmanagement. Reviewer kontrollieren Datenverlust-, Nebenläufigkeits- und Migrationsrisiken.

## 7. Nachweise und Prüfkriterien

Nachweise sind Schema und Migrationen, Datenmodell, Transaktionsdesign, Backup-/Restore-Protokolle, Integrations- und Migrationstests, Datenklassifikation und Betriebsmetriken.

## 8. Ausnahmen und Abweichungen

Ein kurzlebiger Prototyp kann auf Migrationen verzichten, wenn Daten verwerfbar sind und dies dokumentiert ist. Reale oder wertvolle Daten heben diese Ausnahme auf.

## 9. Verwandte Dokumente

- [Configuration](CONFIGURATION.md)
- [Error Handling](ERROR-HANDLING.md)
- [.NET Testing](DOTNET-TESTING.md)
- [Core Maintenance](../../10-core-standard/MAINTENANCE.md)
