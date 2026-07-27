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

- Proposed- oder Approved-Status und Version 0.9.0 aller Core-Dokumente,
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

Checks the eight Proposed or Approved 0.9.0 profile documents, allocated requirement-ID ranges, normative keywords, exact duplicates, required sections and the generated index.

### `generate-dotnet-requirements-index.py`

Generates `docs/20-profiles/dotnet/DOTNET-REQUIREMENTS-INDEX.md` from the normative requirement tables.

## Desktop profile checks

```bash
python tooling/validate-desktop-profile.py
python tooling/generate-desktop-requirements-index.py --check
```

### `validate-desktop-profile.py`

Checks the four Proposed or Approved 0.9.0 Desktop documents, requirement-ID ranges, normative keywords, duplicates, required sections, generated index and the WinForms/WPF project templates.

### `generate-desktop-requirements-index.py`

Generates `docs/20-profiles/desktop/DESKTOP-REQUIREMENTS-INDEX.md` from the normative requirement tables.


## Operational process checks

```bash
python tooling/validate-operational-processes.py
python tooling/generate-process-requirements-index.py --check
python tooling/generate-process-quality-matrix.py --check
```

### `validate-operational-processes.py`

Checks all seven Proposed or Approved 0.9.0 process documents, requirement-ID ranges, normative keywords, exact duplicates, expected process sections, templates and generated views.

### Generated process views

- `docs/30-processes/PROCESS-REQUIREMENTS-INDEX.md`
- `docs/30-processes/PROCESS-QUALITY-LEVEL-MATRIX.md`


## Reference pilot checks

```bash
python tooling/generate-pilot-portfolio.py --check
python tooling/generate-pilot-feedback-summary.py --check
python tooling/generate-pilot-readiness.py --check
python tooling/validate-reference-pilots.py
python tooling/validate-version-1-pilot-coverage.py
```

### `generate-pilot-portfolio.py`

Erzeugt eine Übersicht mit getrenntem Lebenszyklus-, Umsetzungs- und Verifikationsstatus.

### `generate-pilot-feedback-summary.py`

Erzeugt die kompakte Statusübersicht aus dem Pilotfeedbacklog.

### `validate-reference-pilots.py`

Prüft Pilot-IDs, Manifest-Schemas 1.1 und 1.2, Qualitätsstufen, Umsetzungs- und Verifikationszustände, optionale Artefakt-Hashes, Pflichtdokumente, Gap- und Decision-IDs sowie die Aktualität der erzeugten Übersichten.

### `validate-version-1-pilot-coverage.py`

Prüft die für Version 1.0 erforderliche Small-, Medium- und Large/Complex-Abdeckung, Baseline-Artefakte, Standardbezug, Gap Register und Lessons Learned. Die Prüfung bestätigt die Bewertung, nicht eine technische Migration.

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

## Repository quality gates

The canonical local and GitHub entry point is:

```bash
python tooling/run-quality-gates.py
```

The orchestrator executes every blocking validator, writes per-check logs,
creates `quality-gates.json` and `quality-gates.md`, and runs the Version 1.0
readiness report as informational evidence.

### CI and repository checks

```bash
python tooling/validate-repository-hygiene.py
python tooling/validate-ci-policy.py
python tooling/generate-repository-manifest.py --check
```

- `validate-repository-hygiene.py` rejects duplicated repository roots,
  generated operating-system files, symbolic links, invalid UTF-8, missing
  final newlines, trailing whitespace, and tabs in structured text.
- `validate-ci-policy.py` checks triggers, read-only permissions, timeouts,
  concurrency, immutable action pins, checkout credential handling,
  Dependabot, and CODEOWNERS.
- `generate-repository-manifest.py` deterministically writes or verifies
  `REPOSITORY-MANIFEST.txt`. Regenerate it after adding or removing files:

```bash
python tooling/generate-repository-manifest.py --write
```

Generated execution evidence is stored below `artifacts/quality-gates/` and is
not committed.


## Repository boundary

`validate-repository-boundary.py` verifies the machine-readable
`REPOSITORY-IDENTITY.json`, canonical root markers, the allowed top-level layout,
foreign repository markers, and the Git origin when available. It is a blocking
quality gate.

## Repository CI recovery and ruleset activation

The activation toolchain separates remote CI evidence from branch-protection
configuration:

