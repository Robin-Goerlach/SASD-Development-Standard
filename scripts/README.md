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

## Repository boundary repair

The one-time `repair-repository-boundary.ps1` and
`repair-repository-boundary.sh` scripts remove the known TaskHost Local and nested
starter-repository paths that were accidentally committed to this repository. The
scripts verify the repository identity first, regenerate the manifest, and execute
all quality gates.

## CI activation evidence

After a repair commit has been pushed and the remote quality-gate workflow has
completed successfully:

```powershell
.\scripts\capture-ci-activation.ps1
```

```bash
bash scripts/capture-ci-activation.sh
```

Add `--require-active-ruleset` in the shell version or
`-RequireActiveRuleset` in PowerShell after the branch ruleset has been
activated. The scripts write committed evidence only after reading the exact
remote workflow and ruleset state.
