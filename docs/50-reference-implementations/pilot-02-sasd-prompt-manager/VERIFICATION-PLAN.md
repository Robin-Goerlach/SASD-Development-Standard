---
title: "Pilot 02 Verifikationsplan – SASD Prompt Manager"
document-id: SASD-REF-PILOT-212
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
depends-on: [SASD-REF-PILOT-207, SASD-REF-PILOT-002]
---

# Verifikationsplan – SASD Prompt Manager

## Automatische Nachweise

- `dotnet --info`, Restore und Release-Build,
- vollständiger Testlauf mit TRX-Ergebnis,
- NuGet-Audit,
- isolierter Import/Export-Roundtrip,
- Backup/Restore-Test,
- Secret-Warnungs-Testfälle,
- CI-Lauf für exakt denselben Commit.

## Manuelle Nachweise

- Start und Grundnavigation unter Windows,
- Anlage, Bearbeitung, Suche und Archivierung eines Testprompts,
- Projekt-, Kategorie- und Tagzuordnung,
- Export, Löschung und Wiederherstellung aus Backup,
- sichere Darstellung von Fehlern ohne Offenlegung von Secrets.

## Abschlussgate

`Wave Validated` ist erst zulässig, wenn automatisierte und manuelle Ergebnisse, Commit-SHA, Umgebung und bekannte Einschränkungen dokumentiert sind.
