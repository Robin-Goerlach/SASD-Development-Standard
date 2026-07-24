# TaskHost Local – Wave 01 Closeout

**Current status:** Pending verification

## Completion gate

Wave 01 may be declared complete only when every item below is evidenced for the same committed source state.

| Gate | Required evidence | Current state |
|---|---|---|
| Source state | immutable Git commit SHA | Pending |
| Repository cleanliness | clean worktree during local verification | Pending |
| Restore and build | successful recorded command logs | Pending |
| Automated tests | successful TRX result | Pending |
| Dependency audit | recorded NuGet audit without blocking finding | Pending |
| Published application | generated publish directory | Pending |
| Headless self-check | JSON report with `success: true` | Pending |
| GitHub Actions | successful run URL for the same commit | Pending |
| Fresh-database UI start | signed manual test result | Pending |
| Existing-database UI start | signed manual test result using a secured copy | Pending |
| Core UI smoke tests | completed manual test plan | Pending |
| Historical SQLite issue | reproduced and resolved, or closed as not reproducible with evidence | Pending |
| Closeout record | reviewed verification record committed | Pending |

## Status semantics

- `Prepared`: verification code and procedures exist.
- `Automated Passed`: local automated steps passed.
- `CI Passed`: GitHub Actions passed for the named commit.
- `Manual Passed`: Windows UI checks passed.
- `Completed`: all gates above are satisfied and the evidence record is committed.

No earlier state may be described as completed.

## Historical SQLite issue

The historical `near "=": syntax error` report must be handled transparently:

- If reproduced, document the exact source, failing SQL, fix and regression test.
- If not reproduced after fresh and existing-database tests, close it as **not reproducible in the verified commit**, not as an implicitly proven code fix.

## Wave 02 gate

Wave 02 remains blocked until this closeout document can reference a committed `docs/evidence/WAVE-01-VERIFICATION-RECORD.md`.
