# Build, Test und technische Verifikation

**Stand:** 2026-07-24

## Voraussetzungen

- Windows 10 oder Windows 11,
- .NET 8 SDK 8.0.414 oder neuer im Featureband 8.0.400,
- optional Visual Studio mit Workload `.NET-Desktopentwicklung`.

`global.json` erlaubt den jeweils neuesten installierten Patch des 8.0.400-Featurebands ab SDK 8.0.414.

## Vollständige automatische Prüfung

In PowerShell aus dem Repository-Stamm:

```powershell
.\scripts\verify-wave-01.ps1
```

Das Skript führt aus:

1. SDK-Information,
2. Restore,
3. Release-Build,
4. automatisierte Tests mit Coverage,
5. NuGet-Schwachstellenprüfung.

## Einzelbefehle

```powershell
dotnet restore .\TaskHostLocal.sln
dotnet build .\TaskHostLocal.sln --configuration Release --no-restore
dotnet test .\TaskHostLocal.sln --configuration Release --no-build
dotnet list .\TaskHostLocal.sln package --vulnerable --include-transitive
```

## Statischer SQL- und Strukturtest

Falls Python 3 verfügbar ist:

```powershell
python .\tooling\validate-wave-01.py
```

Dieser Test ersetzt keinen .NET-Build. Er prüft jedoch die Paketstruktur, MSBuild-XML, Solution-Einträge und führt die eingebetteten Schemaanweisungen mit SQLite aus.

## Manueller Starttest

```powershell
dotnet run --project .\TaskHostLocal.WinForms\TaskHostLocal.WinForms.csproj
```

Für einen frischen Start darf eine bestehende Datenbank nur nach vorheriger Sicherung umbenannt werden. Produktive Aufgabendaten dürfen nicht gelöscht werden.

## Diagnoseprotokolle

Bei einem fehlgeschlagenen Programmstart wird – soweit möglich – ein Bericht erzeugt:

```text
%LocalAppData%\SASD\TaskHostLocal\logs\startup-*.log
```

Vor einer öffentlichen Weitergabe ist das Protokoll auf lokale Pfade oder andere personenbezogene Informationen zu prüfen.
