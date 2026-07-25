---
title: "UI-Architektur für Desktopanwendungen"
document-id: SASD-PROF-DESKTOP-002
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
applies-to-profiles: [Desktop]
depends-on: [SASD-PROF-DESKTOP-001, SASD-PROF-DOTNET-002, SASD-PROF-DOTNET-003, SASD-PROF-DOTNET-004, SASD-PROF-DOTNET-008, SASD-CORE-003, SASD-CORE-009]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# UI-Architektur für Desktopanwendungen

## 1. Zweck

Dieses Dokument definiert Verantwortlichkeiten, Zustandsmodell, Navigation, Dialoge, Datenbindung, Threading und Testbarkeit der Präsentationsschicht. Es verlangt keine dogmatische Architektur, sondern eine zur Projektgröße passende Trennung.

## 2. Geltungsbereich

Die Regeln gelten für Formulare, Fenster, Views, UserControls, ViewModels, Presenter, Controller, Commands, UI-Dienste und deren Zusammenarbeit mit Anwendungs- und Infrastrukturschichten.

## 3. Normative Anforderungen

| ID | Anforderung |
|---|---|
| SASD-DESKTOP-REQ-101 | Die Benutzeroberfläche MUSS Präsentationsaufgaben von fachlichen Entscheidungen und technischen Integrationen trennen. |
| SASD-DESKTOP-REQ-102 | UI-Ereignishandler SOLLTEN Interaktionen koordinieren und DÜRFEN NICHT umfangreiche Geschäftslogik, Datenzugriffe oder Protokollimplementierungen enthalten. |
| SASD-DESKTOP-REQ-103 | Fachliche Operationen MÜSSEN über testbare Anwendungs- oder Domänendienste aufgerufen werden, sobald ihre Logik über triviale UI-Zustandsänderungen hinausgeht. |
| SASD-DESKTOP-REQ-104 | Die Präsentationsarchitektur MUSS benennen, ob sie beispielsweise einfache Code-behind-Koordination, Presenter, Controller, ViewModel oder eine Kombination verwendet. |
| SASD-DESKTOP-REQ-105 | MVVM, MVP oder vergleichbare Muster DÜRFEN NICHT nur nominell eingeführt werden; Verantwortlichkeiten und Abhängigkeiten MÜSSEN tatsächlich getrennt sein. |
| SASD-DESKTOP-REQ-106 | Ein kleines Formular oder Fenster KANN einfache UI-nahe Logik enthalten, sofern diese keine wiederverwendbare Fachregel darstellt und nachvollziehbar testbar oder prüfbar bleibt. |
| SASD-DESKTOP-REQ-107 | Designer-generierter Code DARF NICHT manuell mit fachlicher Logik vermischt werden. |
| SASD-DESKTOP-REQ-108 | Views, Formulare und Fenster SOLLTEN keine globalen Service-Locator-Zugriffe verwenden. |
| SASD-DESKTOP-REQ-109 | Abhängigkeiten von Präsentationskomponenten MÜSSEN explizit über Konstruktion, definierte Eigenschaften oder kontrollierte Composition Roots bereitgestellt werden. |
| SASD-DESKTOP-REQ-110 | Dependency Injection KANN verwendet werden, MUSS aber Designerfähigkeit, Lebenszyklus und Dispose-Verhalten der UI-Komponenten berücksichtigen. |
| SASD-DESKTOP-REQ-111 | Navigation MUSS einen eindeutigen Verantwortlichen besitzen und DARF NICHT unkoordiniert über beliebige Views verteilt werden. |
| SASD-DESKTOP-REQ-112 | Dialoge SOLLTEN über klar definierte UI-Dienste oder koordinierte View-Verantwortung geöffnet werden, wenn ihre Verwendung mehrere Bereiche betrifft. |
| SASD-DESKTOP-REQ-113 | Modale Dialoge MÜSSEN einen begrenzten Zweck, eindeutige Abschlussaktionen und ein definiertes Abbruchverhalten besitzen. |
| SASD-DESKTOP-REQ-114 | Der Rückgabevertrag eines Dialogs MUSS zwischen Bestätigung, Abbruch und Fehler unterscheiden, wenn diese Zustände fachlich relevant sind. |
| SASD-DESKTOP-REQ-115 | UI-Zustände wie Laden, leer, bereit, geändert, gespeichert, fehlerhaft und deaktiviert SOLLTEN explizit modelliert werden. |
| SASD-DESKTOP-REQ-116 | Mehrere widersprüchliche boolesche Zustandsfelder SOLLTEN durch ein eindeutiges Zustandsmodell ersetzt werden, wenn ungültige Kombinationen entstehen können. |
| SASD-DESKTOP-REQ-117 | Der aktive Datensatz, die aktuelle Auswahl und ungespeicherte Änderungen MÜSSEN als getrennte Zustände behandelt werden. |
| SASD-DESKTOP-REQ-118 | Ein Wechsel von Ansicht, Datensatz oder Anwendungskontext DARF NICHT ungespeicherte Änderungen ohne definierte Richtlinie verwerfen. |
| SASD-DESKTOP-REQ-119 | Befehle und Aktionen MÜSSEN nur ausführbar sein, wenn ihre Vorbedingungen erfüllt sind. |
| SASD-DESKTOP-REQ-120 | Die Aktivierung oder Deaktivierung von Befehlen SOLLTE aus dem Anwendungszustand abgeleitet und nicht an vielen Stellen manuell synchronisiert werden. |
| SASD-DESKTOP-REQ-121 | WPF-Anwendungen SOLLTEN Datenbindung und Commands verwenden, wenn dadurch Präsentationslogik testbar und Kopplung reduziert wird. |
| SASD-DESKTOP-REQ-122 | WPF-Code-behind KANN für rein visuelles Verhalten, Fokus, Animation, Drag-and-drop oder Frameworkintegration verwendet werden, DARF aber keine versteckte Fachlogik aufnehmen. |
| SASD-DESKTOP-REQ-123 | WPF-Bindings MÜSSEN hinsichtlich Quelle, Modus und Aktualisierungszeitpunkt bewusst gewählt werden, wenn Eingaben oder Seiteneffekte betroffen sind. |
| SASD-DESKTOP-REQ-124 | WPF-Bindingfehler SOLLTEN während Entwicklung und Test sichtbar gemacht und DÜRFEN NICHT dauerhaft ignoriert werden. |
| SASD-DESKTOP-REQ-125 | WinForms-Anwendungen SOLLTEN umfangreiche Abläufe aus Form-Klassen in Presenter, Controller oder Anwendungsdienste verlagern. |
| SASD-DESKTOP-REQ-126 | WinForms-UserControls SOLLTEN wiederverwendbare UI-Bereiche kapseln, DÜRFEN aber keine versteckten globalen Datenzugriffe erzeugen. |
| SASD-DESKTOP-REQ-127 | Direkte Abhängigkeiten zwischen Formularen SOLLTEN durch Navigation, Ereignisse oder definierte Verträge begrenzt werden. |
| SASD-DESKTOP-REQ-128 | Event-Abonnements MÜSSEN so verwaltet werden, dass geschlossene Views nicht durch lang lebende Publisher im Speicher gehalten werden. |
| SASD-DESKTOP-REQ-129 | Disposable UI-Ressourcen, Timer, Streams, Images und native Handles MÜSSEN deterministisch freigegeben werden. |
| SASD-DESKTOP-REQ-130 | Hintergrundoperationen MÜSSEN vom UI-Thread entkoppelt sein und ihre Ergebnisse kontrolliert auf den UI-Kontext zurückführen. |
| SASD-DESKTOP-REQ-131 | UI-Komponenten DÜRFEN NICHT aus beliebigen Hintergrundthreads verändert werden. |
| SASD-DESKTOP-REQ-132 | WPF-Code MUSS Thread-Affinität und Dispatcher-Verhalten UI-gebundener Objekte beachten. |
| SASD-DESKTOP-REQ-133 | WinForms-Code MUSS für threadübergreifende UI-Aktualisierungen einen geeigneten UI-Kontext, `Invoke`, `BeginInvoke` oder gleichwertigen Mechanismus verwenden. |
| SASD-DESKTOP-REQ-134 | Asynchrone UI-Aktionen MÜSSEN Exceptions, Abbruch und konkurrierende Mehrfachausführung behandeln. |
| SASD-DESKTOP-REQ-135 | `async void` SOLLTE außerhalb echter UI-Ereignishandler vermieden werden. |
| SASD-DESKTOP-REQ-136 | Während einer nicht parallel zulässigen Operation MUSS die auslösende Aktion gegen unbeabsichtigte Mehrfachausführung geschützt werden. |
| SASD-DESKTOP-REQ-137 | Abbruchtoken SOLLTEN von der UI-Grenze bis zu lang laufenden Anwendungs- und Integrationsoperationen weitergegeben werden. |
| SASD-DESKTOP-REQ-138 | Fortschrittsmeldungen MÜSSEN gedrosselt oder aggregiert werden, wenn häufige Updates die Reaktionsfähigkeit beeinträchtigen können. |
| SASD-DESKTOP-REQ-139 | UI-Aktualisierungen SOLLTEN inkrementell und virtualisiert erfolgen, wenn große Listen oder Datenmengen dargestellt werden. |
| SASD-DESKTOP-REQ-140 | Die Anwendung DARF NICHT große Datenmengen ungeprüft vollständig in visuelle Controls laden, wenn Paging, Filterung oder Virtualisierung erforderlich ist. |
| SASD-DESKTOP-REQ-141 | Eingabevalidierung MUSS auf der UI-Ebene früh rückmelden, darf aber fachliche Validierung in tieferen Schichten nicht ersetzen. |
| SASD-DESKTOP-REQ-142 | Validierungszustände MÜSSEN mit dem bearbeiteten Wert und dem Speicher- oder Commit-Zustand konsistent bleiben. |
| SASD-DESKTOP-REQ-143 | ViewModels und Presenter SOLLTEN keine konkreten Fenster, MessageBoxen oder statischen UI-APIs direkt aufrufen, wenn dadurch Tests und Wiederverwendung verhindert werden. |
| SASD-DESKTOP-REQ-144 | UI-Dienste MÜSSEN schmale, fachlich verständliche Verträge besitzen und DÜRFEN nicht als allgemeine Service-Locator-Fassade dienen. |
| SASD-DESKTOP-REQ-145 | Das Schließen eines Fensters MUSS zwischen Navigationswechsel, Benutzerabbruch, Anwendungsshutdown und fatalem Fehler unterscheiden können, sofern diese Fälle verschiedene Behandlung benötigen. |
| SASD-DESKTOP-REQ-146 | Mehrfensteranwendungen MÜSSEN Besitzverhältnisse, Modalität, Lebensdauer und Fokusübergänge der Fenster definieren. |
| SASD-DESKTOP-REQ-147 | Ein UI-Shell- oder Modulkonzept SOLLTE erst eingeführt werden, wenn mehrere funktionale Bereiche, Navigation oder Erweiterbarkeit den zusätzlichen Aufwand rechtfertigen. |
| SASD-DESKTOP-REQ-148 | Plugin- oder Modul-UIs MÜSSEN Verträge, Versionskompatibilität, Fehlerisolation und Lebenszyklus dokumentieren. |
| SASD-DESKTOP-REQ-149 | Die Präsentationslogik SOLLTE ohne gestartete vollständige Desktopanwendung testbar sein. |
| SASD-DESKTOP-REQ-150 | Kritische UI-Zustandsübergänge MÜSSEN durch Unit-, Komponenten- oder UI-Tests nachvollziehbar geprüft werden. |

