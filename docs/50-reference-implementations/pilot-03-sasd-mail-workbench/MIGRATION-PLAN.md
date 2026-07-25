---
title: "Pilot 03 Migrationsplan – SASD Mail Workbench"
document-id: SASD-REF-PILOT-306
document-type: informative
status: Draft
version: 0.11.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-25
applies-to-quality-levels: [Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-REF-PILOT-305, SASD-PROC-005]
---

# Migrationsplan – SASD Mail Workbench

## Leitprinzip

Die vorhandene modulare Architektur wird als Hypothese behandelt, die durch Build-, Test- und Dependency-Evidenz bestätigt werden muss. Der Pilot führt keine Zusammenlegung oder zusätzliche Schichtung ohne konkreten Befund durch.

## Wave 01 – Baseline, Architektur und Recovery

- exakten Commit und Toolchain erfassen,
- vollständigen Restore-, Release-Build- und Testlauf ausführen,
- GitHub-Actions-Ergebnis für denselben Commit sichern,
- Projektabhängigkeiten und Architecture Tests auswerten,
- Datenfluss und Trust Boundaries dokumentieren,
- Migration, Staging, atomare Übernahme und Wiederanlauf mit Fehlerfällen testen,
- Sample-Mails auf synthetische Herkunft, Datenschutz und Lizenz prüfen,
- Applicability Matrix und Production-Gate ergänzen.

## Wave 02 – Release- und Erweiterungshärtung

- Packaging, Upgrade und Rollback,
- Extension-Vertrauensmodell,
- Diagnose- und Supportpaket,
- Vorbereitung des Desktop-Meilensteins ohne fachliche Kernkopplung.

## Rückfallstrategie

Tests verwenden ausschließlich isolierte temporäre Arbeitsverzeichnisse und synthetische Maildaten. Migrations- und Recovery-Änderungen werden getrennt committed und mit alten Katalogständen geprüft.
