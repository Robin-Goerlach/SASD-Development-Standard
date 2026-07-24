# TaskHost Local – Migrationswelle 01 Update Manifest

**Erstellt:** 2026-07-24

## Zweck

Dieses Paket wird direkt über den Stamm des bestehenden Repositories `SASD-TaskHost-Local` entpackt. Es enthält neue und geänderte Dateien für die erste Migrationswelle des SASD-Development-Standard-Piloten.

## Hauptänderungen

- Build- und Paketkonfiguration,
- .NET-SDK-Auswahl,
- SQLite-Härtung und Testbarkeit,
- automatisierte Integrationstests,
- GitHub Actions und Dependabot,
- Security Policy und MIT License,
- Pilot-Alignment und Wave-Review,
- lokale und statische Prüfscripte.

## Verifikation nach dem Entpacken

```powershell
.\scripts\backup-taskhost-data.ps1
python .\tooling\validate-wave-01.py
.\scripts\verify-wave-01.ps1
```

Danach folgt der manuelle Windows-Test gemäß `docs/100_Manual_Test_Plan.md`.

## Wichtiger Statushinweis

Die .NET- und Windows-Verifikation war in der Erstellungsumgebung nicht möglich. Das Paket behauptet daher nicht, dass der historische Startfehler bereits praktisch geschlossen ist. Erst ein erfolgreicher lokaler Test und ein grüner CI-Lauf schließen die Migrationswelle ab.
