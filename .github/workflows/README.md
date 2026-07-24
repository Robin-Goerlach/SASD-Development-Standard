# GitHub Workflows

## `quality-gates.yml`

The active repository workflow runs the complete dependency-free validation
suite on both Ubuntu and Windows for:

- pushes to `main`,
- pull requests,
- manual workflow dispatches.

The stable aggregate check is named:

```text
SASD merge gate
```

After the first successful pushed run, this check can be selected in a branch
ruleset as the required status check for `main`.

## Security baseline

- workflow permissions are read-only,
- checkout credentials are not persisted,
- all external actions are pinned to immutable full commit SHAs,
- release versions are retained as same-line comments for review and Dependabot,
- jobs have explicit timeouts,
- obsolete concurrent runs are cancelled,
- no `pull_request_target` workflow is used.

## Evidence

Every operating-system job uploads its evidence under an artifact name similar
to:

```text
sasd-quality-gates-Linux-<run>-<attempt>
sasd-quality-gates-Windows-<run>-<attempt>
```

The artifact contains JSON and Markdown summaries plus one log per validator.
It is uploaded even when validation fails.

## Local equivalent

```powershell
.\scripts\validate-repository.ps1
```

```bash
bash scripts/validate-repository.sh
```

A local success and a GitHub Actions success are separate evidence records.