```bash
python tooling/validate-ci-activation.py
python tooling/capture-ci-activation.py --verify-only
python tooling/manage-main-ruleset.py --plan
```

After the exact remote `main` commit has a successful Ubuntu, Windows, and
`SASD merge gate` result, evidence can be written with:

```bash
python tooling/capture-ci-activation.py --write
```

Ruleset activation is an explicit administrative operation and requires both a
write-capable token and confirmation of the switch to branch and pull-request
work:

```bash
python tooling/manage-main-ruleset.py \
  --activate \
  --confirm-switch-to-pull-requests
```

`capture-ci-activation.py` and `manage-main-ruleset.py` use only the Python
standard library. Public read operations can work without a token; ruleset
writes require repository `Administration: write` permission.

## Integrated normative baseline review

The 32 Core, C#/.NET, Desktop, and operational-process documents are reviewed as one bundle:

```bash
python tooling/generate-normative-baseline-review.py --check
python tooling/validate-normative-baseline-review.py
```

The generator maintains:

- `docs/40-governance/NORMATIVE-BASELINE-DEPENDENCY-MAP-0.9.0.md`
- `docs/40-governance/NORMATIVE-BASELINE-REVIEW-MANIFEST-0.9.0.md`

The validator checks the 32-document bundle, 1,345 requirements, exact duplicates, unresolved markers, external dependency approval, dependency cycles, required document sections, and current generated evidence. It does not grant Maintainer approval.


## Normative baseline approval

```bash
python tooling/generate-normative-baseline-approval-manifest.py --check
python tooling/validate-normative-baseline-review.py
python tooling/validate-normative-baseline-approval.py
```

The review validator supports both the Proposed review state and the later Approved state. The approval validator is blocking once the 32-document bundle is Approved and verifies approval metadata, evidence records, dependency state, catalog entries, requirement count, and SHA-256 manifest freshness.

## Pilotportfolio und Version-1.0-Abdeckung

```bash
python tooling/generate-pilot-portfolio.py --check
python tooling/generate-pilot-feedback-summary.py --check
python tooling/generate-pilot-readiness.py --check
python tooling/validate-reference-pilots.py
python tooling/validate-version-1-pilot-coverage.py
```

Die Abdeckungsprüfung bestätigt Small-, Medium- und Large-Piloten sowie die zugehörigen Baseline-, Gap-, Migrations- und Lessons-Learned-Nachweise. Sie behauptet keine erfolgreichen Builds, Tests, Laufzeittests oder CI-Läufe der Ziel-Repositories.

## Version 1.0 Release Candidate preparation

```bash
python tooling/generate-release-candidate-readiness.py --check
python tooling/validate-release-candidate-preparation.py
python tooling/build-release-candidate.py --mode preview
python tooling/verify-release-candidate.py --directory artifacts/release-candidate
```

The readiness generator distinguishes Approved content, pilot coverage, practical pilot verification, exact-commit remote CI evidence, and active ruleset evidence. `--require-ready` fails while a blocking RC condition is open.

The package builder creates deterministic source and Markdown ZIP files, a machine-readable release manifest, `SHA256SUMS.txt`, and a build report. Preview mode may be used before release readiness and is visibly marked as such. Release mode requires a clean Git working tree and complete readiness.

The independent verifier checks SHA-256 values, ZIP integrity, safe paths, excluded build state, release metadata, and manifest consistency. The tools do not create a Git tag or GitHub Release.


## SASD Prompt Package

```bash
python tooling/generate-prompt-catalog.py --check
python tooling/validate-prompt-packages.py
python tooling/build-prompt-package.py --clean --output-dir artifacts/prompt-packages
python tooling/verify-prompt-package.py --directory artifacts/prompt-packages
```

- `generate-prompt-catalog.py` maintains the machine-readable catalog, human-readable catalog, and tracked-file checksums.
- `validate-prompt-packages.py` checks package identity, prompt metadata, sections, variables, placeholders, category and workflow coverage, security markers, and generated evidence.
- `build-prompt-package.py` creates a deterministic candidate ZIP with a fixed timestamp, build manifest, and SHA-256 sums.
- `verify-prompt-package.py` independently checks sums, ZIP integrity, safe paths, one archive root, identity, and required files.

The package is an exchange format. These tools do not write to the SASD Prompt Manager and do not prove direct-import compatibility.
