---
title: "Pilot 01 – SASD TaskHost Local"
document-id: SASD-REF-PILOT-101
document-type: informative
status: Draft
version: 0.8.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Recommended]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-REF-PILOT-001, SASD-PROC-005]
---

# Pilot 01 – SASD TaskHost Local

## Status

```text
Pilotstatus: In Execution
Umsetzung: Artifact Prepared
Verifikation: Pending
Aktuelle Welle: Wave 01
Ziel-Commit: noch nicht erfasst
```

Ein 36-Dateien-Overlay für Wave 01 wurde erstellt und statisch geprüft. Es ist noch nicht als gebauter, getesteter, gestarteter oder per CI bestätigter Zielstand dokumentiert.

## Ziel

Der Pilot prüft die proportionale Anwendung von Core, C#/.NET-, Desktop- und Prozessstandard auf ein kleines, langfristig gepflegtes WinForms-/SQLite-Projekt.

## Dokumente

1. [Pilot Charter](PILOT-CHARTER.md)
2. [Projektklassifikation](PROJECT-CLASSIFICATION.md)
3. [Baseline Assessment](BASELINE-ASSESSMENT.md)
4. [Gap Register](GAP-REGISTER.md)
5. [Migrationsplan](MIGRATION-PLAN.md)
6. [Wave-01-Plan](WAVE-01-PLAN.md)
7. [Wave-01-Implementierungsreview](WAVE-01-IMPLEMENTATION-REVIEW.md)
8. [Wave-01-Verifikationsplan](WAVE-01-VERIFICATION-PLAN.md)
9. [Evidenzzuordnung](EVIDENCE-MAP.md)
10. [Entscheidungslog](DECISION-LOG.md)
11. [Zwischenreview](PILOT-REVIEW.md)
12. [Zwischenretrospektive](INTERIM-RETROSPECTIVE.md)

## Nächster Schritt

Das Overlay wird kontrolliert in einen sauberen Clone des Ziel-Repositories eingespielt. Danach werden Restore, Build, Tests, Windows-Start, Datenbankzustände, Diagnose und CI gemäß Verifikationsplan nachgewiesen.

Wave 02 bleibt bis zu diesem Nachweis gesperrt.
