# Desktop Application Review Prompt

Review the supplied C#/.NET desktop repository against the SASD Desktop Application Profile.

## Required context

- repository tree and relevant source files,
- selected quality level,
- UI technology and target framework,
- supported Windows matrix,
- build/test instructions,
- screenshots or descriptions of critical states,
- deployment and update model.

## Review tasks

1. Identify the project size model actually implemented.
2. Check separation of UI, application logic and infrastructure.
3. Inspect event handlers, ViewModels, Presenter and UI services for misplaced logic.
4. Review threading, cancellation, repeated execution and shutdown behavior.
5. Review validation, errors, focus, keyboard, accessibility, DPI and multi-monitor behavior.
6. Review data paths, migration, crash diagnosis, packaging, updates and uninstall behavior.
7. Map findings to exact `SASD-DESKTOP-REQ-*` IDs.
8. Distinguish defect, open requirement, not applicable item and justified exception.
9. Prioritize findings by data-loss, security, accessibility, operability and maintainability impact.
10. Produce concrete remediation steps without demanding unnecessary architecture.

## Output

- executive assessment,
- strengths,
- critical findings,
- requirement matrix,
- proportional target architecture,
- prioritized remediation plan,
- proposed evidence for reassessment.
