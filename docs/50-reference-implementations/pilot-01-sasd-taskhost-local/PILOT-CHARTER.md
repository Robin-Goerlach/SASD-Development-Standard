---
title: "Pilot 01 Charter – SASD TaskHost Local"
document-id: SASD-REF-PILOT-102
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
depends-on: [SASD-REF-PILOT-001, SASD-PROC-002, SASD-PROC-005]
---

# Pilot 01 Charter – SASD TaskHost Local

## 1. Pilotziel

Der Pilot soll zeigen, ob der SASD Development Standard ein kleines, bestehendes WinForms-Projekt kontrolliert stabilisieren und vereinheitlichen kann, ohne unnötige Projektaufteilung oder grundlegende Neuentwicklung zu verursachen.

## 2. Validierungsfragen

- Ist SASD Recommended für ein kleines, langfristig genutztes lokales Werkzeug angemessen?
- Lassen sich Core-, .NET- und Desktopprofil proportional anwenden?
- Reicht bei diesem Projekt ein Produktionsprojekt plus ein Testprojekt?
- Sind die Legacy-Migrations- und Reviewprozesse für Einzelentwicklung handhabbar?
- Welche Vorlagen und Nachweise fehlen für einen schnellen ersten Durchlauf?
- Wie klar trennt der Standard Blocker von langfristigen Qualitätsverbesserungen?

## 3. In Scope

- Klassifikation und Evidenzaufnahme,
- reproduzierbarer Restore und Release-Build,
- Analyse und Behebung des dokumentierten SQLite-Startfehlers,
- minimale automatisierte Regressionstests,
- Toolchain- und Analyzer-Basis,
- Windows-CI für Build und Tests,
- Lizenz- und Security-Grundlagen,
- SASD-Alignment- und Abweichungsnachweis,
- Verifikation von Datenpfad und Backupgrundlagen.

## 4. Out of Scope

- Migration von WinForms zu WPF, Avalonia oder MAUI,
- Cloud-Synchronisierung oder TaskHost-API,
- Benutzerkonten, Collaboration oder Netzwerkbetrieb,
- Aufteilung in Domain-, Application- und Infrastructure-Projekte,
- Entity Framework oder generische Repository-Frameworks,
- vollständiger UI-Neuentwurf,
- Production-Qualitätsstufe,
- installerfertiges Release bereits in Wave 01.

## 5. Erfolgskriterien für Wave 01

- Restore und Release-Build sind reproduzierbar dokumentiert.
- Die Anwendung startet ohne den dokumentierten SQLite-Syntaxfehler.
- Die Datenbankinitialisierung besitzt mindestens einen automatisierten Regressionstest.
- Ein Windows-CI-Lauf baut und testet die Solution.
- Lizenzentscheidung, Security-Hinweise und Pilot-Alignment sind nachvollziehbar dokumentiert.
- Die bestehende einfache Architektur bleibt erhalten, sofern kein konkreter Fehler eine Änderung verlangt.
- Alle offenen Punkte sind als Gap, Ausnahme oder spätere Welle klassifiziert.

## 6. Nicht-Erfolg

Der Pilot gilt nicht als erfolgreich, wenn lediglich Ordner umbenannt oder Standarddateien kopiert werden, während Startfehler, Datenrisiken oder Reproduzierbarkeit ungeklärt bleiben.
