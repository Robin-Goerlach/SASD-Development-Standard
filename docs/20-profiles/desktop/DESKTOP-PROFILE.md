---
title: "Desktopanwendungsprofil"
document-id: SASD-PROF-DESKTOP-001
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
depends-on: [SASD-PROF-DOTNET-001, SASD-CORE-003, SASD-CORE-005, SASD-CORE-006, SASD-CORE-007, SASD-CORE-008, SASD-CORE-009, SASD-CORE-010, SASD-CORE-011]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Desktopanwendungsprofil

## 1. Zweck

Dieses Dokument konkretisiert den SASD Development Standard für interaktive Desktopanwendungen. Es legt die gemeinsame Basis für Technologieauswahl, Plattformunterstützung, Datenpfade, Bedienbarkeit, Deployment, Wartung und die Anwendung der weiteren Desktop-Profildokumente fest.

## 2. Geltungsbereich

Das Profil gilt in Version 1.0 primär für C#/.NET-Desktopanwendungen auf Windows, insbesondere WinForms und WPF. Andere Desktoptechnologien können die gemeinsamen Anforderungen anwenden, benötigen für technologiespezifische Details jedoch ein ergänzendes Profil oder dokumentierte Abweichungen.

Nicht Teil dieses Dokuments sind konkrete Corporate-Design-Vorgaben, ein verbindliches visuelles Theme oder produktspezifische Bedienkonzepte.

## 3. Profilzusammensetzung

Ein Desktopprojekt wendet mindestens folgende Dokumente an:

