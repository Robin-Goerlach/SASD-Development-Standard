---
title: "Pilot 01 Entscheidungslog – SASD TaskHost Local"
document-id: SASD-REF-PILOT-109
document-type: informative
status: Draft
version: 0.7.0
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
| P01-DEC-004 | Ein separates Testprojekt darf ergänzt werden. | Datenbankinitialisierung benötigt isolierten Regressionsschutz | Accepted |
| P01-DEC-005 | Der Startblocker hat Vorrang vor kosmetischen Standarddateien. | Nutzbarkeit und Datenintegrität sind wichtiger als Repository-Optik | Accepted |
| P01-DEC-006 | Wave 01 enthält kein WPF-, EF-Core- oder DI-Refactoring. | nicht zur Fehlerbehebung erforderlich und außerhalb des MVP-Scopes | Accepted |
| P01-DEC-007 | Öffentliche Repository-Beobachtungen werden nicht als lokale Verifikation dargestellt. | schützt vor unzutreffenden Compliance-Aussagen | Accepted |
| P01-DEC-008 | Lizenz wird im Ziel-Repository bewusst entschieden. | der Standard darf Eigentümerentscheidung nicht automatisch vorwegnehmen | Proposed |
| P01-DEC-009 | Pilotabschluss erfordert technische Ausführung im Ziel-Repository. | Dokumentplanung allein ist keine Referenzimplementierung | Accepted |

## ADR-Bedarf im Ziel-Repository

Für Wave 01 ist mindestens zu prüfen, ob folgende Entscheidungen als ADR festgehalten oder in bestehende ADRs integriert werden:

- Ein-Projekt-Architektur für das MVP,
- direkter SQLite-Zugriff ohne ORM,
- Ablagepfad lokaler Daten,
- gewählte Lizenz,
- Teststrategie für Datenbankinitialisierung.
