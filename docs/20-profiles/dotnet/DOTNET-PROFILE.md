---
title: "C#/.NET-Profil"
document-id: SASD-PROF-DOTNET-001
document-type: normative
status: Proposed
version: 0.4.0
standard-version: "1.0"
language: de
authoritative: true
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [DotNet]
depends-on: [SASD-CORE-003, SASD-CORE-005, SASD-CORE-006, SASD-CORE-007, SASD-CORE-008, SASD-CORE-009, SASD-CORE-010, SASD-CORE-011]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# C#/.NET-Profil

## 1. Zweck

Dieses Dokument konkretisiert den SASD Core Standard für C#- und .NET-Projekte. Es definiert die gemeinsame technische Basis für SDK-Auswahl, Build, Paketverwaltung, statische Analyse, Laufzeit, Deployment und die Anwendung der übrigen .NET-Profildokumente.

## 2. Geltungsbereich

Das Profil gilt für moderne .NET-Projekte mit C#, darunter Bibliotheken, Kommandozeilenwerkzeuge, Worker, Dienste, Webanwendungen und Desktopanwendungen. Projekttypen können zusätzliche Profile anwenden. Klassisches .NET Framework wird als Legacy- oder plattformspezifischer Sonderfall unterstützt, ist aber nicht die bevorzugte Basis für neue SASD-Projekte.

Das Profil legt keine konkrete UI-Technologie, Datenbank oder Webarchitektur fest.

## 3. Profilzusammensetzung

Ein C#/.NET-Projekt wendet mindestens dieses Dokument sowie die tatsächlich relevanten Fachbereiche an:

