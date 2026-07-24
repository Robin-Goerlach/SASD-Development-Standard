---
title: "Projektcharta — SASD Development Standard Version 1.0"
document-id: SASD-FND-001
document-type: normative
status: Proposed
version: 0.1.0
standard-version: "1.0"
language: de
authoritative: true
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: []
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Projektcharta — SASD Development Standard Version 1.0


## Projektdefinition

Der **SASD Development Standard** ist ein offener Entwicklungs- und Arbeitsstandard für professionell strukturierte technische Projekte. Er richtet sich insbesondere an Einzelentwickler, Freelancer, Open-Source-Projekte, Auszubildende, Studierende, Administratoren mit Entwicklungsaufgaben sowie kleine Softwareunternehmen und Teams.

Der Standard beschreibt nicht primär, wie einzelne Programmiersprachen oder Werkzeuge verwendet werden. Er beantwortet vielmehr die übergeordnete Frage:

> Wie wird aus einer Idee ein nachvollziehbares, reproduzierbares, sicheres und langfristig wartbares technisches Produkt?

Er definiert dafür einen vollständigen Entwicklungsprozess – von der Ideenfindung und Zieldefinition über Architektur, Implementierung, Dokumentation und Qualitätssicherung bis hin zu Veröffentlichung, Betrieb, Wartung und Weiterentwicklung.

## Vision

Jedes nach dem SASD Development Standard entwickelte Projekt soll so aufgebaut und dokumentiert sein, dass ein fremder Entwickler oder Administrator auch nach mehreren Jahren:

- den Zweck des Projekts versteht,
- den Aufbau nachvollziehen kann,
- technische Entscheidungen rekonstruieren kann,
- das Projekt reproduzierbar erstellen und betreiben kann,
- Fehler systematisch untersuchen kann,
- Änderungen sicher durchführen kann,
- Tests ausführen und erweitern kann,
- Releases erstellen kann,
- und das Projekt langfristig weiterentwickeln kann.

Wissen darf nicht ausschließlich im Kopf einzelner Beteiligter, in vergänglichen Chatverläufen oder in nicht dokumentierten Arbeitsabläufen existieren.

## Mission

Der SASD Development Standard legt fest:

- welche Projektphasen existieren,
- welche Dokumente benötigt werden,
- wann diese Dokumente erstellt und aktualisiert werden,
- welchen Zweck jedes Dokument erfüllt,
- welche Qualitätsanforderungen gelten,
- wie Anforderungen und Projektgrenzen definiert werden,
- wie technische Entscheidungen dokumentiert werden,
- wie Software und Infrastruktur strukturiert werden,
- wie Sicherheit und Datenschutz berücksichtigt werden,
- wie Tests, Reviews und Freigaben erfolgen,
- wie Releases vorbereitet und veröffentlicht werden,
- wie Projekte betrieben, gewartet und archiviert werden,
- und wie KI-Unterstützung nachvollziehbar und verantwortungsvoll eingesetzt wird.

## Kernidee

Der SASD Development Standard beantwortet nicht nur die Frage:

> Wie programmiert man guten Code?

Sondern insbesondere:

> Wie entwickelt, dokumentiert, prüft, veröffentlicht, betreibt und pflegt man ein professionelles technisches Projekt?

Guter Code allein ergibt noch kein professionelles, wartbares und reproduzierbares Produkt.

## Zielgruppen

Der Standard richtet sich primär an:

- Einzelentwickler,
- Freelancer,
- Open-Source-Maintainer,
- kleine Softwareunternehmen und Teams,
- Auszubildende und Fachinformatiker,
- Studierende,
- Trainer und Bildungseinrichtungen,
- Systemadministratoren mit Entwicklungsaufgaben,
- DevOps- und Plattformverantwortliche,
- technisch orientierte Anwender mit KI-Unterstützung.

## Zu lösende Probleme

Der Standard adressiert unter anderem:

- unklare Ziele und Projektgrenzen,
- fehlende oder nicht nachvollziehbare Architektur,
- inkonsistente Repository-Strukturen,
- unvollständige Dokumentation,
- fehlende Roadmaps und Prioritäten,
- unzureichende Tests und Reviews,
- nicht dokumentierte Entscheidungen,
- fehlende Sicherheitsbetrachtungen,
- nicht reproduzierbare Builds,
- unklare Release- und Wartungsprozesse,
- sowie Wissen, das nur bei einzelnen Personen vorhanden ist.

## Geltungsbereich

Langfristig umfasst der Standard alle technischen SASD-Projekte, darunter:

- Softwareentwicklung,
- C#/.NET-Anwendungen,
- Webanwendungen und APIs,
- Kommandozeilen- und Desktopwerkzeuge,
- Linux-Administration,
- Datenbanken,
- Docker und Kubernetes,
- Infrastrukturautomatisierung,
- DevOps und CI/CD,
- IT-Sicherheit,
- Monitoring und Logging,
- technische Dokumentation,
- Weiterbildung und Lernprojekte,
- Prompt Engineering,
- KI-gestützte Entwicklungsprozesse,
- Open-Source-Projekte,
- Betrieb und Wartung technischer Systeme.

## Produktmodell

Der SASD Development Standard besteht aus drei logisch getrennten Ebenen:

1. **Standard:** normative Regeln, Profile, Prozesse, Vorlagen und Checklisten.
2. **Referenzimplementierungen:** konkrete SASD-Projekte, an denen die Regeln angewendet und validiert werden.
3. **Development Tooling:** wiederverwendbare Dateien und Werkzeuge zur Erzeugung und Prüfung standardkonformer Projekte.

## Ziel von Version 1.0

Version 1.0 soll ein belastbares Fundament schaffen. Dazu gehören insbesondere:

1. ein technologieunabhängiger Kernstandard,
2. ein verbindliches Repository- und Dokumentationsmodell,
3. ein C#/.NET-Entwicklungsprofil,
4. ein Desktopanwendungsprofil,
5. ein GitHub-Standard,
6. eine Klassifikation von Projektgrößen und Qualitätsstufen,
7. grundlegende Sicherheits- und Testanforderungen,
8. Regeln für Prompt Engineering und KI-Unterstützung,
9. Vorlagen und Checklisten,
10. technische Basisdateien für C#-Projekte,
11. die exemplarische Migration ausgewählter SASD-Repositories.

## Leitprinzipien

- **Nachvollziehbarkeit:** Entscheidungen, Anforderungen und Änderungen werden dokumentiert.
- **Reproduzierbarkeit:** Build, Test, Installation und Betrieb sind wiederholbar.
- **Wartbarkeit:** Projekte werden für langfristige Weiterentwicklung entworfen.
- **Pragmatismus:** Regeln müssen einen erkennbaren Nutzen besitzen.
- **Angemessenheit:** Anforderungen richten sich nach Größe, Risiko und Lebensdauer.
- **Automatisierung:** Wiederholbare Prüfungen und Abläufe werden möglichst automatisiert.
- **Security by Design:** Sicherheit beginnt bei Anforderungen und Architektur.
- **Documentation as Product:** Dokumentation ist Teil des Projektergebnisses.
- **Lernfähigkeit:** Erfahrungen aus Projekten fließen in den Standard zurück.
- **Offenheit:** Der Standard soll auch außerhalb von SASD verständlich und nutzbar sein.

## Zusammenfassende Produktvision

Der SASD Development Standard ist das gemeinsame Betriebssystem für die Entwicklung und Pflege aller technischen SASD-Projekte.
