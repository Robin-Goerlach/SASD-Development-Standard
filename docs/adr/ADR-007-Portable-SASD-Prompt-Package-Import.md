# ADR-007: Portables SASD-Promptpaket als Importgrenze

- Status: Accepted
- Datum: 2026-07-27

## Kontext

Der SASD Development Standard veröffentlicht Prompts im Format `sasd-prompt-package/1.0`. Der
Prompt Manager besitzt dagegen ein internes, entwicklungsfähiges JSON-Datenmodell. Eine direkte
Übernahme der internen Speicherdateien würde beide Produkte unnötig koppeln.

## Entscheidung

Der Prompt Manager implementiert einen expliziten Application-Service-Adapter. Er liest das
portable Paket, validiert dessen Manifest und Prüfsummen, erzeugt eine Vorschau und verwendet für
die Speicherung ausschließlich vorhandene `PromptService`- und `CategoryService`-Operationen.

Die stabile Paket-Prompt-ID wird als externe Identität in Source und Notes erhalten. Candidate-
Prompts werden als `NeedsReview` importiert. Vor dem Schreiben entsteht eine Dateisicherung.

## Konsequenzen

- Paket- und Speicherformat können unabhängig versioniert werden.
- Importregeln sind automatisiert testbar.
- Ein Import ist wegen dateibasierter Einzeloperationen nicht vollständig transaktional.
- Für neue Paketformatversionen sind neue Reader oder Migrationen erforderlich.
- Ein erfolgreicher Roundtrip muss gegen reale Releasepakete geprüft werden.
