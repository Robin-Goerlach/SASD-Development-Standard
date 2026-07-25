---
title: "C# Coding Standard"
document-id: SASD-PROF-DOTNET-003
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
depends-on: [SASD-PROF-DOTNET-001, SASD-CORE-004, SASD-CORE-006, SASD-CORE-007, SASD-CORE-008]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# C# Coding Standard

## 1. Zweck

Dieses Dokument definiert die SASD-Konventionen für verständlichen, robusten und automatisiert prüfbaren C#-Code. Es bevorzugt klare Absicht vor maximaler Kürze und erlaubt moderne Sprachfeatures, wenn sie Wartbarkeit und Korrektheit verbessern.

## 2. Geltungsbereich

Die Regeln gelten für manuell gepflegten C#-Code. Generierter Code ist ausgenommen, sofern Herkunft und Regeneration nachvollziehbar sind. Frameworkvorgaben dürfen Bezeichner oder Signaturen bestimmen.

## 3. Normative Anforderungen

| ID | Anforderung |
|---|---|
| SASD-DOTNET-REQ-201 | C#-Code MUSS lesbar, konsistent und über eine versionierte `.editorconfig` oder gleichwertige Konfiguration prüfbar sein. |
| SASD-DOTNET-REQ-202 | Öffentlich sichtbare Bezeichner SOLLTEN den etablierten .NET-Namenskonventionen folgen. |
| SASD-DOTNET-REQ-203 | Typen und Member MÜSSEN nach ihrer fachlichen Bedeutung und nicht nach zufälligen Implementierungsdetails benannt werden. |
| SASD-DOTNET-REQ-204 | Abkürzungen SOLLTEN vermieden oder im Projektglossar konsistent definiert werden. |
| SASD-DOTNET-REQ-205 | Interfaces SOLLTEN das Präfix `I` verwenden, sofern sie reguläre .NET-Abstraktionen darstellen. |
| SASD-DOTNET-REQ-206 | Asynchrone Methoden, die ein `Task` oder `ValueTask` zurückgeben, SOLLTEN das Suffix `Async` tragen, ausgenommen etablierte Framework-Signaturen. |
| SASD-DOTNET-REQ-207 | Private Felder SOLLTEN mit `_camelCase` benannt werden; Konstanten und statische readonly-Felder MÜSSEN innerhalb des Projekts konsistent benannt sein. |
| SASD-DOTNET-REQ-208 | Eine Datei SOLLTE einen primären Typ enthalten; eng gekoppelte kleine Hilfstypen DÜRFEN gemeinsam abgelegt werden, wenn die Lesbarkeit steigt. |
| SASD-DOTNET-REQ-209 | Namespaces und `using`-Direktiven MÜSSEN konsistent formatiert und durch Analyzer oder Formatter kontrolliert werden. |
| SASD-DOTNET-REQ-210 | Geschweifte Klammern MÜSSEN bei Kontrollstrukturen verwendet werden, auch bei einzeiligen Blöcken. |
| SASD-DOTNET-REQ-211 | `var` SOLLTE verwendet werden, wenn der Typ aus der rechten Seite eindeutig erkennbar ist oder ein anonymer Typ vorliegt; ein expliziter Typ SOLLTE verwendet werden, wenn er das Verständnis verbessert. |
| SASD-DOTNET-REQ-212 | Ausdrücke, Pattern Matching und moderne Sprachfeatures SOLLTEN nur eingesetzt werden, wenn sie die Lesbarkeit oder Korrektheit verbessern. |
| SASD-DOTNET-REQ-213 | Eine explizite `LangVersion` SOLLTE nur gesetzt werden, wenn der SDK-Standard nicht ausreicht oder eine Kompatibilitätsanforderung besteht. |
| SASD-DOTNET-REQ-214 | Nullable Reference Types MÜSSEN als Vertragsbestandteil behandelt werden; Nullunterdrückung mit `!` benötigt eine lokal nachvollziehbare Invariante. |
| SASD-DOTNET-REQ-215 | Nullable-Warnungen DÜRFEN NICHT durch großflächiges `#nullable disable` oder pauschale Unterdrückungen verborgen werden. |
| SASD-DOTNET-REQ-216 | Parameter und Rückgabewerte MÜSSEN Nullfähigkeit, optionale Werte und Fehlerzustände eindeutig ausdrücken. |
| SASD-DOTNET-REQ-217 | Öffentliche APIs MÜSSEN Eingaben an der geeigneten Grenze validieren und aussagekräftige Standard- oder Domänenfehler liefern. |
| SASD-DOTNET-REQ-218 | Methoden SOLLTEN eine klar erkennbare Aufgabe besitzen; hohe Komplexität oder viele unabhängige Seiteneffekte MÜSSEN überprüft und gegebenenfalls aufgeteilt werden. |
| SASD-DOTNET-REQ-219 | Boolesche Parameter SOLLTEN vermieden werden, wenn ihre Bedeutung am Aufrufort nicht klar ist; benannte Optionen, Enums oder getrennte Methoden SOLLTEN bevorzugt werden. |
| SASD-DOTNET-REQ-220 | Magische Zahlen, Pfade, Schlüssel und fachliche Zeichenketten SOLLTEN durch benannte Konstanten, Value Objects, Optionen oder Ressourcen ersetzt werden. |
| SASD-DOTNET-REQ-221 | Globale mutable Zustände und öffentliche Setter SOLLTEN minimiert werden. |
| SASD-DOTNET-REQ-222 | Records, readonly-Strukturen und unveränderliche Typen SOLLTEN verwendet werden, wenn Wertsemantik und Unveränderlichkeit fachlich passen. |
| SASD-DOTNET-REQ-223 | Gleichheit, Hashcodes und Sortierung MÜSSEN konsistent implementiert werden, wenn benutzerdefinierte Wertsemantik benötigt wird. |
| SASD-DOTNET-REQ-224 | Zeitpunkte SOLLTEN als `DateTimeOffset` oder fachlich geeignete Typen verarbeitet werden; UTC-Konvertierung und Zeitzonenannahmen MÜSSEN an Systemgrenzen dokumentiert sein. |
| SASD-DOTNET-REQ-225 | Zeitabhängige Logik SOLLTE über `TimeProvider` oder eine gleichwertige kontrollierbare Abstraktion testbar gemacht werden. |
| SASD-DOTNET-REQ-226 | Kulturabhängige Formatierung, Parsing und Vergleiche MÜSSEN die beabsichtigte Kultur explizit berücksichtigen. |
| SASD-DOTNET-REQ-227 | Stringvergleiche MÜSSEN eine fachlich passende `StringComparison` verwenden, wenn Kultur oder Groß-/Kleinschreibung relevant sind. |
| SASD-DOTNET-REQ-228 | Asynchrone Vorgänge DÜRFEN NICHT ohne begründete Synchronisationsgrenze durch `.Result`, `.Wait()` oder blockierendes Warten konsumiert werden. |
| SASD-DOTNET-REQ-229 | `async void` DARF NICHT außerhalb von Ereignishandlern oder durch ein Framework zwingend vorgegebenen Signaturen verwendet werden. |
| SASD-DOTNET-REQ-230 | Länger laufende oder abbrechbare asynchrone APIs SOLLTEN ein `CancellationToken` akzeptieren und weiterreichen. |
| SASD-DOTNET-REQ-231 | Ein empfangenes `CancellationToken` DARF NICHT ohne dokumentierten Grund durch `CancellationToken.None` ersetzt oder ignoriert werden. |
| SASD-DOTNET-REQ-232 | `IDisposable`- und `IAsyncDisposable`-Ressourcen MÜSSEN deterministisch freigegeben werden. |
| SASD-DOTNET-REQ-233 | Finalizer SOLLTEN nur verwendet werden, wenn tatsächlich unmanaged Ressourcen direkt verwaltet werden und das Dispose-Pattern korrekt umgesetzt ist. |
| SASD-DOTNET-REQ-234 | Kommentare MÜSSEN Gründe, Invarianten, Risiken oder nicht offensichtliche Entscheidungen erklären und SOLLTEN nicht lediglich den Code paraphrasieren. |
| SASD-DOTNET-REQ-235 | Öffentliche APIs von Bibliotheken MÜSSEN XML-Dokumentation besitzen; reguläre Anwendungen SOLLTEN mindestens öffentliche und komplexe interne Bestandteile dokumentieren. |
| SASD-DOTNET-REQ-236 | XML-Kommentare MÜSSEN Parameter, Rückgabewerte, Ausnahmen und Nebenwirkungen korrekt beschreiben, soweit sie für die Nutzung relevant sind. |
| SASD-DOTNET-REQ-237 | Auskommentierter Altcode DARF NICHT dauerhaft im Repository verbleiben; Historie gehört in die Versionskontrolle. |
| SASD-DOTNET-REQ-238 | Regionen SOLLTEN nicht verwendet werden, um übergroße oder unklar strukturierte Typen zu verbergen. |
| SASD-DOTNET-REQ-239 | Analyzer-Warnungen SOLLTEN nur lokal oder zentral mit dokumentierter Begründung unterdrückt werden. |
| SASD-DOTNET-REQ-240 | Eine Unterdrückung MUSS die kleinste sinnvolle Reichweite besitzen und SOLLTE auf eine Issue-, ADR- oder Codebegründung verweisen. |
| SASD-DOTNET-REQ-241 | Unsafe-Code, Reflection, dynamische Typisierung und Expression-Kompilierung SOLLTEN auf klar begründete technische Grenzen beschränkt werden. |
| SASD-DOTNET-REQ-242 | Sicherheitskritische Vergleiche, Zufallswerte und kryptographische Operationen MÜSSEN geeignete Plattform-APIs statt selbst entwickelter Verfahren verwenden. |
| SASD-DOTNET-REQ-243 | Quellgeneratoren und automatische Formatter MÜSSEN reproduzierbar eingebunden und versioniert sein. |
| SASD-DOTNET-REQ-244 | Codeänderungen SOLLTEN vor dem Commit formatiert und mindestens gegen die konfigurierten Compiler- und Analyzerregeln geprüft werden. |

