---
title: "Desktop Project Sizing Guide"
document-id: SASD-REF-DESKTOP-004
document-type: informative
status: Draft
version: 0.9.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Desktop]
depends-on: [SASD-PROF-DESKTOP-001, SASD-PROF-DESKTOP-002]
generated: false
---

# Desktop Project Sizing Guide

## Zweck

Der Leitfaden verhindert sowohl unstrukturierte Großformulare als auch überdimensionierte Architektur in kleinen Werkzeugen.

## Modell A: Compact Desktop Tool

Geeignet bei:

- ein bis drei Hauptansichten,
- lokalem oder einfachem externem Datenzugriff,
- einem Maintainer,
- begrenzter Lebensdauer oder kleinem Funktionsumfang.

Mindestartefakte:

- ein UI-Projekt,
- ein Testprojekt, sobald fachliche Logik existiert,
- README, Datenpfade und Release-Smoke-Test,
- Dienste für I/O und Integrationen.

Nicht automatisch erforderlich:

- Generic Host,
- Domainprojekt,
- Navigation Framework,
- globaler Event Bus,
- Pluginarchitektur.

## Modell B: Maintained Desktop Application

Geeignet bei:

- mehreren Arbeitsbereichen,
- langfristiger Pflege,
- lokaler Persistenz oder externen Diensten,
- regelmäßigen Releases,
- mehreren komplexen Formularen oder Fenstern.

Empfehlungen:

- UI-, Application- und Infrastructure-Projekt,
- Presenter oder ViewModels,
- gemeinsame Dialog-, Navigation- und Benachrichtigungsdienste,
- automatisierte Tests der Präsentationslogik,
- definierter Installer- und Updateprozess,
- dokumentierte UX- und Accessibility-Prüfung.

## Modell C: Complex Desktop Product

Geeignet bei:

- mehreren fachlichen Modulen,
- Erweiterbarkeit oder Plugins,
- geschäftskritischen Daten,
- mehreren Teams oder Releasekanälen,
- umfangreicher Offline-/Online-Synchronisation.

Zusätzliche Anforderungen:

- explizite Modulgrenzen,
- Shell- und Navigationmodell,
- Verträge und Versionsregeln,
- Fehlerisolation,
- observierbare Hintergrundprozesse,
- systematische UI-Automatisierung,
- Update-, Rollback- und Datenmigrationsmatrix.

## Entscheidungshilfe

Ein Projekt SOLLTE mit dem kleinsten Modell beginnen, das die absehbaren Anforderungen sicher trägt. Der Übergang zu einem größeren Modell wird durch konkrete Schmerzen ausgelöst, beispielsweise untestbare Formklassen, zyklische Abhängigkeiten, widersprüchliche Navigation oder unbeherrschbare Releasevarianten.
