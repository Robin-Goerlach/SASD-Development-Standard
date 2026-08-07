# Dokumentation

Dieses Verzeichnis enthält die fachliche Dokumentation und die Source of Truth des SASD Development Standard.

## Progressive Disclosure

Ein Anwender soll nicht zuerst die gesamte Dokumenthierarchie lesen müssen. Nutze den Bereich, der zu deiner aktuellen Aufgabe gehört, und gehe erst bei Bedarf tiefer.

> **Complexity available, not imposed.**

## 1. Using SASD — ein Produkt nach SASD entwickeln

Für neue Anwender und Projektentwickler:

1. [Quick Start](../QUICKSTART.md) — der kürzeste Einstieg.
2. [Projektbrief-Vorlage](../templates/documents/PROJECT-BRIEF-TEMPLATE.md) — Problem, Ziel, Scope und Risiken kompakt erfassen.
3. [Projektklassifikation](30-processes/PROJECT-CLASSIFICATION.md) — Größenklasse, Qualitätsstufe und Profile wählen.
4. [New Project Process](30-processes/NEW-PROJECT.md) — wenn der Projektstart vollständig durchlaufen werden soll.
5. [Solo Developer Guide](10-core-standard/SOLO-DEVELOPER-GUIDE.md) — proportionaler Einsatz ohne unnötige Dokumenttrennung.
6. [Templates](../templates/) und [Checklists](../checklists/) — nur die für die aktuelle Tätigkeit hilfreichen Artefakte verwenden.

Für bestehende Projekte beginnt der Weg mit der [Legacy Migration](30-processes/LEGACY-MIGRATION.md).

## 2. SASD Specification — Regeln und fachliche Tiefe

Wenn du die vollständige Regel oder Begründung brauchst:

- [Foundation](00-foundation/) — Mandat, Scope, Prinzipien, Begriffe und Inhaltsarchitektur.
- [Core Standard](10-core-standard/README.md) — technologieunabhängige Anforderungen.
- [C#/.NET Profile](20-profiles/dotnet/README.md) — .NET-spezifische Konkretisierung.
- [Desktop Profile](20-profiles/desktop/README.md) — Desktop-/WinForms-/WPF-spezifische Konkretisierung.
- [Operative Prozesse](30-processes/README.md) — Klassifikation, Initialisierung, ADRs, Reviews, Migration, Releases und Archivierung.
- [Governance](40-governance/README.md) — normative Sprache, Dokumentlebenszyklus, Änderungen, Ausnahmen und Alignment.

Die verbindliche Rangfolge und die Trennung zwischen normativen, informativen und unterstützenden Inhalten stehen in der [Content Architecture](00-foundation/CONTENT-ARCHITECTURE.md).

## 3. Maintaining SASD — den Standard selbst pflegen

Diese Inhalte sind hauptsächlich für Maintainer und Reviewer des **SASD Development Standard** relevant, nicht für den normalen Projektstart:

- [Project Status](../PROJECT-STATUS.md)
- [Roadmap](../ROADMAP.md)
- [Version 1.0 Specification Baseline](40-governance/VERSION-1.0-SPECIFICATION-BASELINE.md)
- [Governance Overview](40-governance/README.md)
- [Reference Implementations and Pilots](50-reference-implementations/README.md)
- [Release-Candidate Readiness](40-governance/VERSION-1.0-RELEASE-CANDIDATE-READINESS.md)
- [Project History](90-project-history/README.md)

Historische Reviews, Approval-Manifeste, Readiness-Berichte und Pilot-Evidenz bleiben vollständig verfügbar, werden aber nicht als Pflichtlektüre für den Einstieg präsentiert.

## Standard und Tooling

Der Standard definiert anwendbare Regeln, erwartete Ergebnisse und erforderliche Evidenz. Die Repository-Tooling-Schicht (`../tooling/`, `../scripts/`, `../.github/`) automatisiert Prüfungen und Pflege, ist aber nicht mit dem normativen Standard gleichzusetzen.

Ein Projekt muss anwendbare normative Anforderungen erfüllen. Wo keine konkrete technische Umsetzung vorgeschrieben ist, darf dafür ein projekttauglicher gleichwertiger Mechanismus verwendet werden.

## Dokumentgruppen

| Verzeichnis | Inhalt |
|---|---|
| `00-foundation` | Mandat, Scope, Prinzipien, Begriffe und Inhaltsarchitektur |
| `10-core-standard` | technologieunabhängige Anforderungen und Anwendungshilfen |
| `20-profiles` | technologie- und projektspezifische Konkretisierungen |
| `30-processes` | operative Projektprozesse |
| `40-governance` | Pflege, Ausnahmen, Alignment, Baselines und Releases des Standards |
| `50-reference-implementations` | Pilotprogramm, Evidenz, Assessments, Migrationswellen und Lessons Learned |
| `90-project-history` | informative Entwicklungs- und Reviewhistorie |

## Vollständiger Review-Pfad

Wer den Standard selbst vollständig reviewen möchte, beginnt mit:

1. [Project Charter](00-foundation/PROJECT-CHARTER.md),
2. [Scope](00-foundation/SCOPE.md),
3. [Principles](00-foundation/PRINCIPLES.md),
4. [Content Architecture](00-foundation/CONTENT-ARCHITECTURE.md),
5. [Document Catalog](00-foundation/DOCUMENT-CATALOG.md),
6. anschließend Core, Profile, Prozesse und Governance nach Bedarf.

Dieser Review-Pfad ist bewusst **nicht** der normale Nutzerpfad.
