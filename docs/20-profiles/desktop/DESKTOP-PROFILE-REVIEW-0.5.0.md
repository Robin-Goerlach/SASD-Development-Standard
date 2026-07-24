---
title: "Desktop Profile Review 0.5.0"
document-id: SASD-REF-DESKTOP-005
document-type: informative
status: Draft
version: 0.5.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Desktop]
depends-on: [SASD-PROF-DESKTOP-001, SASD-PROF-DESKTOP-002, SASD-PROF-DESKTOP-003, SASD-PROF-DESKTOP-004]
generated: false
---

# Desktop Profile Review 0.5.0

## Reviewziel

Prüfung des ersten vollständigen Desktopprofils auf Konsistenz mit Core und .NET-Profil, Proportionalität für Einzelentwickler, Technologie-Neutralität zwischen WinForms und WPF sowie Abdeckung von UI-Architektur, UX und Lebenszyklus.

## Prüfergebnis

| Prüffeld | Ergebnis |
|---|---|
| Dokumentstruktur und Metadaten | bestanden |
| eindeutige Anforderungs-IDs | bestanden |
| Überschneidungen zwischen vier Dokumenten | bereinigt |
| Core- und .NET-Abhängigkeiten | nachvollziehbar |
| Minimum/Recommended/Production | proportional |
| kleine WinForms-Werkzeuge | ohne Pflicht zur Überarchitektur abgedeckt |
| WPF und MVVM | pragmatisch statt dogmatisch geregelt |
| Accessibility und DPI | als Produktqualität enthalten |
| Deployment und Update | als Architektur- und Lebenszyklusthema enthalten |
| technologiespezifische Hilfe | getrennte informative Leitfäden vorhanden |

## Bewusste Abgrenzungen

Version 0.5.0 enthält noch keine normativen Spezialprofile für:

- WinUI 3,
- Avalonia,
- .NET MAUI Desktop,
- Electron oder WebView-basierte Shells,
- macOS- oder Linux-Desktopdistribution,
- ein verbindliches SASD-Visual-Design-System.

Diese Technologien können gemeinsame Desktopanforderungen übernehmen, benötigen aber vor einer formalen Alignment-Aussage technologiespezifische Ergänzungen.

## Offene Pilotfragen

1. Sind die Minimum-Anforderungen für TaskHost Local oder vergleichbare Werkzeuge schlank genug?
2. Lassen sich bestehende WinForms-Anwendungen ohne künstliche Presenter-Schicht sinnvoll bewerten?
3. Welche Anforderungen deckt der Prompt Manager bereits nachweisbar ab?
4. Welche WPF-Regeln müssen am Personal Desktop Dashboard praktisch nachgeschärft werden?
5. Welche Deploymentformen werden in SASD-Projekten tatsächlich benötigt?

## Reifeentscheidung

Die vier normativen Dokumente werden als **Proposed 0.5.0** eingestuft. Sie sind vollständig genug für Pilot Assessments, stellen aber vor Abschluss der Pilotierung noch keine Approved-Version dar.
