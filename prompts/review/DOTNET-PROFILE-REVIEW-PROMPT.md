---
prompt-id: "SASD-PROMPT-REVIEW-002"
title: "C#/.NET-Profilreview"
version: "0.13.0"
status: "Candidate"
package-id: "sasd-development-standard-v1"
category: "review"
language: "de"
summary: "Prüft ein C#/.NET-Repository gegen Core und das SASD-.NET-Profil."
variables: ["project_name", "repository_tree", "quality_level", "evidence", "architecture_context", "source_material", "output_language"]
tags: ["dotnet", "csharp", "profile-review", "tests"]
quality-levels: ["Minimum", "Recommended", "Production"]
profiles: ["Core", ".NET"]
last-reviewed: "2026-07-25"
---

# C#/.NET-Profilreview
## Zweck

Prüfe **{{project_name}}** gegen den SASD Core Standard und das C#/.NET-Profil.

## Eingaben

- Repository-Struktur: {{repository_tree}}
- Qualitätsstufe: {{quality_level}}
- Build-, Test- und CI-Nachweise: {{evidence}}
- Architektur: {{architecture_context}}
- Projektdateien und Konfiguration: {{source_material}}

## Arbeitsauftrag

Prüfe SDK- und Runtimewahl, Solutionstruktur, Abhängigkeitsrichtung, Nullable, Analyzer, Async, Ressourcenfreigabe, Fehlerbehandlung, Logging, Konfiguration, Secrets, Datenpfade, Persistenz, Migrationen, Testisolation, Paketverwaltung, CI und Packaging. Ordne Befunde exakten `SASD-DOTNET-REQ-*`-IDs zu.

## Qualitätsregeln

- Unterscheide erfüllt, nicht anwendbar, Ausnahme, offen und nicht bewertet.
- Empfehle keine zusätzlichen Projekte, Abstraktionen oder Frameworks ohne konkreten Nutzen.
- Sourcecode und erfolgreicher Lauf sind verschiedene Nachweise.
- Priorisiere Datenverlust, Security, Buildreproduzierbarkeit und Wartbarkeit.

## Ausgabeformat

Erzeuge in {{output_language}}: Zusammenfassung, Annahmen, Befunde, Requirement-Matrix, Quick Wins, Migrationsplan, Ausnahmen und Validierungsbefehle.
