# Security Policy

## Supported versions

TaskHost Local befindet sich vor dem ersten stabilen Release. Sicherheitskorrekturen werden grundsätzlich nur auf dem aktuellen Stand des Branches `main` vorbereitet.

| Version | Unterstützt |
|---|---|
| aktueller `main`-Stand | ja |
| ältere Arbeitsstände | nein |

## Sicherheitslücken melden

Bitte veröffentliche vermutete Sicherheitslücken, Datenverlustrisiken oder Wege zur Offenlegung lokaler Aufgabendaten **nicht als öffentliches GitHub Issue**.

Verwende stattdessen die private Funktion des Repositories:

1. Repository auf GitHub öffnen.
2. **Security** auswählen.
3. **Advisories** beziehungsweise **Report a vulnerability** öffnen.
4. Beschreibung, betroffene Version, Reproduktionsschritte und mögliche Auswirkungen angeben.

## Schutzbereich

Besonders relevant sind:

- ungewollter Zugriff auf die lokale SQLite-Datenbank,
- Verlust oder Beschädigung von Aufgaben und Listen,
- unsichere Backup-Dateien,
- Pfadmanipulation,
- versehentlich eingecheckte Datenbanken oder private Daten,
- verwundbare NuGet-Abhängigkeiten,
- unerwartete Netzwerkkommunikation.

## Datenschutz

TaskHost Local arbeitet im MVP lokal und ohne Telemetrie. Aufgaben können dennoch private oder geschäftliche Inhalte enthalten. Diagnoseprotokolle dürfen deshalb keine Aufgabentitel, Beschreibungen oder sonstige Inhaltsdaten protokollieren.
