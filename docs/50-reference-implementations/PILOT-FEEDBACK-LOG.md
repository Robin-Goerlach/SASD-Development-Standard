---
title: "Feedbacklog aus Referenzpiloten"
document-id: SASD-REF-PILOT-004
document-type: informative
status: Draft
version: 0.8.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-REF-PILOT-001, SASD-REF-PILOT-002]
---

# Feedbacklog aus Referenzpiloten

## Statuswerte

- `Candidate`: fachlich zu prüfen
- `Accepted`: in Pilotprogramm oder Hilfsmitteln übernommen
- `Deferred`: sinnvoll, aber für einen späteren Release vorgesehen
- `Rejected`: mit Begründung verworfen
- `Confirmed`: bestehende Regel wurde praktisch bestätigt

## Feedback

| Feedback-ID | Pilot | Befund | Betroffener Bereich | Entscheidung | Status |
|---|---|---|---|---|---|
| SASD-PFB-001 | Pilot 01 | Ein erzeugtes Updatepaket wurde leicht mit einem verifizierten Zielzustand verwechselt. | Evidenzmodell, Pilotstatus | Evidenzklasse `A` und getrennte Umsetzungs-/Verifikationszustände einführen. | Accepted |
| SASD-PFB-002 | Pilot 01 | Der historische SQLite-Fehler war im sichtbaren Stand nicht eindeutig reproduzierbar. | Legacy-Migration, Fehlerbehebung | Keine Behauptung „behoben“, bevor Fehler oder Regressionstest eindeutig nachgewiesen sind. | Accepted |
| SASD-PFB-003 | Pilot 01 | Vorbereitete CI-Dateien belegen keinen erfolgreichen Workflow. | CI, Evidence | CI-Erfolg benötigt Lauf-ID, Commit und Ergebnis; Dateiexistenz bleibt Artefaktnachweis. | Accepted |
| SASD-PFB-004 | Pilot 01 | ZIP-Overlays benötigen eine nachvollziehbare Identität. | Tooling, Migration | Dateiname, SHA-256, Ziel-Repository, Baseline und offene Prüfungen im Implementierungsreview erfassen. | Accepted |
| SASD-PFB-005 | Pilot 01 | Kleine WinForms-Projekte profitieren von Integrationstests, ohne mehrere Produktionsassemblies zu benötigen. | .NET-Profil, Projektgröße | Bestehende proportionale Strukturregel bestätigt; separates Testprojekt ist ausreichend. | Confirmed |
| SASD-PFB-006 | Pilot 01 | Lizenzwahl ist eine Eigentümerentscheidung, auch wenn eine plausible Vorlage vorliegt. | Governance, Repository | Lizenzdatei vor Commit bewusst prüfen; vorbereitete Wahl nicht als automatisch genehmigt darstellen. | Accepted |
| SASD-PFB-007 | Pilot 01 | Folgewellen würden ohne Verifikationsgate offene Risiken verdecken. | Pilotprogramm, Prozesse | Wave 02 erst nach Commit-, Build-, Test-, Start- und CI-Nachweis beginnen. | Accepted |
| SASD-PFB-008 | Pilot 01 | Ein öffentlicher Snapshot kann nach lokaler Arbeit veraltet sein. | Evidence, Tooling | Dauerhafte Nachweise nach Commit auf vollständige Commit-ID umstellen. | Candidate |

## Änderungsregel

`Accepted` bedeutet, dass das Feedback in informativen Pilotregeln, Vorlagen oder Tooling berücksichtigt wurde. Änderungen an normativen Core-, Profil- oder Prozessanforderungen benötigen weiterhin den Governance-Änderungsprozess.
