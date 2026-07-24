# Changelog

Alle nennenswerten Änderungen an **SASD TaskHost Local** sollen in dieser Datei dokumentiert werden.

Das Format orientiert sich pragmatisch an einer einfachen Versionshistorie. Die Versionierung ist vorerst projektintern zu verstehen und wird erst nach einem stabilen lauffähigen Stand als Release-Version relevant.

## Unreleased

### Added

- Erstes Pilot-Alignment zum SASD Development Standard dokumentiert.
- Separates xUnit-Testprojekt mit SQLite-Integrationstests ergänzt.
- Tests für Datenbankinitialisierung, Bestandsdaten, Listen, Aufgaben, Suche, Statuswechsel und Backup ergänzt.
- Windows-CI für Restore, Build, Tests, Coverage und NuGet-Audit ergänzt.
- Dependabot für NuGet und GitHub Actions eingerichtet.
- `global.json`, `.editorconfig`, `Directory.Build.props` und zentrale Paketverwaltung ergänzt.
- Startdiagnose unter `%LocalAppData%\SASD\TaskHostLocal\logs` ergänzt.
- `SECURITY.md`, MIT License und ADR-006 ergänzt.
- PowerShell-Skripte für Datensicherung und technische Verifikation ergänzt.
- Statischer Wave-01-Validator ergänzt.
- Projekt als lokales Windows-Forms-/SQLite-Vorhaben angelegt.
- Erste Repository- und Dokumentationsstruktur aufgebaut.
- Strategische Einordnung, Lastenheft, Pflichtenheft, UI-Konzept, Datenmodell, Roadmap und manueller Testplan ergänzt.

### Changed

- `Microsoft.Data.Sqlite` innerhalb der .NET-8-Linie auf 8.0.29 aktualisiert.
- Datenbankpfad ist für isolierte Integrationstests konfigurierbar.
- Datenbankinitialisierung erfolgt transaktional, idempotent und mit Objektprüfung.
- Schemaversion und zusätzlicher Aufgabenindex ergänzt.
- Sortierung von Aufgaben mit optionalem Fälligkeitsdatum explizit als `CASE` formuliert.
- Known Issues und manueller Testplan auf Migrationswelle 01 aktualisiert.
- Dateirechte im Repository normalisiert (`100755` → `100644`).
- Dokumentation stärker auf Lastenheft/Pflichtenheft v0.2 ausgerichtet.

### Verification pending

- .NET Restore, Build und Tests müssen nach dem Einspielen lokal oder über GitHub Actions ausgeführt werden.
- Der historische SQLite-Startfehler bleibt bis zum erfolgreichen Windows-Smoke-Test in Verifikation.

### Known Issues

- Der historische SQLite-Startfehler benötigt noch einen manuellen Windows-Smoke-Test.
- README-Screenshot fehlt noch.

## v0.1.0 – Initialer Arbeitsstand

### Added

- Erste C# WinForms-Anwendung.
- SQLite-Anbindung über `Microsoft.Data.Sqlite`.
- Grundstruktur mit Forms, Models, Services, Repositories und Database.
- Grundlegende Listen- und Aufgabenlogik.
- Erste README-Datei.

### Status

- Build wurde im damaligen Arbeitsstand als erfolgreich dokumentiert.
- Der Stand war wegen eines gemeldeten SQLite-Laufzeitfehlers noch nicht arbeitsfähig.
