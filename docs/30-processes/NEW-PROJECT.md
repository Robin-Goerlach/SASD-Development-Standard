---
title: "Neues Projekt initialisieren"
document-id: SASD-PROC-001
document-type: normative
status: Proposed
version: 0.6.0
standard-version: "1.0"
language: de
authoritative: true
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-PROC-002, SASD-CORE-001, SASD-CORE-002, SASD-CORE-003, SASD-CORE-005, SASD-CORE-006, SASD-CORE-008, SASD-GOV-006]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Neues Projekt initialisieren

## 1. Zweck

Dieser Prozess führt eine Projektidee zu einem entwicklungsbereiten, nachvollziehbaren Repository. Er erzeugt gerade genug Klarheit, Struktur und Nachweise, um verantwortbar mit der Umsetzung zu beginnen.

## 2. Geltungsbereich

Der Prozess gilt für neue Software-, Automatisierungs-, Infrastruktur-, Datenbank- und Dokumentationsprojekte. Für Experimente darf er kompakt durchgeführt werden; für langfristige oder produktive Vorhaben ist eine größere Tiefe erforderlich.

## 3. Auslöser und Startbedingungen

- eine priorisierte Projektidee soll umgesetzt werden
- ein Lern- oder Experimentvorhaben soll als nachvollziehbares Repository angelegt werden
- ein Produkt oder technischer Dienst wird neu begonnen
- ein Prototyp wird bewusst als neues, gepflegtes Projekt neu aufgesetzt

## 4. Benötigte Eingaben

- Projektidee und erwarteter Nutzen
- erste Stakeholder- oder Nutzerinformationen
- vorläufige Ressourcen- und Zeitgrenzen
- bekannte technische, rechtliche und sicherheitsbezogene Vorgaben
- Ergebnis der Projektklassifikation

## 5. Rollen und Verantwortlichkeiten

| Rolle | Verantwortung |
|---|---|
| Projektverantwortlicher | verantwortet Ziel, Scope, Prioritäten und Freigabe |
| Fachverantwortlicher | präzisiert Bedarf und Akzeptanzkriterien |
| Technischer Verantwortlicher | erstellt Architektur- und Repository-Grundlage |
| Security-/Datenschutzrolle | bewertet Schutzbedarf und Startbedingungen |
| Reviewer | prüft Readiness und Nachvollziehbarkeit |

Eine Person darf mehrere Rollen übernehmen. Die Kombination von Rollen hebt jedoch keine Nachweis-, Selbstreview- oder Freigabepflichten auf.

## 6. Prozessablauf

1. Projektidee in einem Projektbrief erfassen.
2. Projekt klassifizieren und Qualitätsstufe sowie Profile festlegen.
3. Scope, Nicht-Ziele, Anforderungen und erste Akzeptanzkriterien bestimmen.
4. Risiken, Sicherheit, Datenschutz und externe Verpflichtungen bewerten.
5. Architekturgrundlage und wesentliche ADRs erstellen.
6. Repository, Toolchain, Build, Tests und Dokumentation initialisieren.
7. Release-, Betriebs- und Wartungsperspektive passend zur Stufe festlegen.
8. Readiness Gate durchführen und ersten Meilenstein freigeben.

## 7. Normative Anforderungen

### Auftrag und Projektbrief

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-001 | Jedes neue Projekt MUSS mit einem dokumentierten Projektauftrag oder Projektbrief beginnen. |
| SASD-PROC-REQ-002 | Der Projektbrief MUSS Problem, Ziel, Zielgruppe, erwarteten Nutzen und verantwortliche Person benennen. |
| SASD-PROC-REQ-003 | Nicht-Ziele MÜSSEN dokumentiert werden, wenn sie den Scope wirksam begrenzen. |
| SASD-PROC-REQ-004 | Annahmen und ungeklärte Fragen MÜSSEN von bestätigten Fakten unterscheidbar sein. |
| SASD-PROC-REQ-005 | Ein Projekt DARF NICHT allein mit einer Werkzeug- oder Technologieentscheidung begründet werden, wenn das zu lösende Problem unklar ist. |
| SASD-PROC-REQ-006 | Der geplante Lebenszyklus MUSS mindestens als Experiment, befristetes Vorhaben oder langfristig gepflegtes Produkt benannt werden. |

### Klassifikation und Planung

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-007 | Vor der strukturellen Einrichtung MUSS die Projektklassifikation abgeschlossen oder vorläufig freigegeben sein. |
| SASD-PROC-REQ-008 | Die Initialisierung MUSS die gewählte Qualitätsstufe und alle anwendbaren Profile übernehmen. |
| SASD-PROC-REQ-009 | Die erwarteten Meilensteine MÜSSEN mindestens bis zu einem ersten überprüfbaren Ergebnis beschrieben werden. |
| SASD-PROC-REQ-010 | Risiken, externe Abhängigkeiten und wesentliche Unsicherheiten SOLLTEN vor Beginn der Implementierung sichtbar sein. |
| SASD-PROC-REQ-011 | Bei begrenzten Ressourcen MUSS der Scope reduziert werden, bevor unverzichtbare Qualitäts- oder Sicherheitsmaßnahmen entfallen. |
| SASD-PROC-REQ-012 | Die Initialisierung SOLLTE eine Definition of Ready für den ersten Entwicklungsabschnitt enthalten. |

