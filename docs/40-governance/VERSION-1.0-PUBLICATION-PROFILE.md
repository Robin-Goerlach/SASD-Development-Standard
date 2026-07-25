---
title: "Publikationsprofil für Version 1.0"
document-id: SASD-REF-RC-006
document-type: informative
status: Draft
version: 0.12.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-25
applies-to-quality-levels: [Recommended, Production]
applies-to-profiles: [Core]
depends-on: [SASD-GOV-004, SASD-CORE-005, SASD-CORE-010, SASD-REF-RC-001]
---

# Publikationsprofil für Version 1.0

## 1. Zweck

Das Publikationsprofil definiert, welche Repository-Inhalte in den Releasearchiven enthalten sind und welche Ausgaben erst für die stabile Fassung erzeugt werden.

## 2. Release-Candidate-Artefakte

### Source Archive

Das Source Archive enthält den freigegebenen Repository-Quellstand einschließlich:

- Root-Dokumente,
- `.github`-Konfiguration,
- `docs`, `templates`, `checklists`, `prompts`, `examples`, `scripts` und `tooling`,
- Repository- und Approval-Manifeste,
- Lizenz und Security Policy.

Ausgeschlossen werden:

- `.git`,
- lokale `artifacts`-Ausgaben,
- Python-Caches,
- IDE-Dateien,
- temporäre Dateien,
- generierte Word- und PDF-Dateien,
- bereits erzeugte Releasearchive.

### Markdown Publication Archive

Das Markdown-Archiv ist die leserorientierte Fassung und enthält:

- README, LICENSE, CHANGELOG und ROADMAP,
- gesamte Dokumentation,
- Vorlagen, Checklisten und Prompts,
- Beispiele,
- Release Notes und Release Record.

CI-Workflows, Reparaturskripte und interne Entwicklungswerkzeuge werden dort nicht benötigt.

## 3. Stabile Publikationsartefakte

Für `1.0.0` sind zusätzlich vorgesehen:

- Word-Ausgabe aus der autoritativen Markdown-Quelle,
- PDF-Ausgabe aus demselben Quellstand,
- dokumentierte Konvertierungswerkzeuge und Versionen,
- visueller Review von Inhaltsverzeichnis, Tabellen, Seitenumbrüchen und Links,
- SHA-256-Prüfsummen aller Publikationsdateien.

## 4. Reproduzierbarkeitsregeln

- Archivpfade müssen relativ und normalisiert sein.
- Dateireihenfolge muss stabil sein.
- ZIP-Zeitstempel müssen fest sein.
- Textdateien müssen unverändert aus dem Quellstand übernommen werden.
- Manifest und Archive müssen dieselbe Version und Commit-SHA nennen.
- Verifikation muss in einem getrennten Ausgabeverzeichnis möglich sein.
- Archivinhalt darf keine Pfade außerhalb seines Wurzelordners schreiben.

## 5. Versionierung der Artefakte

| Artefakt | Dateiname |
|---|---|
| Source | `SASD-Development-Standard-1.0.0-rc.1-source.zip` |
| Markdown | `SASD-Development-Standard-1.0.0-rc.1-markdown.zip` |
| Manifest | `SASD-Development-Standard-1.0.0-rc.1-release-manifest.json` |
| Prüfsummen | `SHA256SUMS.txt` |
| Word, später | `SASD-Development-Standard-1.0.0.docx` |
| PDF, später | `SASD-Development-Standard-1.0.0.pdf` |
