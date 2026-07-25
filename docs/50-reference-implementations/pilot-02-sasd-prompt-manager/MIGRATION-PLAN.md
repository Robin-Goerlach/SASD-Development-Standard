---
title: "Pilot 02 Migrationsplan – SASD Prompt Manager"
document-id: SASD-REF-PILOT-206
document-type: informative
status: Draft
version: 0.11.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-25
applies-to-quality-levels: [Recommended]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-REF-PILOT-205, SASD-PROC-005]
---

# Migrationsplan – SASD Prompt Manager

## Leitprinzip

Die bestehende Vier-Projekt-Struktur bleibt erhalten, solange der lokale Dependency- und Buildreview keinen konkreten Verstoß oder unnötige Kopplung nachweist. Der Pilot ergänzt Evidenz und Schutzmaßnahmen, nicht Schichten um ihrer selbst willen.

## Wave 01 – Reproduzierbarkeit, Tests und Datensicherheit

- Baseline auf exakte Commit-ID festlegen,
- Restore, Release-Build und bestehende Tests ausführen,
- Projektabhängigkeiten dokumentieren,
- CI und Paket-Audit ergänzen oder nachweisen,
- Persistenz, Import/Export und Backup/Restore testen,
- Secret-Warnung und Fehlerbehandlung prüfen,
- Security- und Alignment-Dokumentation ergänzen,
- priorisierte Application-/Infrastructure-Testfälle umsetzen.

## Wave 02 – Desktop-Release und Wartung

- Installer- oder portable Veröffentlichung bewerten,
- Upgrade- und Datenmigrationspfad prüfen,
- UI-Smoke-Test und High-DPI-/Tastaturtest ergänzen,
- Release Notes, Changelog und Supportdiagnose vereinheitlichen.

## Rückfallstrategie

Wave 01 wird in kleinen Commits durchgeführt. Vor Datenformatänderungen wird eine anonymisierte Testkopie und ein Restore-Pfad hergestellt. Architektur- oder Persistenzänderungen werden getrennt von CI- und Dokumentänderungen committed.