## 4. SASD-Standardentscheidungen

| Thema | Standardentscheidung |
|---|---|
| Klammern | immer bei Kontrollstrukturen |
| `var` | bei eindeutigem Typ; sonst explizit |
| Nullable | für neuen Code aktiviert |
| asynchrone Methoden | `Async`-Suffix, außer Frameworksignaturen |
| private Felder | `_camelCase` |
| öffentliche Member | PascalCase |
| Interfaces | `I`-Präfix |
| XML-Kommentare | öffentliche Bibliotheks-APIs MUSS; komplexe Anwendungs-APIs SOLLTE |
| Analyzer | über `.editorconfig` und Buildkonfiguration |
| Zeilenlänge | keine starre normative Grenze; Lesbarkeit und Formatter entscheiden |
| Regions | nur ausnahmsweise, nicht zur Komplexitätsverschleierung |

## 5. Zuordnung zu Qualitätsstufen

| Bereich | Minimum | Recommended | Production |
|---|---|---|---|
| `.editorconfig` | SOLLTE | MUSS | MUSS |
| Nullable | neuer Code MUSS | MUSS | MUSS, Nullunterdrückungen geprüft |
| Analyzer | Compiler MUSS | Quality Analyzer MUSS | Quality und Security Analyzer MÜSSEN |
| Warnings as Errors | KANN | neue Warnungen SOLLTEN blockieren | CI-Warnungen MÜSSEN kontrolliert sein |
| XML-Dokumentation | wichtige APIs SOLLTE | öffentliche APIs MUSS | öffentliche APIs und Betriebsgrenzen MÜSSEN |
| Complexity Review | risikobasiert | SOLLTE | für kritischen Code MUSS |
| automatische Formatierung | KANN | SOLLTE | MUSS für wiederholbare CI-Prüfung |

