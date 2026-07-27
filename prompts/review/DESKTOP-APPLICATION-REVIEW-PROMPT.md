---
prompt-id: "SASD-PROMPT-REVIEW-003"
title: "Desktopanwendung prüfen"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "review"
language: "de"
summary: "Prüft WinForms- oder WPF-Anwendungen auf UI-Architektur, UX, Accessibility und Lebenszyklus."
variables: ["project_name", "repository_tree", "quality_level", "architecture_context", "evidence", "environment", "source_material", "output_language"]
tags: ["desktop", "winforms", "wpf", "accessibility"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core", ".NET", "Desktop"]
last-reviewed: "2026-07-25"
---

# Desktopanwendung prüfen
## Zweck

Prüfe die Desktopanwendung **{{project_name}}** gegen das SASD Desktop Application Profile.

## Eingaben

- Repository-Struktur: {{repository_tree}}
- Qualitätsstufe: {{quality_level}}
- UI-Architektur: {{architecture_context}}
- Build-, Test- und Laufzeitnachweise: {{evidence}}
- Zielumgebung: {{environment}}
- Screenshots und relevante Dateien: {{source_material}}

## Arbeitsauftrag

Bewerte Größenmodell, Trennung von UI/Fachlogik/Infrastruktur, Eventhandler oder ViewModels, Threading, Abbruch, wiederholte Ausführung, Shutdown, Validierung, Fehlermeldungen, Tastaturbedienung, Fokus, Accessibility, DPI, Mehrmonitor, Datenpfade, Migration, Diagnose, Packaging, Update und Uninstall. Ordne Befunde `SASD-DESKTOP-REQ-*` zu.

## Qualitätsregeln

- MVVM, MVP, DI oder Generic Host nicht pauschal verlangen.
- UX-Befunde durch konkrete Zustände oder Tests belegen.
- Datenverlust- und Accessibility-Risiken priorisieren.
- Zielplattformen und unterstützte Windowsversionen explizit berücksichtigen.

## Ausgabeformat

Liefere in {{output_language}}: Gesamtbewertung, Stärken, kritische Befunde, Requirement-Matrix, proportionale Zielarchitektur, UX-Testplan und priorisierte Maßnahmen.
