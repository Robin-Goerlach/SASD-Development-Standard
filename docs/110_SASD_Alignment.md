# SASD Development Standard – Pilot Alignment

**Stand:** 2026-07-24  
**Status:** Pilot Alignment – Migrationswelle 01  
**Projekt:** SASD TaskHost Local

## 1. Zweck

Dieses Dokument beschreibt, wie TaskHost Local den derzeit noch nicht freigegebenen SASD Development Standard praktisch erprobt.

Es handelt sich ausdrücklich **nicht** um eine formale Compliance-Erklärung. Die zugrunde liegenden Standarddokumente besitzen noch den Status `Proposed`.

## 2. Projektklassifikation

| Merkmal | Einstufung |
|---|---|
| Projektgröße | Small |
| Qualitätsstufe | Recommended |
| Lebensdauer | langfristig gepflegte Desktopanwendung |
| Risikoprofil | moderat; lokale persönliche oder geschäftliche Aufgabendaten |
| Core Standard | Pilot Alignment |
| C#/.NET Profile | Pilot Alignment |
| Desktop Profile | Pilot Alignment |
| Operational Processes | Pilot Alignment |

## 3. In Migrationswelle 01 umgesetzte Maßnahmen

- SDK-Auswahl über `global.json` dokumentiert.
- gemeinsame Buildregeln über `Directory.Build.props` eingeführt.
- NuGet-Versionen und Audit-Konfiguration zentralisiert.
- Nullable Reference Types und Analyzer-Basis vereinheitlicht.
- SQLite-Paket innerhalb der .NET-8-Linie aktualisiert.
- Datenbankpfad für isolierte Integrationstests injizierbar gemacht.
- Datenbankinitialisierung transaktional und idempotent ausgeführt.
- Schemaversion und Objektprüfung ergänzt.
- Regressionstests für Initialisierung, Listen und Aufgaben ergänzt.
- Windows-CI für Restore, Build, Tests und Paket-Audit ergänzt.
- Dependabot für NuGet und GitHub Actions konfiguriert.
- Startdiagnose ohne Protokollierung von Aufgabeninhalten ergänzt.
- MIT License und Security Policy ergänzt.

## 4. Bewusst nicht umgesetzt

Die erste Welle führt keine neue Architektur um ihrer selbst willen ein. Insbesondere nicht enthalten sind:

- Wechsel von WinForms zu WPF,
- Entity Framework,
- Dependency-Injection-Container,
- Generic Host,
- Aufteilung in Domain-, Application- und Infrastructure-Projekte,
- Repository-Interfaces ohne konkreten Austauschbedarf,
- UI-Neugestaltung,
- Installer oder automatisches Updateverfahren.

## 5. Offene Nachweise

Vor Abschluss der Welle sind auf einem Windows-System noch nachzuweisen:

1. `scripts/verify-wave-01.ps1` läuft vollständig durch.
2. GitHub Actions meldet einen grünen Build.
3. Anwendung startet mit neuer und bestehender Datenbank.
4. Manueller Smoke-Test aus `100_Manual_Test_Plan.md` ist dokumentiert.
5. Backup und Wiederanlauf wurden geprüft.

## 6. Vorläufige Bewertung

| Bereich | Status |
|---|---|
| Repository- und Buildgrundlage | umgesetzt, technische Verifikation ausstehend |
| Datenbankinitialisierung | implementiert und statisch geprüft |
| Automatisierte Tests | implementiert, .NET-Ausführung ausstehend |
| CI | implementiert, erster GitHub-Lauf ausstehend |
| Security und Lizenz | umgesetzt |
| Releasefähigkeit | noch nicht erreicht |
| Formale SASD-Compliance | nicht möglich, Standard noch `Proposed` |
