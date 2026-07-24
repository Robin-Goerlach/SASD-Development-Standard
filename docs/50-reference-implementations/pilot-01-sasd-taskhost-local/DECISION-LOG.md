---
title: "Pilot 01 Entscheidungslog – SASD TaskHost Local"
document-id: SASD-REF-PILOT-109
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
depends-on: [SASD-REF-PILOT-102, SASD-PROC-003]
---

# Entscheidungslog – SASD TaskHost Local

| Decision-ID | Entscheidung | Begründung | Status |
|---|---|---|---|
| P01-DEC-001 | TaskHost Local ist Pilot 01. | kleines reales WinForms-/SQLite-Projekt mit dokumentiertem Blocker und guter Dokumentationsbasis | Accepted |
| P01-DEC-002 | Zielstufe ist SASD Recommended. | langfristige Nutzung und persistente private Daten; Production wäre derzeit unverhältnismäßig | Accepted |
| P01-DEC-003 | Das eine Produktionsprojekt bleibt in Wave 01 bestehen. | Small-Projekt; zusätzliche Schichtenprojekte würden keinen belegten Nutzen liefern | Accepted |
| P01-DEC-004 | Ein separates Testprojekt wird ergänzt. | Datenbankinitialisierung benötigt isolierten Regressionsschutz | Accepted |
| P01-DEC-005 | Der Startblocker hat Vorrang vor kosmetischen Standarddateien. | Nutzbarkeit und Datenintegrität sind wichtiger als Repository-Optik | Accepted |
| P01-DEC-006 | Wave 01 enthält kein WPF-, EF-Core- oder DI-Refactoring. | nicht zur Stabilisierung erforderlich und außerhalb des MVP-Scopes | Accepted |
| P01-DEC-007 | Öffentliche Repository-Beobachtungen werden nicht als lokale Verifikation dargestellt. | schützt vor unzutreffenden Alignment-Aussagen | Accepted |
| P01-DEC-008 | MIT wird als Lizenzentscheidung vorbereitet, aber vor Commit vom Eigentümer geprüft. | plausible Open-Source-Lizenz, dennoch bewusste Eigentümerentscheidung | Accepted |
| P01-DEC-009 | Pilotabschluss erfordert technische Ausführung im Ziel-Repository. | Dokumentplanung allein ist keine Referenzimplementierung | Accepted |
| P01-DEC-010 | Der historische SQLite-Fehler wird nicht als ursächlich behoben bezeichnet, solange er nicht reproduziert oder eindeutig durch einen Regressionstest abgedeckt ist. | sichtbare SQL-Anweisungen lieferten keine sichere Ursachenzuordnung | Accepted |
| P01-DEC-011 | Das Wave-01-ZIP gilt als Evidenzklasse `A`, nicht `V`. | statisch geprüftes Artefakt ist kein gebauter oder gestarteter Zielstand | Accepted |
| P01-DEC-012 | Wave 02 beginnt erst nach Wave-01-Verifikation. | offene Build-, Daten- und Laufzeitrisiken dürfen nicht verdeckt werden | Accepted |
| P01-DEC-013 | Startup-Diagnose darf teilweise aus Wave 02 vorgezogen werden. | Diagnose ist für die Verifikation des historischen Startfehlers unmittelbar erforderlich | Accepted |

## ADR-Bedarf im Ziel-Repository

Für Wave 01 sind mindestens zu prüfen oder zu dokumentieren:

- Ein-Projekt-Architektur für das MVP,
- direkter SQLite-Zugriff ohne ORM,
- Ablagepfad lokaler Daten,
- MIT-Lizenz,
- Teststrategie für Datenbankinitialisierung,
- Diagnosepfad bei Startfehlern.
