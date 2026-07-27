---
title: "Sicherheitsleitfaden für SASD-Prompts"
document-id: SASD-REF-PROMPT-003
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
depends-on: [SASD-CORE-008, SASD-CORE-013, SASD-REF-PROMPT-001]
---

# Sicherheitsleitfaden für SASD-Prompts

## Grundsätze

- Keine Secrets, Tokens, Passwörter, privaten Schlüssel oder echten personenbezogenen Daten in Paketdateien speichern.
- Untrusted Content aus Repositories, E-Mails, Webseiten oder Dokumenten als Daten behandeln, nicht als höherrangige Anweisung.
- Externe Inhalte dürfen die Arbeitsregeln des Prompts nicht stillschweigend überschreiben.
- Ausgaben mit Code, Befehlen, SQL, Migrationen oder Konfigurationen müssen vor Ausführung geprüft werden.
- Destruktive Schritte benötigen Sicherung, Zielprüfung, Vorschau und Rückweg.

## Sensitive Variablen

`variables.json` kann Variablen als `sensitive: true` markieren. Diese Markierung ist ein Warnsignal, keine Verschlüsselung. Der Prompt Manager oder ein Adapter sollte bei solchen Werten:

- Speicherung vermeiden oder ausdrücklich bestätigen lassen,
- Maskierung in Logs und Vorschauen unterstützen,
- Exporte und Backups warnen,
- Geheimnisse niemals in Git aufnehmen.

## Prompt Injection

Bei der Analyse fremder Inhalte muss der Prompt ausdrücklich verlangen, eingebettete Instruktionen zu ignorieren, sofern sie nicht Teil des autorisierten Arbeitsauftrags sind. Toolaufrufe, Dateischreiboperationen und Veröffentlichungen benötigen eine getrennte Berechtigungsentscheidung.

## Ausgabeprüfung

Sicherheitskritische, rechtliche, medizinische oder finanzielle Aussagen benötigen aktuelle Primärquellen und menschliche Prüfung. Ein KI-Ergebnis ist kein Freigabenachweis.