- [Solution- und Projektstruktur](SOLUTION-STRUCTURE.md)
- [C# Coding Standard](CODING-STANDARD.md)
- [Fehler- und Ausnahmebehandlung](ERROR-HANDLING.md)
- [Logging und Diagnose](LOGGING.md)
- [Konfiguration und Secrets](CONFIGURATION.md)
- [Persistenz](PERSISTENCE.md), sofern Daten dauerhaft gespeichert werden
- [.NET-Tests](DOTNET-TESTING.md)

## 4. Normative Anforderungen

| ID | Anforderung |
|---|---|
| SASD-DOTNET-REQ-001 | Ein Projekt, das dieses Profil anwendet, MUSS den technologieunabhängigen Core Standard und alle zusätzlich ausgewählten Profile gemeinsam betrachten. |
| SASD-DOTNET-REQ-002 | Die Anwendung des Profils MUSS im README oder in `docs/SASD-COMPLIANCE.md` mit Qualitätsstufe, Ziel-Frameworks und Profildokumentversion benannt werden. |
| SASD-DOTNET-REQ-003 | Neue Projekte SOLLTEN das SDK-Projektformat und ein aktuell unterstütztes modernes .NET verwenden. |
| SASD-DOTNET-REQ-004 | Ein neues Recommended- oder Production-Projekt SOLLTE eine unterstützte LTS-Version von .NET verwenden; eine STS- oder Vorschauversion benötigt eine dokumentierte fachliche Begründung. |
| SASD-DOTNET-REQ-005 | Nicht mehr unterstützte .NET-Versionen DÜRFEN NICHT für produktive Releases verwendet werden, sofern keine zeitlich begrenzte, risikobewertete Ausnahme vorliegt. |
| SASD-DOTNET-REQ-006 | Die verwendeten Target Framework Monikers, SDK-Anforderungen und unterstützten Betriebssysteme MÜSSEN nachvollziehbar dokumentiert sein. |
| SASD-DOTNET-REQ-007 | Ein Repository mit reproduzierbaren Build-Anforderungen SOLLTE das SDK mit `global.json` oder einem gleichwertigen Mechanismus eingrenzen. |
| SASD-DOTNET-REQ-008 | Die Roll-forward-Strategie des SDK MUSS für Recommended- und Production-Projekte bewusst gewählt und dokumentiert werden. |
| SASD-DOTNET-REQ-009 | Vorschau-SDKs, Vorschau-Sprachversionen und Vorschaupakete DÜRFEN NICHT unbeabsichtigt in reguläre Releases gelangen. |
| SASD-DOTNET-REQ-010 | Ein Projekt auf klassischem .NET Framework MUSS als Legacy- oder Plattformanforderung gekennzeichnet werden und SOLLTE eine Wartungs- oder Migrationsentscheidung dokumentieren. |
| SASD-DOTNET-REQ-011 | Build, Test und Paketwiederherstellung MÜSSEN über dokumentierte `dotnet`- oder MSBuild-Befehle reproduzierbar sein. |
| SASD-DOTNET-REQ-012 | Der kanonische Build DARF NICHT ausschließlich von nicht versionierten IDE-Einstellungen abhängen. |
| SASD-DOTNET-REQ-013 | Recommended- und Production-Projekte MÜSSEN mindestens Restore, Build und Test automatisiert oder mit einem wiederholbaren Skript ausführen können. |
| SASD-DOTNET-REQ-014 | Production-Releases SOLLTEN aus einem sauberen Checkout und mit deterministischen Build-Einstellungen erzeugt werden. |
| SASD-DOTNET-REQ-015 | Gemeinsame MSBuild-Eigenschaften SOLLTEN zentral über `Directory.Build.props`, `Directory.Build.targets` oder einen begründeten gleichwertigen Mechanismus gepflegt werden. |
| SASD-DOTNET-REQ-016 | Paketversionen in Solutions mit mehreren Projekten SOLLTEN zentral verwaltet werden. |
| SASD-DOTNET-REQ-017 | Direkte und transitive Abhängigkeiten MÜSSEN prüfbar sein; unnötige Pakete SOLLTEN entfernt werden. |
| SASD-DOTNET-REQ-018 | Paketquellen MÜSSEN explizit vertrauenswürdig sein und SOLLTEN für Production-Projekte über eine versionierte NuGet-Konfiguration oder eine kontrollierte Buildumgebung festgelegt werden. |
| SASD-DOTNET-REQ-019 | Lockfiles, Paketquellzuordnung oder andere Wiederherstellungsmechanismen SOLLTEN risikobasiert eingesetzt werden, wenn reproduzierbare oder abgesicherte Restores erforderlich sind. |
| SASD-DOTNET-REQ-020 | Kompilierungswarnungen MÜSSEN sichtbar sein und DÜRFEN NICHT pauschal ohne dokumentierten Grund unterdrückt werden. |
| SASD-DOTNET-REQ-021 | Nullable Reference Types MÜSSEN für neue Projekte aktiviert sein; Legacy-Projekte MÜSSEN eine schrittweise Aktivierungs- oder Ausnahmeentscheidung dokumentieren. |
| SASD-DOTNET-REQ-022 | Compiler- und Codeanalyse-Regeln SOLLTEN zentral und versionskontrolliert konfiguriert werden. |
| SASD-DOTNET-REQ-023 | Recommended- und Production-Builds SOLLTEN neue Warnungen in geändertem Code als Fehler behandeln oder durch eine gleichwertige Quality Gate verhindern. |
| SASD-DOTNET-REQ-024 | Die öffentliche und betriebliche Angriffsfläche MUSS minimiert werden; nicht benötigte Frameworks, Pakete, Reflection-Freigaben und native Komponenten SOLLTEN vermieden werden. |
| SASD-DOTNET-REQ-025 | Runtime-, SDK- und Paketupdates MÜSSEN nach dem Wartungsstandard geplant und hinsichtlich Kompatibilität, Sicherheit und Supportstatus geprüft werden. |
| SASD-DOTNET-REQ-026 | Cross-Plattform-Kompatibilität DARF NICHT behauptet werden, wenn die unterstützten Plattformen nicht gebaut und angemessen getestet wurden. |
| SASD-DOTNET-REQ-027 | Plattformspezifischer Code MUSS erkennbar gekapselt oder über bedingte Ziel-Frameworks, Adapter oder klar benannte Projekte getrennt werden. |
| SASD-DOTNET-REQ-028 | Ein Projekt MUSS einen klaren Composition Root oder einen gleichwertigen Ort für Abhängigkeitsverdrahtung und Anwendungsstart besitzen. |
| SASD-DOTNET-REQ-029 | Dependency Injection KANN eingesetzt werden, MUSS aber der Projektgröße angemessen bleiben und DARF keine versteckten Service-Locator-Abhängigkeiten erzeugen. |
| SASD-DOTNET-REQ-030 | Der Generic Host SOLLTE verwendet werden, wenn die Anwendung von einheitlichem Lebenszyklus, Konfiguration, Logging, Dependency Injection oder Hintergrunddiensten profitiert. |
| SASD-DOTNET-REQ-031 | Ein kleines Werkzeug KANN ohne Generic Host und ohne mehrschichtige Architektur umgesetzt werden; Start, Konfiguration, Fehlerbehandlung und Testbarkeit MÜSSEN dennoch nachvollziehbar bleiben. |
| SASD-DOTNET-REQ-032 | Automatisch erzeugter Code MUSS von manuell gepflegtem Code unterscheidbar sein und SOLLTE nicht manuell verändert werden. |
| SASD-DOTNET-REQ-033 | Unsicherer Code, P/Invoke, COM-Interop und native Bibliotheken MÜSSEN begründet, gekapselt und risikobasiert getestet werden. |
| SASD-DOTNET-REQ-034 | Trimming, Native AOT, Single-File-Publishing oder ReadyToRun DÜRFEN NICHT als unterstützte Veröffentlichungseigenschaft angegeben werden, solange Kompatibilität und Diagnosefähigkeit nicht geprüft wurden. |
| SASD-DOTNET-REQ-035 | Ein Projekt MUSS die für seinen Einsatz erforderliche Runtime- und Deployment-Art benennen, beispielsweise framework-dependent, self-contained oder containerisiert. |

## 5. Zuordnung zu Qualitätsstufen

| Bereich | Minimum | Recommended | Production |
|---|---|---|---|
| .NET-Version | unterstützte stabile Version MUSS | unterstützte LTS SOLLTE | unterstützte LTS MUSS, sofern keine freigegebene Begründung |
| SDK-Festlegung | dokumentiert SOLLTE | `global.json` SOLLTE | SDK und Roll-forward MÜSSEN festgelegt sein |
| Build | lokal reproduzierbar MUSS | Skript oder CI MUSS | sauberer automatisierter Build MUSS |
| Analyzer | Compilerwarnungen MUSS | zentrale Analyzer-Konfiguration MUSS | Quality Gate und Sicherheitsanalyse MÜSSEN |
| Nullable | bei neuem Projekt MUSS | MUSS | MUSS und Restwarnungen MÜSSEN bewertet sein |
| Paketversionen | nachvollziehbar MUSS | zentral SOLLTE | zentral und kontrolliert MUSS |
| Deployment | Nutzung beschrieben MUSS | reproduzierbar SOLLTE | reproduzierbar und freigegeben MUSS |
| Supportstatus | beim Release SOLLTE | MUSS | laufend überwacht MUSS |

## 6. Verantwortlichkeiten

Der Maintainer legt SDK-, Runtime- und Paketbaseline fest. Entwickler halten Projektdateien und zentrale Buildkonfiguration konsistent. Reviewer prüfen Änderungen an Target Frameworks, Paketquellen, Build-Flags und Deployment-Modellen besonders auf Support-, Sicherheits- und Kompatibilitätsfolgen.

## 7. Nachweise und Prüfkriterien

Geeignete Nachweise sind `global.json`, Projektdateien, `Directory.Build.props`, `Directory.Packages.props`, NuGet-Konfiguration, Buildskripte, CI-Protokolle, Paketlisten, dokumentierte Supportmatrix und veröffentlichte Artefakte.

## 8. Ausnahmen und Abweichungen

Legacy-Frameworks, Vorschauversionen, abweichende SDKs oder nicht reproduzierbare Toolchains benötigen eine dokumentierte Ausnahme mit technischem Grund, Risiko, Laufzeit und Migrations- oder Beendigungsplan.

## 9. Verwandte Dokumente

- [Core Architecture](../../10-core-standard/ARCHITECTURE.md)
- [Core Repository Standard](../../10-core-standard/REPOSITORY.md)
- [Core Quality Standard](../../10-core-standard/QUALITY.md)
- [Core Security Standard](../../10-core-standard/SECURITY.md)
- [.NET Reference Baseline](DOTNET-REFERENCE-BASELINE.md)
- [.NET Project Sizing Guide](DOTNET-PROJECT-SIZING-GUIDE.md)
