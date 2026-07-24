---
title: "Review der operativen Prozesse 0.6.0"
document-id: SASD-REF-PROC-002
document-type: informative
status: Draft
version: 0.6.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-PROC-001, SASD-PROC-002, SASD-PROC-003, SASD-PROC-004, SASD-PROC-005, SASD-PROC-006, SASD-PROC-007, SASD-GOV-006]
---

# Review der operativen Prozesse 0.6.0

## Reviewziel

Geprüft wurde, ob die sieben Prozesse den Proposed Core, das C#/.NET-Profil und das Desktopprofil ohne unnötige Bürokratie operationalisieren.

## Prüffragen

- Sind Startbedingungen, Rollen, Schritte, Ergebnisse und Abschlusskriterien eindeutig?
- Sind Minimum, Recommended und Production proportional skaliert?
- Können Einzelentwickler die Prozesse anwenden, ohne fiktive Organisationsstrukturen zu erzeugen?
- Werden Projektgröße, Kritikalität, Qualitätsstufe und Profile getrennt behandelt?
- Sind Notfälle, Ausnahmen und nachgelagerte Reviews kontrolliert möglich?
- Vermeiden die Prozesse verdeckte Komplettumbauten bei Legacy-Projekten?
- Sind die Ergebnisse als Vorlagen und Checklisten praktisch nutzbar?

## Zentrale Entscheidungen

1. **Recommended ist der Normalfall für gepflegte SASD-Projekte.** Minimum bleibt für kleine, risikoarme und zeitlich begrenzte Vorhaben zulässig.
2. **Qualitätsstufe ist nicht Projektgröße.** Sicherheits- und Betriebsrisiken können ein kleines Projekt auf Production-Tiefe heben.
3. **Legacy-Migration beginnt mit Stabilisierung.** Build, Verhalten, Daten und Sicherung haben Vorrang vor kosmetischer Strukturangleichung.
4. **Reviews sind risikobasiert.** Einzelentwickler verwenden strukturierte, zeitlich getrennte Selbstreviews; kritische Production-Themen benötigen unabhängige Expertise.
5. **ADRs bleiben historisch stabil.** Wesentliche Änderungen erzeugen Nachfolgeentscheidungen statt stiller Umschreibung.
6. **Releases beziehen sich auf unveränderte Artefakte.** Nachträgliche manuelle Änderungen am geprüften Paket sind unzulässig.
7. **Archivierung ist ein technischer Prozess.** Repository-Status allein beendet weder Zugänge noch Daten-, Kosten- oder Aufbewahrungspflichten.

## Ergebnis

Alle sieben Prozessdokumente erfüllen die Struktur- und Konsistenzkriterien für **Proposed 0.6.0**. Sie sind für Pilotprojekte geeignet. Eine formale Freigabe als Approved erfolgt erst nach Anwendung auf mindestens einem kleinen, einem mittleren und einem komplexeren SASD-Projekt.

## Offene Pilotfragen

- Reicht die Klassifikationsvorlage für sehr kleine Hilfsprogramme aus?
- Welche Prozessnachweise können in einem einzigen `SASD-PROJECT-RECORD.md` sinnvoll zusammengeführt werden?
- Welche Releaseprüfungen lassen sich zuverlässig automatisieren?
- Welche Legacy-Assessment-Kategorien liefern den größten praktischen Nutzen?
- Wann ist ein externer Security- oder Fachreview für Einzelentwickler realistisch erforderlich?
