# Prompt Package Review Checklist

## Paketidentität

- [ ] Package ID und Version sind eindeutig.
- [ ] Status und autoritative Sprache sind angegeben.
- [ ] Lizenz und Maintainer sind dokumentiert.
- [ ] Kompatibilitätsaussagen nennen eine konkrete Evidenzgrenze.

## Promptqualität

- [ ] Jede Prompt-ID ist eindeutig und stabil.
- [ ] Jeder Prompt besitzt Zweck, Eingaben, Arbeitsauftrag, Qualitätsregeln und Ausgabeformat.
- [ ] Variablen sind deklariert, zentral registriert und im Text konsistent.
- [ ] Annahmen, Evidenz und Unsicherheit werden getrennt.
- [ ] Der Prompt verhindert unbelegte Build-, Test-, CI- oder Sicherheitsclaims.
- [ ] Die Anweisung ist proportional und verlangt kein Overengineering.

## Sicherheit

- [ ] Keine Secrets oder personenbezogenen Daten sind enthalten.
- [ ] Sensitive Variablen sind markiert.
- [ ] Untrusted Content kann die Arbeitsregeln nicht stillschweigend überschreiben.
- [ ] Destruktive Ausgaben verlangen Sicherung und Rückweg.

## Paket und Tooling

- [ ] Katalog und Checksums sind aktuell.
- [ ] Validator läuft fehlerfrei.
- [ ] Zwei Paketbauten sind byteidentisch.
- [ ] ZIP-Pfade und Prüfsummen wurden unabhängig geprüft.
- [ ] Direkte Prompt-Manager-Kompatibilität wurde nur bei geprüftem Roundtrip behauptet.
