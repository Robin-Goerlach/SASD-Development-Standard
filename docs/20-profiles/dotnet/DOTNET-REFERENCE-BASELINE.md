---
title: "C#/.NET Reference Baseline"
document-id: SASD-REF-DOTNET-001
document-type: informative
status: Draft
version: 0.4.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [DotNet]
depends-on: [SASD-PROF-DOTNET-001]
generated: false
---

# C#/.NET Reference Baseline

## Zweck

Dieses informative Dokument hält die technische Referenzbasis fest, auf deren Grundlage das Proposed-0.4.0-Profil erstellt wurde. Die Links sind Orientierung; normative Anforderungen stehen ausschließlich in den Profildokumenten.

## Baseline am 24. Juli 2026

- .NET 10 ist die aktuelle LTS-Linie. Der Standard bindet Projekte dennoch nicht dauerhaft an eine konkrete Hauptversion, sondern verlangt eine unterstützte und dokumentierte Version.
- LTS-Versionen erhalten längere Unterstützung als STS-Versionen. Production-Projekte bevorzugen deshalb LTS, sofern fachliche Anforderungen nicht dagegensprechen.
- Nullable Reference Types, Roslyn-Analyzer und `.editorconfig` sind zentrale Werkzeuge für compile-time geprüfte Verträge und konsistenten Stil.
- `Directory.Build.props` ermöglicht gemeinsame MSBuild-Eigenschaften; `Directory.Packages.props` unterstützt zentrale NuGet-Paketversionen.
- `Microsoft.Extensions.DependencyInjection`, Configuration, Options, Logging und Generic Host bilden eine gemeinsame Plattform für Anwendungen, die diese Infrastruktur benötigen.

## Primärquellen

- [.NET Support Policy](https://dotnet.microsoft.com/platform/support/policy/dotnet-core)
- [.NET Releases and Support](https://learn.microsoft.com/dotnet/core/releases-and-support)
- [C# Coding Conventions](https://learn.microsoft.com/dotnet/csharp/fundamentals/coding-style/coding-conventions)
- [Nullable Reference Types](https://learn.microsoft.com/dotnet/csharp/nullable-references)
- [.NET Code Analysis](https://learn.microsoft.com/dotnet/fundamentals/code-analysis/overview)
- [Code Style Rule Options](https://learn.microsoft.com/dotnet/fundamentals/code-analysis/code-style-rule-options)
- [Central Package Management](https://learn.microsoft.com/nuget/consume-packages/central-package-management)
- [Dependency Injection in .NET](https://learn.microsoft.com/dotnet/core/extensions/dependency-injection/overview)
- [.NET Generic Host](https://learn.microsoft.com/dotnet/core/extensions/generic-host)
- [Logging in .NET](https://learn.microsoft.com/dotnet/core/extensions/logging/overview)
- [Options Pattern](https://learn.microsoft.com/dotnet/core/extensions/options)

## Aktualisierung

Vor der Freigabe eines Approved-Profils sind Support- und Toolingannahmen erneut anhand offizieller Primärquellen zu prüfen. Versionssnapshots werden informativ aktualisiert, ohne die stabilen normativen Ziele unnötig zu verändern.
