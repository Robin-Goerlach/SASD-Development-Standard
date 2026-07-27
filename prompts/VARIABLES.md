---
title: "Variablenmodell für SASD-Prompts"
document-id: SASD-REF-PROMPT-004
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
depends-on: [SASD-REF-PROMPT-001, SASD-REF-PROMPT-003]
---

# Variablenmodell für SASD-Prompts

Variablen verwenden die Syntax `{{variable_name}}` und werden zentral in [`variables.json`](packages/sasd-development-standard-v1/variables.json) beschrieben.

## Regeln

- Namen: `^[a-z][a-z0-9_]*$`
- UTF-8-Inhalte sind zulässig.
- Fehlende Pflichtvariablen blockieren eine vollständige Ausführung.
- Defaultwerte dürfen keine projektspezifischen Annahmen oder Secrets enthalten.
- Sensitive Variablen werden nicht automatisch gespeichert oder exportiert.
- Literaltext mit geschweiften Klammern darf nicht wie eine Variable aussehen.

## Auflösung

Ein Client soll vor Ausführung:

1. benötigte Variablen anzeigen,
2. Defaultwerte kenntlich machen,
3. Pflichtwerte validieren,
4. sensitive Werte markieren,
5. die aufgelöste Vorschau anzeigen,
6. keine nicht deklarierten Platzhalter übrig lassen.
