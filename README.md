# SASD TaskHost Local

**TaskHost Local** ist eine lokale Windows-Aufgabenverwaltung für die TaskHost-Projektfamilie. Das Projekt ist bewusst pragmatisch angelegt: Es soll schnell arbeitsfähig werden, lokal ohne Server funktionieren und trotzdem so sauber strukturiert sein, dass spätere Weiterentwicklung, Debugging und eine mögliche Integration in TaskHost nicht verbaut werden.

> English summary: TaskHost Local is a small local Windows task management application built with C#, Windows Forms and SQLite. It is part of the TaskHost project family, but the MVP is intentionally offline-only and does not include cloud sync, collaboration or a TaskHost API connection.

## Projektstatus

| Bereich | Status |
|---|---|
| Repository | vorhanden |
| Grundprojekt | vorhanden |
| Buildbasis | .NET 8, zentrale Konfiguration und Windows-CI vorbereitet |
| Automatisierte Tests | SQLite-Integrationstests vorhanden; erster CI-Lauf ausstehend |
| Historischer SQLite-Startfehler | technisch abgesichert, manueller Windows-Smoke-Test ausstehend |
| Dokumentation | Migrationswelle 01 dokumentiert |
| Lizenz | MIT License |
| Screenshot | noch zu ergänzen |

TaskHost Local ist der erste praktische Pilot des **SASD Development Standard**. Die Anwendung richtet sich am Core Standard sowie am C#/.NET- und Desktopprofil auf der Qualitätsstufe **Recommended** aus. Da diese Standardteile noch `Proposed` sind, wird dies als Pilot Alignment und nicht als formale Compliance bezeichnet.

Die frühere Meldung `SQLite Error 1: near "=": syntax error` konnte aus dem aktuellen öffentlichen Quellstand nicht eindeutig reproduziert oder einer bestimmten SQL-Zeile zugeordnet werden. Migrationswelle 01 ergänzt deshalb transaktionale Initialisierung, Regressionstests und Startdiagnose. Der Known Issue bleibt bis zum erfolgreichen Windows-Smoke-Test in Verifikation.

## Ziel des MVP

Das MVP soll eine einfache, lokale und alltagstaugliche Aufgabenverwaltung bereitstellen.

Der Fokus liegt auf:

- lokalen Aufgabenlisten,
- Aufgaben mit Titel, Notiz, Fälligkeit und Priorität,
- erledigt/offen-Status,
- einfacher Suche,
- lokaler SQLite-Speicherung,
- einfacher Datenbanksicherung,
- klassischer Windows-Bedienung mit Menüleiste und Toolbar.

Das Projekt soll **nicht** durch Cloud, Synchronisierung, Login, Benutzerverwaltung oder Collaboration verlangsamt werden.

## Nicht-Ziele des MVP

Nicht Bestandteil der ersten Version:

- Cloud-Synchronisierung,
- Multi-Geräte-Synchronisierung,
- geteilte Listen,
- Benutzerkonten,
- Rechteverwaltung,
- Kommentare oder Collaboration,
- mobile Apps,
- aktive Windows-Benachrichtigungen,
- Hintergrunddienst,
- komplexe Wiederholungslogik,
- direkte TaskHost-API-Anbindung,
- Telemetrie,
- automatische Update-Prüfung,
- Netzwerkkommunikation zur Laufzeit.

## Verhältnis zu TaskHost

TaskHost Local ist **kein konkurrierendes Produkt** zum bestehenden TaskHost-Projekt.

Die strategische Einordnung lautet:

> TaskHost Local ist eine eigenständige lokale Windows-Aufgabenverwaltung, die kurzfristig produktiv nutzbar werden soll und langfristig als möglicher Desktop- oder Offline-Client der TaskHost-Produktfamilie vorbereitet wird.

Für das MVP bedeutet das:

- TaskHost Local arbeitet eigenständig.
- Es gibt keine API-Anbindung.
- Es gibt keinen Login.
- Es gibt keine Synchronisierung.
- Die Begriffe und Datenstrukturen sollen dennoch kompatibel genug bleiben, damit Migration, Export/Import oder spätere API-Anbindung nicht unnötig erschwert werden.

## Technik

| Bereich | Entscheidung |
|---|---|
| Sprache | C# |
| Framework | .NET 8 Windows |
| Oberfläche | Windows Forms |
| Datenbank | SQLite |
| Datenbankbibliothek | Microsoft.Data.Sqlite |
| ORM | keines |
| Zielplattform MVP | Windows |
| Architektur | einfache Schichtung: Forms → Services → Repositories → Database |

## Start in Visual Studio

1. Visual Studio öffnen.
2. `TaskHostLocal.sln` öffnen.
3. NuGet-Pakete wiederherstellen, falls Visual Studio dies nicht automatisch erledigt.
4. Projekt `TaskHostLocal.WinForms` starten.

