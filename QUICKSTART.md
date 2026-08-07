# SASD Quick Start

> **Ziel:** In wenigen Minuten produktiv mit SASD beginnen, ohne vorher den vollständigen Standard zu lesen.

Dieser Quick Start ist eine **informative Einstiegshilfe**. Er ersetzt weder die für dein Projekt anwendbaren normativen Anforderungen noch einen späteren Konformitäts- oder Release-Nachweis.

## 1. Projekt kurz beschreiben

Erstelle einen kompakten Projektbrief mit der vorhandenen Vorlage:

- [PROJECT-BRIEF-TEMPLATE.md](templates/documents/PROJECT-BRIEF-TEMPLATE.md)

Für den Start reichen vor allem:

- Problem und Ziel,
- Zielgruppe,
- Scope und Nicht-Ziele,
- wichtigste Randbedingungen und Risiken,
- überprüfbare Erfolgskriterien.

Halte ihn klein. Ein kleines Projekt braucht nicht für jeden Gedanken ein eigenes Dokument.

## 2. Projekt vorläufig klassifizieren

Bestimme nur, was du für die nächsten Entscheidungen brauchst:

- Größenklasse,
- Qualitätsstufe `Minimum`, `Recommended` oder `Production`,
- tatsächlich anwendbare Profile.

Die Regeln stehen im [Project Classification Process](docs/30-processes/PROJECT-CLASSIFICATION.md). Wenn du allein arbeitest, hilft zusätzlich der [Solo Developer Guide](docs/10-core-standard/SOLO-DEVELOPER-GUIDE.md).

## 3. Repository, Build und Tests reproduzierbar machen

Richte das Projekt so ein, dass ein frischer Checkout nachvollziehbar gebaut und getestet werden kann:

- Repository und `.gitignore`,
- dokumentierter Buildbefehl,
- dokumentierter Testbefehl,
- keine Secrets im Repository,
- erster erfolgreicher Build/Test, sobald ausführbarer Code vorhanden ist.

Wenn du den Start formaler nachweisen willst, nutze den vorhandenen [Projektinitialisierungsnachweis](templates/documents/PROJECT-INITIALIZATION-RECORD-TEMPLATE.md). Er vermeidet, Build-, Test- und Readiness-Informationen in den Projektbrief zu duplizieren.

## 4. Den ersten kleinen Meilenstein festlegen

Definiere den kleinsten sinnvollen nächsten Stand:

- Was soll danach funktionieren?
- Was gehört ausdrücklich noch nicht dazu?
- Woran erkennst du, dass der Meilenstein fertig ist?

Dann arbeite am **Produkt**. SASD soll die Entwicklung unterstützen, nicht verdrängen.

## 5. Erst bei Bedarf tiefer einsteigen

Öffne die vollständige Spezifikation, wenn eine konkrete Entscheidung sie benötigt, zum Beispiel bei:

- komplexerer Architektur oder mehreren Komponenten,
- sensiblen Daten, Security- oder Privacy-Risiken,
- Persistenz und Migrationen,
- `Recommended`- oder `Production`-Qualitätsniveau,
- Veröffentlichung, Betrieb, Wartung oder Archivierung.

Startpunkte:

- [New Project Process](docs/30-processes/NEW-PROJECT.md)
- [Core Standard](docs/10-core-standard/README.md)
- [C#/.NET Profile](docs/20-profiles/dotnet/README.md)
- [Desktop Profile](docs/20-profiles/desktop/README.md)

## Was du am Anfang normalerweise nicht lesen musst

Solange du **ein Produkt mit SASD entwickelst** und nicht den SASD Development Standard selbst pflegst, kannst du zunächst ignorieren:

- interne Governance-, Approval- und Release-Candidate-Unterlagen des Standard-Repositories,
- Pilotportfolio- und Readiness-Dokumente des Standard-Repositories,
- Repository-Manifeste und Maintainer-Evidenz,
- SASD-eigene Validatoren und CI-Workflows, sofern du sie nicht nutzen möchtest,
- Prompt-Pakete, wenn sie dir bei der aktuellen Arbeit nicht helfen,
- Profile und Regeln, die für dein Projekt nicht anwendbar sind.

**Nicht ignorieren** darfst du anwendbare normative Anforderungen. Progressive Disclosure bedeutet: die richtige Tiefe zur richtigen Zeit — nicht das Weglassen notwendiger Qualität.

## Merksatz

> **Complexity available, not imposed.**
