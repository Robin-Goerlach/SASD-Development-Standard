---
title: "Migration bestehender Projekte"
document-id: SASD-PROC-005
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
depends-on: [SASD-PROC-002, SASD-PROC-003, SASD-PROC-004, SASD-CORE-005, SASD-GOV-007]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Migration bestehender Projekte

## 1. Zweck

Dieser Prozess führt bestehende Repositories risikobasiert an den SASD Development Standard heran, ohne funktionierende Systeme durch unnötige Komplettumbauten zu gefährden.

## 2. Geltungsbereich

Der Prozess gilt für Legacy-Code, ältere SASD-Projekte, übernommene Repositories, nicht reproduzierbare Werkzeuge und Projekte, deren Qualitätsstufe oder Profile sich ändern.

## 3. Auslöser und Startbedingungen

- ein bestehendes Projekt soll weiter gepflegt oder veröffentlicht werden
- ein Repository soll auf SASD-Strukturen und Nachweise ausgerichtet werden
- Sicherheits-, Build-, Test- oder Wartungsprobleme erfordern Modernisierung
- ein Prototyp wird zum langfristig genutzten Produkt

## 4. Benötigte Eingaben

- vollständiger Repository- und Artefaktbestand
- verfügbare Build-, Test-, Installations- und Betriebsinformationen
- bekannte Nutzer, Daten und Integrationen
- bestehende Issues, Fehler, Schulden und Sicherheitsbefunde
- Zielklassifikation und verfügbare Ressourcen

## 5. Rollen und Verantwortlichkeiten

| Rolle | Verantwortung |
|---|---|
| Projekt-/Produktverantwortlicher | legt Ziel, Prioritäten und akzeptierbare Risiken fest |
| Maintainer | erstellt Assessment und Migrationsplan |
| Fachverantwortlicher | sichert benötigtes Bestandsverhalten |
| Security-/Betriebsrolle | prüft Risiken, Daten und Übergang |
| Reviewer | prüft Wellen und Abschlussnachweise |

Eine Person darf mehrere Rollen übernehmen. Die Kombination von Rollen hebt jedoch keine Nachweis-, Selbstreview- oder Freigabepflichten auf.

## 6. Prozessablauf

1. Ist-Zustand sichern und reproduzierbare Baseline schaffen.
2. Projekt klassifizieren und Standardabweichungen bewerten.
3. Risiken stabilisieren, insbesondere Secrets, Daten und kritische Abhängigkeiten.
4. Migrationsbacklog priorisieren und in Wellen planen.
5. Wellen mit Tests, Reviews und Rückfalloptionen durchführen.
6. Betrieb, Daten, Dokumentation und Releases verifizieren.
7. Zielalignment erneut bewerten und Migration abschließen.

## 7. Normative Anforderungen

### Grundsätze und Ausgangsbasis

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-400 | Eine Legacy-Migration MUSS mit einer Bestandsaufnahme beginnen und DARF NICHT allein auf äußere Strukturänderungen reduziert werden. |
| SASD-PROC-REQ-401 | Das bestehende System MUSS vor wesentlichen Umbauten soweit möglich reproduzierbar gebaut, gestartet oder in seinem Ist-Verhalten dokumentiert werden. |
| SASD-PROC-REQ-402 | Bekannte Nutzerabläufe, Datenformate, Integrationen und Betriebsabhängigkeiten MÜSSEN vor ihrer Änderung erfasst werden. |
| SASD-PROC-REQ-403 | Die Migration MUSS die Erhaltung fachlich benötigten Verhaltens von bewussten Produktänderungen unterscheiden. |
| SASD-PROC-REQ-404 | Eine vollständige Neuentwicklung SOLLTE NICHT als Standardlösung gewählt werden, solange schrittweise Verbesserung realistisch und risikoärmer ist. |
| SASD-PROC-REQ-405 | Unverständlicher oder ungetesteter Code MUSS als Risiko und nicht automatisch als entbehrlich behandelt werden. |

### Klassifikation und Assessment

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-406 | Das bestehende Projekt MUSS nach dem aktuellen SASD-Klassifikationsprozess bewertet werden. |
| SASD-PROC-REQ-407 | Das Assessment MUSS Build, Tests, Architektur, Dokumentation, Abhängigkeiten, Sicherheit, Daten, Releases und Wartbarkeit betrachten. |
| SASD-PROC-REQ-408 | Abweichungen MÜSSEN nach Risiko, Nutzen, Aufwand und Abhängigkeiten priorisiert werden. |
| SASD-PROC-REQ-409 | Das Assessment MUSS zwischen Not Applicable, offener Lücke, genehmigter Ausnahme und bewusst späterer Verbesserung unterscheiden. |
| SASD-PROC-REQ-410 | Fehlende Informationen MÜSSEN als Unsicherheit mit Klärungsmaßnahme erfasst werden. |
| SASD-PROC-REQ-411 | Die geplante Zielstufe MUSS realistisch zum Projektzweck und zur Wartungsperspektive passen. |

