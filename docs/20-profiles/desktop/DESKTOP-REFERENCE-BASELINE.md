---
title: "Desktop Reference Baseline"
document-id: SASD-REF-DESKTOP-001
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
depends-on: [SASD-PROF-DESKTOP-001]
generated: false
---

# Desktop Reference Baseline

## Zweck

Diese Referenzbasis dokumentiert die primären technischen Quellen und die daraus abgeleiteten Leitentscheidungen des Desktopprofils. Normative Anforderungen stehen ausschließlich in den vier Profildokumenten.

## Offizielle Primärquellen

Stand der Prüfung: **24. Juli 2026**.

| Thema | Primärquelle | Relevanz |
|---|---|---|
| .NET Desktop Guide | <https://learn.microsoft.com/en-us/dotnet/desktop/> | gemeinsame Dokumentation für WinForms und WPF |
| .NET Desktop SDK | <https://learn.microsoft.com/en-us/dotnet/core/project-sdk/msbuild-props-desktop> | `UseWindowsForms`, `UseWPF`, Windows-TFM und Desktop-MSBuild-Eigenschaften |
| WinForms Overview | <https://learn.microsoft.com/en-us/dotnet/desktop/winforms/overview/> | Plattformmodell und typische UI-Entwicklung |
| WPF Overview | <https://learn.microsoft.com/en-us/dotnet/desktop/wpf/overview/> | Windows-only, XAML, Binding, Layout und Rendering |
| WinForms Generic Host | <https://learn.microsoft.com/en-us/dotnet/desktop/winforms/advanced/how-to-use-host-builder> | optionaler Host-Lebenszyklus und DI |
| WinForms Accessibility | <https://learn.microsoft.com/en-us/dotnet/desktop/winforms/advanced/windows-forms-accessibility> | Accessibility-Grundlagen |
| WinForms Accessible Information | <https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/provide-accessibility-information> | `AccessibleName` und Beschreibungen |
| WinForms ErrorProvider | <https://learn.microsoft.com/en-us/dotnet/desktop/winforms/controls/errorprovider-component-overview-windows-forms> | nicht intrusive Eingabevalidierung |
| WinForms High DPI | <https://learn.microsoft.com/en-us/dotnet/desktop/winforms/high-dpi-support-in-windows-forms> | DPI-Verhalten und Migration |
| WPF Data Binding | <https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/> | Bindingmodell und Zustandskopplung |
| WPF Binding Validation | <https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/how-to-implement-binding-validation> | Validierungsrückmeldung |
| WPF Threading Model | <https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/threading-model> | Dispatcher und Thread-Affinität |
| WPF Focus | <https://learn.microsoft.com/en-us/dotnet/desktop/wpf/advanced/focus-overview> | Fokus und Tastaturnavigation |
| .NET Publishing | <https://learn.microsoft.com/en-us/dotnet/core/deploying/> | framework-dependent, self-contained und Publishoptionen |
| Single File | <https://learn.microsoft.com/en-us/dotnet/core/deploying/single-file/overview> | Grenzen und plattformspezifische Artefakte |
| Windows Packaging | <https://learn.microsoft.com/en-us/windows/apps/package-and-deploy/packaging/> | paketierte und nicht paketierte Desktopapps |
| SmartScreen | <https://learn.microsoft.com/en-us/windows/apps/package-and-deploy/smartscreen-reputation> | Vertrauens- und Verteilungsaspekte |

## Leitentscheidungen

1. **WinForms und WPF bleiben gültige Technologien.** Das Profil bevorzugt keine Technologie pauschal.
2. **WPF ist Windows-only.** Die Nutzung von .NET macht eine WPF-Anwendung nicht plattformübergreifend.
3. **Modernes .NET ist die bevorzugte Basis.** .NET Framework bleibt ein begründeter Legacyfall.
4. **UI-Thread-Regeln sind verbindlich.** WPF Dispatcher und WinForms UI-Kontext müssen bewusst behandelt werden.
5. **MVVM ist kein Selbstzweck.** WPF profitiert häufig davon, kleine Anwendungen dürfen proportional bleiben.
6. **High DPI und Accessibility sind Produktqualität.** Sie werden nicht auf spätere kosmetische Nacharbeit verschoben.
7. **Deployment ist Architektur.** Paketierung, Runtime, Signierung, Update und Datenmigration beeinflussen das Produktdesign.
8. **Single File und Trimming sind Optionen, keine Qualitätsmerkmale.** Sie werden nur nach Kompatibilitätsprüfung eingesetzt.

## Aktualisierung

Die Quellenbasis SOLLTE vor der Freigabe des Profils als `Approved`, bei Wechsel der .NET-LTS-Baseline und bei wesentlichen Änderungen an WinForms, WPF oder Windows-Paketierung erneut geprüft werden.
