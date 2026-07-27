# SASD Prompt Package Update Manifest

## Package identity

- Target repository: `Robin-Goerlach/SASD-Development-Standard`
- Update version: `0.13.0`
- Prompt package ID: `sasd-development-standard-v1`
- Prompt package format: `sasd-prompt-package/1.0`
- Package status: `candidate`
- Authoritative language: German
- Prepared on: `2026-07-25`

## Included scope

- 39 versioned prompts,
- nine lifecycle categories,
- 35 centrally registered variables,
- stable prompt IDs and semantic prompt versions,
- package and prompt JSON schemas,
- generated JSON and Markdown catalogs,
- tracked-file SHA-256 checksums,
- lifecycle workflow ordering,
- quality, security and variable guidance,
- deterministic package builder and independent verifier,
- local PowerShell and shell wrappers,
- manual read-only GitHub Actions preview workflow,
- Prompt Manager adapter plan, mapping template and roundtrip checklist.

## Compatibility boundary

This update defines the canonical SASD exchange format. It does **not** claim direct compatibility with an unspecified SASD Prompt Manager build. Direct import remains disabled until an adapter is mapped and roundtrip-tested against an exact application version or commit.

## Verification commands

```bash
python tooling/generate-prompt-catalog.py --check
python tooling/validate-prompt-packages.py
python tooling/build-prompt-package.py --clean --output-dir artifacts/prompt-packages
python tooling/verify-prompt-package.py --directory artifacts/prompt-packages
python tooling/run-quality-gates.py
```

## Expected evidence

- prompt-package validation: passed,
- prompt count: 39,
- categories: 9,
- registered variables: 35,
- workflow coverage: complete and unique,
- deterministic package builds: byte-identical for identical source state,
- ZIP integrity and safe paths: passed,
- direct Prompt Manager import: not claimed.

## Prepared-tree verification result

- Repository quality gates: `PASSED`
- Prompt source files in distributable archive: `69`
- Candidate archive SHA-256: `9b491f04e5c49ed7fee55c4844cc5cae17bd953dd54b0d7b6f812961af6949a4`
- Independent artifact verification: `PASSED`
- Repeated deterministic build: byte-identical archive and manifest
- Remote GitHub Actions preview: `Pending` until the update is committed and pushed