### Stabilisierung

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-412 | Vor strukturellen Großänderungen MUSS eine belastbare Sicherung oder ein wiederherstellbarer Versionsstand vorhanden sein. |
| SASD-PROC-REQ-413 | Secrets und sensible Daten MÜSSEN aus dem Repository entfernt oder geschützt werden, bevor weitere Verteilung erfolgt. |
| SASD-PROC-REQ-414 | Kritische Build- und Startprobleme SOLLTEN vor kosmetischen Standardisierungen behoben werden. |
| SASD-PROC-REQ-415 | Ein minimaler Charakterisierungstest oder dokumentierter manueller Baseline-Test MUSS für kritisches Verhalten geschaffen werden. |
| SASD-PROC-REQ-416 | Abhängigkeiten mit bekannten kritischen Risiken MÜSSEN priorisiert behandelt werden. |
| SASD-PROC-REQ-417 | Datenmigrationen MÜSSEN vor ihrer Ausführung auf Sicherung und Rückweg geprüft werden. |

### Migrationsplanung

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-418 | Die Migration MUSS in nachvollziehbare, möglichst reversible Wellen oder Meilensteine zerlegt werden. |
| SASD-PROC-REQ-419 | Jede Migrationswelle MUSS Ziel, Scope, Abhängigkeiten, Akzeptanzkriterien und Rückfalloption benennen. |
| SASD-PROC-REQ-420 | Funktionale Änderungen SOLLTEN von reiner Struktur- und Standardmigration getrennt werden. |
| SASD-PROC-REQ-421 | Änderungen an öffentlichen Schnittstellen oder Datenformaten MÜSSEN mit Kompatibilitäts- und Migrationsstrategie geplant werden. |
| SASD-PROC-REQ-422 | Architekturentscheidungen mit langfristiger Wirkung MÜSSEN über ADRs dokumentiert werden. |
| SASD-PROC-REQ-423 | Der Plan MUSS Quick Wins von sicherheits- oder betriebsnotwendigen Maßnahmen unterscheiden. |
| SASD-PROC-REQ-424 | Nicht priorisierte Abweichungen MÜSSEN im Migrationsbacklog sichtbar bleiben. |

### Durchführung

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-425 | Jede Migrationswelle MUSS einen prüfbaren Ausgangs- und Zielzustand besitzen. |
| SASD-PROC-REQ-426 | Automatisierte oder manuelle Regressionstests MÜSSEN das relevante Bestandsverhalten absichern. |
| SASD-PROC-REQ-427 | Die Repository-Struktur SOLLTE erst dann erweitert werden, wenn tatsächliche Verantwortungs- oder Abhängigkeitsgrenzen dies rechtfertigen. |
| SASD-PROC-REQ-428 | Umbenennungen und Verschiebungen SOLLTEN getrennt von funktionalen Änderungen erfolgen, wenn dies Reviews erleichtert. |
| SASD-PROC-REQ-429 | Neue Standards MÜSSEN auf neu oder wesentlich geänderten Code angewendet werden, soweit keine dokumentierte Übergangsregel besteht. |
| SASD-PROC-REQ-430 | Technische Schulden DÜRFEN NICHT durch reine Dateiverschiebung als behoben ausgewiesen werden. |
| SASD-PROC-REQ-431 | Jede Welle MUSS dokumentieren, welche Abweichungen geschlossen, akzeptiert oder neu entdeckt wurden. |

### Daten, Deployment und Betrieb

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-432 | Datenhaltende Legacy-Projekte MÜSSEN Datenmodell, Speicherorte, Migrationen, Backup und Wiederherstellung vor Änderungen dokumentieren. |
| SASD-PROC-REQ-433 | Deployment- oder Installationsänderungen MÜSSEN in einer repräsentativen Umgebung getestet werden. |
| SASD-PROC-REQ-434 | Betriebsrelevante Logs, Diagnosewege und Fehlerbilder SOLLTEN während der Migration verbessert werden. |
| SASD-PROC-REQ-435 | Externe Integrationen MÜSSEN auf Verträge, Versionen, Authentisierung und Fehlerverhalten geprüft werden. |
| SASD-PROC-REQ-436 | Ein Parallelbetrieb KANN verwendet werden, wenn er Risiken reduziert und Datenkonsistenz kontrolliert werden kann. |
| SASD-PROC-REQ-437 | Abschaltungen alter Komponenten MÜSSEN erst nach verifizierter Übernahme ihrer benötigten Funktionen erfolgen. |

