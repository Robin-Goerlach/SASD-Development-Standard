# Migrationshinweise für Migrationswelle 01

**Stand:** 2026-07-24

## 1. Vor dem ersten Start

Eine bestehende Datenbank darf nicht ungesichert für den ersten Test verwendet werden.

```powershell
.\scripts\backup-taskhost-data.ps1
```

Standardziel:

```text
%UserProfile%\Documents\SASD-TaskHostLocal-Backups
```

Das Skript erstellt eine Kopie und zeigt deren SHA-256-Prüfsumme an.

## 2. Verhalten des Updates

Die Initialisierung verwendet ausschließlich additive und idempotente Anweisungen:

- vorhandene Tabellen werden nicht gelöscht,
- vorhandene Aufgaben und Listen werden nicht überschrieben,
- fehlende Indizes werden ergänzt,
- die interne Schemaversion wird auf `1` gesetzt,
- eine Standardliste wird nur bei vollständig leerer Listentabelle angelegt.

## 3. Testreihenfolge

1. Repository-Update einspielen.
2. bestehende Datenbank sichern.
3. `scripts/verify-wave-01.ps1` ausführen.
4. Anwendung zunächst mit einer frischen Testdatenbank starten.
5. Anwendung anschließend mit einer Kopie der vorhandenen Datenbank testen.
6. Erst nach erfolgreichem Test die normale Produktivdatei verwenden.

## 4. Rückkehr zum vorherigen Stand

Bei einem Problem:

1. Anwendung schließen.
2. betroffene Datenbank separat sichern und nicht löschen.
3. Code auf den vorherigen Commit zurücksetzen.
4. gesicherte Datenbankkopie an den ursprünglichen Pfad zurückkopieren.
5. Diagnoseprotokoll aus `%LocalAppData%\SASD\TaskHostLocal\logs` prüfen.

## 5. Keine automatische Reparatur

Migrationswelle 01 löscht oder ersetzt keine beschädigte Datenbank automatisch. Eine automatische „Reparatur“ könnte Datenverlust verdecken und ist daher bewusst nicht Bestandteil dieses Updates.
