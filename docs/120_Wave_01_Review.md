# Migrationswelle 01 – Review Record

**Stand:** 2026-07-24  
**Status:** Implementierung vorbereitet – Windows- und CI-Verifikation ausstehend

## 1. Ziel

Migrationswelle 01 soll den dokumentierten SQLite-Startfehler nachvollziehbar untersuchen, die Persistenz regressionssicher machen und die kleinste tragfähige Qualitätsbasis für ein langfristig gepflegtes WinForms-Projekt herstellen.

## 2. Analyseergebnis zum historischen SQLite-Fehler

Der öffentlich sichtbare Quellstand enthält keine eindeutig fehlerhafte SQL-Anweisung. Die Schemaanweisungen sowie die Abfragen zum Laden und Suchen von Aufgaben wurden zusätzlich mit SQLite ausgeführt und waren syntaktisch gültig.

Daraus folgt:

- Der historische Fehler wird nicht ohne Beleg einer bestimmten Codezeile zugeschrieben.
- Die alte Beobachtung kann aus einem früheren Stand, einer abweichenden lokalen Datei oder einer inzwischen veränderten Abfrage stammen.
- Die Behebung wird erst nach einem erfolgreichen Windows-Starttest als abgeschlossen markiert.

## 3. Technische Maßnahmen

### Datenbank

- expliziter Datenbankpfad für Integrationstests,
- transaktionale Initialisierung,
- idempotente Standardliste,
- `PRAGMA user_version`,
- Prüfung erforderlicher Tabellen und Indizes,
- Fremdschlüssel und Busy-Timeout,
- klarere `CASE`-Sortierung bei optionalem Fälligkeitsdatum.

### Tests

Automatisierte Integrationstests decken ab:

- Erzeugung des Schemas,
- wiederholte Initialisierung,
- Standardliste,
- Fremdschlüsselverletzung,
- Listen anlegen und umbenennen,
- leere Aufgabenliste laden,
- Aufgaben anlegen und laden,
- Suche in Titel und Beschreibung,
- Erledigt-Status umschalten.

### Build und Supply Chain

- SDK-Rollforward innerhalb des .NET-8-Featurebands,
- zentrale Paketversionen,
- NuGet-Audit,
- Windows-CI,
- Dependabot,
- Testartefakte und Coverage-Ausgabe.

### Diagnose

Ein unbehandelter Startfehler erzeugt unter `%LocalAppData%\SASD\TaskHostLocal\logs` einen Diagnosebericht. Aufgabeninhalte werden nicht protokolliert; die bestehende Datenbank wird bei einem Fehler weder gelöscht noch automatisch ersetzt.

## 4. Durchgeführte Prüfung in der Erstellungsumgebung

- Paketstruktur statisch geprüft,
- MSBuild-XML geparst,
- Solution-Eintrag für Testprojekt geprüft,
- eingebettete Schema-SQL mit Python SQLite ausgeführt,
- Repository-Abfragen als SQLite-Smoke-Test ausgeführt.

Nicht durchgeführt werden konnten:

- `dotnet restore`,
- `dotnet build`,
- `dotnet test`,
- WinForms-Programmstart,
- Test gegen eine vorhandene produktive Benutzerdatei.

Der Grund ist, dass in der Erstellungsumgebung kein .NET SDK und keine Windows-Desktoplaufzeit verfügbar waren.

## 5. Abschlusskriterien

Die Welle darf erst auf `Completed` gesetzt werden, wenn:

- automatisches PowerShell-Prüfskript erfolgreich ist,
- GitHub Actions erfolgreich ist,
- frischer Start ohne Fehlerdialog funktioniert,
- Start mit gesicherter vorhandener Datenbank funktioniert,
- manueller Smoke-Test dokumentiert ist,
- keine offene Blocker- oder Major-Abweichung verbleibt.

## 6. Overengineering-Review

Die bestehende Schichtung `Forms → Services → Repositories → Database` bleibt erhalten. Die Welle ergänzt Testbarkeit, Nachweise und Diagnose, ohne eine für das kleine Projekt unangemessene Architektur einzuführen.
## 7. Verifikations-Harness

Wave 01 besitzt nun einen kopflosen Selbsttest, einen einheitlichen lokalen/CI-Lauf und einen geschützten Closeout-Prozess. Diese Ergänzungen erhöhen die Nachweisfähigkeit, ändern den Status der Welle aber noch nicht.

Der Abschluss bleibt ausstehend, bis `docs/160_Wave_01_Closeout.md` vollständig belegt und ein commitbezogener Verifikationsnachweis erzeugt wurde.
