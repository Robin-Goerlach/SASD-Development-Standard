---
title: "Index der Prozessanforderungen"
document-id: SASD-REF-PROC-003
document-type: informative
status: Draft
version: 0.9.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-PROC-001, SASD-PROC-002, SASD-PROC-003, SASD-PROC-004, SASD-PROC-005, SASD-PROC-006, SASD-PROC-007]
---

# Index der Prozessanforderungen

Diese Datei wird aus den normativen Prozessdokumenten erzeugt und nicht manuell bearbeitet.

## Umfang

| Dokument | Anforderungen |
|---|---:|
| [Neues Projekt initialisieren](NEW-PROJECT.md) | 49 |
| [Projektklassifikation](PROJECT-CLASSIFICATION.md) | 42 |
| [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) | 35 |
| [Reviewprozess](REVIEW-PROCESS.md) | 44 |
| [Migration bestehender Projekte](LEGACY-MIGRATION.md) | 45 |
| [Releaseprozess](RELEASE-PROCESS.md) | 53 |
| [Projektarchivierung](PROJECT-ARCHIVAL.md) | 40 |

**Gesamt:** 308 Anforderungen

## Anforderungen

| ID | Anforderung | Quelle |
|---|---|---|
| SASD-PROC-REQ-001 | Jedes neue Projekt MUSS mit einem dokumentierten Projektauftrag oder Projektbrief beginnen. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-002 | Der Projektbrief MUSS Problem, Ziel, Zielgruppe, erwarteten Nutzen und verantwortliche Person benennen. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-003 | Nicht-Ziele MÜSSEN dokumentiert werden, wenn sie den Scope wirksam begrenzen. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-004 | Annahmen und ungeklärte Fragen MÜSSEN von bestätigten Fakten unterscheidbar sein. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-005 | Ein Projekt DARF NICHT allein mit einer Werkzeug- oder Technologieentscheidung begründet werden, wenn das zu lösende Problem unklar ist. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-006 | Der geplante Lebenszyklus MUSS mindestens als Experiment, befristetes Vorhaben oder langfristig gepflegtes Produkt benannt werden. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-007 | Vor der strukturellen Einrichtung MUSS die Projektklassifikation abgeschlossen oder vorläufig freigegeben sein. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-008 | Die Initialisierung MUSS die gewählte Qualitätsstufe und alle anwendbaren Profile übernehmen. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-009 | Die erwarteten Meilensteine MÜSSEN mindestens bis zu einem ersten überprüfbaren Ergebnis beschrieben werden. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-010 | Risiken, externe Abhängigkeiten und wesentliche Unsicherheiten SOLLTEN vor Beginn der Implementierung sichtbar sein. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-011 | Bei begrenzten Ressourcen MUSS der Scope reduziert werden, bevor unverzichtbare Qualitäts- oder Sicherheitsmaßnahmen entfallen. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-012 | Die Initialisierung SOLLTE eine Definition of Ready für den ersten Entwicklungsabschnitt enthalten. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-013 | Die initialen funktionalen Anforderungen MÜSSEN ausreichend konkret sein, um den ersten Meilenstein planen und prüfen zu können. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-014 | Nichtfunktionale Anforderungen MÜSSEN berücksichtigt werden, soweit Sicherheit, Daten, Leistung, Bedienbarkeit, Betrieb oder Wartung betroffen sind. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-015 | Jeder erste Meilenstein MUSS überprüfbare Akzeptanzkriterien besitzen. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-016 | Anforderungen SOLLTEN priorisiert und auf ihren Ursprung zurückführbar sein. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-017 | Ungeklärte Anforderungen MÜSSEN als offene Punkte mit Verantwortlichem behandelt werden. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-018 | Die Initialisierung DARF NICHT vorgeben, dass sämtliche späteren Anforderungen bereits vollständig bekannt sein müssen. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-019 | Vor dem ersten wesentlichen Implementierungsschritt MUSS eine angemessene Architekturgrundlage vorhanden sein. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-020 | Wesentliche Technologieentscheidungen MÜSSEN begründet und bei langfristiger Wirkung als ADR erfasst werden. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-021 | Die Projektstruktur MUSS zur klassifizierten Größe passen und DARF NICHT vorsorglich unnötige Schichten oder Projekte erzeugen. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-022 | Externe Dienste, Datenbanken, Dateiformate und Integrationen MÜSSEN in einer ersten Systemkontextsicht sichtbar sein. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-023 | Persistente Daten MÜSSEN hinsichtlich Speicherort, Schemaentwicklung, Sicherung und Löschung vorläufig bewertet werden. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-024 | Bekannte technische Schulden, die bewusst zum Start akzeptiert werden, MÜSSEN dokumentiert und terminiert werden. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-025 | Das Repository MUSS einen eindeutigen Namen, eine Lizenzentscheidung und eine verständliche README-Grundlage besitzen. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-026 | Quellcode, Tests, Dokumentation und erzeugte Artefakte MÜSSEN nachvollziehbar getrennt werden. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-027 | Secrets, lokale Nutzerdaten und nicht veröffentlichbare Artefakte DÜRFEN NICHT in die Versionsverwaltung aufgenommen werden. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-028 | Die benötigten Entwicklungswerkzeuge und Versionen MÜSSEN dokumentiert oder maschinenlesbar festgelegt werden. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-029 | Ein frischer Checkout SOLLTE mit dokumentierten Schritten gebaut und getestet werden können. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-030 | Die Initialisierung MUSS mindestens einen erfolgreichen Baseline-Build oder eine begründete offene Build-Aufgabe enthalten. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-031 | Repository-Metadaten, Branching und Commit-Konventionen SOLLTEN vor der parallelen Zusammenarbeit festgelegt werden. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-032 | Die Initialisierung MUSS eine zur Qualitätsstufe passende Teststrategie oder einen kompakten Testabschnitt enthalten. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-033 | Kritische Annahmen und risikoreiche Komponenten SOLLTEN früh durch Spikes, Prototypen oder Tests validiert werden. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-034 | Die Sicherheitsbaseline MUSS vor der Verarbeitung sensibler Daten oder Zugangsdaten angewendet werden. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-035 | Abhängigkeiten MÜSSEN aus nachvollziehbaren Quellen bezogen und in ihrer Funktion begründet werden. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-036 | Die Definition of Done MUSS für den ersten Meilenstein festgelegt sein. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-037 | Geplante manuelle Prüfungen MÜSSEN so beschrieben sein, dass sie reproduzierbar durchgeführt werden können. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-038 | Für verteilte oder betriebene Projekte MUSS das vorgesehene Deployment- und Updateverfahren beschrieben werden. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-039 | Die Speicherorte für Konfiguration, Logs, Nutzerdaten und Backups MÜSSEN vor dem ersten produktionsnahen Einsatz festgelegt werden. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-040 | Der verantwortliche Wartungs- und Supportweg MUSS benannt werden. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-041 | Ein langfristig gepflegtes Projekt SOLLTE eine Roadmap und einen Änderungsprozess besitzen. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-042 | Production-Projekte MÜSSEN bereits bei der Initialisierung Wiederherstellung, Rollback und Betriebsübergabe berücksichtigen. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-043 | Ein Projekt ohne realistische Pflegeperspektive MUSS diesen Umstand und die daraus entstehenden Grenzen offen dokumentieren. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-044 | Der Start der regulären Implementierung MUSS durch ein dokumentiertes Readiness Gate bestätigt werden. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-045 | Das Readiness Gate MUSS offene Blocker von akzeptierten Restunsicherheiten unterscheiden. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-046 | Blockierende Sicherheits-, Lizenz- oder Zugangsfragen MÜSSEN vor Freigabe gelöst oder formell eskaliert sein. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-047 | Bei Einzelentwicklung MUSS ein zeitlich getrennter Selbstreview der Initialisierungsartefakte erfolgen. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-048 | Die Freigabe MUSS benennen, welcher Meilenstein als Nächstes umgesetzt und woran sein Erfolg erkannt wird. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-049 | Änderungen nach dem Readiness Gate MÜSSEN kontrolliert in Anforderungen, Entscheidungen oder Planung zurückgeführt werden. | [Neues Projekt initialisieren](NEW-PROJECT.md) |
| SASD-PROC-REQ-100 | Jedes neue oder wesentlich veränderte Projekt MUSS vor der Umsetzungsfreigabe klassifiziert werden. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-101 | Die Klassifikation MUSS Projektgröße, Qualitätsstufe, Risikomerkmale und anwendbare Profile getrennt ausweisen. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-102 | Die Teamgröße DARF NICHT allein über die erforderliche Qualitätsstufe entscheiden. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-103 | Ein kleines Projekt mit hoher Kritikalität MUSS strengere Maßnahmen erhalten können als ein großes, risikoarmes Lernprojekt. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-104 | Die Klassifikation MUSS auf nachvollziehbaren Fakten und ausdrücklich gekennzeichneten Annahmen beruhen. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-105 | Unbekannte risikorelevante Eigenschaften SOLLTEN als offene Klärung dokumentiert und nicht stillschweigend als unkritisch bewertet werden. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-106 | Die strukturelle Projektgröße MUSS mindestens als Small, Medium oder Large erfasst werden. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-107 | Die Größenbewertung SOLLTE Umfang, Komponentenanzahl, Integrationen, Datenmodell, Betriebsaufwand und erwartete Änderungsrate berücksichtigen. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-108 | Die erwartete Lebensdauer MUSS als Experiment, befristetes Vorhaben oder langfristig gepflegtes Produkt dokumentiert werden. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-109 | Ein Prototyp, der produktiv weiterverwendet wird, MUSS neu klassifiziert werden. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-110 | Projektgröße KANN die Artefakttiefe beeinflussen, DARF aber Sicherheits- oder Betriebsrisiken nicht herabstufen. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-111 | SASD Recommended SOLLTE die Standardauswahl für langfristig gepflegte oder öffentlich bereitgestellte Projekte sein. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-112 | SASD Minimum DARF NICHT gewählt werden, wenn die reduzierte Tiefe mit Zweck, Risiko, Lebensdauer oder Verteilung unvereinbar ist. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-113 | SASD Production MUSS geprüft werden, wenn externe Nutzer, kritische Geschäftsabläufe, sensible Daten oder verbindliche Betriebszusagen betroffen sind. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-114 | Die gewählte Qualitätsstufe MUSS mit einer kurzen Begründung dokumentiert werden. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-115 | Bei konkurrierenden Kriterien MUSS die strengere angemessene Qualitätsstufe gewählt oder eine dokumentierte Ausnahme beschlossen werden. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-116 | Eine Herabstufung der Qualitätsstufe MUSS begründet, genehmigt und auf ihre Risiken geprüft werden. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-117 | Eine höhere Qualitätsstufe KANN freiwillig gewählt werden, ohne dass das Projekt seine Größenklassifikation ändert. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-118 | Die Klassifikation MUSS mindestens Datenvertraulichkeit, Datenintegrität, Verfügbarkeit und Wiederherstellbarkeit bewerten. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-119 | Die Klassifikation MUSS externe Erreichbarkeit, Verteilung an Dritte und privilegierte Systemzugriffe erfassen. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-120 | Die Klassifikation MUSS rechtliche, regulatorische, vertragliche und lizenzbezogene Anforderungen berücksichtigen. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-121 | Abhängigkeiten von einzelnen Personen, externen Diensten oder nicht reproduzierbaren Umgebungen MÜSSEN als Kontinuitätsrisiken erfasst werden. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-122 | Mögliche Auswirkungen fehlerhafter Ergebnisse auf Menschen, Finanzen, Betrieb oder Reputation MÜSSEN bewertet werden. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-123 | Der Einsatz von Kryptographie, Zugangsdaten oder personenbezogenen Daten MUSS als gesondertes Risikomerkmal dokumentiert werden. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-124 | KI-generierte oder KI-gestützte Ergebnisse MÜSSEN bei sicherheits-, rechts- oder geschäftskritischen Entscheidungen als Prüfbedarf berücksichtigt werden. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-125 | Der Core Standard MUSS für jedes klassifizierte SASD-Projekt als Ausgangsbasis ausgewählt werden. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-126 | Anwendbare Technologie- und Projektprofile MÜSSEN anhand der tatsächlich eingesetzten Technologien und Betriebsformen bestimmt werden. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-127 | Mehrere Profile KÖNNEN gleichzeitig gelten und MÜSSEN dann gemeinsam betrachtet werden. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-128 | Nicht anwendbare Profile SOLLTEN ausdrücklich ausgeschlossen werden, wenn ihre Anwendung sonst naheliegend wäre. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-129 | Profilkonflikte MÜSSEN nach der im Qualitätsstufenmodell definierten Vorrangregel aufgelöst werden. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-130 | Die Klassifikation MUSS den erwarteten Dokumentationsumfang und die zulässige Zusammenlegung von Artefakten festlegen. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-131 | Für Small-Projekte KÖNNEN Projektbrief, Scope, Risiken und Architekturübersicht in einem kompakten Dokument zusammengeführt werden. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-132 | Recommended-Projekte SOLLTEN Anforderungen, Architektur, Teststrategie, Roadmap und Wartung nachvollziehbar trennen oder eindeutig gliedern. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-133 | Production-Projekte MÜSSEN sicherheits-, release-, betriebs- und wiederherstellungsrelevante Nachweise separat prüfbar halten. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-134 | Die Zusammenlegung von Dokumenten DARF NICHT dazu führen, dass Verantwortlichkeiten oder Entscheidungen unauffindbar werden. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-135 | Das Klassifikationsergebnis MUSS vor der Projektinitialisierung oder Migration freigegeben werden. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-136 | Bei Einzelentwicklung MUSS die Freigabe mindestens durch einen zeitlich getrennten strukturierten Selbstreview erfolgen. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-137 | Die Klassifikation MUSS bei wesentlichen Scope-, Daten-, Betriebs-, Nutzer- oder Sicherheitsänderungen erneut geprüft werden. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-138 | Eine Neubewertung SOLLTE mindestens vor jedem Major Release und vor dem Übergang in produktiven Betrieb erfolgen. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-139 | Änderungen der Klassifikation MÜSSEN mit Datum, Anlass und Auswirkungen dokumentiert werden. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-140 | Offene Klassifikationsfragen MÜSSEN einen Verantwortlichen und einen Zieltermin erhalten. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-141 | Das Ergebnis MUSS so gespeichert werden, dass spätere Entscheidungen auf die damals bekannten Grundlagen zurückgeführt werden können. | [Projektklassifikation](PROJECT-CLASSIFICATION.md) |
| SASD-PROC-REQ-200 | Eine Entscheidung mit langfristiger, schwer reversibler oder projektübergreifender Wirkung MUSS als ADR geprüft werden. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-201 | Technologie-, Daten-, Integrations-, Sicherheits- und Deploymententscheidungen SOLLTEN als ADR erfasst werden, wenn mehrere tragfähige Alternativen bestehen. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-202 | Triviale lokale Implementierungsdetails SOLLTEN NICHT als ADR dokumentiert werden. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-203 | Ein ADR DARF NICHT verwendet werden, um fehlende Anforderungen oder unklare Verantwortlichkeiten zu verdecken. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-204 | Die Entscheidungstiefe MUSS dem Risiko und der erwarteten Lebensdauer entsprechen. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-205 | Jeder ADR MUSS eine repositoryweit eindeutige, stabile Kennung besitzen. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-206 | ADRs MÜSSEN mindestens die Zustände Proposed, Accepted, Rejected, Superseded und Deprecated unterstützen. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-207 | Der aktuelle Status und das Entscheidungsdatum MÜSSEN im ADR sichtbar sein. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-208 | Ein akzeptierter ADR DARF NICHT in seiner ursprünglichen Entscheidungsbegründung stillschweigend umgeschrieben werden. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-209 | Sachliche Korrekturen an akzeptierten ADRs MÜSSEN als solche kenntlich gemacht werden. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-210 | Eine abgelöste Entscheidung MUSS auf ihren Nachfolger verweisen. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-211 | Ein ADR MUSS Kontext, Entscheidungsproblem, gewählte Option und wesentliche Konsequenzen enthalten. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-212 | Relevante Alternativen MÜSSEN mit ihren wichtigsten Vor- und Nachteilen dargestellt werden. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-213 | Annahmen, Randbedingungen und nicht verhandelbare Vorgaben MÜSSEN von Präferenzen unterscheidbar sein. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-214 | Sicherheits-, Datenschutz-, Betriebs- und Wartungsauswirkungen MÜSSEN berücksichtigt werden, wenn sie betroffen sind. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-215 | Bewusste Nachteile und technische Schulden MÜSSEN im ADR ausdrücklich benannt werden. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-216 | Die Entscheidung MUSS so formuliert sein, dass ihre spätere Umsetzung und Prüfung möglich ist. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-217 | Der Autor MUSS vor der Entscheidung ausreichend Informationen für einen Vergleich der realistischen Optionen sammeln. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-218 | Zeitlich begrenzte Experimente KÖNNEN zur Validierung einer ADR-Option eingesetzt werden. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-219 | Bewertungskriterien SOLLTEN vor der endgültigen Auswahl festgelegt werden. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-220 | Bei Production-relevanten Sicherheits- oder Datenentscheidungen MUSS geeignete unabhängige Fachprüfung eingeholt werden. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-221 | KI KANN bei Recherche und Strukturierung unterstützen, DARF aber nicht als alleinige Entscheidungsinstanz oder Quelle verwendet werden. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-222 | Unsichere externe Fakten MÜSSEN auf Primärquellen oder reproduzierbare Tests zurückgeführt werden. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-223 | Ein ADR MUSS vor oder spätestens mit der ersten irreversiblen Umsetzung akzeptiert werden. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-224 | Die Freigabe MUSS zur Qualitätsstufe und zum Entscheidungsrisiko passen. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-225 | Bei Einzelentwicklung MUSS zwischen Erstellung und Akzeptanz ein strukturierter Selbstreview erfolgen. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-226 | Die Umsetzung SOLLTE auf den ADR verweisen, wenn der Zusammenhang sonst nicht auffindbar ist. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-227 | Offene Umsetzungsfolgen MÜSSEN als Aufgaben, Risiken oder Folgemaßnahmen nachverfolgt werden. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-228 | Ein akzeptierter ADR MUSS in einem ADR-Index oder einer gleichwertigen Navigation auffindbar sein. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-229 | Eine wesentlich geänderte Entscheidung MUSS durch einen neuen ADR dokumentiert werden. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-230 | Der neue ADR MUSS den ersetzten ADR und den Grund der Änderung nennen. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-231 | Ein ADR SOLLTE überprüft werden, wenn zentrale Annahmen, Technologie-Support oder Betriebsbedingungen entfallen. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-232 | Nicht mehr relevante ADRs KÖNNEN als Deprecated markiert werden, dürfen aber nicht ohne Archivnachweis verschwinden. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-233 | Die Historie abgelehnter Optionen SOLLTE erhalten bleiben, wenn sie spätere Wiederholungsdiskussionen verhindert. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-234 | Widersprüche zwischen gültigen ADRs MÜSSEN vor dem nächsten betroffenen Release aufgelöst werden. | [Prozess für Architekturentscheidungen](ARCHITECTURE-DECISION-PROCESS.md) |
| SASD-PROC-REQ-300 | Jedes Review MUSS Ziel, Gegenstand, Prüftiefe und Abschlusskriterien benennen. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-301 | Der Reviewumfang MUSS zur Qualitätsstufe, Änderungsgröße und zum Risiko passen. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-302 | Reviewer MÜSSEN Zugriff auf die für ihre Bewertung erforderlichen Artefakte und Kontextinformationen erhalten. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-303 | Ein Review DARF NICHT durch unnötig große Änderungspakete faktisch unprüfbar gemacht werden. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-304 | Große Änderungen SOLLTEN in logisch prüfbare Einheiten zerlegt werden. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-305 | Zeitkritische Reviews MÜSSEN verbleibende Prüflücken ausdrücklich dokumentieren. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-306 | Dokumente MÜSSEN auf Vollständigkeit, Widerspruchsfreiheit, Verständlichkeit und Aktualität geprüft werden. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-307 | Architekturreviews MÜSSEN Anforderungen, Abhängigkeiten, Risiken, Datenflüsse und Betriebsfolgen berücksichtigen. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-308 | Codereviews MÜSSEN Korrektheit, Wartbarkeit, Sicherheit und Testauswirkungen bewerten. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-309 | Securityreviews MÜSSEN von Personen mit angemessener Fachkenntnis durchgeführt oder unterstützt werden. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-310 | Release-Reviews MÜSSEN Nachweise statt nur Aussagen über Build, Tests und Artefakte prüfen. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-311 | Post-Incident-Reviews SOLLTEN Ursachen, beitragende Faktoren und systemische Verbesserungen betrachten, nicht Schuldzuweisungen. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-312 | Recommended-Projekte SOLLTEN für risikoreiche Änderungen einen zweiten menschlichen Reviewer einbeziehen. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-313 | Production-Projekte MÜSSEN für kritische Sicherheits-, Daten- oder Betriebsänderungen angemessene unabhängige Prüfung vorsehen. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-314 | Bei Einzelentwicklung MUSS ein strukturierter Selbstreview zeitlich oder kontextuell von der Erstellung getrennt werden. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-315 | Ein Selbstreview MUSS eine Checkliste oder eine gleichwertige systematische Prüfmethode verwenden. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-316 | KI-basierte Reviews KÖNNEN zusätzliche Hinweise liefern, DÜRFEN aber erforderliche menschliche Freigaben nicht ersetzen. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-317 | Der Autor DARF NICHT eigene offene Zweifel oder bekannte Schwachstellen aus dem Reviewkontext entfernen. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-318 | Reviewer MÜSSEN Anforderungen und Entscheidungen von persönlichen Stilpräferenzen unterscheiden. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-319 | Feststellungen MÜSSEN auf konkrete Stellen, Anforderungen, Risiken oder reproduzierbare Beobachtungen verweisen. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-320 | Automatisierte Prüfungen SOLLTEN vor dem manuellen Review ausgeführt werden, damit menschliche Aufmerksamkeit auf nicht automatisierbare Fragen gerichtet wird. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-321 | Der Review MUSS geänderte Dokumentation, Tests, Konfiguration und Betriebsfolgen gemeinsam mit dem Code berücksichtigen. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-322 | Unklare Anforderungen MÜSSEN als Klärungsbedarf und nicht als stillschweigende Reviewer-Annahme behandelt werden. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-323 | Sicherheitsrelevante Details DÜRFEN NICHT unnötig in öffentlichen Reviewkommentaren offengelegt werden. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-324 | Reviewer SOLLTEN zwischen verbindlichem Änderungsbedarf und optionaler Verbesserung unterscheiden. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-325 | Reviewfeststellungen MÜSSEN mindestens als Blocker, Major, Minor oder Observation klassifizierbar sein. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-326 | Ein Blocker MUSS vor Freigabe behoben oder formell eskaliert werden. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-327 | Major Findings MÜSSEN vor Freigabe behoben oder durch eine genehmigte Ausnahme abgedeckt sein. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-328 | Minor Findings KÖNNEN nachverfolgt werden, wenn ihr Risiko und ein Zieltermin dokumentiert sind. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-329 | Observations DÜRFEN NICHT als versteckte Pflichtanforderungen verwendet werden. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-330 | Die Schweregrade MÜSSEN nach Auswirkung und Eintrittswahrscheinlichkeit und nicht nach persönlicher Präferenz vergeben werden. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-331 | Jedes verbindliche Finding MUSS einen Status und einen Verantwortlichen erhalten. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-332 | Behobene Findings MÜSSEN durch erneute Prüfung oder nachvollziehbaren Nachweis geschlossen werden. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-333 | Das bloße Antworten auf einen Reviewkommentar DARF NICHT automatisch als Behebung gelten. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-334 | Abgelehnte Findings MÜSSEN mit einer sachlichen Begründung dokumentiert werden. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-335 | Wiederkehrende Findings SOLLTEN in Standards, Checklisten, Tests oder Tooling zurückgeführt werden. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-336 | Der Reviewabschluss MUSS offene Risiken, Ausnahmen und Nacharbeiten zusammenfassen. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-337 | Die Freigabe MUSS eindeutig erkennen lassen, wer was auf welcher Evidenzbasis genehmigt hat. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-338 | Reviewnachweise MÜSSEN zusammen mit dem betroffenen Änderungsstand auffindbar sein. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-339 | Vertrauliche Reviewartefakte MÜSSEN angemessen geschützt gespeichert werden. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-340 | Personenbezogene oder sensible Inhalte SOLLTEN in Reviewnachweisen auf das notwendige Maß begrenzt werden. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-341 | Produktionskritische Freigaben MÜSSEN gegen nachträgliche unbemerkte Änderung geschützt oder versioniert sein. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-342 | Reviewmetriken KÖNNEN zur Prozessverbesserung genutzt werden, DÜRFEN aber nicht zu oberflächlichen Mengenkennzahlen verzerren. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-343 | Der Reviewprozess SOLLTE regelmäßig auf unnötige Reibung und übersehene Risiken überprüft werden. | [Reviewprozess](REVIEW-PROCESS.md) |
| SASD-PROC-REQ-400 | Eine Legacy-Migration MUSS mit einer Bestandsaufnahme beginnen und DARF NICHT allein auf äußere Strukturänderungen reduziert werden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-401 | Das bestehende System MUSS vor wesentlichen Umbauten soweit möglich reproduzierbar gebaut, gestartet oder in seinem Ist-Verhalten dokumentiert werden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-402 | Bekannte Nutzerabläufe, Datenformate, Integrationen und Betriebsabhängigkeiten MÜSSEN vor ihrer Änderung erfasst werden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-403 | Die Migration MUSS die Erhaltung fachlich benötigten Verhaltens von bewussten Produktänderungen unterscheiden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-404 | Eine vollständige Neuentwicklung SOLLTE NICHT als Standardlösung gewählt werden, solange schrittweise Verbesserung realistisch und risikoärmer ist. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-405 | Unverständlicher oder ungetesteter Code MUSS als Risiko und nicht automatisch als entbehrlich behandelt werden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-406 | Das bestehende Projekt MUSS nach dem aktuellen SASD-Klassifikationsprozess bewertet werden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-407 | Das Assessment MUSS Build, Tests, Architektur, Dokumentation, Abhängigkeiten, Sicherheit, Daten, Releases und Wartbarkeit betrachten. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-408 | Abweichungen MÜSSEN nach Risiko, Nutzen, Aufwand und Abhängigkeiten priorisiert werden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-409 | Das Assessment MUSS zwischen Not Applicable, offener Lücke, genehmigter Ausnahme und bewusst späterer Verbesserung unterscheiden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-410 | Fehlende Informationen MÜSSEN als Unsicherheit mit Klärungsmaßnahme erfasst werden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-411 | Die geplante Zielstufe MUSS realistisch zum Projektzweck und zur Wartungsperspektive passen. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-412 | Vor strukturellen Großänderungen MUSS eine belastbare Sicherung oder ein wiederherstellbarer Versionsstand vorhanden sein. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-413 | Secrets und sensible Daten MÜSSEN aus dem Repository entfernt oder geschützt werden, bevor weitere Verteilung erfolgt. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-414 | Kritische Build- und Startprobleme SOLLTEN vor kosmetischen Standardisierungen behoben werden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-415 | Ein minimaler Charakterisierungstest oder dokumentierter manueller Baseline-Test MUSS für kritisches Verhalten geschaffen werden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-416 | Abhängigkeiten mit bekannten kritischen Risiken MÜSSEN priorisiert behandelt werden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-417 | Datenmigrationen MÜSSEN vor ihrer Ausführung auf Sicherung und Rückweg geprüft werden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-418 | Die Migration MUSS in nachvollziehbare, möglichst reversible Wellen oder Meilensteine zerlegt werden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-419 | Jede Migrationswelle MUSS Ziel, Scope, Abhängigkeiten, Akzeptanzkriterien und Rückfalloption benennen. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-420 | Funktionale Änderungen SOLLTEN von reiner Struktur- und Standardmigration getrennt werden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-421 | Änderungen an öffentlichen Schnittstellen oder Datenformaten MÜSSEN mit Kompatibilitäts- und Migrationsstrategie geplant werden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-422 | Architekturentscheidungen mit langfristiger Wirkung MÜSSEN über ADRs dokumentiert werden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-423 | Der Plan MUSS Quick Wins von sicherheits- oder betriebsnotwendigen Maßnahmen unterscheiden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-424 | Nicht priorisierte Abweichungen MÜSSEN im Migrationsbacklog sichtbar bleiben. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-425 | Jede Migrationswelle MUSS einen prüfbaren Ausgangs- und Zielzustand besitzen. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-426 | Automatisierte oder manuelle Regressionstests MÜSSEN das relevante Bestandsverhalten absichern. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-427 | Die Repository-Struktur SOLLTE erst dann erweitert werden, wenn tatsächliche Verantwortungs- oder Abhängigkeitsgrenzen dies rechtfertigen. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-428 | Umbenennungen und Verschiebungen SOLLTEN getrennt von funktionalen Änderungen erfolgen, wenn dies Reviews erleichtert. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-429 | Neue Standards MÜSSEN auf neu oder wesentlich geänderten Code angewendet werden, soweit keine dokumentierte Übergangsregel besteht. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-430 | Technische Schulden DÜRFEN NICHT durch reine Dateiverschiebung als behoben ausgewiesen werden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-431 | Jede Welle MUSS dokumentieren, welche Abweichungen geschlossen, akzeptiert oder neu entdeckt wurden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-432 | Datenhaltende Legacy-Projekte MÜSSEN Datenmodell, Speicherorte, Migrationen, Backup und Wiederherstellung vor Änderungen dokumentieren. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-433 | Deployment- oder Installationsänderungen MÜSSEN in einer repräsentativen Umgebung getestet werden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-434 | Betriebsrelevante Logs, Diagnosewege und Fehlerbilder SOLLTEN während der Migration verbessert werden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-435 | Externe Integrationen MÜSSEN auf Verträge, Versionen, Authentisierung und Fehlerverhalten geprüft werden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-436 | Ein Parallelbetrieb KANN verwendet werden, wenn er Risiken reduziert und Datenkonsistenz kontrolliert werden kann. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-437 | Abschaltungen alter Komponenten MÜSSEN erst nach verifizierter Übernahme ihrer benötigten Funktionen erfolgen. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-438 | Jede Migrationswelle MUSS vor ihrer Übernahme in den Hauptstand reviewt werden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-439 | Production-relevante Wellen MÜSSEN eine Release-, Rollback- und Betriebsfreigabe erhalten. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-440 | Das Gesamtprojekt MUSS nach Abschluss erneut gegen Zielstufe und Profile bewertet werden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-441 | Verbleibende Ausnahmen und Schulden MÜSSEN mit Verantwortlichen und Zielterminen dokumentiert sein. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-442 | Lessons Learned SOLLTEN in Standards, Templates oder Projektwissen zurückgeführt werden. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-443 | Die Migration DARF NICHT als abgeschlossen gelten, solange Build, Tests, Dokumentation oder Betrieb nur im Wissen einer Person reproduzierbar sind. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-444 | Ein Abschlussbericht MUSS erreichte Ziele, offene Punkte und den neuen Wartungsbaseline-Stand zusammenfassen. | [Migration bestehender Projekte](LEGACY-MIGRATION.md) |
| SASD-PROC-REQ-500 | Jedes veröffentlichte Release MUSS eine eindeutige Version oder anderweitig eindeutige Releasekennung besitzen. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-501 | Der Release-Scope MUSS die enthaltenen Änderungen, behobenen Fehler und bekannten Einschränkungen benennen. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-502 | Änderungen außerhalb des freigegebenen Scopes DÜRFEN NICHT unbemerkt in das Release aufgenommen werden. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-503 | Releaseart und erwartete Kompatibilitätswirkung MÜSSEN vor der Freigabe festgelegt werden. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-504 | Ein Hotfix MUSS auf den kleinsten vertretbaren Scope begrenzt werden. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-505 | Interne Builds MÜSSEN von freigegebenen Releases unterscheidbar sein. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-506 | Der zu veröffentlichende Commit oder Artefaktstand MUSS eindeutig festgelegt und unverändert prüfbar sein. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-507 | Alle anwendbaren Releasekriterien MÜSSEN vor der Freigabe gegen diesen Stand geprüft werden. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-508 | Blockierende Issues MÜSSEN geschlossen, verschoben oder formell eskaliert sein. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-509 | Bekannte Risiken und Ausnahmen MÜSSEN in der Releaseentscheidung sichtbar sein. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-510 | Die Dokumentation MUSS zum veröffentlichten Funktions- und Konfigurationsstand passen. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-511 | Das Changelog MUSS die für Nutzer und Maintainer relevanten Änderungen enthalten. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-512 | Migrations- oder Upgradehinweise MÜSSEN vor der Veröffentlichung verfügbar sein, wenn Nutzermaßnahmen erforderlich sind. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-513 | Releaseartefakte MÜSSEN durch einen dokumentierten oder automatisierten Buildprozess erzeugt werden. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-514 | Der Build MUSS aus einem sauberen Checkout oder einer gleichwertig kontrollierten Umgebung reproduzierbar angestoßen werden können. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-515 | Releaseartefakte DÜRFEN NICHT manuell nach dem geprüften Build verändert werden. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-516 | Artefaktnamen MÜSSEN Produkt, Version und gegebenenfalls Plattform eindeutig erkennen lassen. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-517 | Prüfsummen SOLLTEN für herunterladbare Releaseartefakte bereitgestellt werden. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-518 | Production-Artefakte MÜSSEN angemessen signiert oder auf andere Weise gegen unbemerkte Manipulation geschützt werden, soweit die Plattform dies unterstützt. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-519 | Debug-Symbole und Diagnoseartefakte MÜSSEN gemäß Schutz- und Supportbedarf getrennt behandelt werden. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-520 | Alle für das Release vorgeschriebenen automatisierten Tests MÜSSEN erfolgreich sein. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-521 | Manuelle Smoke- oder Abnahmetests MÜSSEN für die unterstützten Hauptszenarien durchgeführt werden. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-522 | Fehlgeschlagene oder übersprungene Tests MÜSSEN vor Freigabe bewertet und dokumentiert werden. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-523 | Regressionen mit hoher Auswirkung MÜSSEN die Freigabe blockieren. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-524 | Unterstützte Plattformen, Installationswege und Upgradepfade MÜSSEN entsprechend der Qualitätsstufe geprüft werden. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-525 | Performance- oder Lasttests MÜSSEN durchgeführt werden, wenn das Release leistungsrelevante Risiken verändert. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-526 | Die Releaseprüfung SOLLTE die Definition of Done und nicht nur den erfolgreichen Build berücksichtigen. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-527 | Offene kritische Sicherheitsbefunde MÜSSEN die Veröffentlichung blockieren, sofern keine ausdrücklich genehmigte Notfallausnahme besteht. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-528 | Abhängigkeiten MÜSSEN auf bekannte relevante Schwachstellen und unerwartete Änderungen geprüft werden. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-529 | Secrets und vertrauliche Testdaten DÜRFEN NICHT in Releaseartefakten, Logs oder Metadaten enthalten sein. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-530 | Lizenz- und Herkunftsanforderungen für enthaltene Drittkomponenten MÜSSEN erfüllt sein. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-531 | Sicherheitsrelevante Änderungen MÜSSEN in angemessener Weise kommuniziert werden, ohne ausnutzbare Details unnötig vorzeitig offenzulegen. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-532 | Release-Zugangsdaten und Signierschlüssel MÜSSEN geschützt und auf notwendige Rollen begrenzt sein. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-533 | Daten- oder Schemaänderungen MÜSSEN mit getesteter Migrationsstrategie veröffentlicht werden. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-534 | Vor irreversiblen Migrationen MUSS eine geprüfte Sicherungs- oder Wiederherstellungsoption bestehen. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-535 | Rollbackfähigkeit und ihre Grenzen MÜSSEN vor Freigabe dokumentiert werden. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-536 | Ein Release DARF NICHT als rückrollbar bezeichnet werden, wenn Datenänderungen den Rückweg verhindern. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-537 | Kompatibilitätsgrenzen zwischen alten und neuen Versionen MÜSSEN dokumentiert werden. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-538 | Production-Releases MÜSSEN einen Abbruch- oder Rollback-Entscheidungspunkt für die Einführung besitzen. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-539 | Die Releasefreigabe MUSS durch eine benannte verantwortliche Rolle erfolgen. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-540 | Der Freigabeverantwortliche MUSS Zugriff auf die relevanten Prüf- und Risikonachweise besitzen. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-541 | Bei Einzelentwicklung MUSS ein zeitlich getrennter Release-Selbstreview dokumentiert werden. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-542 | Der Release-Tag MUSS auf den freigegebenen Quellstand zeigen. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-543 | Release Notes, Artefakte und Prüfsummen MÜSSEN konsistent dieselbe Version bezeichnen. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-544 | Veröffentlichungskanäle MÜSSEN gegen versehentliche oder unautorisierte Releases geschützt werden. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-545 | Ein Production-Release SOLLTE nach dem Vier-Augen-Prinzip freigegeben werden, soweit realistisch verfügbar. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-546 | Nach der Veröffentlichung MUSS geprüft werden, ob Artefakte erreichbar, installierbar und unverändert sind. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-547 | Betriebene Releases MÜSSEN auf unmittelbare Fehlerindikatoren und kritische Nutzerprobleme überwacht werden. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-548 | Ein fehlgeschlagenes Release MUSS nach dem vorbereiteten Rollback-, Stop- oder Hotfixverfahren behandelt werden. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-549 | Releasebezogene Vorfälle MÜSSEN mit Ursache, Auswirkung und Folgemaßnahmen dokumentiert werden. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-550 | Die tatsächlich veröffentlichte Version MUSS in Roadmap, Changelog oder Releasehistorie nachvollziehbar sein. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-551 | Wiederkehrende Releaseprobleme SOLLTEN in Automatisierung, Checklisten oder Standardregeln zurückgeführt werden. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-552 | Veraltete oder unsichere Releases SOLLTEN mit Supportstatus und empfohlenem Nachfolger gekennzeichnet werden. | [Releaseprozess](RELEASE-PROCESS.md) |
| SASD-PROC-REQ-600 | Die Stilllegung eines gepflegten Projekts MUSS als ausdrückliche Entscheidung dokumentiert werden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-601 | Der Archivierungsgrund MUSS zwischen Abschluss, Ablösung, fehlender Wartbarkeit, Sicherheitsrisiko und Aufgabe des Nutzens unterscheiden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-602 | Betroffene Nutzer, Betreiber und abhängige Projekte MÜSSEN vor der Stilllegung identifiziert werden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-603 | Eine Archivierung DARF NICHT als Ersatz für die Behandlung weiterhin bestehender rechtlicher oder sicherheitsbezogener Pflichten verwendet werden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-604 | Das Zieldatum und der verantwortliche Eigentümer der Archivierung MÜSSEN festgelegt werden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-605 | Aktive Nutzer MÜSSEN angemessen über Ende, Supportstatus und Alternativen informiert werden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-606 | Abhängige Systeme, Automatisierungen und Dokumente MÜSSEN auf verbleibende Verweise geprüft werden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-607 | Ein Nachfolgeprojekt MUSS eindeutig verlinkt werden, sofern es existiert. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-608 | Nicht ersetzte Funktionen oder Datenzugänge MÜSSEN als verbleibendes Risiko dokumentiert werden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-609 | Externe Veröffentlichungen SOLLTEN mit einem klaren Archivierungs- oder End-of-Life-Hinweis versehen werden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-610 | Projekt- und Nutzerdaten MÜSSEN nach dokumentierten Aufbewahrungs-, Export- und Löschregeln behandelt werden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-611 | Vor der Löschung benötigter Daten MUSS ihre erfolgreiche Übernahme oder ein genehmigter Verzicht bestätigt werden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-612 | Backups MÜSSEN entsprechend Schutzbedarf, Aufbewahrungsfrist und späterer Wiederherstellbarkeit behandelt werden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-613 | Personenbezogene oder vertrauliche Daten DÜRFEN NICHT allein wegen einer Repository-Archivierung unbegrenzt aufbewahrt werden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-614 | Datenformate und benötigte Lesewerkzeuge SOLLTEN dokumentiert werden, wenn spätere Auskunft oder Wiederherstellung erforderlich sein kann. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-615 | Kryptographische Schlüssel für archivierte Daten MÜSSEN entweder sicher weiterverwahrt oder die Daten kontrolliert unbrauchbar gemacht werden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-616 | Nicht mehr benötigte Dienste, Jobs, Domains, Tokens und Zugangsdaten MÜSSEN kontrolliert deaktiviert oder widerrufen werden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-617 | Cloud-, Hosting- und Drittanbieterkosten SOLLTEN nach erfolgreicher Stilllegung beendet werden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-618 | Gemeinsam genutzte Infrastruktur DARF NICHT durch unkoordinierte Archivierung beeinträchtigt werden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-619 | Monitoring und Alerts MÜSSEN angepasst werden, damit weder blinde Flecken noch dauerhafte Fehlalarme entstehen. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-620 | Verbleibende öffentliche Endpunkte MÜSSEN entfernt, umgeleitet oder mit sicherem End-of-Life-Verhalten versehen werden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-621 | Signier-, Deployment- und Administrationsrechte MÜSSEN nach dem Prinzip minimaler verbleibender Berechtigung reduziert werden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-622 | Das Repository MUSS einen abschließenden Statushinweis mit Archivierungsdatum, Grund und Supportstatus erhalten. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-623 | Der letzte unterstützte Stand MUSS durch Tag oder gleichwertige unveränderliche Referenz auffindbar sein. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-624 | Build-, Installations-, Daten- und Wiederherstellungsinformationen MÜSSEN soweit erforderlich für spätere Nachvollziehbarkeit erhalten bleiben. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-625 | Offene Sicherheitsprobleme MÜSSEN vor öffentlicher Archivierung bewertet und angemessen kommuniziert oder vertraulich behandelt werden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-626 | Issues und Roadmap MÜSSEN so geschlossen oder gekennzeichnet werden, dass keine fortgesetzte aktive Pflege suggeriert wird. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-627 | Wichtige Entscheidungen und Lessons Learned SOLLTEN vor der Archivierung in dauerhafte Wissensartefakte überführt werden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-628 | Nicht reproduzierbare Binärartefakte SOLLTEN zusammen mit Herkunft, Version und Prüfsumme archiviert werden, wenn sie für Wiederherstellung benötigt werden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-629 | Es MUSS festgelegt werden, ob das Projekt dauerhaft beendet oder grundsätzlich reaktivierbar ist. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-630 | Für reaktivierbare Production-Projekte MUSS ein minimaler Wiederherstellungsweg dokumentiert und geschützt aufbewahrt werden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-631 | Voraussetzungen für eine Wiederaufnahme MÜSSEN benannt werden, einschließlich Eigentümer, Daten, Zugänge und Toolchain. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-632 | Eine spätere Reaktivierung MUSS eine neue Klassifikation und Sicherheitsbewertung auslösen. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-633 | Archivierte Abhängigkeiten DÜRFEN NICHT ungeprüft als weiterhin sicher oder unterstützt angenommen werden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-634 | Die Archivierung MUSS mit einer Checkliste oder einem gleichwertigen Abschlussnachweis dokumentiert werden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-635 | Nach Abschaltung MUSS geprüft werden, ob öffentliche Endpunkte, Kosten, Jobs und Zugänge tatsächlich beendet sind. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-636 | Verbleibende Aufbewahrungs- und Löschtermine MÜSSEN Verantwortliche und Fälligkeit besitzen. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-637 | Production-Archivierungen MÜSSEN eine unabhängige Prüfung der Daten- und Zugangsbehandlung erhalten. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-638 | Die Abschlussentscheidung MUSS verbleibende Risiken und nicht erfüllte Punkte ausdrücklich benennen. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
| SASD-PROC-REQ-639 | Das Projekt DARF NICHT als archiviert gelten, bevor Repository, Daten, Infrastruktur, Nutzerkommunikation und Wissen konsistent behandelt wurden. | [Projektarchivierung](PROJECT-ARCHIVAL.md) |
