---
title: "C#/.NET Project Sizing Guide"
document-id: SASD-REF-DOTNET-002
document-type: informative
status: Draft
version: 0.9.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [DotNet]
depends-on: [SASD-PROF-DOTNET-001, SASD-PROF-DOTNET-002, SASD-CORE-006]
generated: false
---

# C#/.NET Project Sizing Guide

## Zweck

Dieser Leitfaden hilft Einzelentwicklern und kleinen Teams, eine angemessene Solution-Struktur zu wählen. Er ist informativ und darf nicht als Zwang zu einer bestimmten Anzahl von Projekten gelesen werden.

## Variante A: kleines Werkzeug

Geeignet für kleine CLI-, Desktop- oder Automatisierungswerkzeuge mit überschaubarer Fachlogik.

```text
src/Sasd.Tool/
tests/Sasd.Tool.Tests/
```

Innerhalb des Produktprojekts können Ordner wie `Features`, `Services`, `Persistence` und `Diagnostics` Zuständigkeiten sichtbar machen. Eine zusätzliche Schicht entsteht erst bei realem Nutzen.

## Variante B: gewartete Anwendung

Geeignet für reguläre SASD-Anwendungen mit UI oder Host, Fachlogik, lokaler Persistenz und mehreren Integrationen.

```text
src/
├── Sasd.Product.Domain/
├── Sasd.Product.Application/
├── Sasd.Product.Infrastructure/
└── Sasd.Product.Host/
tests/
├── Sasd.Product.Domain.Tests/
├── Sasd.Product.Application.Tests/
└── Sasd.Product.IntegrationTests/
```

## Variante C: komplexeres Produkt

Geeignet bei mehreren Hosts, Plugins, öffentlichen Contracts, separaten Deployment-Einheiten oder sicherheitskritischen Grenzen.

```text
src/
├── Sasd.Product.Domain/
├── Sasd.Product.Application/
├── Sasd.Product.Contracts/
├── Sasd.Product.Infrastructure/
├── Sasd.Product.ExtensionModel/
├── Sasd.Product.Desktop/
└── Sasd.Product.Worker/
tests/
├── ...UnitTests/
├── ...IntegrationTests/
├── ...ArchitectureTests/
└── ...SystemTests/
```

## Signale für eine Aufteilung

- ein Bereich benötigt andere Pakete oder Plattformtargets,
- fachliche Logik lässt sich nicht ohne UI oder Datenbank testen,
- mehrere Hosts verwenden denselben Kern,
- öffentliche Contracts benötigen eigene Stabilität,
- Build- oder Änderungszeiten koppeln unabhängige Bereiche,
- Sicherheits- oder Plugin-Grenzen benötigen eine Assembly-Grenze.

## Signale gegen eine Aufteilung

- Projekte enthalten nur wenige Weiterleitungs- oder DTO-Typen,
- jede kleine Änderung erfordert Änderungen in fast allen Projekten,
- Abstraktionen existieren ohne zweite Implementierung, Testnutzen oder Grenze,
- die Struktur erschwert das Verständnis stärker als sie schützt.
