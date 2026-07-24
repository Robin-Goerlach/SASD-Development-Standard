# Beispiel: ADR-0001 – SQLite als lokale Persistenz

- Status: Accepted
- Datum: 2026-07-24

## Kontext

Eine lokale Desktopanwendung benötigt strukturierte Persistenz, Transaktionen und einfache Sicherung ohne separaten Datenbankserver.

## Optionen

1. JSON-Dateien: einfach, aber schwächer bei Abfragen, parallelen Änderungen und Migrationen.
2. SQLite: eingebettet, transaktional, gut sicherbar, erfordert Schema- und Migrationsdisziplin.
3. Externer Datenbankserver: leistungsfähig, aber für ein lokales Einzelplatzwerkzeug unverhältnismäßig.

## Entscheidung

SQLite wird verwendet. Das Datenbankschema erhält versionierte Migrationen; Sicherung und Wiederherstellung werden dokumentiert.

## Konsequenzen

- Positiv: keine Serverabhängigkeit, Transaktionen, gute Abfragemöglichkeiten.
- Negativ: Schemaänderungen und Datei-Locking müssen bewusst behandelt werden.
- Folgemaßnahme: Migrationstest und Backup-Smoke-Test vor dem ersten Release.