Voraussetzung:

- Workload **.NET-Desktopentwicklung**.

## Start per Kommandozeile

```powershell
.\scripts\verify-wave-01.ps1
dotnet run --project .\TaskHostLocal.WinForms\TaskHostLocal.WinForms.csproj
```

Da Windows Forms verwendet wird, sollte die Anwendung unter Windows gestartet werden. Ein Build aus WSL kann funktionieren, der eigentliche Programmstart sollte aber bevorzugt in einer Windows-Umgebung erfolgen.

## Speicherort der Datenbank

Die lokale SQLite-Datenbank liegt absichtlich nicht im Programmverzeichnis, sondern im Benutzerprofil:

```text
%AppData%\SASD\TaskHostLocal\taskhost.db
```

Beispiel:

```text
C:\Users\<Benutzername>\AppData\Roaming\SASD\TaskHostLocal\taskhost.db
```

Vorteile:

- keine Adminrechte erforderlich,
- Daten bleiben bei Programmupdates erhalten,
- Daten liegen benutzerspezifisch,
- Backups können nachvollziehbar erstellt werden.

## Architekturüberblick

```text
TaskHostLocal.sln
├── TaskHostLocal.WinForms
│   ├── Forms/          Dialoge und zusätzliche Fenster
│   ├── Models/         einfache Datenmodelle
│   ├── Services/       fachliche Operationen und Koordination
│   ├── Repositories/   SQLite-Zugriff mit parametrisierten SQL-Abfragen
│   ├── Database/       Datenbankpfad, Verbindung, Initialisierung
│   ├── Diagnostics/    lokale Startdiagnose ohne Aufgabendaten
│   ├── MainForm.cs     Hauptfenster und UI-Koordination
│   └── Program.cs
└── TaskHostLocal.Tests/    SQLite-Integrationstests
```

Wichtige Architekturregel:

> SQL gehört nicht in Formularcode. Formulare rufen Services auf, Services verwenden Repositories, Repositories kapseln SQLite.

## Dokumentation

Wichtige Dokumente:

| Dokument | Zweck |
|---|---|
| `docs/000_Project_Overview.md` | Projektüberblick |
| `docs/010_Strategic_Positioning.md` | strategische Einordnung und Verhältnis zu TaskHost |
| `docs/020_Lastenheft_MVP.md` | fachliche Anforderungen an das MVP |
| `docs/030_Pflichtenheft_MVP.md` | technische Umsetzung des MVP |
| `docs/040_UI_Concept.md` | UI-Richtung und Zielbild |
| `docs/050_Technical_Design.md` | technische Architektur |
| `docs/060_Data_Model.md` | SQLite-Datenmodell und Erweiterungen |
| `docs/070_Roadmap.md` | Entwicklungsplanung |
| `docs/080_Known_Issues.md` | bekannte Fehler und Risiken |
| `docs/090_Documentation_Checklist.md` | Dokumentations- und Projektcheckliste |
| `docs/100_Manual_Test_Plan.md` | manueller Testplan für MVP-Abnahme |
| `docs/110_SASD_Alignment.md` | Pilot Alignment zum SASD Development Standard |
| `docs/120_Wave_01_Review.md` | Review und offene Nachweise der ersten Migrationswelle |
| `docs/130_Build_and_Test.md` | Build-, Test- und Audit-Anleitung |
| `docs/140_Migration_Notes.md` | Datensicherung, Testreihenfolge und Rollback |
| `docs/adr/` | Architekturentscheidungen |

## Datenschutz und lokale Daten

Aufgaben können private oder geschäftliche Informationen enthalten. Deshalb gilt:

- keine echten Aufgaben in Screenshots,
- keine `.db`-Dateien ins Repository,
- keine Backup-Dateien ins Repository,
- keine Zugangsdaten oder Secrets ins Repository,
- keine Telemetrie im MVP,
- keine Netzwerkkommunikation im MVP.

## Nächste technische Schritte

1. Update einspielen und `scripts/verify-wave-01.ps1` ausführen.
2. Ersten GitHub-Actions-Lauf prüfen.
3. Anwendung mit frischer Datenbank starten.
4. Gesicherte vorhandene Datenbank testen.
5. manuellen Smoke-Test dokumentieren.
6. historischen SQLite-Known-Issue erst danach schließen.
7. Backup-Funktion und Wiederherstellung vertiefen.
8. README-Screenshot mit ausschließlich fiktiven Daten ergänzen.

## Lizenz

Dieses Projekt steht unter der [MIT License](LICENSE). Die Entscheidung ist in `docs/adr/ADR-006-Use-MIT-License.md` dokumentiert.
