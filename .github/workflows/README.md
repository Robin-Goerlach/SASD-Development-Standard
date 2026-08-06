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

## `release-candidate-preview.yml`

This workflow is manual only. It runs the same blocking repository checks, creates deterministic `1.0.0-rc.1` preview archives, verifies ZIP integrity, checksums and safe paths, and uploads the result for 14 days. It is deliberately read-only and does not create a tag or GitHub Release.

Local equivalent:

```powershell
.\scripts\prepare-release-candidate.ps1 -Mode preview
```

```bash
bash scripts/prepare-release-candidate.sh preview
```


## `prompt-package-preview.yml`

This workflow is manual only and read-only. It executes the complete repository checks, builds the deterministic `sasd-development-standard-v1` candidate prompt package, verifies checksums and safe ZIP paths, and uploads the package plus validation evidence for 14 days. It neither imports Prompt Manager data nor publishes a GitHub Release.

Local equivalent:

```powershell
.\scripts\build-prompt-package.ps1
```

```bash
bash scripts/build-prompt-package.sh
```


## `ci.yml` – TaskHost Local reference baseline

This read-only Windows workflow checks out the Development Standard and the
public `Robin-Goerlach/SASD-TaskHost-Local` repository separately. The target
revision is the immutable `target_commit` recorded in Pilot 01. The workflow
records restore, build, available tests, NuGet audit execution, and publish
evidence without copying product source into this repository or claiming that
Wave 01 is complete.
