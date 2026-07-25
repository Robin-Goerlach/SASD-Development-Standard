---
title: "Testen von C#/.NET-Projekten"
document-id: SASD-PROF-DOTNET-008
document-type: normative
status: Approved
version: 0.9.0
standard-version: "1.0"
approval-bundle: SASD-NORMATIVE-BASELINE-0.9.0
approval-review-state: approved
language: de
authoritative: true
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
approved-on: 2026-07-24
approval-record: SASD-REF-BASELINE-007
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [DotNet]
depends-on: [SASD-PROF-DOTNET-001, SASD-PROF-DOTNET-002, SASD-PROF-DOTNET-003, SASD-PROF-DOTNET-004, SASD-CORE-006, SASD-CORE-008, SASD-CORE-009]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Testen von C#/.NET-Projekten

## 1. Zweck

Dieses Dokument konkretisiert die Core-Testanforderungen für .NET: Testframework, Projektstruktur, Isolation, asynchrone Tests, Zeit und Zufall, Integration, Architektur, Coverage und CI.

## 2. Geltungsbereich

Die Regeln gelten für Unit-, Integrations-, Architektur-, Komponenten-, Migrations-, Packaging- und Systemtests in .NET-Projekten.

## 3. Normative Anforderungen

| ID | Anforderung |
|---|---|
| SASD-DOTNET-REQ-701 | Jedes .NET-Projekt MUSS eine der Qualitätsstufe angemessene automatisierte oder reproduzierbare Teststrategie besitzen. |
| SASD-DOTNET-REQ-702 | Neue SASD-.NET-Projekte SOLLTEN xUnit als Standard-Testframework verwenden; NUnit, MSTest oder andere Frameworks sind bei dokumentierter Begründung zulässig. |
| SASD-DOTNET-REQ-703 | Testprojekte MÜSSEN ihren Testtyp und das getestete System im Namen erkennen lassen. |
| SASD-DOTNET-REQ-704 | Tests MÜSSEN unabhängig von Ausführungsreihenfolge und vorherigen Testläufen sein. |
| SASD-DOTNET-REQ-705 | Tests MÜSSEN reproduzierbar sein und DÜRFEN nicht unbeabsichtigt von lokaler Zeitzone, Sprache, Benutzerprofil, Netzwerk oder installierter IDE abhängen. |
| SASD-DOTNET-REQ-706 | Ein Test MUSS eine verständliche Absicht besitzen; sein Name SOLLTE Verhalten, Bedingung und erwartetes Ergebnis erkennen lassen. |
| SASD-DOTNET-REQ-707 | Tests SOLLTEN Arrange-Act-Assert oder eine gleichwertig klare Struktur verwenden. |
| SASD-DOTNET-REQ-708 | Ein Test SOLLTE primär einen fachlichen oder technischen Sachverhalt prüfen und unnötig viele unabhängige Behauptungen vermeiden. |
| SASD-DOTNET-REQ-709 | Testdaten SOLLTEN durch Builder, Factories, Fixtures oder gut benannte Hilfen lesbar und wartbar erzeugt werden. |
| SASD-DOTNET-REQ-710 | Gemeinsame Fixtures MÜSSEN Nebenwirkungen und Lebenszyklus sichtbar machen. |
| SASD-DOTNET-REQ-711 | Unit-Tests SOLLTEN schnell sein und externe I/O-Grenzen kontrollieren. |
| SASD-DOTNET-REQ-712 | Mocks und Stubs SOLLTEN an stabilen Systemgrenzen eingesetzt werden und DÜRFEN nicht die interne Implementierung unnötig festschreiben. |
| SASD-DOTNET-REQ-713 | Ein Test DARF NICHT nur bestätigen, dass ein Mock wie konfiguriert reagiert, ohne relevantes Verhalten des Systems zu prüfen. |
| SASD-DOTNET-REQ-714 | Integrationstests MÜSSEN reale Integrationsannahmen prüfen, beispielsweise Datenbankprovider, Dateisystem, Serialisierung oder Netzwerkprotokolle. |
| SASD-DOTNET-REQ-715 | Integrationstests MÜSSEN isolierte Ressourcen verwenden und nach dem Lauf zuverlässig aufräumen. |
| SASD-DOTNET-REQ-716 | Temporäre Dateien und Verzeichnisse MÜSSEN eindeutig und testlokal angelegt werden. |
| SASD-DOTNET-REQ-717 | Datenbanktests MÜSSEN einen bekannten Ausgangszustand herstellen und DÜRFEN keine produktiven Datenbanken verwenden. |
| SASD-DOTNET-REQ-718 | Providerabhängiges Verhalten MUSS gegen den tatsächlichen oder einen kompatiblen realen Provider getestet werden. |
| SASD-DOTNET-REQ-719 | Architekturtests SOLLTEN Projekt- und Namespace-Abhängigkeitsregeln prüfen, wenn das System mehrere Schichten oder Module besitzt. |
| SASD-DOTNET-REQ-720 | Öffentliche Bibliotheken SOLLTEN API-Kompatibilität, Serialisierung und erwartete Exceptions testen. |
| SASD-DOTNET-REQ-721 | Asynchrone Tests MÜSSEN selbst asynchron sein und DÜRFEN nicht durch `.Wait()` oder `.Result` synchronisiert werden. |
| SASD-DOTNET-REQ-722 | Cancellation, Timeout und Fehlerpfade MÜSSEN für kritische asynchrone Vorgänge getestet werden. |
| SASD-DOTNET-REQ-723 | Zeitabhängige Tests SOLLTEN kontrollierte Zeitquellen verwenden und DÜRFEN nicht unnötig mit realen Wartezeiten arbeiten. |
| SASD-DOTNET-REQ-724 | Zufallsbasierte Tests MÜSSEN bei Fehlern den Seed oder eine reproduzierbare Eingabe ausgeben. |
| SASD-DOTNET-REQ-725 | Kultur-, Zeitzonen- und Plattformvarianten MÜSSEN getestet werden, wenn das Produkt entsprechende Unterstützung verspricht. |
| SASD-DOTNET-REQ-726 | Snapshot- oder Golden-Master-Tests MÜSSEN lesbar reviewbar sein und DÜRFEN Änderungen nicht blind akzeptieren. |
| SASD-DOTNET-REQ-727 | Flaky Tests DÜRFEN NICHT dauerhaft ignoriert werden; sie MÜSSEN priorisiert stabilisiert, isoliert oder mit dokumentiertem Ablaufdatum quarantänisiert werden. |
| SASD-DOTNET-REQ-728 | Übersprungene Tests MÜSSEN einen nachvollziehbaren Grund besitzen und SOLLTEN auf eine Aufgabe oder Bedingung verweisen. |
| SASD-DOTNET-REQ-729 | Code Coverage DARF NICHT als alleiniger Qualitätsnachweis verwendet werden. |
| SASD-DOTNET-REQ-730 | Coverage SOLLTE als Hinweis auf ungetestete Risiken verwendet werden; kritische Logik und geänderte Fehlerpfade MÜSSEN angemessen geprüft sein. |
| SASD-DOTNET-REQ-731 | Build und Test MÜSSEN in einer sauberen Umgebung mit `dotnet restore`, `dotnet build` und `dotnet test` oder gleichwertigen Befehlen ausführbar sein. |
| SASD-DOTNET-REQ-732 | CI MUSS für Recommended- und Production-Projekte mindestens Restore, Build, Analyzer und relevante automatisierte Tests ausführen. |
| SASD-DOTNET-REQ-733 | Testresultate MÜSSEN bei fehlgeschlagenen CI-Läufen zugänglich sein. |
| SASD-DOTNET-REQ-734 | Parallelisierung SOLLTE nur aktiviert werden, wenn Tests und gemeinsam genutzte Ressourcen dafür geeignet sind. |
| SASD-DOTNET-REQ-735 | Lange Tests SOLLTEN kategorisiert und von schnellen Feedbacktests unterscheidbar sein. |
| SASD-DOTNET-REQ-736 | Sicherheitsrelevante Parser, Validierung, Autorisierung, Kryptonutzung und Secretbehandlung MÜSSEN risikobasiert getestet werden. |
| SASD-DOTNET-REQ-737 | Publish-, Packaging- oder Installationspfade SOLLTEN für verteilte Anwendungen automatisiert oder reproduzierbar getestet werden. |
| SASD-DOTNET-REQ-738 | AOT-, Trimming- und Single-File-Varianten MÜSSEN in der tatsächlich veröffentlichten Form getestet werden, wenn sie unterstützt werden. |
| SASD-DOTNET-REQ-739 | Migrationen MÜSSEN mit Upgradepfaden aus mindestens der ältesten noch unterstützten Projektversion getestet werden, soweit Datenbestände betroffen sind. |
| SASD-DOTNET-REQ-740 | Tests DÜRFEN keine realen Secrets enthalten und SOLLTEN Security-Scanner oder Secret-Checks nicht unnötig durch täuschend echte Werte auslösen. |

