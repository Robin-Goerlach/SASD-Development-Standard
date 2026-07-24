---
title: "Akzeptanzkriterien für SASD Development Standard Version 1.0"
document-id: SASD-FND-007
document-type: normative
status: Draft
version: 0.1.0
standard-version: "1.0"
language: de
authoritative: true
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-FND-002, SASD-FND-005, SASD-FND-006, SASD-GOV-007]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Akzeptanzkriterien für Version 1.0

## 1. Zweck

Dieses Dokument definiert die überprüfbaren Bedingungen, unter denen SASD Development Standard Version 1.0 veröffentlicht werden kann.

## 2. Foundation und Governance

- Projektcharta, Scope, Prinzipien, Inhaltsarchitektur und Dokumentkatalog sind Approved.
- Normative Sprache, Dokumentlebenszyklus, Metadaten, Versionierung, Änderungen, Ausnahmen und Compliance sind Approved.
- Alle normativen Dokumente besitzen eindeutige Dokument-IDs und vollständige Metadaten.
- Deutsch ist als autoritative Fassung eindeutig gekennzeichnet.

## 3. Core Standard

- Alle im Dokumentkatalog für Version 1.0 vorgesehenen Core-Dokumente sind Approved.
- Qualitätsstufen sind eindeutig unterscheidbar und praktisch auswählbar.
- MUSS-Anforderungen besitzen nachvollziehbare Prüfkriterien oder Nachweise.
- Es bestehen keine bekannten ungelösten normativen Widersprüche.
- Anwendbarkeit, Qualitätsstufenpräzedenz und `Not Applicable` sind eindeutig geregelt.
- Mindestens ein dokumentierter Core-Konsistenz- und Proportionalitätsreview liegt vor.

## 4. Profile

- C#/.NET-Profil und Desktopprofil sind Approved.
- Profile verweisen auf den Kernstandard und enthalten keine stillschweigenden Widersprüche.
- Kleine, mittlere und komplexere Projektstrukturen werden angemessen unterstützt.

## 5. Unterstützende Materialien

- zentrale Dokumentvorlagen sind praktisch verwendbar,
- Projektstart-, Milestone-, Security-, Dokumentreview- und Release-Checklisten sind vorhanden,
- Prompt-Pakete decken mindestens Initialisierung, Architektur, Entwicklung, Review, Debugging und Release ab,
- `.editorconfig`, zentrale .NET-Buildkonfiguration und grundlegende Prüfwerkzeuge sind verfügbar,
- interne Links und Dokumentmetadaten können automatisiert geprüft werden.

## 6. Pilotierung

Mindestens drei unterschiedlich große C#/.NET-Projekte wurden bewertet oder migriert:

1. kleines Werkzeug,
2. mittlere Desktopanwendung,
3. komplexere geschichtete Anwendung.

Für jedes Pilotprojekt sind dokumentiert:

- Standardversion,
- Profile,
- Qualitätsstufe,
- Ausgangszustand,
- Maßnahmen,
- Abweichungen,
- Lessons Learned.

## 7. Veröffentlichung

- Changelog und Release Notes sind vollständig,
- ein Release Candidate wurde praktisch geprüft,
- Word- und PDF-Ausgaben wurden aus der Markdown-Quelle erzeugt,
- Tag `v1.0.0` verweist auf den freigegebenen Stand,
- ein fremder Entwickler kann aus README und Dokumentation heraus mit der Anwendung beginnen.