### Anforderungen und Akzeptanz

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-013 | Die initialen funktionalen Anforderungen MÜSSEN ausreichend konkret sein, um den ersten Meilenstein planen und prüfen zu können. |
| SASD-PROC-REQ-014 | Nichtfunktionale Anforderungen MÜSSEN berücksichtigt werden, soweit Sicherheit, Daten, Leistung, Bedienbarkeit, Betrieb oder Wartung betroffen sind. |
| SASD-PROC-REQ-015 | Jeder erste Meilenstein MUSS überprüfbare Akzeptanzkriterien besitzen. |
| SASD-PROC-REQ-016 | Anforderungen SOLLTEN priorisiert und auf ihren Ursprung zurückführbar sein. |
| SASD-PROC-REQ-017 | Ungeklärte Anforderungen MÜSSEN als offene Punkte mit Verantwortlichem behandelt werden. |
| SASD-PROC-REQ-018 | Die Initialisierung DARF NICHT vorgeben, dass sämtliche späteren Anforderungen bereits vollständig bekannt sein müssen. |

### Architektur und technische Basis

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-019 | Vor dem ersten wesentlichen Implementierungsschritt MUSS eine angemessene Architekturgrundlage vorhanden sein. |
| SASD-PROC-REQ-020 | Wesentliche Technologieentscheidungen MÜSSEN begründet und bei langfristiger Wirkung als ADR erfasst werden. |
| SASD-PROC-REQ-021 | Die Projektstruktur MUSS zur klassifizierten Größe passen und DARF NICHT vorsorglich unnötige Schichten oder Projekte erzeugen. |
| SASD-PROC-REQ-022 | Externe Dienste, Datenbanken, Dateiformate und Integrationen MÜSSEN in einer ersten Systemkontextsicht sichtbar sein. |
| SASD-PROC-REQ-023 | Persistente Daten MÜSSEN hinsichtlich Speicherort, Schemaentwicklung, Sicherung und Löschung vorläufig bewertet werden. |
| SASD-PROC-REQ-024 | Bekannte technische Schulden, die bewusst zum Start akzeptiert werden, MÜSSEN dokumentiert und terminiert werden. |

### Repository und Entwicklungsumgebung

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-025 | Das Repository MUSS einen eindeutigen Namen, eine Lizenzentscheidung und eine verständliche README-Grundlage besitzen. |
| SASD-PROC-REQ-026 | Quellcode, Tests, Dokumentation und erzeugte Artefakte MÜSSEN nachvollziehbar getrennt werden. |
| SASD-PROC-REQ-027 | Secrets, lokale Nutzerdaten und nicht veröffentlichbare Artefakte DÜRFEN NICHT in die Versionsverwaltung aufgenommen werden. |
| SASD-PROC-REQ-028 | Die benötigten Entwicklungswerkzeuge und Versionen MÜSSEN dokumentiert oder maschinenlesbar festgelegt werden. |
| SASD-PROC-REQ-029 | Ein frischer Checkout SOLLTE mit dokumentierten Schritten gebaut und getestet werden können. |
| SASD-PROC-REQ-030 | Die Initialisierung MUSS mindestens einen erfolgreichen Baseline-Build oder eine begründete offene Build-Aufgabe enthalten. |
| SASD-PROC-REQ-031 | Repository-Metadaten, Branching und Commit-Konventionen SOLLTEN vor der parallelen Zusammenarbeit festgelegt werden. |

### Qualität, Tests und Sicherheit

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-032 | Die Initialisierung MUSS eine zur Qualitätsstufe passende Teststrategie oder einen kompakten Testabschnitt enthalten. |
| SASD-PROC-REQ-033 | Kritische Annahmen und risikoreiche Komponenten SOLLTEN früh durch Spikes, Prototypen oder Tests validiert werden. |
| SASD-PROC-REQ-034 | Die Sicherheitsbaseline MUSS vor der Verarbeitung sensibler Daten oder Zugangsdaten angewendet werden. |
| SASD-PROC-REQ-035 | Abhängigkeiten MÜSSEN aus nachvollziehbaren Quellen bezogen und in ihrer Funktion begründet werden. |
| SASD-PROC-REQ-036 | Die Definition of Done MUSS für den ersten Meilenstein festgelegt sein. |
| SASD-PROC-REQ-037 | Geplante manuelle Prüfungen MÜSSEN so beschrieben sein, dass sie reproduzierbar durchgeführt werden können. |

