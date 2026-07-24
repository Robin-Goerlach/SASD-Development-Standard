---
title: "WPF Guidance"
document-id: SASD-REF-DESKTOP-003
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

# WPF Guidance

## Ziel

Dieser Leitfaden zeigt eine pragmatische Umsetzung des Desktopprofils mit WPF. Er erzeugt keine zusätzlichen normativen Anforderungen.

## Empfohlene Struktur

```text
Product.Wpf
├── Views/
├── ViewModels/
├── Controls/
├── Resources/
├── Services/
├── App.xaml
└── App.xaml.cs
Product.Application
Product.Domain          optional
Product.Infrastructure
Product.Tests
```

Bei modularen Produkten können Views und ViewModels fachlich pro Modul statt rein technisch gegliedert werden.

## MVVM pragmatisch anwenden

ViewModels eignen sich für:

- darstellungsbezogenen Zustand,
- Commands und deren Verfügbarkeit,
- Validierungsrückmeldung,
- Auswahl und Filter,
- Koordination testbarer Use Cases.

Code-behind ist angemessen für:

- Fokus und Tastaturdetails,
- Animationen,
- Drag-and-drop,
- rein visuelles Verhalten,
- Frameworkereignisse, die nicht sinnvoll abstrahiert werden.

Code-behind wird problematisch, wenn es Datenzugriff, Geschäftsregeln oder komplexe Workflowsteuerung übernimmt.

## Binding

- Binding Mode und `UpdateSourceTrigger` werden bewusst gewählt.
- Eingabedialoge können Änderungen explizit committen, statt jedes Zeichen sofort in das Modell zu schreiben.
- Bindingfehler werden in Entwicklung und Tests sichtbar gemacht.
- Konverter bleiben klein und frei von Geschäftslogik.
- Teure Berechnungen werden nicht bei jedem Bindingzugriff wiederholt.

## Commands und Dialoge

Commands modellieren Benutzeraktionen und `CanExecute`. Dialoge und Dateiauswahl können über schmale UI-Dienste abstrahiert werden. Ein allgemeiner Dialogservice mit beliebigen Strings und Objekten ist weniger hilfreich als fachlich verständliche Verträge.

## Dispatcher und Hintergrundarbeit

WPF-Objekte besitzen Thread-Affinität. Lange Operationen laufen außerhalb des UI-Threads; Ergebnisse werden über Dispatcher, Progress oder auf dem erfassten Synchronisationskontext zurückgeführt. Große Mengen einzelner Dispatcher-Aufrufe werden aggregiert.

## Ressourcen, Styles und Themes

- Gemeinsame Styles und Ressourcen werden zentral gepflegt.
- `DynamicResource` wird nur eingesetzt, wenn Laufzeitänderungen benötigt werden.
- ControlTemplates dürfen Fokus, Accessibility und Standardzustände nicht unabsichtlich entfernen.
- Themeänderungen werden auf Kontrast, deaktivierte Zustände und Validierungsdarstellung geprüft.

## Validierung

WPF bietet Binding Validation, `IDataErrorInfo`, `INotifyDataErrorInfo` und benutzerdefinierte ValidationRules. Das Projekt wählt ein konsistentes Modell. Fehlermeldungen müssen textlich verfügbar, fokussierbar oder assistiv erreichbar sein.

## Testbarkeit

ViewModels und Präsentationsdienste werden ohne `Application`-Start getestet. UI-Tests konzentrieren sich auf Bindingintegration, Fokus, Navigation, Dialogabläufe und kritische visuelle Zustände.
