# Desktop Release Smoke Test Checklist

## Artefact

- [ ] Release version matches application, installer and release notes.
- [ ] Hash and signature are verified when applicable.
- [ ] Correct architecture and runtime model are used.

## Clean installation

- [ ] Install or extract on a representative clean system.
- [ ] Start without development tools or source checkout.
- [ ] Verify version/about information.
- [ ] Verify expected program, data, configuration and log paths.

## Core operation

- [ ] Complete one critical create/read/update workflow.
- [ ] Validate an invalid input and recover.
- [ ] Exercise one failure or unavailable-service state.
- [ ] Confirm background operation keeps UI responsive.
- [ ] Save and reopen representative data.

## Display and interaction

- [ ] Run keyboard-only core path.
- [ ] Check representative DPI and resized window.
- [ ] Verify dialogs open visibly and return focus.

## Shutdown and restart

- [ ] Close with no changes.
- [ ] Close with unsaved changes.
- [ ] Close during an active operation.
- [ ] Restart and verify settings/data recovery.

## Upgrade and removal

- [ ] Upgrade from the last supported version.
- [ ] Verify migration and retained user data.
- [ ] Uninstall or remove the application.
- [ ] Confirm user data is retained or removed only as documented.
