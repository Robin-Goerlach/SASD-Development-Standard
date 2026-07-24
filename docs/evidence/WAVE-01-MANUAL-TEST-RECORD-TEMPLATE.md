# TaskHost Local – Wave 01 Manual Test Record

> Copy this file to `WAVE-01-MANUAL-TEST-RECORD.md` before execution. Do not mark it passed without performing every required test on Windows.

**Test date UTC:** `<YYYY-MM-DDTHH:MM:SSZ>`  
**Tester:** `<name>`  
**Verified commit:** `<full Git commit SHA>`  
**Windows version:** `<version>`  
**.NET SDK:** `<version>`  
**Overall result:** Pending

## Database preparation

- [ ] Existing database was backed up before testing.
- [ ] Backup SHA-256 was recorded outside the repository.
- [ ] No real task content was copied into this record.

## Fresh database

- [ ] Application starts without an error dialog.
- [ ] Database file is created.
- [ ] Exactly one default list `Eingang` is visible.
- [ ] Repeated startup does not duplicate the default list.

## Existing database copy

- [ ] Application starts with a secured copy of the existing database.
- [ ] Existing lists and tasks are visible.
- [ ] No destructive migration or silent data reset occurred.

## Core UI smoke test

- [ ] Create, rename and delete an empty list.
- [ ] Create, edit, complete, reopen and delete a task.
- [ ] Search by title and description.
- [ ] Close and restart the application; changes persist.
- [ ] Create a database backup and verify that the file exists.

## Diagnostics and privacy

- [ ] A controlled startup failure produces an understandable message.
- [ ] The diagnostic report contains no task title or description.
- [ ] The existing database is not deleted after a failed startup.

## Historical SQLite issue

Choose exactly one:

- [ ] Reproduced. Exact failing action, SQL source and regression test are documented below.
- [ ] Not reproducible in the verified commit after fresh- and existing-database tests.

Details:

`<result and evidence>`

## Findings

| ID | Severity | Finding | Resolution or follow-up |
|---|---|---|---|
| — | — | No finding recorded | — |

## Final declaration

Change `Overall result` to `Passed` only when all mandatory checks passed and no Blocker or Major finding remains.
