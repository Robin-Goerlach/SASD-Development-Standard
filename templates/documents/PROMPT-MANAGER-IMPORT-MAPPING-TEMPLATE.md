# Prompt-Manager-Import-Mapping

## Identität

- Paket-ID:
- Paketversion:
- Paketformat:
- Prompt-Manager-Version:
- Prompt-Manager-Commit:
- Adapterversion:
- Bewertungsdatum:
- Verantwortlich:

## Feldzuordnung

| SASD-Paketfeld | Prompt-Manager-Feld | Transformation | Pflicht | Verlustfrei | Bemerkung |
|---|---|---|---:|---:|---|
| `prompt-id` |  |  | Ja |  |  |
| `title` |  |  | Ja |  |  |
| `version` |  |  | Ja |  |  |
| `status` |  |  | Ja |  |  |
| Prompttext |  |  | Ja |  |  |
| `category` |  |  | Ja |  |  |
| `tags` |  |  | Nein |  |  |
| `variables` |  |  | Ja |  |  |
| `quality-levels` |  |  | Nein |  |  |
| `profiles` |  |  | Nein |  |  |
| `summary` |  |  | Nein |  |  |

## Konfliktstrategie

- Bereits vorhandene Prompt-ID:
- Gleiche Version und gleiche Prüfsumme:
- Gleiche Version und anderer Inhalt:
- Neuere Zielversion:
- Ältere Zielversion:
- Unbekannte Kategorie oder Variable:

## Schutzmaßnahmen

- Backupverfahren:
- Dry-run-Ausgabe:
- Transaktions-/Rollbackverhalten:
- Secret-Maskierung:
- Abbruchbedingungen:

## Roundtrip-Nachweis

- Ausgangs-Commit:
- Importlauf:
- Exportlauf:
- Vergleichswerkzeug:
- Ergebnis:
- Bekannte Verluste:
- Freigabeentscheidung:
