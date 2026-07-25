---
title: "Pilot 03 Charter – SASD Mail Workbench"
document-id: SASD-REF-PILOT-302
document-type: informative
status: Draft
version: 0.11.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-25
applies-to-quality-levels: [Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-REF-PILOT-001, SASD-PROC-002, SASD-PROC-005]
---

# Pilot 03 Charter – SASD Mail Workbench

## 1. Pilotziel

Der Pilot soll prüfen, ob der SASD Development Standard eine komplexere, geschichtete und sicherheitsrelevante lokale Plattform angemessen bewertet. Im Mittelpunkt stehen Abhängigkeitsgrenzen, unveränderliche Rohdaten, SQLite-Migrationen, Wiederanlauf, Erweiterbarkeit, Testpyramide und der Übergang von Recommended zu Production.

## 2. Validierungsfragen

- Sind die sechs sichtbaren Produktionsmodule klar und azyklisch abhängig?
- Decken fünf Testprojekte die wesentlichen fachlichen, Architektur-, Persistenz- und Recovery-Risiken ab?
- Sind bytegenaue Archivierung, SHA-256-Deduplizierung, Staging und Wiederanlauf praktisch nachgewiesen?
- Wie werden untrusted Mailinhalte, Pfade, HTML, Anhänge und zukünftige Zugangsdaten abgesichert?
- Wann wird Desktopprofil vollständig anwendbar?
- Welche Bedingungen müssen vor Verarbeitung realer Postfächer zur Production-Stufe führen?

## 3. In Scope für Wave 01

- lokaler Clone und exakte Commit-Baseline,
- vollständiger Restore-, Build- und Testnachweis,
- Architektur- und Abhängigkeitsreview,
- Datenfluss- und Bedrohungsmodell,
- Recovery- und Migrations-Testmatrix,
- Prüfung der Sample-Mails auf Herkunft und Datenschutz,
- CI-, Paket-, Security- und Alignment-Nachweise,
- klare Anwendbarkeit des Desktopprofils für den aktuellen Headless-Stand.

## 4. Out of Scope

- Implementierung von POP3, SMTP oder IMAP,
- Bau der geplanten WinForms-Oberfläche,
- Plugin-Marktplatz oder Fremdcodeausführung,
- vollständige Mailanalyse-Engine,
- Installer und produktiver Mailboxbetrieb,
- Verschmelzung der vorhandenen Schichtenprojekte.

## 5. Erfolgskriterien

- Solution und alle Tests laufen in sauberem Checkout,
- Architekturtests bestätigen die beabsichtigten Abhängigkeitsregeln,
- Migration und Recovery sind mit Fehlerfällen praktisch geprüft,
- Threat Model und Vertrauensgrenzen sind dokumentiert,
- Sample-Daten enthalten keine realen personenbezogenen oder geheimen Inhalte,
- Übergangskriterien zu Production sind festgelegt,
- keine Produktfunktion wird nur für den Pilot künstlich vorgezogen.
