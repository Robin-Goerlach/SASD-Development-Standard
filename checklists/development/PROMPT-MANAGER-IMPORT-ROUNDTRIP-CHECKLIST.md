# Prompt-Manager-Import-Roundtrip-Checkliste

## Identität und Vorbereitung

- [ ] Exakte Prompt-Manager-Version und Commit-SHA sind dokumentiert.
- [ ] Paket-ID, Paketversion und Paketformat sind dokumentiert.
- [ ] Feldzuordnung ist vollständig ausgefüllt.
- [ ] Test erfolgt in einer isolierten Datenbank oder einem isolierten Datenverzeichnis.
- [ ] Wiederherstellbare Sicherung wurde erstellt.
- [ ] Dry-run wurde ohne Schreiboperationen geprüft.

## Import

- [ ] Alle 39 Prompt-IDs wurden erkannt.
- [ ] Alle Prompttexte wurden ohne Encodingverlust importiert.
- [ ] Kategorien, Tags und Status wurden korrekt abgebildet.
- [ ] Alle 35 Variablen wurden geprüft.
- [ ] Sensitive Variablen erzeugen keine Klartextlogs.
- [ ] Unbekannte Felder werden sichtbar gemeldet.
- [ ] Konfliktstrategie wurde mindestens einmal getestet.
- [ ] Wiederholter Import ist idempotent oder kontrolliert blockiert.

## Export und Vergleich

- [ ] Importierter Bestand wurde wieder exportiert.
- [ ] IDs und Versionen stimmen mit dem Ausgangspaket überein.
- [ ] Prompttexte sind semantisch identisch.
- [ ] Variablen, Kategorien und Tags sind semantisch identisch.
- [ ] Abweichungen sind vollständig dokumentiert.
- [ ] Prüfsummen oder normalisierte Vergleiche wurden archiviert.

## Freigabe

- [ ] Backup-/Rollbacktest war erfolgreich.
- [ ] Importbericht enthält keine Secrets oder personenbezogenen Testdaten.
- [ ] Unterstützter Versionsbereich ist eng und eindeutig formuliert.
- [ ] `prompt_manager_direct_import` wird erst nach bestandenem Roundtrip auf `true` gesetzt.
- [ ] Maintainer-Entscheidung ist dokumentiert.