### Freigabe und Abschluss

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-438 | Jede Migrationswelle MUSS vor ihrer Übernahme in den Hauptstand reviewt werden. |
| SASD-PROC-REQ-439 | Production-relevante Wellen MÜSSEN eine Release-, Rollback- und Betriebsfreigabe erhalten. |
| SASD-PROC-REQ-440 | Das Gesamtprojekt MUSS nach Abschluss erneut gegen Zielstufe und Profile bewertet werden. |
| SASD-PROC-REQ-441 | Verbleibende Ausnahmen und Schulden MÜSSEN mit Verantwortlichen und Zielterminen dokumentiert sein. |
| SASD-PROC-REQ-442 | Lessons Learned SOLLTEN in Standards, Templates oder Projektwissen zurückgeführt werden. |
| SASD-PROC-REQ-443 | Die Migration DARF NICHT als abgeschlossen gelten, solange Build, Tests, Dokumentation oder Betrieb nur im Wissen einer Person reproduzierbar sind. |
| SASD-PROC-REQ-444 | Ein Abschlussbericht MUSS erreichte Ziele, offene Punkte und den neuen Wartungsbaseline-Stand zusammenfassen. |

## 8. Zuordnung zu Qualitätsstufen

| Qualitätsstufe | Mindesttiefe des Prozesses |
|---|---|
| **Minimum** | Kompaktes Assessment, Build-/Verhaltensbaseline, priorisierte Kernlücken und kleine reversible Schritte. |
| **Recommended** | Vollständiges Alignment-Assessment, Migrationsbacklog, Wellenplanung, Regressionstests und Abschlussbericht. |
| **Production** | Formale Risiko-, Daten-, Betriebs- und Rollbackplanung, unabhängige Reviews sowie kontrollierte Übergabe und Stilllegung alter Komponenten. |

Die Qualitätsstufe bestimmt die erforderliche Tiefe, nicht den grundsätzlichen Zweck des Prozesses. Risikoreiche Eigenschaften können unabhängig von Projektgröße oder Teamgröße strengere Maßnahmen auslösen.

## 9. Ergebnisse und Nachweise

- Legacy-Assessment
- Zielklassifikation und Alignment-Baseline
- priorisiertes Migrationsbacklog
- Migrationsplan mit Wellen und Rückfalloptionen
- Review- und Testnachweise
- Abschlussbericht und verbleibende Ausnahmen

## 10. Abschlusskriterien

Der Prozess gilt erst als abgeschlossen, wenn die anwendbaren Kriterien erfüllt und die Nachweise auffindbar sind:

- [ ] Ist-Zustand und Sicherung sind nachvollziehbar.
- [ ] Zielstufe und Profile sind bestätigt.
- [ ] Kritische Risiken sind behoben oder formell behandelt.
- [ ] Migrationswellen sind verifiziert.
- [ ] Betrieb, Daten und Dokumentation sind übergabefähig.
- [ ] Verbleibende Lücken besitzen Verantwortliche und Termine.

## 11. Ausnahmen und Abweichungen

Ist ein Projekt nicht mehr wirtschaftlich oder sicher migrierbar, MUSS statt einer Scheinmigration eine kontrollierte Ablösung oder Archivierung beschlossen werden. Die Begründung und der Schutz verbleibender Daten und Nutzer sind zu dokumentieren.

Abweichungen von MUSS-Anforderungen werden gemäß [Ausnahmen](../40-governance/EXCEPTIONS.md) behandelt. Nicht anwendbare Anforderungen benötigen eine kurze, überprüfbare Begründung.

## 12. Verwandte Dokumente

- [Compliance und Alignment](../40-governance/COMPLIANCE.md)
- [Legacy-Assessment-Vorlage](../../templates/documents/LEGACY-MIGRATION-ASSESSMENT-TEMPLATE.md)
- [Migrationsplan-Vorlage](../../templates/documents/LEGACY-MIGRATION-PLAN-TEMPLATE.md)
- [Migrationscheckliste](../../checklists/development/LEGACY-MIGRATION-CHECKLIST.md)

---

**Anforderungsumfang:** 45 Prozessanforderungen in diesem Dokument.
