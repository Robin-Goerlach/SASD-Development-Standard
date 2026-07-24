# TaskHost Local – CI Evidence Guide

## Purpose

This guide explains what GitHub Actions can and cannot prove for the Wave 01 pilot.

## CI proves

For the commit shown in the workflow run, CI can provide evidence that:

- the repository was checked out,
- the selected .NET SDK was installed,
- restore and Release build completed,
- automated tests completed,
- the package audit command completed,
- the application was published,
- the published executable completed its headless self-check,
- evidence artifacts were uploaded.

## CI does not prove

CI does not prove that:

- the visible WinForms UI starts correctly on the user's workstation,
- an existing user database behaves correctly,
- focus order and dialogs are usable,
- screen scaling and layout are acceptable,
- a human-reviewed backup can be restored,
- the historical SQLite report was reproduced.

These require the manual plan.

## Required capture

For final Wave 01 evidence record, retain:

- workflow run URL,
- commit SHA,
- job conclusion,
- uploaded evidence artifact name,
- execution date,
- local manual test record.

Do not copy access tokens, local database files or task content into an evidence record.
