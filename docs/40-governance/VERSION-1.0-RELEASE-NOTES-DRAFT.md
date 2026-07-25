---
title: "Release Notes Draft 1.0.0-rc.1"
document-id: SASD-REF-RC-004
document-type: informative
status: Draft
version: 0.12.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-25
applies-to-quality-levels: [Recommended, Production]
applies-to-profiles: [Core]
depends-on: [SASD-REF-RC-001, SASD-REF-BASELINE-007, SASD-REF-PILOT-007]
---

# SASD Development Standard 1.0.0-rc.1 – Release Notes Draft

> **Status:** Entwurf. Dieses Dokument ist noch keine Veröffentlichung und darf erst nach Abschluss der Release-Gates als GitHub Release Notes verwendet werden.

## Überblick

`1.0.0-rc.1` ist der erste geplante Release Candidate des SASD Development Standard. Er stellt den vollständigen technologieunabhängigen Kernstandard, das C#/.NET-Profil, das Desktopprofil und die operativen Prozesse erstmals als zusammenhängende, freigegebene Version-1.0-Baseline zur praktischen Prüfung bereit.

## Enthaltene normative Bereiche

- Foundation und Governance,
- Qualitätsstufen und Projektlebenszyklus,
- Anforderungen und Architektur,
- Dokumentation und Repositoryorganisation,
- Qualität, Sicherheit und Tests,
- Releases, Wartung und Wissensmanagement,
- verantwortungsvolle KI-gestützte Entwicklung,
- C#/.NET-Profil,
- WinForms-/WPF-orientiertes Desktopprofil,
- Projektklassifikation, Projektstart, ADRs, Reviews, Legacy-Migration, Releases und Archivierung.

## Unterstützende Materialien

- Dokument- und Repositoryvorlagen,
- Projekt-, Entwicklungs-, Security- und Releasechecklisten,
- Prompt-Pakete für Projektstart, Architektur, Entwicklung, Review, Debugging und Release,
- dependency-freie Validatoren,
- plattformübergreifende GitHub-Actions-Quality-Gates,
- Referenzpilot-Baselines für Small, Medium und Large.

## Wichtigste Eigenschaften

- skalierbare Qualitätsstufen `Minimum`, `Recommended` und `Production`,
- stabile Dokument- und Anforderungs-IDs,
- nachvollziehbare Freigabe-, Ausnahme- und Alignment-Regeln,
- bewusster Schutz vor Overengineering kleiner Projekte,
- klare Trennung von vorbereitetem Artefakt und ausgeführtem Nachweis,
- maschinenlesbare Repository-, Pilot- und Releaseevidenz,
- reproduzierbare Source- und Markdown-Archive mit SHA-256-Prüfsummen.

## Bekannte Einschränkungen des Release Candidate

- Der Release Candidate ist eine Vorabversion und kann vor `1.0.0` noch kompatibilitätsrelevante Korrekturen erhalten.
- Die normative Hauptfassung ist Deutsch; die englische Ausgabe ist noch nicht Bestandteil dieses Releases.
- Word- und PDF-Publikationsartefakte werden im Anschluss an den RC praktisch erzeugt und geprüft.
- Nicht alle drei Referenzpiloten sind technisch abgeschlossen; der konkrete Stand muss vor Veröffentlichung aus dem Release Record übernommen werden.
- Spätere Linux-, Datenbank-, Container-, Kubernetes- und erweiterte Security-Profile sind nicht enthalten.

## Upgrade und Migration

Da dies der erste veröffentlichte Release Candidate ist, existiert keine frühere stabile SASD-Version, von der migriert werden muss. Projekte, die Vorabstände oder einzelne Vorlagen übernommen haben, sollten:

1. die referenzierte Standardversion und Profile dokumentieren,
2. die Qualitätsstufe neu bestätigen,
3. Abweichungen gegen die freigegebenen Anforderungen bewerten,
4. vorhandene lokale Kopien nicht stillschweigend als vollständig aligned bezeichnen.

## Verifikation

Vor Veröffentlichung werden ergänzt:

- freigegebene Commit-SHA,
- Git-Tag,
- GitHub-Actions-Lauf,
- Artefaktnamen und SHA-256-Prüfsummen,
- Ergebnis der Paketverifikation,
- abschließende Known Issues,
- Maintainer-Entscheidung.

## Feedback

Feedback soll als Documentation Issue oder Standard Change Proposal mit exakter Standardversion, Dokument-ID und möglichst konkreter Anforderungs-ID eingereicht werden.