- [UI-Architektur](UI-ARCHITECTURE.md)
- [User Experience](USER-EXPERIENCE.md)
- [Anwendungslebenszyklus](APPLICATION-LIFECYCLE.md)
- die tatsächlich relevanten Dokumente des [C#/.NET-Profils](../dotnet/README.md)

WinForms- und WPF-Projekte verwenden zusätzlich die informativen Technologieleitfäden dieses Verzeichnisses.

## 4. Normative Anforderungen

| ID | Anforderung |
|---|---|
| SASD-DESKTOP-REQ-001 | Eine Desktopanwendung, die dieses Profil anwendet, MUSS den SASD Core Standard und das C#/.NET-Profil gemeinsam anwenden. |
| SASD-DESKTOP-REQ-002 | Die Profilanwendung MUSS im README oder in `docs/SASD-COMPLIANCE.md` mit UI-Technologie, Qualitätsstufe, unterstützten Betriebssystemen und Profilversion benannt werden. |
| SASD-DESKTOP-REQ-003 | Die Auswahl von WinForms, WPF oder einer anderen Desktoptechnologie MUSS anhand von Anforderungen, Wartbarkeit, Teamkompetenz, Plattformbindung und Lebensdauer begründet werden. |
| SASD-DESKTOP-REQ-004 | Eine Desktoptechnologie DARF NICHT allein aufgrund modischer Präferenzen oder vermeintlicher Modernität gewählt werden. |
| SASD-DESKTOP-REQ-005 | Neue WinForms- und WPF-Anwendungen SOLLTEN ein unterstütztes modernes .NET und ein Windows-spezifisches Target Framework verwenden. |
| SASD-DESKTOP-REQ-006 | Die tatsächlich unterstützten Windows-Versionen, Architekturen und Anzeigeumgebungen MÜSSEN dokumentiert sein. |
| SASD-DESKTOP-REQ-007 | Eine Anwendung DARF NICHT als plattformübergreifend bezeichnet werden, wenn nur die Windows-Desktopvariante implementiert und geprüft wurde. |
| SASD-DESKTOP-REQ-008 | Ein Projekt MUSS die Benutzergruppen, Hauptaufgaben und typischen Nutzungssituationen der Desktopanwendung beschreiben. |
| SASD-DESKTOP-REQ-009 | Der Umfang der Benutzeroberfläche MUSS sich an den priorisierten Arbeitsabläufen orientieren und DARF nicht durch ungeordnete Funktionsansammlungen bestimmt werden. |
| SASD-DESKTOP-REQ-010 | Die Anwendung MUSS eine nachvollziehbare Trennung zwischen Benutzeroberfläche, Anwendungslogik und technischen Integrationen besitzen. |
| SASD-DESKTOP-REQ-011 | Die gewählte UI-Struktur MUSS zur Größe und Änderungsrate des Projekts passen; unnötige Frameworks und Schichten SOLLTEN vermieden werden. |
| SASD-DESKTOP-REQ-012 | Ein kleines Desktopwerkzeug KANN eine kompakte Struktur verwenden, sofern fachliche Logik testbar bleibt und nicht unkontrolliert in Formularen oder Fenstern verteilt wird. |
| SASD-DESKTOP-REQ-013 | Eine langfristig gepflegte Anwendung SOLLTE gemeinsame UI-Dienste für Dialoge, Navigation, Benachrichtigungen und Benutzerpräferenzen definieren. |
| SASD-DESKTOP-REQ-014 | Production-Anwendungen MÜSSEN ihre UI-Technologie, zentrale Bibliotheken und Drittanbieterkomponenten in der Wartungs- und Abhängigkeitsplanung berücksichtigen. |
| SASD-DESKTOP-REQ-015 | Desktopanwendungen MÜSSEN ohne Administratorrechte betrieben werden können, sofern erhöhte Rechte keine ausdrücklich dokumentierte Kernanforderung sind. |
| SASD-DESKTOP-REQ-016 | Erhöhte Rechte DÜRFEN NICHT nur zur Vereinfachung von Datei-, Registry- oder Installationszugriffen verlangt werden. |
| SASD-DESKTOP-REQ-017 | Benutzerdaten, Maschinendaten, Konfiguration, Cache, Logs und Programmdateien MÜSSEN logisch getrennt gespeichert werden. |
| SASD-DESKTOP-REQ-018 | Schreibzugriffe in das Installationsverzeichnis SOLLTEN vermieden werden und benötigen bei regulärer Installation eine dokumentierte Begründung. |
| SASD-DESKTOP-REQ-019 | Portable Betriebsarten MÜSSEN ausdrücklich gekennzeichnet werden und SOLLTEN Datenpfade, Updateverhalten und Mehrbenutzerbetrieb gesondert behandeln. |
| SASD-DESKTOP-REQ-020 | Die Anwendung MUSS eine definierte Strategie für Einstellungen, lokale Daten, Migrationen und Wiederherstellung besitzen, sofern solche Daten existieren. |
| SASD-DESKTOP-REQ-021 | Dateiformate und lokale Datenbanken, die Benutzerdaten enthalten, MÜSSEN hinsichtlich Kompatibilität, Integrität und Sicherung dokumentiert werden. |
| SASD-DESKTOP-REQ-022 | Die Anwendung MUSS ihre Online- und Offlineabhängigkeiten transparent machen und bei erwartbaren Verbindungsunterbrechungen einen definierten Zustand anzeigen. |
| SASD-DESKTOP-REQ-023 | Netzwerkzugriffe DÜRFEN NICHT den UI-Thread blockieren. |
| SASD-DESKTOP-REQ-024 | Länger laufende Operationen MÜSSEN eine angemessene Fortschritts-, Beschäftigt- oder Statusrückmeldung liefern. |
| SASD-DESKTOP-REQ-025 | Abbruchbare Operationen SOLLTEN einen sichtbaren und sicheren Abbruch ermöglichen. |
| SASD-DESKTOP-REQ-026 | Die Anwendung MUSS bei Fehlern zwischen benutzerverständlicher Meldung und technischer Diagnose unterscheiden. |
| SASD-DESKTOP-REQ-027 | Sensible Informationen DÜRFEN NICHT ungefiltert in Dialogen, Zwischenablage, Screenshots, Logs oder Crashberichten erscheinen. |
| SASD-DESKTOP-REQ-028 | Barrierefreiheit, Tastaturbedienung, Fokusführung, Skalierung und Textlesbarkeit MÜSSEN als Qualitätsmerkmale des Produkts behandelt werden. |
| SASD-DESKTOP-REQ-029 | Die Anwendung MUSS bei unterstützten Skalierungsfaktoren und Mehrmonitorbetrieb risikobasiert geprüft werden. |
| SASD-DESKTOP-REQ-030 | Farben, Symbole und Animationen DÜRFEN NICHT die einzige Trägerform einer erforderlichen Information sein. |
| SASD-DESKTOP-REQ-031 | Die Anwendung SOLLTE auf Änderungen von Schriftgröße, Darstellungsskalierung und Windows-Design angemessen reagieren. |
| SASD-DESKTOP-REQ-032 | Lokalisierung und kulturspezifische Formate MÜSSEN berücksichtigt werden, wenn mehr als eine Sprache oder Region unterstützt wird. |
| SASD-DESKTOP-REQ-033 | Benutzertexte SOLLTEN von technischem Code und fachlichen Konstanten getrennt verwaltet werden, wenn Lokalisierung oder häufige Textänderungen zu erwarten sind. |
| SASD-DESKTOP-REQ-034 | Das Deployment-Modell MUSS festlegen, wie Runtime, Installation, Updates, Signierung, Rollback und Deinstallation behandelt werden. |
| SASD-DESKTOP-REQ-035 | Eine Anwendung, die an Dritte verteilt wird, MUSS eine eindeutige Produktversion und einen für Supportzwecke auffindbaren Versionsdialog besitzen. |
| SASD-DESKTOP-REQ-036 | Der Produktname, Herausgeber, Installationspfade und Anwendungseinträge MÜSSEN über Releases hinweg konsistent bleiben oder migrationsfähig geändert werden. |
| SASD-DESKTOP-REQ-037 | Installations- und Updateartefakte MÜSSEN aus einer reproduzierbaren Build- und Releasekonfiguration erzeugt werden. |
| SASD-DESKTOP-REQ-038 | Production-Anwendungen SOLLTEN ausführbare Dateien und Installationsartefakte mit einer nachvollziehbaren Code-Signing-Strategie versehen. |
| SASD-DESKTOP-REQ-039 | Ein Desktopprojekt MUSS mindestens eine dokumentierte manuelle Start-, Kernablauf- und Shutdown-Prüfung besitzen. |
| SASD-DESKTOP-REQ-040 | Recommended- und Production-Projekte MÜSSEN die testbare Logik außerhalb der UI automatisiert prüfen. |
| SASD-DESKTOP-REQ-041 | UI-Automatisierung SOLLTE risikobasiert für geschäftskritische oder regressionsanfällige Bedienabläufe eingesetzt werden. |
| SASD-DESKTOP-REQ-042 | Ein Desktopprojekt MUSS bekannte Einschränkungen der UI-Technologie, des Designers und der Deploymentform dokumentieren. |
| SASD-DESKTOP-REQ-043 | Migrationen von .NET Framework zu modernem .NET MÜSSEN Kompatibilität, Designerverhalten, DPI, Accessibility, Drittanbieterkomponenten und Deployment getrennt bewerten. |
| SASD-DESKTOP-REQ-044 | Ein neues Desktopframework oder eine neue größere UI-Bibliothek SOLLTE durch einen begrenzten Prototyp oder Spike gegen die wichtigsten Anforderungen geprüft werden. |
| SASD-DESKTOP-REQ-045 | Desktopanwendungen mit personenbezogenen oder geschäftskritischen Daten MÜSSEN Datenschutz, Backup, Export, Löschung und Supportzugriff ausdrücklich regeln. |

## 5. Technologieauswahl

| Situation | WinForms ist häufig angemessen | WPF ist häufig angemessen |
|---|---|---|
| kleine Verwaltungs- und Datenwerkzeuge | ja | möglich, aber oft nicht notwendig |
| vorhandene WinForms-Codebasis und Designerwissen | ja | nur bei tragfähigem Migrationsnutzen |
| komplexe Datenbindung, Templates und Styling | eingeschränkt | ja |
| stark individualisierte oder dynamische UI | eingeschränkt | ja |
| schnelle, pragmatische interne Windows-Anwendung | ja | ja, bei vorhandenem WPF-Know-how |
| plattformübergreifende Anforderung | nein | nein |

Die Tabelle ist eine Entscheidungshilfe, keine automatische Auswahlregel.

## 6. Zuordnung zu Qualitätsstufen

| Bereich | Minimum | Recommended | Production |
|---|---|---|---|
| Technologieentscheidung | kurz dokumentiert MUSS | bewertete Entscheidung MUSS | Lebenszyklus- und Lieferantenrisiken MÜSSEN |
| Plattformmatrix | Zielsystem MUSS | Versionen und Architekturen MÜSSEN | Support- und Testmatrix MUSS |
| UI-Struktur | fachliche Logik trennbar MUSS | klare Präsentationsstruktur MUSS | modulare und überwachte Grenzen MÜSSEN |
| Barrierefreiheit | grundlegende Tastaturbedienung MUSS | systematischer Review MUSS | risikobasierter assistiver Test MUSS |
| DPI und Mehrmonitor | Kernansichten SOLLTEN | repräsentative Prüfung MUSS | definierte Matrix und Regression MUSS |
| Deployment | manuell reproduzierbar MUSS | automatisierbar SOLLTE | reproduzierbar, signiert und rollbackfähig SOLLTE |
| Supportdiagnose | Version und Logs MÜSSEN | Diagnosepaket SOLLTE | Support- und Datenschutzprozess MÜSSEN |

## 7. Verantwortlichkeiten

Der Product Owner oder Maintainer definiert Benutzergruppen und Einsatzkontext. Der technische Verantwortliche dokumentiert UI-Technologie, Plattformmatrix und Deploymentmodell. Entwickler halten UI- und Fachlogik getrennt. Reviewer prüfen Bedienbarkeit, Fehlergrenzen, DPI, Accessibility, Datenpfade und Wartbarkeit.

Bei Einzelentwicklung KANN eine Person alle Rollen übernehmen; Entscheidungs-, Review- und Freigabenachweise MÜSSEN dennoch zeitlich und inhaltlich nachvollziehbar bleiben.

## 8. Nachweise und Prüfkriterien

Geeignete Nachweise sind Projektbrief, Technologieentscheidung, Supportmatrix, Screenshots wichtiger Zustände, UX-Review, Accessibility-Check, Deploymentplan, Release-Smoke-Test, automatisierte Tests, Installationsartefakte und `SASD-COMPLIANCE.md`.

## 9. Ausnahmen und Abweichungen

Legacy-Technologien, Administratoranforderungen, nicht standardkonforme Datenpfade oder fehlende Barrierefreiheitsfunktionen benötigen eine dokumentierte Ausnahme mit Risiko, Kompensation und Zieltermin. Eine bloße Designer- oder Frameworkeinschränkung ersetzt keine Risikobewertung.

## 10. Verwandte Dokumente

- [C#/.NET-Profil](../dotnet/DOTNET-PROFILE.md)
- [Core Architektur](../../10-core-standard/ARCHITECTURE.md)
- [Core Sicherheit](../../10-core-standard/SECURITY.md)
- [Desktop Reference Baseline](DESKTOP-REFERENCE-BASELINE.md)
- [Desktop Project Sizing Guide](DESKTOP-PROJECT-SIZING-GUIDE.md)
