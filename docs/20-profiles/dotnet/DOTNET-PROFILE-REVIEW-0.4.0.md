---
title: "C#/.NET Profile Review 0.4.0"
document-id: SASD-REF-DOTNET-003
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
depends-on: [SASD-PROF-DOTNET-001, SASD-PROF-DOTNET-002, SASD-PROF-DOTNET-003, SASD-PROF-DOTNET-004, SASD-PROF-DOTNET-005, SASD-PROF-DOTNET-006, SASD-PROF-DOTNET-007, SASD-PROF-DOTNET-008]
generated: false
---

# C#/.NET Profile Review 0.4.0

## Ziel

Dokumentation des internen Reviews, mit dem die acht .NET-Dokumente von `Planned` auf `Proposed 0.4.0` angehoben wurden.

## Prüfumfang

- Abgrenzung zum technologieunabhängigen Core Standard,
- Skalierbarkeit für kleine, mittlere und komplexe SASD-Projekte,
- Vermeidung dogmatischer Clean-Architecture-Vorgaben,
- reproduzierbarer Build und unterstützte .NET-Versionen,
- Nullable, Analyzer, XML-Dokumentation und Kommentare,
- Fehlerbehandlung, Logging, Secrets und lokale Pfade,
- Persistenz, Migration, Backup und Provider-Tests,
- Teststruktur, CI, Flaky Tests und Packaging,
- Eindeutigkeit und maschinelle Prüfbarkeit der Anforderungs-IDs.

## Wesentliche Entscheidungen

1. Das Profil bindet nicht dauerhaft an eine konkrete .NET-Hauptversion, sondern an unterstützte Releases und eine dokumentierte Supportentscheidung.
2. LTS ist die bevorzugte Baseline für Recommended und Production, aber keine starre Vorgabe für alle Projekte.
3. Kleine Werkzeuge dürfen ein Produktprojekt behalten; Schichten und Assemblies entstehen erst bei realem Nutzen.
4. Nullable Reference Types sind für neuen Code verbindlich.
5. `var` wird pragmatisch verwendet, wenn der Typ eindeutig ist.
6. Öffentliche Bibliotheks-APIs benötigen XML-Dokumentation; Anwendungscode dokumentiert vor allem komplexe oder öffentliche Verträge.
7. xUnit ist SASD-Default, andere etablierte Frameworks bleiben zulässig.
8. DI und Generic Host werden nicht für jedes kleine Programm vorgeschrieben.
9. Persistence-Abstraktionen werden nicht pauschal erzwungen.
10. Proposed bedeutet pilotierbar, noch nicht Approved.

## Ergebnis

Die acht normativen Profildokumente sind vollständig, untereinander verlinkt und für die Pilotierung an bestehenden SASD-C#-Repositories geeignet. Offene Erkenntnisse aus den Piloten werden vor einer späteren Approval-Entscheidung in Version 0.5.x oder höher eingearbeitet.