### Betrieb, Veröffentlichung und Pflege

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-038 | Für verteilte oder betriebene Projekte MUSS das vorgesehene Deployment- und Updateverfahren beschrieben werden. |
| SASD-PROC-REQ-039 | Die Speicherorte für Konfiguration, Logs, Nutzerdaten und Backups MÜSSEN vor dem ersten produktionsnahen Einsatz festgelegt werden. |
| SASD-PROC-REQ-040 | Der verantwortliche Wartungs- und Supportweg MUSS benannt werden. |
| SASD-PROC-REQ-041 | Ein langfristig gepflegtes Projekt SOLLTE eine Roadmap und einen Änderungsprozess besitzen. |
| SASD-PROC-REQ-042 | Production-Projekte MÜSSEN bereits bei der Initialisierung Wiederherstellung, Rollback und Betriebsübergabe berücksichtigen. |
| SASD-PROC-REQ-043 | Ein Projekt ohne realistische Pflegeperspektive MUSS diesen Umstand und die daraus entstehenden Grenzen offen dokumentieren. |

### Readiness Gate

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-044 | Der Start der regulären Implementierung MUSS durch ein dokumentiertes Readiness Gate bestätigt werden. |
| SASD-PROC-REQ-045 | Das Readiness Gate MUSS offene Blocker von akzeptierten Restunsicherheiten unterscheiden. |
| SASD-PROC-REQ-046 | Blockierende Sicherheits-, Lizenz- oder Zugangsfragen MÜSSEN vor Freigabe gelöst oder formell eskaliert sein. |
| SASD-PROC-REQ-047 | Bei Einzelentwicklung MUSS ein zeitlich getrennter Selbstreview der Initialisierungsartefakte erfolgen. |
| SASD-PROC-REQ-048 | Die Freigabe MUSS benennen, welcher Meilenstein als Nächstes umgesetzt und woran sein Erfolg erkannt wird. |
| SASD-PROC-REQ-049 | Änderungen nach dem Readiness Gate MÜSSEN kontrolliert in Anforderungen, Entscheidungen oder Planung zurückgeführt werden. |

## 8. Zuordnung zu Qualitätsstufen

| Qualitätsstufe | Mindesttiefe des Prozesses |
|---|---|
| **Minimum** | Kompakter Projektbrief, Klassifikation, Repository-Baseline, Build-/Testnachweis und erster Meilenstein. |
| **Recommended** | Getrennt nachvollziehbare Anforderungen, Architektur, Roadmap, Teststrategie, Risiken und Wartungsperspektive. |
| **Production** | Formale Freigaben, Schutzbedarf, Betriebs-, Wiederherstellungs-, Release- und Supportplanung vor produktionsnaher Nutzung. |

Die Qualitätsstufe bestimmt die erforderliche Tiefe, nicht den grundsätzlichen Zweck des Prozesses. Risikoreiche Eigenschaften können unabhängig von Projektgröße oder Teamgröße strengere Maßnahmen auslösen.

## 9. Ergebnisse und Nachweise

- Projektbrief und Scope
- Projektklassifikation
- initiale Anforderungen und Akzeptanzkriterien
- Architekturgrundlage und erste ADRs
- initialisiertes Repository mit Build- und Testbaseline
- Risiko-, Sicherheits-, Release- und Wartungsgrundlage
- Readiness-Entscheidung und erster Meilenstein

## 10. Abschlusskriterien

Der Prozess gilt erst als abgeschlossen, wenn die anwendbaren Kriterien erfüllt und die Nachweise auffindbar sind:

- [ ] Projektauftrag und Nicht-Ziele sind verständlich.
- [ ] Qualitätsstufe und Profile sind festgelegt.
- [ ] Erster Meilenstein und Akzeptanzkriterien sind prüfbar.
- [ ] Repository kann nachvollziehbar gebaut oder die verbleibende Blockade ist dokumentiert.
- [ ] Sicherheits- und Lizenzblocker sind behandelt.
- [ ] Readiness Gate ist abgeschlossen.

## 11. Ausnahmen und Abweichungen

Bei zeitkritischen technischen Spikes darf die Initialisierung auf Projektbrief, Klassifikation, Sicherheitsbaseline, Repository-Baseline und zeitlich begrenzte Lernziele reduziert werden. Eine Übernahme in dauerhafte Nutzung erfordert anschließend die vollständige Neubewertung.

Abweichungen von MUSS-Anforderungen werden gemäß [Ausnahmen](../40-governance/EXCEPTIONS.md) behandelt. Nicht anwendbare Anforderungen benötigen eine kurze, überprüfbare Begründung.

## 12. Verwandte Dokumente

- [Projektklassifikation](PROJECT-CLASSIFICATION.md)
- [Projektbrief-Vorlage](../../templates/documents/PROJECT-BRIEF-TEMPLATE.md)
- [Initialisierungsnachweis](../../templates/documents/PROJECT-INITIALIZATION-RECORD-TEMPLATE.md)
- [Neue-Projekt-Checkliste](../../checklists/project-initiation/NEW-PROJECT-CHECKLIST.md)

---

**Anforderungsumfang:** 49 Prozessanforderungen in diesem Dokument.
