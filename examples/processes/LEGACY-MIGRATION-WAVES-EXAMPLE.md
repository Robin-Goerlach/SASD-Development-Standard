# Beispiel: Migrationswellen für eine bestehende WinForms-Anwendung

## Welle 0 – Sicherung und Baseline

- Repository und lokale Daten sichern
- Build dokumentieren
- Secrets prüfen
- kritische manuelle Nutzerabläufe erfassen

## Welle 1 – Reproduzierbarkeit

- SDK-Version festlegen
- `.editorconfig` und zentrale Buildregeln einführen
- Baseline-Tests für Persistenz und wichtigste Workflows anlegen

## Welle 2 – Dokumentation und Diagnose

- README, Architekturübersicht und Datenpfade dokumentieren
- strukturiertes Logging ergänzen
- bekannte Fehler und technische Schulden erfassen

## Welle 3 – Struktur mit Bedarf

- nur tatsächlich getrennte Verantwortlichkeiten in Projekte oder Komponenten auslagern
- langfristige Entscheidungen als ADR dokumentieren
- keine pauschale Clean-Architecture-Neuentwicklung

## Welle 4 – Releasebaseline

- Releasebuild, Smoke-Tests, Changelog und Backup-/Rollbackhinweise einführen
- Alignment erneut bewerten