## 4. Proportionale Strukturmodelle

### 4.1 Kompaktes Werkzeug

```text
DesktopApp
├── Forms oder Windows
├── Services
├── Models
└── Program / App
```

Geeignet für wenige Ansichten und begrenzte Fachlogik. Die UI darf koordinieren, aber Datenzugriff und wiederverwendbare Regeln bleiben außerhalb der Views.

### 4.2 Gepflegte Anwendung

```text
DesktopApp.UI
DesktopApp.Application
DesktopApp.Domain          optional bei echter Domäne
DesktopApp.Infrastructure
DesktopApp.Tests
```

Presenter oder ViewModels kapseln Zustände und Aktionen. Dialoge, Navigation und Hintergrundoperationen erhalten klare Verträge.

### 4.3 Komplexeres Produkt

```text
Product.Desktop.Shell
Product.Modules.*.Presentation
Product.Application
Product.Domain
Product.Infrastructure.*
Product.Tests.*
```

Nur angemessen bei mehreren Modulen, unabhängigen Lebenszyklen oder echter Erweiterbarkeit.

## 5. Zuordnung zu Qualitätsstufen

| Bereich | Minimum | Recommended | Production |
|---|---|---|---|
| UI-/Fachlogik-Trennung | erkennbare Grenze MUSS | Presenter/ViewModel oder gleichwertig SOLLTE | überprüfte Modulgrenzen MÜSSEN |
| Navigation | lokale Verantwortung MUSS | zentraler Vertrag SOLLTE | getestete Navigation und Wiederherstellung MÜSSEN |
| UI-Zustände | Kernzustände MÜSSEN | explizites Zustandsmodell SOLLTE | vollständige Fehler- und Wiederanlaufzustände MÜSSEN |
| Threading | UI nicht blockieren MUSS | Abbruch und Fortschritt MÜSSEN | Last-, Race- und Shutdownfälle MÜSSEN geprüft sein |
| UI-Dienste | KANN | für wiederkehrende Dialoge SOLLTE | konsistente, testbare Verträge MÜSSEN |
| Präsentationstests | kritische Logik MUSS | ViewModel/Presenter-Tests MÜSSEN | kritische End-to-End-Abläufe SOLLTEN |