## 4. SASD-Testpyramide

Die konkrete Verteilung ist risikobasiert. Typischerweise gelten:

- viele schnelle Tests für fachliche Logik,
- gezielte Integrationstests für echte technische Grenzen,
- wenige, wertvolle End-to-End- oder Installationsprüfungen,
- Architekturtests für dauerhaft wichtige Strukturregeln.

## 5. Zuordnung zu Qualitätsstufen

| Bereich | Minimum | Recommended | Production |
|---|---|---|---|
| Unit-/Verhaltenstests | kritische Logik MUSS | risikobasiert MUSS | kritische und Fehlerpfade MÜSSEN |
| Integrationstests | bei echter Integration SOLLTE | MUSS | MUSS mit Production-naher Technik |
| Architekturtests | KANN | bei Schichten SOLLTE | bei kritischen Grenzen MUSS |
| CI | KANN, Skript MUSS reproduzierbar sein | MUSS | MUSS mit Quality Gates |
| Coverage | KANN | Trend SOLLTE | Risiko- und Änderungsreview MUSS |
| Flaky Management | MUSS | MUSS | MUSS mit Beobachtung |
| Packaging/Publish | bei Verteilung SOLLTE | MUSS | MUSS auf Zielplattformen |
| Migrationstests | bei Daten SOLLTE | MUSS | MUSS mit Upgradepfaden |

## 6. Verantwortlichkeiten

Entwickler schreiben und pflegen Tests. Maintainer definieren Framework, Kategorien und CI. Reviewer bewerten Aussagekraft statt bloßer Anzahl. Betreiber oder Releaseverantwortliche prüfen deploymentspezifische und wiederherstellungsrelevante Tests.

## 7. Nachweise und Prüfkriterien

Nachweise sind Testprojekte, Teststrategie, CI-Protokolle, Testresultate, Coverage-Trends, Flaky-Liste, Architekturtests, Migrations- und Publish-Tests.

## 8. Ausnahmen und Abweichungen

Ein kurzfristiger Prototyp darf manuelle reproduzierbare Tests verwenden, wenn das Risiko gering ist und die Testschritte dokumentiert sind. Vor langfristiger Nutzung oder Verteilung MUSS die Teststrategie neu bewertet werden.

## 9. Verwandte Dokumente

- [Core Testing](../../10-core-standard/TESTING.md)
- [Coding Standard](CODING-STANDARD.md)
- [Persistence](PERSISTENCE.md)
- [Solution Structure](SOLUTION-STRUCTURE.md)
