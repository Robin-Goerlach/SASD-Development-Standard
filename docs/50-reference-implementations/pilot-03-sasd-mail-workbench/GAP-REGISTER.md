---
title: "Pilot 03 Gap Register – SASD Mail Workbench"
document-id: SASD-REF-PILOT-305
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
depends-on: [SASD-REF-PILOT-304, SASD-GOV-006]
---

# Gap Register – SASD Mail Workbench

| Gap-ID | Priorität | Bereich | Beobachtung | Zielzustand | Geplante Welle | Status |
|---|---|---|---|---|---|---|
| P03-GAP-001 | Blocker | Baseline | exakte Commit-ID und lokaler Toolchain-Nachweis fehlen | unveränderliche Baseline | Wave 01 | Open |
| P03-GAP-002 | Major | Build/Tests | sichtbare Projekte und Workflows nicht unabhängig ausgeführt | grüner Restore-, Build-, Test- und CI-Nachweis | Wave 01 | Open |
| P03-GAP-003 | Major | Architektur | Dependency-Regeln nicht praktisch ausgewertet | dokumentierter Architekturtest- und Dependency-Nachweis | Wave 01 | Open |
| P03-GAP-004 | Major | Recovery | Crash-, Staging-, Migration- und Wiederanlauffälle nicht provoziert | reproduzierbare Recovery-Testmatrix | Wave 01 | Open |
| P03-GAP-005 | Major | Security | vollständiges Threat Model für Maildaten fehlt im Pilotnachweis | Datenfluss-, Trust-Boundary- und Missbrauchsanalyse | Wave 01 | Open |
| P03-GAP-006 | Major | Testdaten | Herkunft und Datenschutz der Sample-Mails nicht bestätigt | dokumentierte synthetische oder freigegebene Testdaten | Wave 01 | Open |
| P03-GAP-007 | Major | Production Gate | Übergang von Recommended zu Production nicht operationalisiert | messbare Kriterien vor realer Mailboxnutzung | Wave 01 | Open |
| P03-GAP-008 | Minor | Desktop | Desktopprofil nur teilweise anwendbar | sichtbare Applicability-Matrix bis UI-Meilenstein | Wave 01 | Open |
| P03-GAP-009 | Minor | Release | Paketierung, Upgrade und Rollback nicht praktisch geprüft | Release- und Recovery-Plan | Wave 02 | Planned |
| P03-GAP-010 | Minor | Extensions | Vertrauensmodell für spätere Erweiterungen nicht verifiziert | signierte/vertrauenswürdige Erweiterungsgrenzen | Wave 02 | Planned |
| P03-GAP-011 | Later | Protocols | Mailprotokolle noch nicht implementiert | separates Feature-Milestone mit Credential-Security | außerhalb Pilot Wave 01 | Planned |
| P03-GAP-012 | Minor | Alignment | kein aktueller SASD-Alignment-Record | Core-/DotNet-/partielle Desktopbewertung | Wave 01 | Open |
