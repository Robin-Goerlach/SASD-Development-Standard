# Tooling

Dieses Verzeichnis enthält kleine, dependency-free Prüf- und Generierungswerkzeuge für das Standard-Repository.

## Prüfungen

```bash
python tooling/validate-document-metadata.py
python tooling/validate-markdown-links.py
python tooling/validate-core-requirements.py
python tooling/validate-core-consistency.py
python tooling/validate-reference-pilots.py
```

### `validate-document-metadata.py`

Prüft Front Matter, Dokument-IDs, Statuswerte und Dokumentabhängigkeiten.

### `validate-markdown-links.py`

Prüft relative Markdown-Links innerhalb des Repositories.

### `validate-core-requirements.py`

Prüft Vorhandensein und Eindeutigkeit der Core-Anforderungs-IDs.

### `validate-core-consistency.py`

Prüft zusätzlich:

- Proposed-Status und Version 0.3.0 aller Core-Dokumente,
- erwartete Abschnittsrollen,
- normative Schlüsselwörter in Requirement-Zeilen,
- exakte dokumentübergreifende Textduplikate,
- veraltete Compliance-Begriffe,
- Platzhalter wie TODO oder TBD,
- Aktualität der erzeugten Core-Übersichten.

## Erzeugte Übersichten

```bash
python tooling/generate-core-requirements-index.py
python tooling/generate-core-quality-matrix.py
```

Die erzeugten Dateien sind informativ und werden nicht manuell bearbeitet:

- `docs/10-core-standard/CORE-REQUIREMENTS-INDEX.md`
- `docs/10-core-standard/CORE-QUALITY-LEVEL-MATRIX.md`

Mit `--check` prüfen die Generatoren, ob die committed Fassungen aktuell sind.

## Perspektive

Spätere Werkzeuge können Repository-Initialisierung, .NET-Basiskonfiguration, Compliance-Matrizen, Publikation und Releaseprüfungen unterstützen. Automatisierung wird erst verbindlich, wenn die zugrunde liegenden Regeln Approved sind.


## C#/.NET profile checks

```bash
python tooling/validate-dotnet-profile.py
python tooling/generate-dotnet-requirements-index.py --check
```

### `validate-dotnet-profile.py`

Checks the eight Proposed 0.4.0 profile documents, allocated requirement-ID ranges, normative keywords, exact duplicates, required sections and the generated index.

### `generate-dotnet-requirements-index.py`

Generates `docs/20-profiles/dotnet/DOTNET-REQUIREMENTS-INDEX.md` from the normative requirement tables.

## Desktop profile checks

```bash
python tooling/validate-desktop-profile.py
python tooling/generate-desktop-requirements-index.py --check
```

### `validate-desktop-profile.py`

Checks the four Proposed 0.5.0 Desktop documents, requirement-ID ranges, normative keywords, duplicates, required sections, generated index and the WinForms/WPF project templates.

### `generate-desktop-requirements-index.py`

Generates `docs/20-profiles/desktop/DESKTOP-REQUIREMENTS-INDEX.md` from the normative requirement tables.


## Operational process checks

```bash
python tooling/validate-operational-processes.py
python tooling/generate-process-requirements-index.py --check
python tooling/generate-process-quality-matrix.py --check
```

### `validate-operational-processes.py`

Checks all seven Proposed 0.6.0 process documents, requirement-ID ranges, normative keywords, exact duplicates, expected process sections, templates and generated views.

### Generated process views

- `docs/30-processes/PROCESS-REQUIREMENTS-INDEX.md`
- `docs/30-processes/PROCESS-QUALITY-LEVEL-MATRIX.md`


## Reference pilot checks

```bash
python tooling/generate-pilot-portfolio.py --check
python tooling/generate-pilot-feedback-summary.py --check
python tooling/validate-reference-pilots.py
```

### `generate-pilot-portfolio.py`

Erzeugt eine Übersicht mit getrenntem Lebenszyklus-, Umsetzungs- und Verifikationsstatus.

### `generate-pilot-feedback-summary.py`

Erzeugt die kompakte Statusübersicht aus dem Pilotfeedbacklog.

### `validate-reference-pilots.py`

Prüft Pilot-IDs, Manifest-Schema 1.1, Qualitätsstufen, Umsetzungs- und Verifikationszustände, Artefakt-Hashes, Pflichtdokumente, Gap- und Decision-IDs sowie die Aktualität der erzeugten Übersichten.

## Foundation and Governance

```bash
python tooling/generate-governance-requirements-index.py --check
python tooling/validate-governance.py
python tooling/report-version-1-readiness.py
```

The readiness reporter is informational. It intentionally reports non-Approved documents as release blockers and does not change document status.

## Foundation and Governance approval

```bash
python tooling/generate-foundation-governance-approval-manifest.py --check
python tooling/validate-foundation-governance-approval.py
```

The manifest generator verifies SHA-256 hashes for the 14 Approved Foundation and Governance documents. The approval validator checks status, version, approval metadata, catalog entries, the resolved Governance dependency, and the completed approval evidence.
