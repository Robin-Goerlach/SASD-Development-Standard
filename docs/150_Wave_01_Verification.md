# TaskHost Local – Wave 01 Verification

**Status:** Verification harness prepared – execution pending  
**Scope:** Migrationswelle 01  
**Target quality level:** SASD Recommended

## Purpose

This document defines the controlled verification path for Wave 01. It prevents source files, test code, workflow configuration or a prepared ZIP from being mistaken for successful execution evidence.

## Evidence layers

Wave 01 requires all of the following layers:

1. **Static package validation** – structure, XML and embedded SQLite statements.
2. **Automated local verification** – restore, build, tests, package audit, publish and headless product self-check.
3. **GitHub Actions verification** – the same repository script against the committed source state.
4. **Manual Windows smoke test** – visible application startup and core UI behavior.
5. **Closeout record** – immutable commit SHA, CI run and explicit tester confirmation.

## Headless product self-check

The published application supports:

```powershell
.\TaskHostLocal.WinForms.exe --self-check --report .\self-check-report.json
```

The mode does not open the Windows Forms UI. It executes productive code for:

- SQLite initialization,
- `PRAGMA integrity_check`,
- schema-version verification,
- default-list verification,
- list and task CRUD through repositories and services,
- search and completion state,
- database backup,
- repeated initialization,
- foreign-key verification.

Temporary verification data is deleted before the test ends. A temporary database is used unless `--database` is supplied.

## Local automated verification

Run from a clean committed worktree:

```powershell
.\scripts\verify-wave-01.ps1
```

The script creates a timestamped directory under `verification-results/` and records:

- command logs,
- TRX and coverage output,
- published application,
- self-check JSON,
- machine-readable verification summary,
- human-readable Markdown summary.

A successful script run means only that the automated part passed. The overall closeout remains `Pending`.

## CI verification

Push the same commit to GitHub and inspect **Actions → Build, test and verify**. The workflow uploads the complete evidence directory for the commit and writes the summary to the GitHub job summary.

A workflow file in the repository is not evidence. The URL of a successful run for the verified commit is required.

## Manual verification

Execute `docs/100_Manual_Test_Plan.md` on Windows. At minimum verify:

- fresh start without error dialog,
- start using a secured copy of an existing database,
- visible default list,
- list and task CRUD,
- search,
- backup,
- persistence after restart,
- startup diagnostics without task content.

## Formal closeout

After all evidence is available:

```powershell
.\scripts\finalize-wave-01.ps1 `
  -VerificationSummary .\verification-results\wave-01-<timestamp>\verification-summary.json `
  -ManualTestRecord .\docs\evidence\WAVE-01-MANUAL-TEST-RECORD.md `
  -CiResult Passed `
  -CiRunUrl https://github.com/Robin-Goerlach/SASD-TaskHost-Local/actions/runs/<id> `
  -Notes 'Manual test record reviewed.'
```

The script refuses closeout when:

- automated verification failed,
- the repository was dirty during verification,
- no commit SHA was recorded,
- the manual test record is missing, not passed or references another commit,
- CI failed.

The generated `docs/evidence/WAVE-01-VERIFICATION-RECORD.md` must be reviewed before it is committed.
