# SASD Development Standard Version 1 Prompt Package

- Package ID: `sasd-development-standard-v1`
- Version: `0.13.0`
- Status: `candidate`
- Language: German
- Prompt count: **39**

## Contents

- `manifest.json`: package identity and compatibility declaration
- `catalog.json`: generated prompt metadata and SHA-256 hashes
- `CATALOG.md`: human-readable catalog
- `variables.json`: central variable registry
- `categories.json`: category definitions
- `workflow.json`: recommended lifecycle order

## Prompt Manager compatibility

This package is the canonical SASD exchange representation. Direct import into a particular SASD Prompt Manager build is **not yet claimed**. The importer must be mapped and roundtrip-tested against an exact application commit before compatibility is declared.

## Build and verification

```bash
python tooling/validate-prompt-packages.py
python tooling/build-prompt-package.py --output-dir artifacts/prompt-packages
python tooling/verify-prompt-package.py --directory artifacts/prompt-packages
```


## Import-adapter path

Before direct import is enabled, follow the repository's `prompts/PROMPT-MANAGER-IMPORT-ADAPTER-PLAN.md`, complete the field mapping, and pass the roundtrip checklist against an exact Prompt Manager commit.
