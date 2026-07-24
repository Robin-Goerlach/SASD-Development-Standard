# Repository Scripts

The scripts in this directory provide stable local entry points for the same
quality gates used by GitHub Actions.

## Windows PowerShell

```powershell
.\scripts\validate-repository.ps1
```

## Linux, WSL, or macOS

```bash
bash scripts/validate-repository.sh
```

Evidence is written below `artifacts/quality-gates/` and is intentionally
ignored by Git. A successful local run is useful evidence, but the repository
CI run remains a separate execution record for the committed revision.
