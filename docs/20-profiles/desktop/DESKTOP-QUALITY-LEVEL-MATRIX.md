---
title: "Desktop Quality Level Matrix"
document-id: SASD-REF-DESKTOP-007
document-type: informative
status: Draft
version: 0.9.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Desktop]
depends-on: [SASD-PROF-DESKTOP-001, SASD-PROF-DESKTOP-002, SASD-PROF-DESKTOP-003, SASD-PROF-DESKTOP-004]
generated: false
---

# Desktop Quality Level Matrix

## Zweck

Diese konsolidierte Sicht unterstützt Projektklassifikation, Assessment und Pilotierung. Bei Konflikten gelten die normativen Profildokumente.

| Thema | Minimum | Recommended | Production |
|---|---|---|---|
| Benutzergruppen und Kernaufgaben | kurz beschrieben | priorisierte Abläufe | validierte Nutzungsszenarien |
| Technologieentscheidung | begründet | Alternativen bewertet | Lebenszyklus- und Lieferantenrisiko bewertet |
| UI-Struktur | Logik trennbar | Presenter/ViewModel oder gleichwertig | modulare, überprüfte Grenzen |
| Navigation | nachvollziehbar | zentral koordiniert | getestet und wiederherstellbar |
| Dialoge | sicher und eindeutig | gemeinsame Verträge | automatisiert für kritische Abläufe geprüft |
| Hintergrundoperationen | UI bleibt responsiv | Abbruch und Fortschritt | Last, Race und Shutdown geprüft |
| Tastatur | Kernabläufe | vollständiger Review | Regression und assistive Technik |
| Accessibility | wesentliche Controls | systematischer Review | risikobasierter assistiver Test |
| DPI und Mehrmonitor | Hauptansichten | repräsentative Matrix | definierte Regression |
| Validierung | verständlich | inline und fokussiert | barrierefrei getestet |
| Lokalisierung | bei Bedarf berücksichtigt | Ressourcenmodell | Übersetzungs- und Layouttest |
| Datenpfade | getrennt | dokumentiert und migrierbar | Backup, Restore und Datenschutz |
| Crashdiagnose | Log und Version | Fehlerreferenz | Supportpaket und Prozess |
| Publishing | reproduzierbar | CI-/skriptfähig | freigegeben und signiert |
| Installation | Kernpfad | Upgrade und Deinstallation | Zielsystemmatrix |
| Updates | beschrieben | getesteter Upgradepfad | Authentizität und Rollback |
| UI-Tests | kritische Logik | Präsentation und Smoke | kritische End-to-End-Abläufe |
| Support | Pfade und Logs | Troubleshooting | EOL- und Wartungsprozess |

## Anwendung

Die Matrix ersetzt keine Requirement-Matrix. Ein Projekt verwendet sie als Startpunkt und bewertet anschließend die einzelnen `SASD-DESKTOP-REQ-*`-Anforderungen als erfüllt, nicht anwendbar, Ausnahme oder offen.