## 6. Verantwortlichkeiten

Maintainer pflegen `.editorconfig`, Analyzer und zentrale Buildregeln. Entwickler schreiben verständlichen, dokumentierten Code und behandeln Warnungen. Reviewer achten auf Absicht, Komplexität, API-Verträge, Nebenwirkungen und unnötige Unterdrückungen.

## 7. Nachweise und Prüfkriterien

Geeignete Nachweise sind `.editorconfig`, `Directory.Build.props`, Analyzerpakete, Buildprotokolle, Code-Review-Kommentare, XML-Dokumentationsausgabe und dokumentierte Suppressions.

## 8. Ausnahmen und Abweichungen

Legacy-Code darf schrittweise angepasst werden. Neue oder geänderte Bereiche SOLLTEN bereits den Standard erfüllen. Abweichende Namens- oder Formatierungsregeln benötigen eine repositoryweite, automatisierbare Konfiguration und dürfen keine öffentliche API ohne Migrationsentscheidung brechen.

## 9. Verwandte Dokumente

- [Core Quality](../../10-core-standard/QUALITY.md)
- [Core Documentation](../../10-core-standard/DOCUMENTATION.md)
- [Error Handling](ERROR-HANDLING.md)
- [.NET Testing](DOTNET-TESTING.md)
