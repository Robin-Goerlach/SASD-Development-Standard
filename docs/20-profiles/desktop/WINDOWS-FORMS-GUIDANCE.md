---
title: "Windows Forms Guidance"
document-id: SASD-REF-DESKTOP-002
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
depends-on: [SASD-PROF-DESKTOP-001, SASD-PROF-DESKTOP-002, SASD-PROF-DESKTOP-003, SASD-PROF-DESKTOP-004]
generated: false
---

# Windows Forms Guidance

## Ziel

Dieser Leitfaden zeigt eine pragmatische Umsetzung des Desktopprofils mit WinForms. Er erzeugt keine zusätzlichen normativen Anforderungen.

## Empfohlene Struktur

### Kleines Werkzeug

```text
Tool.WinForms
├── Forms/
├── Services/
├── Models/
├── Program.cs
└── Tool.WinForms.csproj
Tool.Tests
```

Formulare koordinieren Eingaben und Darstellung. Datei-, Netzwerk- und Datenbankzugriffe gehören in Dienste. Fachlich relevante Regeln werden separat getestet.

### Gepflegte Anwendung

```text
Product.WinForms
├── Forms/
├── Controls/
├── Presentation/
├── Dialogs/
└── Program.cs
Product.Application
Product.Domain          optional
Product.Infrastructure
Product.Tests
```

`Presentation` kann Presenter, Controller, View-Verträge oder UI-Zustandsmodelle enthalten.

## Bootstrap

Für modernes .NET ist ein kompakter Einstieg angemessen:

```csharp
[STAThread]
static void Main()
{
    ApplicationConfiguration.Initialize();
    Application.Run(new MainForm());
}
```

Wenn Logging, Konfiguration, DI und Hintergrunddienste benötigt werden, kann der Generic Host eingebunden werden. Für eine kleine Anwendung ist er nicht automatisch notwendig.

## Form-Klassen

Günstig:

- Controls konfigurieren,
- Ereignisse an Präsentationslogik weiterleiten,
- UI-Zustand anwenden,
- Fokus und rein visuelles Verhalten steuern,
- Ressourcen beim Schließen freigeben.

Ungünstig:

- SQL oder HTTP direkt im Click-Handler,
- globale Singletonzugriffe,
- mehrere hundert Zeilen fachlicher Ablauf in einer Form,
- unbeobachtete `Task.Run`-Aufrufe,
- direkte Manipulation anderer Formulare über öffentliche Controls.

## Layout und DPI

- `TableLayoutPanel`, `FlowLayoutPanel`, Docking und Anchoring helfen bei variabler Größe.
- AutoSize und Mindestgrößen müssen gemeinsam getestet werden.
- Bei modernem .NET sollte DPI-Konfiguration über Projektoptionen beziehungsweise `ApplicationConfiguration.Initialize()` erfolgen, nicht doppelt im Manifest.
- Pixelperfekte Legacy-Layouts benötigen besondere Migrations- und DPI-Tests.

## Validierung

`ErrorProvider` eignet sich für dauerhafte feldbezogene Fehler. Eine MessageBox allein ist für Eingabefehler meist ungeeignet. Fachliche Validierung bleibt in Application oder Domain wiederverwendbar.

## Accessibility

- Controls mit unklarem visuellen Text erhalten `AccessibleName` und gegebenenfalls `AccessibleDescription`.
- Tab-Reihenfolge und Access Keys werden geprüft.
- Benutzerdefinierte Controls benötigen ein bewusstes Accessibility-Modell.
- Fokus darf nach Fehlern und Dialogen nicht verloren gehen.

## Threading

- I/O wird asynchron ausgeführt.
- UI-Updates erfolgen im UI-Kontext.
- `InvokeRequired`, `Invoke`, `BeginInvoke`, `SynchronizationContext` oder kontrollierte Progress-Mechanismen werden passend eingesetzt.
- Wiederholte Klicks während einer Operation werden verhindert.

## Designerfähigkeit

Designerdateien bleiben generiert. Konstruktoren von Forms und UserControls sollten keine externen Zugriffe ausführen. Abhängigkeiten, die den Designer stören, können über einen schlanken parameterlosen Designerpfad oder eine getrennte Initialisierung behandelt werden, ohne globale Service-Locator einzuführen.
