# SASD-Promptpaket-Import

## Zweck

Phase 25 ergänzt einen kontrollierten Importadapter für das portable Austauschformat
`sasd-prompt-package/1.0`. Der Adapter importiert versionierte Promptbibliotheken, ohne das
interne JSON-Speicherformat des Prompt Managers nach außen zu koppeln.

## Bedienung

1. `Datei > Import > SASD-Promptpaket importieren...` öffnen.
2. ZIP-Datei oder entpackten Paketordner auswählen.
3. `Analysieren` ausführen.
4. Paketidentität, Prüfsummen und Importvorschau prüfen.
5. Duplikatstrategie wählen.
6. Import bestätigen.

Vor der ersten Änderung kopiert die Anwendung sämtliche JSON-Dateien des Datenverzeichnisses
nach `backups/prompt-package-imports/<Zeitstempel>-<Paket>-<Version>`.

## Sicherheits- und Integritätsprüfungen

- nur `sasd-prompt-package/1.0` mit Schema 1.0;
- höchstens 50 MiB ZIP-, 100 MiB entpackte und 4 MiB Einzeldateigröße;
- Schutz vor absoluten Pfaden und `..`-Traversal;
- höchstens 1000 Dateien;
- SHA-256-Prüfung aller im Paket registrierten Dateien;
- zusätzliche Prüfung jeder Promptdatei gegen den Katalog;
- eindeutige Prompt- und Kategorie-IDs;
- Übereinstimmung von Manifest, Katalog und Paketversion;
- Kandidaten werden als `NeedsReview`, nicht als `Active`, importiert.

## Duplikate

Die stabile Prompt-ID wird in `Source` und `Notes` gespeichert. Beim erneuten Import stehen
folgende Strategien zur Verfügung:

- **Skip**: bestehende IDs unverändert lassen (Standard);
- **Update**: bestehenden Prompt über den Application Service aktualisieren und versionieren;
- **CreateCopy**: zusätzliche, im Titel gekennzeichnete Kopie anlegen.

## Fehler und Wiederherstellung

Der JSON-Speicher arbeitet nicht als gemeinsame Datenbanktransaktion über Kategorien und Prompts.
Ein Abbruch kann daher Teiländerungen hinterlassen. Die Anwendung stoppt beim ersten Fehler,
meldet die Vorab-Sicherung und verändert die Sicherung nicht. Zur manuellen Wiederherstellung:

1. Anwendung schließen;
2. aktuelles Datenverzeichnis zusätzlich sichern;
3. JSON-Dateien aus dem genannten Importbackup zurückkopieren;
4. Anwendung starten und Daten prüfen.