## 6. Verantwortlichkeiten

UI-Entwickler verantworten Zustände, Fokus und Darstellung. Anwendungsentwickler stellen testbare Use Cases bereit. Reviewer achten auf Eventhandler mit Fachlogik, Service-Locator, Threadingfehler, Speicherlecks, unkontrollierte Dialoge und nicht testbare statische UI-Aufrufe.

## 7. Nachweise und Prüfkriterien

Nachweise sind Komponentendiagramme, View-/Presenter-/ViewModel-Verträge, Navigationstabellen, Zustandsdiagramme, Tests, Profilergebnisse, Bindingdiagnose, Threadingtests und Code-Review-Protokolle.

## 8. Ausnahmen und Abweichungen

Designer- oder Frameworkrestriktionen können konkrete Formen beeinflussen. Die Kernziele Trennung, kontrollierter Lebenszyklus, Threading-Sicherheit und Testbarkeit bleiben bestehen. Abweichungen MÜSSEN Alternativen und Folgerisiken benennen.

## 9. Verwandte Dokumente

- [WinForms Guidance](WINDOWS-FORMS-GUIDANCE.md)
- [WPF Guidance](WPF-GUIDANCE.md)
- [C# Coding Standard](../dotnet/CODING-STANDARD.md)
- [Fehlerbehandlung](../dotnet/ERROR-HANDLING.md)
- [.NET Testing](../dotnet/DOTNET-TESTING.md)
