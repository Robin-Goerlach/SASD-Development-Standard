---
title: "Qualitätsleitfaden für SASD-Prompts"
document-id: SASD-REF-PROMPT-002
document-type: informative
status: Draft
version: 0.13.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-25
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core]
depends-on: [SASD-CORE-013, SASD-REF-PROMPT-001]
---

# Qualitätsleitfaden für SASD-Prompts

Ein SASD-Prompt soll eine wiederholbare Arbeitsanweisung sein, kein Ersatz für fachliche Prüfung.

## Mindeststruktur

Jeder Paketprompt enthält:

1. Zweck,
2. Eingaben,
3. Arbeitsauftrag,
4. Qualitätsregeln,
5. Ausgabeformat.

## Qualitätsmerkmale

- klarer Geltungsbereich und erwartetes Ergebnis,
- explizite Variablen statt versteckter Annahmen,
- Trennung von Fakten, Annahmen, Empfehlungen und offenen Punkten,
- Verbot unbelegter Build-, Test-, CI- oder Sicherheitsclaims,
- proportionale Anwendung ohne Overengineering,
- eindeutige Ausgabe und überprüfbare Akzeptanzkriterien,
- keine widersprüchlichen Rollen oder impliziten Freigaben.

## Review

Ein Review prüft Inhalt, Metadaten, Variablen, Sicherheitsgrenzen, Überschneidungen, Sprache, Ausgabeformat und praktische Anwendbarkeit. Ein Prompt wird nicht allein wegen syntaktischer Gültigkeit als Stable eingestuft.

## Änderung

Kleine sprachliche Präzisierungen erhöhen die Patch-Version. Neue optionale Ausgaben oder Variablen erhöhen die Minor-Version. Inkompatible Variablen-, Bedeutungs- oder Ausgabeänderungen erhöhen die Major-Version oder erzeugen eine neue Prompt-ID.
