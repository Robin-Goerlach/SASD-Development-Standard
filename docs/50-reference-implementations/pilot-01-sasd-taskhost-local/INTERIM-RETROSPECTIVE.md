---
title: "Pilot 01 Zwischenretrospektive nach Wave-01-Artefakt"
document-id: SASD-REF-PILOT-113
document-type: informative
status: Draft
version: 0.8.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Recommended]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-REF-PILOT-111, SASD-REF-PILOT-004]
---

# Zwischenretrospektive – Pilot 01

## 1. Was bereits funktioniert hat

- Die Klassifikation als Small + Recommended verhinderte eine unnötige Schichtenmigration.
- Gap Register und Wellenplan hielten Produktverbesserungen aus der Stabilitätswelle heraus.
- Die Trennung von Code, Tests, Buildbasis, CI und Dokumentation ermöglichte einen nachvollziehbaren Overlay-Umfang.
- Datenbanktests konnten ergänzt werden, ohne Entity Framework oder ein Repository-Framework einzuführen.
- Das Evidenzmodell verhinderte, dass fehlende Windows-Verifikation verschwiegen wurde.

## 2. Wo der Standard nachgeschärft werden musste

- „Paket erzeugt“ und „Zielstand verifiziert“ waren bisher nicht deutlich genug getrennt.
- Ein historisch gemeldeter Fehler kann in einem später sichtbaren Stand nicht immer reproduziert werden.
- CI-Konfiguration und CI-Erfolg brauchen getrennte Evidenz.
- Updatepakete benötigen Hash, Zielangabe, Baseline und explizite Nicht-Nachweise.
- Der Start einer Folgewelle braucht ein Verifikationsgate.

## 3. Vorläufige Bewertung der Qualitätsstufe

`Recommended` bleibt angemessen. `Minimum` wäre wegen persistenter privater Daten, langfristiger Pflege und öffentlichem Repository zu schwach. `Production` wäre für ein lokales MVP ohne externe Nutzer- oder Betriebsverpflichtung unverhältnismäßig.

## 4. Bewertung des Overengineering-Schutzes

Bestätigt wurden:

- ein Produktprojekt bleibt zulässig,
- ein separates Testprojekt ist proportional,
- direkte SQLite-Nutzung bleibt zulässig,
- WinForms bleibt zulässig,
- DI, Generic Host, WPF, ORM und zusätzliche Assemblies sind nicht automatisch erforderlich.

## 5. Offene Erkenntnisse

Erst die Windows-Verifikation kann zeigen:

- ob die Buildvorlagen ohne unnötige Reibung funktionieren,
- ob die Paketversionen kompatibel sind,
- ob die Tests tatsächlich stabil laufen,
- ob das Start- und Diagnosekonzept praxistauglich ist,
- ob die Dokumentationsmenge für ein kleines Projekt angemessen bleibt.

## 6. Nächste Entscheidung

Wave 01 wird kontrolliert verifiziert. Wave 02 bleibt bis dahin gesperrt. Nach erfolgreicher Verifikation wird eine Abschlussretrospektive erstellt und entschieden, welche Feedbackpunkte normative Änderungen auslösen.
