---
title: "Core-Anforderungsindex"
document-id: SASD-REF-005
document-type: informative
status: Draft
version: 0.1.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core]
depends-on: [SASD-CORE-001, SASD-CORE-002, SASD-CORE-003, SASD-CORE-004, SASD-CORE-005, SASD-CORE-006, SASD-CORE-007, SASD-CORE-008, SASD-CORE-009, SASD-CORE-010, SASD-CORE-011, SASD-CORE-012, SASD-CORE-013]
normative-keywords: []
generated: true
---

# Core-Anforderungsindex

> Automatisch erzeugtes, nicht normatives Navigationsdokument. Änderungen erfolgen in den Quelldokumenten und anschließend über `python tooling/generate-core-requirements-index.py`.

Der Index enthält **545** Core-Anforderungen.

## [Quality Levels](QUALITY-LEVELS.md)

| ID | Anforderung |
|---|---|
| `SASD-QL-001` | Jedes Projekt MUSS genau eine primäre Qualitätsstufe benennen. |
| `SASD-QL-002` | Die gewählte Qualitätsstufe MUSS im README oder in einer eindeutig verlinkten Compliance-Datei dokumentiert sein. |
| `SASD-QL-003` | Die Auswahl MUSS anhand von Projektrisiko, geplanter Lebensdauer, Nutzerkreis, Datenarten, Betriebsrelevanz und Änderungswahrscheinlichkeit begründet werden. |
| `SASD-QL-004` | Ein Projekt DARF NICHT allein deshalb eine niedrigere Qualitätsstufe wählen, weil Anforderungen noch nicht umgesetzt wurden. Fehlende Umsetzung MUSS als Lücke, technische Schuld oder Abweichung dokumentiert werden. |
| `SASD-QL-005` | Änderungen der Qualitätsstufe MÜSSEN mit Datum, Begründung und Auswirkungen auf offene Maßnahmen dokumentiert werden. |
| `SASD-QL-006` | Ein Projekt MUSS mindestens die Sicherheitsanforderungen von SASD Production anwenden, wenn ein Fehler voraussichtlich erhebliche Schäden an Vertraulichkeit, Integrität, Verfügbarkeit, Gesundheit, Finanzen oder gesetzlichen Rechten verursachen kann. |
| `SASD-QL-007` | Ein Projekt, das reale Zugangsdaten, personenbezogene Daten, Zahlungsdaten oder produktive Systeme verarbeitet, MUSS die betreffenden Bereiche mindestens auf Production-Niveau behandeln. |
| `SASD-QL-008` | Ein öffentlich betriebener Dienst SOLLTE als SASD Production klassifiziert werden. Eine niedrigere Einstufung benötigt eine dokumentierte Risikobegründung. |
| `SASD-QL-009` | Ein Prototyp mit realen produktiven Daten DARF NICHT allein wegen seines experimentellen Charakters als risikolos behandelt werden. |
| `SASD-QL-010` | Ein Projekt KANN einzelne Bereiche wie Sicherheit, Tests, Dokumentation oder Betrieb auf eine höhere Stufe anheben. |
| `SASD-QL-011` | Bereichsweise Anhebungen MÜSSEN in der Compliance-Erklärung benannt werden. |
| `SASD-QL-012` | Abhängige Anforderungen MÜSSEN gemeinsam betrachtet werden. Eine Production-Sicherheitsstufe ohne angemessene Test- und Wartungsnachweise ist nicht ausreichend. |
| `SASD-QL-013` | Eine Anforderung MUSS für alle in ihren Dokumentmetadaten genannten Qualitätsstufen angewendet werden, sofern ihr Wortlaut oder eine Qualitätsstufenmatrix die Anwendbarkeit nicht ausdrücklich einschränkt oder skaliert. |
| `SASD-QL-014` | Bedingungen wie „bei Verteilung“, „bei Betrieb“, „soweit anwendbar“ oder „wenn sensible Daten verarbeitet werden“ MÜSSEN anhand der tatsächlichen Projekteigenschaften bewertet werden. |
| `SASD-QL-015` | Eine dokumenteigene Qualitätsstufenmatrix KANN den Verbindlichkeitsgrad einer beschriebenen Maßnahme für eine konkrete Stufe präzisieren. Für diese Maßnahme und Stufe MUSS die Matrix gegenüber einer allgemeineren Formulierung desselben Dokuments vorrangig angewendet werden. |
| `SASD-QL-016` | Eine MUSS- oder DARF-NICHT-Anforderung ohne einschränkende Bedingung oder abweichende Qualitätsstufenregel gilt für Minimum, Recommended und Production. |
| `SASD-QL-017` | Eine als nicht anwendbar bewertete MUSS- oder DARF-NICHT-Anforderung MUSS mit einer kurzen, überprüfbaren Begründung in der Compliance-Bewertung gekennzeichnet werden. |
| `SASD-QL-018` | Eine SOLLTE- oder SOLLTE-NICHT-Anforderung, der ein Projekt nicht folgt, SOLLTE mit der fachlichen Begründung dokumentiert werden, wenn die Abweichung Sicherheit, Wartbarkeit, Reproduzierbarkeit oder Nachweisführung beeinflusst. |
| `SASD-QL-019` | Nachweise MÜSSEN dem Risiko, der Projektgröße und der Qualitätsstufe angemessen sein. Ein kleineres Projekt DARF denselben Inhalt kompakter dokumentieren, aber nicht ersatzlos weglassen. |
| `SASD-QL-020` | Für eine höhere Qualitätsstufe MÜSSEN alle anwendbaren Anforderungen niedrigerer Stufen übernommen werden, sofern keine ausdrücklich strengere oder anders ausgestaltete Regel für die höhere Stufe besteht. |
| `SASD-QL-021` | Profile KÖNNEN Core-Anforderungen konkretisieren oder verschärfen, DÜRFEN sie jedoch nicht stillschweigend abschwächen. |
| `SASD-QL-022` | Gesetzliche, vertragliche, regulatorische und projektspezifisch freigegebene strengere Anforderungen MÜSSEN gegenüber einer weniger strengen SASD-Regel vorrangig angewendet werden. |
| `SASD-QL-023` | Ein erkannter normativer Konflikt MUSS nach den Vorrangregeln der Inhaltsarchitektur bewertet und bis zur Klärung als offene Standard- oder Projektabweichung dokumentiert werden. |
| `SASD-QL-024` | Eine Person KANN mehrere oder alle Projektrollen übernehmen. Die Zusammenlegung von Rollen hebt keine fachliche Prüfung, Freigabe oder Nachweispflicht auf. |
| `SASD-QL-025` | Wo kein unabhängiger Reviewer verfügbar ist, MUSS eine geforderte Prüfung als strukturierte Selbstprüfung durchgeführt und nachvollziehbar dokumentiert werden, sofern die betreffende Anforderung nicht ausdrücklich eine personelle Trennung verlangt. |
| `SASD-QL-026` | Bei hohem oder kritischem Risiko SOLLTE trotz Einzelentwicklung eine unabhängige fachliche, sicherheitsbezogene oder rechtliche Prüfung eingeholt werden. |

## [Project Lifecycle](PROJECT-LIFECYCLE.md)

| ID | Anforderung |
|---|---|
| `SASD-LC-001` | Jedes Projekt MUSS einen benannten Projektverantwortlichen besitzen. |
| `SASD-LC-002` | Zweck, Scope, Qualitätsstufe, Status und nächster geplanter Meilenstein MÜSSEN auffindbar dokumentiert sein. |
| `SASD-LC-003` | Phasen dürfen iterativ bearbeitet werden; wesentliche Entscheidungen und Freigaben MÜSSEN dennoch nachvollziehbar bleiben. |
| `SASD-LC-004` | Ein Projekt MUSS offene Risiken, bekannte Einschränkungen und wesentliche technische Schulden sichtbar führen. |
| `SASD-LC-005` | Ein Projekt DARF NICHT veröffentlicht oder produktiv eingesetzt werden, wenn bekannte nicht akzeptierte Risiken den vorgesehenen Einsatz unvertretbar machen. |
| `SASD-LC-010` | Das zu lösende Problem, die erwartete Zielgruppe und der beabsichtigte Nutzen MÜSSEN beschrieben werden. |
| `SASD-LC-011` | Scope und ausdrückliche Nicht-Ziele MÜSSEN mindestens kompakt dokumentiert werden. |
| `SASD-LC-012` | Die primäre Qualitätsstufe und anwendbare Profile MÜSSEN gewählt werden. |
| `SASD-LC-013` | Wesentliche Machbarkeits-, Rechts-, Sicherheits-, Datenschutz- und Betriebsrisiken SOLLTEN vor der Umsetzungsentscheidung identifiziert werden. |
| `SASD-LC-014` | Doppelentwicklungen und bestehende geeignete Lösungen SOLLTEN geprüft werden, wenn die Recherche im Verhältnis zum Projektwert sinnvoll ist. |
| `SASD-LC-020` | Anforderungen MÜSSEN so weit geklärt sein, dass der nächste Meilenstein prüfbar geplant werden kann. |
| `SASD-LC-021` | Annahmen, Unsicherheiten und offene Fragen MÜSSEN von bestätigten Anforderungen unterscheidbar sein. |
| `SASD-LC-022` | Akzeptanzkriterien MÜSSEN für wesentliche Funktionen und Qualitätsziele festgelegt werden. |
| `SASD-LC-023` | Vor Beginn eines Meilensteins MUSS erkennbar sein, welche Anforderungen für diesen Meilenstein priorisiert sind; die Priorisierung richtet sich nach dem Anforderungsstandard. |
| `SASD-LC-024` | Änderungen am Scope MÜSSEN hinsichtlich Aufwand, Architektur, Sicherheit, Tests, Dokumentation und Terminplanung bewertet werden. |
| `SASD-LC-030` | Das Projekt MUSS in nachvollziehbare Meilensteine oder Lieferabschnitte gegliedert werden. |
| `SASD-LC-031` | Die Architektur MUSS für die gewählte Qualitätsstufe ausreichend dokumentiert sein. |
| `SASD-LC-032` | Wesentliche technische Entscheidungen MÜSSEN mit Kontext und Begründung festgehalten werden. |
| `SASD-LC-033` | Abhängigkeiten, externe Dienste, Datenflüsse und Betriebsannahmen SOLLTEN vor der Implementierung risikoreicher Teile geklärt werden. |
| `SASD-LC-034` | Für wesentliche Risiken SOLLTEN Prototypen oder technische Spikes verwendet werden, bevor große irreversible Investitionen erfolgen. |
| `SASD-LC-040` | Änderungen MÜSSEN auf nachvollziehbare Anforderungen, Fehler, Wartungsziele oder technische Entscheidungen zurückführbar sein. |
| `SASD-LC-041` | Implementierung, Tests und Dokumentation SOLLTEN innerhalb desselben Meilensteins gemeinsam gepflegt werden. |
| `SASD-LC-042` | Wiederholbare Prüfungen SOLLTEN automatisiert werden, sobald manueller Aufwand oder Fehlerrisiko dies rechtfertigen. |
| `SASD-LC-043` | Temporäre Umgehungen MÜSSEN als solche gekennzeichnet und mit einer Nachverfolgung versehen werden. |
| `SASD-LC-044` | Geheimnisse, produktive Zugangsdaten und unnötige personenbezogene Daten DÜRFEN NICHT in Quellcode, Tests oder Repository-Historie eingecheckt werden. |
| `SASD-LC-050` | Vor einem Release MUSS geprüft werden, ob die Akzeptanzkriterien des Lieferumfangs erfüllt sind. |
| `SASD-LC-051` | Bekannte Fehler und Einschränkungen MÜSSEN bewertet und für Nutzer oder Betreiber angemessen dokumentiert werden. |
| `SASD-LC-052` | Sicherheits-, Datenschutz-, Installations-, Upgrade- und Wiederherstellungsrisiken MÜSSEN entsprechend dem Projektkontext geprüft werden. |
| `SASD-LC-053` | Fehlgeschlagene Pflichtprüfungen DÜRFEN NICHT ohne dokumentierte Freigabe ignoriert werden. |
| `SASD-LC-054` | Die Definition of Done MUSS für den Releaseumfang erfüllt oder mit genehmigten Abweichungen versehen sein. |
| `SASD-LC-060` | Ein Release MUSS eindeutig versioniert oder anderweitig unverwechselbar identifizierbar sein. |
| `SASD-LC-061` | Release Notes oder ein Changelog MÜSSEN wesentliche Änderungen, bekannte Einschränkungen und notwendige Migrationsschritte nennen. |
| `SASD-LC-062` | Veröffentlichung und Deployment MÜSSEN für Recommended und Production nachvollziehbar reproduzierbar sein. |
| `SASD-LC-063` | Für Production MUSS ein Rollback-, Wiederherstellungs- oder anderweitiger Schadensbegrenzungsweg vor der Einführung festgelegt sein. |
| `SASD-LC-064` | Ein veröffentlichter Zustand MUSS den dokumentierten Freigabekriterien entsprechen. |
| `SASD-LC-070` | Verantwortlichkeit für Wartung, Sicherheitsupdates und Nutzerkommunikation MUSS geklärt sein. |
| `SASD-LC-071` | Fehler, Sicherheitsprobleme und Änderungswünsche MÜSSEN nach Risiko und Auswirkung priorisiert werden. |
| `SASD-LC-072` | Abhängigkeiten und Laufzeitumgebungen SOLLTEN regelmäßig auf Supportstatus und Risiken geprüft werden. |
| `SASD-LC-073` | Betriebs- und Wiederherstellungswissen MUSS in angemessenem Umfang dokumentiert werden. |
| `SASD-LC-074` | Lessons Learned SOLLTEN nach wesentlichen Releases oder Vorfällen in Projekt oder Standard zurückgeführt werden. |
| `SASD-LC-080` | Das Ende aktiver Wartung MUSS klar kommuniziert werden. |
| `SASD-LC-081` | Datenexport, Migration, Deinstallation und Aufbewahrung MÜSSEN entsprechend dem Projektkontext geregelt sein. |
| `SASD-LC-082` | Archivierte Repositories MÜSSEN Status, letzte unterstützte Version und bekannte Risiken sichtbar nennen. |
| `SASD-LC-083` | Geheimnisse und nicht benötigte sensible Daten MÜSSEN vor Archivierung entfernt oder sicher behandelt werden. |
| `SASD-LC-084` | Historische Releases und Entscheidungen SOLLTEN erhalten bleiben, soweit keine rechtlichen oder sicherheitsbezogenen Gründe dagegensprechen. |

## [Requirements](REQUIREMENTS.md)

| ID | Anforderung |
|---|---|
| `SASD-REQ-001` | Das zu lösende Problem MUSS verständlich beschrieben werden. |
| `SASD-REQ-002` | Der erwartete Nutzen MUSS von der geplanten technischen Lösung getrennt beschrieben werden. |
| `SASD-REQ-003` | Zielgruppen, Nutzer oder betroffene Stakeholder MÜSSEN benannt werden, soweit sie bekannt sind. |
| `SASD-REQ-004` | Erfolgsindikatoren oder überprüfbare Projektziele SOLLTEN definiert werden. |
| `SASD-REQ-010` | Der aktuelle Scope MUSS dokumentiert sein. |
| `SASD-REQ-011` | Wesentliche Nicht-Ziele MÜSSEN dokumentiert werden, wenn sonst Fehlannahmen oder Scope Creep wahrscheinlich sind. |
| `SASD-REQ-012` | Annahmen und offene Fragen MÜSSEN als solche gekennzeichnet sein. |
| `SASD-REQ-013` | Neue Anforderungen DÜRFEN NICHT stillschweigend in einen freigegebenen Meilenstein aufgenommen werden. Auswirkungen MÜSSEN bewertet werden. |
| `SASD-REQ-020` | Anforderungen MÜSSEN so formuliert sein, dass eine fachkundige Person erkennen kann, was erfüllt werden soll. |
| `SASD-REQ-021` | Wesentliche Qualitätsattribute wie Sicherheit, Wartbarkeit, Performance, Verfügbarkeit oder Bedienbarkeit MÜSSEN konkretisiert werden, wenn sie für den Projekterfolg relevant sind. |
| `SASD-REQ-022` | Lösungsdetails SOLLTEN nicht als fachliche Anforderungen formuliert werden, sofern keine echte technische Einschränkung besteht. |
| `SASD-REQ-023` | Widersprüchliche Anforderungen MÜSSEN aufgelöst oder ausdrücklich als offener Konflikt dokumentiert werden. |
| `SASD-REQ-030` | Für Recommended und Production MÜSSEN wesentliche Anforderungen eine stabile Kennung oder eine anderweitig eindeutige Referenz besitzen. |
| `SASD-REQ-031` | Der Status einer Anforderung MUSS unterscheidbar sein, beispielsweise Proposed, Accepted, Implemented, Verified, Rejected oder Deferred. |
| `SASD-REQ-032` | Quelle, Begründung oder verantwortlicher Stakeholder SOLLTE für risikoreiche oder umstrittene Anforderungen dokumentiert werden. |
| `SASD-REQ-033` | Gelöschte oder verworfene Anforderungen SOLLTEN nachvollziehbar bleiben, wenn ihre Historie spätere Entscheidungen erklärt. |
| `SASD-REQ-040` | Jede wesentliche Anforderung MUSS ein prüfbares Akzeptanzkriterium oder einen definierten Nachweis besitzen. |
| `SASD-REQ-041` | Akzeptanzkriterien MÜSSEN beobachtbares Verhalten oder messbare Eigenschaften beschreiben. |
| `SASD-REQ-042` | Reine Formulierungen wie „schnell“, „sicher“ oder „benutzerfreundlich“ DÜRFEN NICHT ohne Kontext oder Prüfkriterium als abschließende Anforderung verwendet werden. |
| `SASD-REQ-043` | Bei nicht vollständig automatisierbaren Kriterien MUSS die manuelle Prüfung beschrieben werden. |
| `SASD-REQ-050` | Anforderungen SOLLTEN priorisiert werden. |
| `SASD-REQ-051` | Priorität MUSS von Umsetzungsstatus und technischer Schwierigkeit unterscheidbar sein. |
| `SASD-REQ-052` | Sicherheits-, Datenintegritäts- und Wiederherstellungsanforderungen DÜRFEN NICHT allein wegen fehlender Sichtbarkeit für Endnutzer als niedrig priorisiert behandelt werden. |
| `SASD-REQ-053` | Ein Meilenstein MUSS einen klar abgegrenzten Anforderungssatz besitzen. |
| `SASD-REQ-060` | Für Recommended MUSS nachvollziehbar sein, welche Tests oder Abnahmen wesentliche Anforderungen verifizieren. |
| `SASD-REQ-061` | Für Production MUSS eine bidirektionale Nachverfolgbarkeit zwischen wesentlichen Anforderungen, Implementierungsartefakten, Risiken und Verifikationsnachweisen möglich sein. |
| `SASD-REQ-062` | Architekturentscheidungen, die Anforderungen wesentlich einschränken oder verändern, MÜSSEN referenziert werden. |
| `SASD-REQ-063` | Ein Test ohne erkennbaren Zweck SOLLTE ebenso vermieden werden wie eine wesentliche Anforderung ohne Nachweis. |
| `SASD-REQ-070` | Änderungen an freigegebenen Anforderungen MÜSSEN hinsichtlich Scope, Architektur, Sicherheit, Daten, Tests, Dokumentation, Migration und Betrieb bewertet werden. |
| `SASD-REQ-071` | Die Entscheidung über wesentliche Änderungen MUSS nachvollziehbar dokumentiert werden. |
| `SASD-REQ-072` | Veraltete Anforderungen MÜSSEN als ersetzt, verworfen oder nicht mehr anwendbar gekennzeichnet werden. |
| `SASD-REQ-073` | Änderungen DÜRFEN NICHT nachträglich so dokumentiert werden, als seien sie von Anfang an unverändert geplant gewesen. |

## [Architecture](ARCHITECTURE.md)

| ID | Anforderung |
|---|---|
| `SASD-ARCH-001` | Zweck, Systemgrenze, Nutzergruppen und wesentliche externe Systeme MÜSSEN erkennbar sein. |
| `SASD-ARCH-002` | Ein Systemkontext MUSS Ein- und Ausgaben, Datenquellen, Integrationen und Vertrauensgrenzen in angemessenem Umfang zeigen. |
| `SASD-ARCH-003` | Annahmen über Netzwerk, Identitäten, Dateisysteme, Laufzeitumgebungen oder externe Dienste SOLLTEN dokumentiert werden. |
| `SASD-ARCH-004` | Nicht zum Projekt gehörende Verantwortlichkeiten SOLLTEN ausdrücklich abgegrenzt werden, wenn Verwechslungen wahrscheinlich sind. |
| `SASD-ARCH-010` | Wesentliche Komponenten, Module oder Arbeitsbereiche MÜSSEN eine klar beschriebene Verantwortung besitzen. |
| `SASD-ARCH-011` | Eine Komponente SOLLTE einen kohärenten Zweck besitzen und nicht zu einer unkontrollierten Sammlung fachfremder Funktionen werden. |
| `SASD-ARCH-012` | Gemeinsam genutzte Funktionen MÜSSEN hinsichtlich Ownership, Stabilität und Abhängigkeiten betrachtet werden. |
| `SASD-ARCH-013` | Architekturgrenzen MÜSSEN im Code, in der Konfiguration oder in der Repository-Struktur soweit möglich erkennbar sein. |
| `SASD-ARCH-014` | Eine zusätzliche Schicht, ein Service oder ein Framework SOLLTE nur eingeführt werden, wenn der Nutzen die zusätzliche Komplexität rechtfertigt. |
| `SASD-ARCH-020` | Abhängigkeiten zwischen wesentlichen Komponenten MÜSSEN bekannt und nachvollziehbar sein. |
| `SASD-ARCH-021` | Zirkuläre Abhängigkeiten SOLLTEN vermieden werden. Unvermeidbare Zyklen MÜSSEN begründet und kontrolliert werden. |
| `SASD-ARCH-022` | Fachliche Kernlogik SOLLTE nicht unnötig an Benutzeroberfläche, konkrete Persistenz oder externe Dienste gekoppelt sein. |
| `SASD-ARCH-023` | Abhängigkeiten zu externen Produkten, APIs und Diensten MÜSSEN hinsichtlich Ausfall, Versionierung, Lizenz, Sicherheit und Austauschbarkeit bewertet werden. |
| `SASD-ARCH-024` | Nicht verwendete oder unbegründete Abhängigkeiten MÜSSEN entfernt werden. |
| `SASD-ARCH-030` | Wesentliche Datenobjekte, Zuständigkeiten, Speicherorte und Lebenszyklen MÜSSEN dokumentiert sein. |
| `SASD-ARCH-031` | Datenflüsse über Vertrauens- oder Systemgrenzen MÜSSEN identifizierbar sein. |
| `SASD-ARCH-032` | Integritäts-, Vertraulichkeits-, Aufbewahrungs- und Löschanforderungen MÜSSEN in Architekturentscheidungen berücksichtigt werden. |
| `SASD-ARCH-033` | Datenformate und Schnittstellen SOLLTEN versioniert oder migrationsfähig gestaltet sein, wenn sie längerfristig gespeichert oder extern genutzt werden. |
| `SASD-ARCH-034` | Versteckte globale Zustände und nicht dokumentierte Seiteneffekte SOLLTEN vermieden werden. |
| `SASD-ARCH-040` | Relevante Qualitätsattribute MÜSSEN priorisiert und durch Architekturmaßnahmen unterstützt werden. |
| `SASD-ARCH-041` | Zielkonflikte, beispielsweise zwischen Sicherheit, Bedienbarkeit, Performance und Einfachheit, MÜSSEN bei wesentlichen Entscheidungen dokumentiert werden. |
| `SASD-ARCH-042` | Architekturentscheidungen DÜRFEN NICHT ausschließlich auf hypothetische Skalierungs- oder Erweiterungsanforderungen gestützt werden. |
| `SASD-ARCH-043` | Für Production MÜSSEN Ausfallmodi, Wiederherstellung, Beobachtbarkeit und Kapazitätsgrenzen betrachtet werden. |
| `SASD-ARCH-044` | Barrierefreiheit und Internationalisierung SOLLTEN berücksichtigt werden, wenn Nutzeroberflächen oder öffentliche Inhalte entstehen. |
| `SASD-ARCH-050` | Vertrauensgrenzen, Identitäten, Berechtigungen und sensible Daten MÜSSEN in der Architektur berücksichtigt werden. |
| `SASD-ARCH-051` | Sicherheitskontrollen SOLLTEN möglichst nahe an der zu schützenden Grenze und zusätzlich durch übergreifende Schutzmaßnahmen umgesetzt werden. |
| `SASD-ARCH-052` | Sicherheitsrelevante Entscheidungen DÜRFEN NICHT allein auf Geheimhaltung der Architektur beruhen. |
| `SASD-ARCH-053` | Externe Eingaben MÜSSEN als nicht vertrauenswürdig behandelt werden, bis sie angemessen validiert wurden. |
| `SASD-ARCH-054` | Datenschutz durch Datenminimierung, Zweckbindung und begrenzte Aufbewahrung MUSS berücksichtigt werden, wenn personenbezogene Daten verarbeitet werden. |
| `SASD-ARCH-060` | Unterstützte Laufzeit- und Zielumgebungen MÜSSEN dokumentiert sein. |
| `SASD-ARCH-061` | Deployment-Einheiten, Konfigurationsquellen und externe Voraussetzungen MÜSSEN für Recommended und Production beschrieben werden. |
| `SASD-ARCH-062` | Konfiguration MUSS von Geheimnissen unterscheidbar und soweit sinnvoll von der Implementierung getrennt sein. |
| `SASD-ARCH-063` | Für Production MÜSSEN Überwachung, Diagnose, Backup und Wiederherstellung architektonisch berücksichtigt werden. |
| `SASD-ARCH-064` | Lokale Entwicklungs-, Test- und Produktivumgebungen SOLLTEN in relevanten Eigenschaften vergleichbar oder Unterschiede ausdrücklich dokumentiert sein. |
| `SASD-ARCH-070` | Wesentliche, schwer umkehrbare oder risikoreiche Architekturentscheidungen MÜSSEN als ADR oder gleichwertiger Entscheidungsnachweis dokumentiert werden. |
| `SASD-ARCH-071` | Ein Entscheidungsnachweis MUSS mindestens Kontext, Entscheidung, Alternativen und Konsequenzen enthalten. |
| `SASD-ARCH-072` | Ersetzte Entscheidungen MÜSSEN als superseded gekennzeichnet werden und auf ihre Nachfolge verweisen. |
| `SASD-ARCH-073` | Architekturentscheidungen DÜRFEN NICHT rückwirkend verfälscht werden. Neue Erkenntnisse werden durch neue oder aktualisierte Entscheidungen dokumentiert. |
| `SASD-ARCH-074` | Architektur und Implementierung MÜSSEN regelmäßig auf erkennbare Abweichungen geprüft werden. |
| `SASD-ARCH-080` | Bekannte Architekturabweichungen und technische Schulden MÜSSEN sichtbar und priorisierbar sein. |
| `SASD-ARCH-081` | Erweiterungspunkte SOLLTEN nur dort geschaffen werden, wo reale oder hinreichend wahrscheinliche Änderungen erwartet werden. |
| `SASD-ARCH-082` | Refactoring MUSS durch Tests oder andere angemessene Verifikationsmaßnahmen abgesichert werden. |
| `SASD-ARCH-083` | Ein Architekturwechsel MUSS Migration, Kompatibilität, Daten und Rückfallmöglichkeiten berücksichtigen. |

## [Documentation](DOCUMENTATION.md)

| ID | Anforderung |
|---|---|
| `SASD-DOC-001` | Jedes Projekt MUSS eine eindeutige Source of Truth für seine Dokumentation benennen. |
| `SASD-DOC-002` | Dokumentation SOLLTE gemeinsam mit dem Projekt versioniert werden, wenn sie den jeweiligen Projektstand beschreibt. |
| `SASD-DOC-003` | Parallel gepflegte, inhaltlich gleichwertige Fassungen DÜRFEN NICHT ohne festgelegten Synchronisationsprozess als gleichermaßen verbindlich gelten. |
| `SASD-DOC-004` | Erzeugte Word-, PDF-, HTML- oder andere Publikationen MÜSSEN als abgeleitete Artefakte erkennbar sein. |
| `SASD-DOC-005` | Geheimnisse, produktive Zugangsdaten und unnötige personenbezogene Daten DÜRFEN NICHT in Dokumentation oder Beispielen enthalten sein. |
| `SASD-DOC-010` | Das Root-README MUSS Zweck, Status, Einstieg, Nutzung oder Buildweg sowie weiterführende Dokumentation auffindbar machen. |
| `SASD-DOC-011` | Dokumente MÜSSEN über README, Dokumentationsindex oder nachvollziehbare Verzeichnisstruktur erreichbar sein. |
| `SASD-DOC-012` | Dateinamen SOLLTEN stabil, eindeutig und sprechend sein. |
| `SASD-DOC-013` | Relative Links SOLLTEN innerhalb des Repositories verwendet und automatisiert geprüft werden. |
| `SASD-DOC-014` | Veraltete Dokumente MÜSSEN als veraltet gekennzeichnet, aktualisiert oder archiviert werden. |
| `SASD-DOC-020` | Ein Dokument MUSS seinen Zweck und seine primäre Zielgruppe erkennen lassen. |
| `SASD-DOC-021` | Anweisungen MÜSSEN Voraussetzungen, Schritte und erwartete Ergebnisse enthalten, soweit dies für eine reproduzierbare Durchführung erforderlich ist. |
| `SASD-DOC-022` | Begriffe und Abkürzungen SOLLTEN konsistent verwendet und bei Bedarf im Glossar erklärt werden. |
| `SASD-DOC-023` | Beispiele MÜSSEN als Beispiele erkennbar sein und DÜRFEN NICHT unbeabsichtigt neue normative Regeln einführen. |
| `SASD-DOC-024` | Aussagen über unterstützte Versionen, Plattformen oder Betriebsbedingungen MÜSSEN überprüfbar und aktuell sein. |
| `SASD-DOC-030` | Dokumentation MUSS im selben Änderungsvorgang aktualisiert werden, wenn Verhalten, Konfiguration, Schnittstellen, Installation, Sicherheit oder Betrieb geändert werden. |
| `SASD-DOC-031` | Jedes wesentliche Dokument MUSS einen verantwortlichen Owner besitzen oder eindeutig einem Projektverantwortlichen zugeordnet sein. |
| `SASD-DOC-032` | Recommended- und Production-Projekte SOLLTEN Dokumentation zu Meilensteinen oder Releases systematisch prüfen. |
| `SASD-DOC-033` | Production-Dokumentation MUSS vor einem Release auf sicherheits-, betriebs- und migrationsrelevante Aktualität geprüft werden. |
| `SASD-DOC-034` | Bekannte Dokumentationslücken MÜSSEN nachverfolgbar sein. |
| `SASD-DOC-040` | Jedes Projekt MUSS mindestens README, Lizenzstatus, Qualitätsstufe, Build- oder Nutzungshinweise und bekannte wesentliche Einschränkungen dokumentieren. |
| `SASD-DOC-041` | Ein öffentlich verteiltes Projekt MUSS eine Lizenz oder einen ausdrücklichen Hinweis auf fehlende Nutzungsrechte enthalten. |
| `SASD-DOC-042` | Recommended- und Production-Projekte MÜSSEN Roadmap oder Wartungsstatus, Changelog oder Releasehistorie, Anforderungen, Architektur, Testansatz und Sicherheitskontakt oder Sicherheitsrichtlinie dokumentieren. |
| `SASD-DOC-043` | Production-Projekte MÜSSEN zusätzlich Betriebs-, Backup-, Wiederherstellungs-, Incident-, Migrations- und End-of-Life-Informationen bereitstellen, soweit anwendbar. |
| `SASD-DOC-044` | API-, Datenbank-, Deployment-, Benutzer- oder Administratorendokumentation MUSS vorhanden sein, wenn das Projekt entsprechende Schnittstellen, Datenstrukturen oder Betriebsaufgaben besitzt. |
| `SASD-DOC-050` | Öffentliche Schnittstellen und nicht offensichtliche Verträge SOLLTEN in technologiegeeigneter Form dokumentiert werden. |
| `SASD-DOC-051` | Kommentare SOLLTEN Gründe, Randbedingungen und nicht offensichtliche Konsequenzen erklären, nicht lediglich den Code wiederholen. |
| `SASD-DOC-052` | Temporäre Workarounds, Sicherheitsannahmen und Kompatibilitätsgrenzen MÜSSEN sichtbar und nachverfolgbar sein. |
| `SASD-DOC-053` | Konfigurationsoptionen MÜSSEN Bedeutung, erlaubte Werte, Standardverhalten und Sicherheitsauswirkungen erklären, wenn diese nicht offensichtlich sind. |
| `SASD-DOC-054` | Beispielkonfigurationen DÜRFEN NICHT so gestaltet sein, dass unsichere Werte unbeabsichtigt als empfohlener Produktivstandard erscheinen. |
| `SASD-DOC-060` | Bei mehreren Sprachfassungen MUSS die autoritative Fassung eindeutig benannt werden. |
| `SASD-DOC-061` | Übersetzungen MÜSSEN auf die Version der Ausgangsfassung verweisen. |
| `SASD-DOC-062` | Eine veraltete Übersetzung MUSS als solche erkennbar sein und DARF NICHT denselben Aktualitätsstatus vortäuschen. |
| `SASD-DOC-070` | Dokumente SOLLTEN mit klarer Überschriftenhierarchie, verständlichen Linktexten, beschrifteten Tabellen und Alternativtexten für informative Bilder erstellt werden. |
| `SASD-DOC-071` | Wesentliche Informationen DÜRFEN NICHT ausschließlich durch Farbe oder visuelle Position vermittelt werden. |
| `SASD-DOC-072` | Publikationsformate SOLLTEN Textsuche, Kopieren und maschinelle Verarbeitung ermöglichen, soweit dies praktisch möglich ist. |

## [Repository](REPOSITORY.md)

| ID | Anforderung |
|---|---|
| `SASD-REP-001` | Ein Repository MUSS einen eindeutigen, stabilen und verständlichen Namen besitzen. |
| `SASD-REP-002` | Beschreibung, Zweck, Status und primäre Technologie oder Projektart MÜSSEN im README oder in den Repository-Metadaten erkennbar sein. |
| `SASD-REP-003` | Ein öffentliches Repository MUSS Lizenz, Sicherheitskontakt und Wartungsstatus auffindbar machen. |
| `SASD-REP-004` | Forks, Mirrors, archivierte Kopien und kanonische Repositories MÜSSEN unterscheidbar sein. |
| `SASD-REP-005` | Der kanonische Standort eines Projekts MUSS benannt werden, wenn mehrere gleichartige Kopien existieren. |
| `SASD-REP-010` | Produktive Quellen, Tests, Dokumentation und erzeugte Artefakte MÜSSEN unterscheidbar sein. |
| `SASD-REP-011` | Repository-Struktur SOLLTE der Größe des Projekts entsprechen und DARF nicht allein aus formalen Gründen unnötig tief oder fragmentiert werden. |
| `SASD-REP-012` | Build- und Laufzeitausgaben MÜSSEN standardmäßig von der Versionskontrolle ausgeschlossen werden, sofern sie keine bewusst versionierten Releaseartefakte sind. |
| `SASD-REP-013` | Große Binärdateien SOLLTEN nur versioniert werden, wenn ihr Nutzen, ihre Herkunft und ihre Aktualisierung geregelt sind. |
| `SASD-REP-014` | Fremdmaterial MUSS hinsichtlich Lizenz, Herkunft und Integrität nachvollziehbar sein. |
| `SASD-REP-020` | Jedes Repository MUSS ein `README.md` oder eine gleichwertige Einstiegsdatei besitzen. |
| `SASD-REP-021` | Ein verteiltes oder öffentliches Projekt MUSS eine Lizenzdatei oder einen eindeutigen Rechtehinweis besitzen. |
| `SASD-REP-022` | Eine geeignete Ignore-Datei MUSS Buildausgaben, lokale Einstellungen, temporäre Dateien und Geheimnisse ausschließen. |
| `SASD-REP-023` | Recommended- und Production-Projekte MÜSSEN eine nachvollziehbare Änderungs- oder Releasehistorie führen. |
| `SASD-REP-024` | Sicherheitsrelevante Projekte und öffentliche Repositories SOLLTEN eine `SECURITY.md` oder gleichwertige Meldeanleitung besitzen. |
| `SASD-REP-025` | Projekte mit externen Beiträgen SOLLTEN `CONTRIBUTING.md`, Verhaltensregeln und Reviewhinweise bereitstellen. |
| `SASD-REP-030` | Ein Repository MUSS eine benannte kanonische Hauptlinie besitzen, üblicherweise `main`. |
| `SASD-REP-031` | Die Hauptlinie SOLLTE in einem buildbaren oder anderweitig konsistenten Zustand gehalten werden. |
| `SASD-REP-032` | Branch-Strategie MUSS zur Projektgröße passen. Ein komplexes Flow-Modell DARF nicht ohne erkennbaren Nutzen eingeführt werden. |
| `SASD-REP-033` | Kurzlebige Feature- oder Fix-Branches SOLLTEN zeitnah integriert oder geschlossen werden. |
| `SASD-REP-034` | Direkte Änderungen an geschützten Production-Repositories SOLLTEN durch Reviews und automatisierte Prüfungen kontrolliert werden. |
| `SASD-REP-040` | Commits MÜSSEN eine verständliche, handlungsorientierte Nachricht besitzen. |
| `SASD-REP-041` | Ein Commit SOLLTE eine kohärente Änderung darstellen und nicht unnötig unabhängige Themen vermischen. |
| `SASD-REP-042` | Geheimnisse und produktive Zugangsdaten DÜRFEN NICHT committed werden. Ein späteres Löschen ersetzt nicht die Rotation kompromittierter Zugangsdaten. |
| `SASD-REP-043` | Automatisch erzeugte Massenänderungen SOLLTEN von fachlichen Änderungen getrennt werden. |
| `SASD-REP-044` | Rewriting veröffentlichter Historie SOLLTE vermieden werden, wenn andere Nutzer oder Systeme darauf angewiesen sein können. |
| `SASD-REP-045` | Ein konsistentes Commit-Konventionsmodell, beispielsweise Conventional Commits, KANN verwendet werden und SOLLTE automatisiert geprüft werden, wenn Releases daraus abgeleitet werden. |
| `SASD-REP-050` | Änderungen mit hohem Risiko SOLLTEN über einen nachvollziehbaren Reviewprozess integriert werden. |
| `SASD-REP-051` | Pull Requests oder gleichwertige Änderungsnachweise SOLLTEN Zweck, Auswirkungen, Tests, Dokumentationsänderungen und offene Risiken benennen. |
| `SASD-REP-052` | Production-Änderungen an sicherheits-, daten- oder betriebsrelevanten Bereichen MÜSSEN geprüft oder durch eine dokumentierte strukturierte Selbstprüfung freigegeben werden. |
| `SASD-REP-053` | Fehlgeschlagene Pflichtprüfungen DÜRFEN NICHT ohne dokumentierte Ausnahme umgangen werden. |
| `SASD-REP-054` | Reviewkommentare und Entscheidungen SOLLTEN sachlich, begründet und auf das Projektziel bezogen sein. |
| `SASD-REP-060` | Offene Fehler, Risiken und geplante Arbeiten MÜSSEN in einem auffindbaren System nachverfolgbar sein. |
| `SASD-REP-061` | GitHub Issues, lokale Markdown-Dateien oder andere Systeme KÖNNEN verwendet werden, sofern die Source of Truth eindeutig ist. |
| `SASD-REP-062` | Kritische Sicherheitsprobleme DÜRFEN NICHT unnötig öffentlich offengelegt werden, bevor ein koordinierter Umgang möglich ist. |
| `SASD-REP-063` | Geschlossene oder verworfene Arbeiten SOLLTEN mit einer erkennbaren Entscheidung enden. |
| `SASD-REP-070` | Veröffentlichte Versionen MÜSSEN auf einen unveränderlichen Commit oder gleichwertigen Quellstand zurückführbar sein. |
| `SASD-REP-071` | Tags für Releases MÜSSEN eindeutig und konsistent benannt werden. |
| `SASD-REP-072` | Releaseartefakte MÜSSEN zur dokumentierten Version passen. |
| `SASD-REP-073` | Production-Artefakte SOLLTEN automatisiert aus dem freigegebenen Quellstand erzeugt werden. |
| `SASD-REP-074` | Prüfsummen, Signaturen oder Provenance-Nachweise SOLLTEN für extern verteilte oder sicherheitsrelevante Artefakte bereitgestellt werden. |
| `SASD-REP-080` | Repository-Beschreibung, Topics oder Tags und Website-Verweis SOLLTEN gepflegt werden. |
| `SASD-REP-081` | Branch Protection, Required Reviews und Required Checks SOLLTEN dem Risiko und der Teamgröße entsprechen. |
| `SASD-REP-082` | Automatisierte Abhängigkeits- und Sicherheitsmeldungen SOLLTEN aktiviert werden, wenn die Plattform sie anbietet und sie sinnvoll ausgewertet werden können. |
| `SASD-REP-083` | Workflow-Berechtigungen MÜSSEN nach dem Prinzip geringstmöglicher Rechte konfiguriert werden. |
| `SASD-REP-084` | Drittanbieter-Actions oder Plugins MÜSSEN hinsichtlich Herkunft, Berechtigungen und Versionierung geprüft werden. |
| `SASD-REP-090` | Ein archiviertes Repository MUSS seinen Status im README sichtbar machen. |
| `SASD-REP-091` | Letzte unterstützte Version, Nachfolgeprojekt und bekannte Sicherheitsrisiken SOLLTEN genannt werden. |
| `SASD-REP-092` | Vor Archivierung MÜSSEN offene Geheimnisse, aktive Tokens, Deployments und unnötige Automatisierungen deaktiviert oder entfernt werden. |
| `SASD-REP-093` | Historische Tags und Releases SOLLTEN erhalten bleiben, sofern keine Sicherheits- oder Rechtsgründe dagegensprechen. |

## [Quality](QUALITY.md)

| ID | Anforderung |
|---|---|
| `SASD-QUAL-001` | Relevante Qualitätsattribute MÜSSEN aus Anforderungen und Risiken abgeleitet werden. |
| `SASD-QUAL-002` | Qualitätsziele MÜSSEN soweit möglich beobachtbar oder prüfbar formuliert werden. |
| `SASD-QUAL-003` | Zielkonflikte MÜSSEN bei wesentlichen Entscheidungen dokumentiert werden. |
| `SASD-QUAL-004` | Ein Projekt DARF NICHT Qualitätsmaßnahmen allein nach leicht messbaren Kennzahlen ausrichten. Kennzahlen MÜSSEN dem Projektziel dienen. |
| `SASD-QUAL-010` | Recommended- und Production-Projekte MÜSSEN eine Definition of Done für Änderungen oder Meilensteine besitzen. |
| `SASD-QUAL-011` | Die Definition of Done MUSS mindestens Implementierung, Tests, Dokumentation, Sicherheitsauswirkungen, offene Risiken und Integrationsfähigkeit berücksichtigen. |
| `SASD-QUAL-012` | Eine Änderung DARF NICHT als abgeschlossen gelten, wenn bekannte Pflichtprüfungen ohne dokumentierte Ausnahme fehlschlagen. |
| `SASD-QUAL-013` | Für Minimum MUSS zumindest festgelegt sein, wann ein geplanter Lieferumfang als nutzbar und geprüft gilt. |
| `SASD-QUAL-020` | Projektartefakte MÜSSEN verständlich benannt und strukturiert sein. |
| `SASD-QUAL-021` | Unnötige Duplizierung SOLLTE vermieden werden; erzwungene Abstraktion ohne stabilen gemeinsamen Zweck SOLLTE ebenfalls vermieden werden. |
| `SASD-QUAL-022` | Komplexe oder nicht offensichtliche Logik MUSS durch Struktur, Benennung, Tests oder erklärende Dokumentation verständlich gemacht werden. |
| `SASD-QUAL-023` | Tote, nicht erreichbare oder nicht mehr verwendete Artefakte MÜSSEN entfernt oder ausdrücklich begründet werden. |
| `SASD-QUAL-024` | Öffentliche Verträge und Kompatibilitätsgrenzen MÜSSEN stabil oder klar versioniert sein. |
| `SASD-QUAL-030` | Build- oder Validierungswarnungen MÜSSEN bewertet werden und DÜRFEN NICHT dauerhaft unbegründet ignoriert werden. |
| `SASD-QUAL-031` | Formatierung und einfache Qualitätsregeln SOLLTEN automatisiert und repositoryweit konsistent angewendet werden. |
| `SASD-QUAL-032` | Recommended-Projekte SOLLTEN statische Analyse, Linting oder vergleichbare Prüfungen einsetzen. |
| `SASD-QUAL-033` | Production-Projekte MÜSSEN relevante automatisierbare Qualitäts- und Sicherheitsprüfungen in die Integrations- oder Releasepipeline einbinden. |
| `SASD-QUAL-034` | Unterdrückungen von Warnungen MÜSSEN lokal, begründet und so eng wie möglich sein. |
| `SASD-QUAL-035` | Qualitätsprüfungen DÜRFEN NICHT so konfiguriert werden, dass ein grüner Status durch pauschales Deaktivieren wesentlicher Regeln entsteht. |
| `SASD-QUAL-040` | Änderungen mit erhöhtem Risiko MÜSSEN einer strukturierten Prüfung unterzogen werden. |
| `SASD-QUAL-041` | Reviews MÜSSEN Anforderungen, Korrektheit, Verständlichkeit, Tests, Sicherheit, Dokumentation und Auswirkungen berücksichtigen. |
| `SASD-QUAL-042` | Einpersonenprojekte KÖNNEN Peer Review durch eine dokumentierte Selbstprüfung, zeitversetzte Prüfung oder geeignete Werkzeuge ergänzen. |
| `SASD-QUAL-043` | Reviewumfang MUSS risikobasiert sein; rein formale Freigaben ohne inhaltliche Prüfung sind nicht ausreichend. |
| `SASD-QUAL-044` | Findings MÜSSEN nach Risiko eingeordnet und entweder behoben, akzeptiert oder nachverfolgt werden. |
| `SASD-QUAL-050` | Bewusst eingegangene technische Schulden MÜSSEN mit Auswirkung, Begründung und geplanter Behandlung dokumentiert werden. |
| `SASD-QUAL-051` | Kritische technische Schulden DÜRFEN NICHT unbegrenzt ohne erneute Risikobewertung verschoben werden. |
| `SASD-QUAL-052` | TODO-, FIXME- oder ähnliche Markierungen SOLLTEN auf ein nachverfolgbares Arbeitselement verweisen, wenn sie nicht unmittelbar behoben werden. |
| `SASD-QUAL-053` | Refactoring SOLLTE kontinuierlich und in kontrollierten Schritten erfolgen. |
| `SASD-QUAL-054` | Refactoring MUSS durch angemessene Tests, Reviews oder Vergleichsnachweise abgesichert werden. |
| `SASD-QUAL-060` | Abhängigkeiten MÜSSEN einen erkennbaren Nutzen besitzen und aktiv gepflegt oder vertretbar stabil sein. |
| `SASD-QUAL-061` | Versionen und Kompatibilitätsgrenzen SOLLTEN reproduzierbar festgelegt werden. |
| `SASD-QUAL-062` | Veraltete, nicht unterstützte oder bekannte kritische Abhängigkeiten MÜSSEN bewertet und mit einem Maßnahmenplan versehen werden. |
| `SASD-QUAL-063` | Ein Upgrade MUSS hinsichtlich Verhalten, Daten, Sicherheit, Build, Tests und Deployment geprüft werden. |
| `SASD-QUAL-070` | Fehler MÜSSEN mit vertretbarem Aufwand diagnostizierbar sein. |
| `SASD-QUAL-071` | Relevante Fehlerzustände MÜSSEN verständlich protokolliert oder dem Nutzer angemessen angezeigt werden. |
| `SASD-QUAL-072` | Protokollierung DARF NICHT unnötig Geheimnisse oder personenbezogene Daten offenlegen. |
| `SASD-QUAL-073` | Production-Systeme MÜSSEN für kritische Betriebszustände geeignete Überwachungs- und Diagnosemöglichkeiten besitzen. |
| `SASD-QUAL-080` | Wiederkehrende Fehler und manuelle Problemstellen SOLLTEN als Verbesserungskandidaten behandelt werden. |
| `SASD-QUAL-081` | Nach wesentlichen Vorfällen, Releases oder Migrationen SOLLTEN Lessons Learned festgehalten werden. |
| `SASD-QUAL-082` | Qualitätsregeln MÜSSEN angepasst werden, wenn sie erkennbar keinen Nutzen liefern oder relevante Risiken nicht erfassen. |

## [Security](SECURITY.md)

| ID | Anforderung |
|---|---|
| `SASD-SEC-001` | Ein Projekt MUSS relevante Werte, Daten, Dienste und Vertrauensgrenzen identifizieren. |
| `SASD-SEC-002` | Vertraulichkeit, Integrität und Verfügbarkeit MÜSSEN für wesentliche Assets bewertet werden. |
| `SASD-SEC-003` | Recommended-Projekte MÜSSEN eine dokumentierte Sicherheitsrisikobetrachtung durchführen. |
| `SASD-SEC-004` | Production-Projekte MÜSSEN ein Bedrohungsmodell oder eine gleichwertige strukturierte Analyse pflegen. |
| `SASD-SEC-005` | Risiken MÜSSEN vermieden, reduziert, übertragen oder ausdrücklich akzeptiert werden. |
| `SASD-SEC-010` | Sicherheits- und Datenschutzanforderungen MÜSSEN als prüfbare Projektanforderungen behandelt werden. |
| `SASD-SEC-011` | Sicherheitsrelevante Architekturentscheidungen MÜSSEN dokumentiert werden. |
| `SASD-SEC-012` | Systeme MÜSSEN nach dem Prinzip geringstmöglicher Rechte entworfen und betrieben werden. |
| `SASD-SEC-013` | Sicherheitskontrollen DÜRFEN NICHT allein auf verborgenem Code, geheimen URLs oder unbekannten Dateipfaden beruhen. |
| `SASD-SEC-014` | Standardkonfigurationen SOLLTEN den sichersten praktikablen Zustand herstellen. |
| `SASD-SEC-020` | Identitäten MÜSSEN eindeutig und Berechtigungen nachvollziehbar sein, soweit das Projekt Authentifizierung oder Autorisierung benötigt. |
| `SASD-SEC-021` | Geteilte privilegierte Konten SOLLTEN vermieden werden. |
| `SASD-SEC-022` | Berechtigungen MÜSSEN regelmäßig und bei Rollenwechseln überprüft werden. |
| `SASD-SEC-023` | Authentifizierungsdaten DÜRFEN NICHT unverschlüsselt oder unnötig dauerhaft gespeichert werden. |
| `SASD-SEC-024` | Fehler- und Statusmeldungen DÜRFEN NICHT unnötig Informationen über Konten, Schlüssel oder interne Sicherheitsdetails preisgeben. |
| `SASD-SEC-030` | Geheimnisse DÜRFEN NICHT in Quellcode, Dokumentation, Tests, Logs oder Repository-Historie eingecheckt werden. |
| `SASD-SEC-031` | Geheimnisse MÜSSEN über geeignete Secret Stores, Umgebungsmechanismen oder geschützte Konfiguration bereitgestellt werden. |
| `SASD-SEC-032` | Zugriff auf Geheimnisse MUSS auf notwendige Personen, Prozesse und Umgebungen begrenzt sein. |
| `SASD-SEC-033` | Kompromittierte oder versehentlich veröffentlichte Geheimnisse MÜSSEN unverzüglich widerrufen oder rotiert werden. |
| `SASD-SEC-034` | Schlüsselrotation, Ablauf und Wiederherstellung SOLLTEN für langlebige oder produktive Systeme vorgesehen werden. |
| `SASD-SEC-035` | Beispielwerte MÜSSEN eindeutig nicht produktiv sein. |
| `SASD-SEC-040` | Externe Eingaben MÜSSEN entsprechend ihrem Kontext validiert werden. |
| `SASD-SEC-041` | Ausgaben MÜSSEN kontextgerecht kodiert oder geschützt werden, wenn sie in Interpreter, Abfragen, Shells, Markup oder andere ausführende Kontexte gelangen. |
| `SASD-SEC-042` | Datenmengen und Datentypen MÜSSEN auf den erforderlichen Zweck begrenzt werden. |
| `SASD-SEC-043` | Dateipfade, Uploads, Archive und Deserialisierung MÜSSEN gegen projektrelevante Missbrauchsfälle abgesichert werden. |
| `SASD-SEC-044` | Sicherheitsrelevante Validierung DARF NICHT ausschließlich in einer leicht umgehbaren Benutzerschnittstelle stattfinden. |
| `SASD-SEC-050` | Eigene kryptographische Algorithmen oder Protokolle DÜRFEN NICHT entwickelt werden, wenn etablierte und geeignete Verfahren verfügbar sind. |
| `SASD-SEC-051` | Kryptographische Verfahren MÜSSEN dem Schutzbedarf und aktuellen fachlichen Empfehlungen entsprechen. |
| `SASD-SEC-052` | Schlüssel, Nonces, Initialisierungsvektoren und Zufallswerte MÜSSEN mit geeigneten kryptographischen Mechanismen erzeugt und verwaltet werden. |
| `SASD-SEC-053` | Verschlüsselung DARF NICHT als Ersatz für Zugriffskontrolle, Datenminimierung oder sichere Schlüsselverwaltung betrachtet werden. |
| `SASD-SEC-054` | Passwörter MÜSSEN mit einem geeigneten passwortspezifischen Hashverfahren gespeichert werden, wenn das Projekt Passwörter selbst verwaltet. |
| `SASD-SEC-060` | Direkte Abhängigkeiten MÜSSEN identifizierbar und versionierbar sein. |
| `SASD-SEC-061` | Herkunft, Wartungsstatus, Lizenz und Sicherheitslage neuer kritischer Abhängigkeiten MÜSSEN bewertet werden. |
| `SASD-SEC-062` | Bekannte kritische Schwachstellen MÜSSEN zeitnah bewertet und behandelt werden. |
| `SASD-SEC-063` | Automatisierte Builds MÜSSEN kontrollierte Quellen und so wenig Berechtigungen wie möglich verwenden. |
| `SASD-SEC-064` | Externe Buildschritte, Plugins und CI-Actions MÜSSEN auf Herkunft, Berechtigungen und unveränderliche Versionierung geprüft werden. |
| `SASD-SEC-065` | Production-Projekte MÜSSEN eine Software Bill of Materials oder eine gleichwertige Komponentenübersicht für veröffentlichte Artefakte erzeugen, soweit technisch möglich. |
| `SASD-SEC-066` | Releaseartefakte SOLLTEN auf Quellstand und Buildprozess zurückführbar sein. |
| `SASD-SEC-070` | Personenbezogene Daten MÜSSEN ausschließlich für einen dokumentierten Zweck und in erforderlichem Umfang verarbeitet werden. |
| `SASD-SEC-071` | Aufbewahrungs- und Löschregeln MÜSSEN festgelegt werden, wenn personenbezogene oder vertrauliche Daten gespeichert werden. |
| `SASD-SEC-072` | Test- und Entwicklungsdaten SOLLTEN anonymisiert, synthetisch oder anderweitig geschützt sein. |
| `SASD-SEC-073` | Produktive Daten DÜRFEN NICHT ohne ausdrückliche Freigabe und Schutzmaßnahmen in Entwicklungs- oder KI-Systeme übertragen werden. |
| `SASD-SEC-074` | Nutzer MÜSSEN über relevante Datenverarbeitung informiert werden, soweit dies rechtlich oder funktional erforderlich ist. |
| `SASD-SEC-080` | Sicherheitsrelevante Ereignisse SOLLTEN in angemessenem Umfang protokolliert werden. |
| `SASD-SEC-081` | Logs DÜRFEN NICHT unnötig Geheimnisse, vollständige Zugangsdaten oder sensible Inhalte enthalten. |
| `SASD-SEC-082` | Zugriff, Aufbewahrung und Löschung von Logs MÜSSEN dem Schutzbedarf entsprechen. |
| `SASD-SEC-083` | Production-Systeme MÜSSEN kritische Sicherheits- und Verfügbarkeitsereignisse erkennbar machen. |
| `SASD-SEC-084` | Zeitstempel und Ereigniskontext SOLLTEN eine nachträgliche Untersuchung unterstützen. |
| `SASD-SEC-090` | Schutzwürdige oder nicht leicht reproduzierbare Daten MÜSSEN durch geeignete Backups oder Replikation abgesichert werden. |
| `SASD-SEC-091` | Backups MÜSSEN mindestens denselben angemessenen Schutz wie die Primärdaten erhalten. |
| `SASD-SEC-092` | Production-Wiederherstellungsverfahren MÜSSEN regelmäßig getestet werden. |
| `SASD-SEC-093` | Recovery-Ziele SOLLTEN für geschäfts- oder betriebsrelevante Systeme festgelegt werden. |
| `SASD-SEC-094` | Ein Backup DARF NICHT allein aufgrund seines erfolgreichen Erstellungsprotokolls als wiederherstellbar gelten. |
| `SASD-SEC-100` | Ein öffentlicher oder verteilter Dienst MUSS einen geeigneten Weg zur vertraulichen Meldung von Schwachstellen anbieten. |
| `SASD-SEC-101` | Sicherheitsmeldungen MÜSSEN nach Schwere, Ausnutzbarkeit und Auswirkung bewertet werden. |
| `SASD-SEC-102` | Production-Projekte MÜSSEN Verantwortlichkeiten und grundlegende Schritte für Sicherheitsvorfälle dokumentieren. |
| `SASD-SEC-103` | Behebung, Kommunikation, Rotation, Update und Lessons Learned MÜSSEN bei relevanten Vorfällen berücksichtigt werden. |
| `SASD-SEC-104` | Sicherheitsdetails DÜRFEN NICHT unnötig veröffentlicht werden, solange dies Betroffene zusätzlich gefährden würde. |

## [Testing](TESTING.md)

| ID | Anforderung |
|---|---|
| `SASD-TEST-001` | Jedes Projekt MUSS festlegen, wie die wesentlichen Anforderungen und Risiken verifiziert werden. |
| `SASD-TEST-002` | Recommended- und Production-Projekte MÜSSEN eine dokumentierte, risikobasierte Teststrategie besitzen. |
| `SASD-TEST-003` | Die Teststrategie MUSS Testziele, Testarten, Umgebungen, Verantwortlichkeiten, relevante Daten und Freigabekriterien benennen. |
| `SASD-TEST-004` | Testaufwand MUSS sich an Auswirkung und Eintrittswahrscheinlichkeit möglicher Fehler orientieren. |
| `SASD-TEST-005` | Code Coverage oder andere Kennzahlen DÜRFEN NICHT allein als Beweis ausreichender Qualität verwendet werden. |
| `SASD-TEST-010` | Kritische Geschäfts-, Daten- und Sicherheitslogik MUSS auf einer geeigneten Ebene geprüft werden. |
| `SASD-TEST-011` | Integrationen zu Datenbanken, Dateisystemen, Netzwerken, APIs oder externen Diensten MÜSSEN entsprechend ihrem Risiko getestet oder simuliert werden. |
| `SASD-TEST-012` | Öffentliche Schnittstellen SOLLTEN durch Vertrags- oder Kompatibilitätstests geschützt werden. |
| `SASD-TEST-013` | Production-Projekte MÜSSEN Installations-, Upgrade-, Migration- und Wiederherstellungswege prüfen, soweit anwendbar. |
| `SASD-TEST-014` | Sicherheitsrelevante Fehlbedienung und Missbrauchsfälle SOLLTEN ausdrücklich getestet werden. |
| `SASD-TEST-020` | Freigaberelevante Tests MÜSSEN auf eine Anforderung, ein Risiko, einen Fehler oder einen technischen Vertrag zurückführbar sein. |
| `SASD-TEST-021` | Wesentliche Anforderungen DÜRFEN NICHT ohne definierten Verifikationsweg als erfüllt markiert werden. |
| `SASD-TEST-022` | Für Production MUSS nachvollziehbar sein, welche Testnachweise den freigegebenen Lieferumfang abdecken. |
| `SASD-TEST-023` | Ein Regressionstest SOLLTE ergänzt werden, wenn ein Fehler mit vertretbarem Aufwand automatisiert reproduzierbar ist. |
| `SASD-TEST-030` | Automatisierte Tests MÜSSEN reproduzierbar ausführbar und ihre Voraussetzungen dokumentiert sein. |
| `SASD-TEST-031` | Tests SOLLTEN unabhängig voneinander und ohne unbeabsichtigte Reihenfolgeabhängigkeit ausführbar sein. |
| `SASD-TEST-032` | Wiederholbare Pflichtprüfungen SOLLTEN in CI oder einen gleichwertigen automatisierten Ablauf integriert werden. |
| `SASD-TEST-033` | Production-Releases MÜSSEN aus einem identifizierbaren Prüflauf mit nachvollziehbarer Konfiguration freigegeben werden. |
| `SASD-TEST-034` | Externe Dienste SOLLTEN in Tests kontrolliert ersetzt oder über dedizierte Testumgebungen angebunden werden. |
| `SASD-TEST-035` | Ein Test DARF NICHT unbemerkt produktive Daten, Dienste oder kostenpflichtige Ressourcen verändern. |
| `SASD-TEST-040` | Testdaten MÜSSEN für den jeweiligen Testzweck repräsentativ und kontrollierbar sein. |
| `SASD-TEST-041` | Produktive personenbezogene oder vertrauliche Daten DÜRFEN NICHT ohne ausdrückliche Freigabe und Schutzmaßnahmen als Testdaten verwendet werden. |
| `SASD-TEST-042` | Sensible Testdaten MÜSSEN geschützt, minimiert und nach der vorgesehenen Nutzung gelöscht werden. |
| `SASD-TEST-043` | Grenzwerte, ungültige Eingaben, leere Daten und relevante Fehlerfälle SOLLTEN berücksichtigt werden. |
| `SASD-TEST-044` | Zufallsbasierte Tests MÜSSEN bei Fehlern einen reproduzierbaren Seed oder gleichwertigen Wiederholungsweg liefern. |
| `SASD-TEST-050` | Unterschiede zwischen Test- und Zielumgebung MÜSSEN bekannt sein, wenn sie das Ergebnis beeinflussen können. |
| `SASD-TEST-051` | Production-Projekte SOLLTEN eine produktionsnahe Umgebung für kritische Integrations-, Deployment- und Migrationstests besitzen. |
| `SASD-TEST-052` | Testumgebungen MÜSSEN mit kontrollierter Konfiguration und angemessenen Berechtigungen betrieben werden. |
| `SASD-TEST-053` | Testartefakte und Umgebungen SOLLTEN nach Abschluss bereinigt werden, sofern sie nicht als Nachweis aufbewahrt werden. |
| `SASD-TEST-060` | Fehlgeschlagene Tests MÜSSEN untersucht und dürfen nicht pauschal erneut ausgeführt werden, bis zufällig ein grüner Lauf entsteht. |
| `SASD-TEST-061` | Flaky Tests MÜSSEN sichtbar gekennzeichnet, priorisiert und behoben oder kontrolliert quarantänisiert werden. |
| `SASD-TEST-062` | Quarantänisierte Pflichtprüfungen MÜSSEN eine dokumentierte Risikoakzeptanz und Frist besitzen. |
| `SASD-TEST-063` | Fehlerberichte SOLLTEN Reproduktionsschritte, erwartetes und tatsächliches Verhalten, Umgebung und relevante Protokolle enthalten. |
| `SASD-TEST-064` | Kritische Defekte DÜRFEN NICHT ohne ausdrückliche Freigabe in ein Release übernommen werden. |
| `SASD-TEST-070` | Manuelle freigaberelevante Tests MÜSSEN mit Schritten, erwarteten Ergebnissen und Ergebnis dokumentiert werden. |
| `SASD-TEST-071` | Explorative Tests SOLLTEN Fokus, Beobachtungen und gefundene Risiken festhalten. |
| `SASD-TEST-072` | Benutzeroberflächen SOLLTEN auf Verständlichkeit, Fehlermeldungen, Tastaturbedienung und relevante Barrierefreiheit geprüft werden. |
| `SASD-TEST-073` | Ein manueller Test SOLLTE automatisiert werden, wenn er häufig wiederholt wird und zuverlässig automatisierbar ist. |
| `SASD-TEST-080` | Releasefreigaben MÜSSEN auf die relevanten Prüfergebnisse verweisen. |
| `SASD-TEST-081` | Testnachweise MÜSSEN Version, Zeitpunkt, Umgebung und Ergebnis erkennen lassen, wenn diese für die Bewertung notwendig sind. |
| `SASD-TEST-082` | Production-Projekte MÜSSEN freigaberelevante Nachweise für einen angemessenen Zeitraum aufbewahren. |
| `SASD-TEST-083` | Testberichte DÜRFEN NICHT sensible Daten oder Geheimnisse unnötig offenlegen. |

## [Releases](RELEASES.md)

| ID | Anforderung |
|---|---|
| `SASD-REL-001` | Jedes Release MUSS eindeutig identifizierbar und auf einen unveränderlichen Quellstand zurückführbar sein. |
| `SASD-REL-002` | Das Versionsschema MUSS dokumentiert und konsistent angewendet werden. |
| `SASD-REL-003` | Semantic Versioning SOLLTE verwendet werden, wenn das Projekt einen definierten öffentlichen Vertrag oder eine öffentliche API besitzt. |
| `SASD-REL-004` | Vorabversionen MÜSSEN als Alpha, Beta, Preview, Release Candidate oder gleichwertig erkennbar sein. |
| `SASD-REL-005` | Eine einmal veröffentlichte Versionsnummer DARF NICHT für inhaltlich veränderte Artefakte wiederverwendet werden. |
| `SASD-REL-010` | Der Umfang eines Releases MUSS vor der Freigabe erkennbar sein. |
| `SASD-REL-011` | Enthaltene Änderungen MÜSSEN auf Anforderungen, Fehler, Wartungsarbeiten oder technische Entscheidungen zurückführbar sein. |
| `SASD-REL-012` | Nicht abgeschlossene oder bewusst verschobene Inhalte MÜSSEN vom Releaseumfang unterscheidbar sein. |
| `SASD-REL-013` | Unbeabsichtigte Entwicklungs-, Test- oder Debugartefakte DÜRFEN NICHT im Release enthalten sein. |
| `SASD-REL-020` | Ein Release MUSS die für seine Qualitätsstufe geltende Definition of Done erfüllen. |
| `SASD-REL-021` | Pflichtbuilds, Tests, Dokumentations- und Sicherheitsprüfungen MÜSSEN erfolgreich sein oder eine genehmigte Ausnahme besitzen. |
| `SASD-REL-022` | Bekannte Defekte und Einschränkungen MÜSSEN hinsichtlich Auswirkung und Vertretbarkeit bewertet werden. |
| `SASD-REL-023` | Production-Releases MÜSSEN eine ausdrückliche, nachvollziehbare Freigabe besitzen. |
| `SASD-REL-024` | Ein Release DARF NICHT freigegeben werden, wenn erforderliche Migration, Backup oder Rückfallmaßnahmen ungeklärt sind. |
| `SASD-REL-030` | Jedes extern verteilte oder längerfristig genutzte Release MUSS Änderungen für Nutzer und Betreiber verständlich beschreiben. |
| `SASD-REL-031` | Breaking Changes, Sicherheitsänderungen, Migrationen, bekannte Probleme und erforderliche Handlungen MÜSSEN hervorgehoben werden. |
| `SASD-REL-032` | Ein Changelog SOLLTE einen Unreleased-Bereich und versionierte Einträge besitzen. |
| `SASD-REL-033` | Commit-Historie allein SOLLTE NICHT als nutzerorientierte Releasebeschreibung verwendet werden. |
| `SASD-REL-034` | Sicherheitsrelevante Details MÜSSEN so kommuniziert werden, dass Nutzer handeln können, ohne unnötig Missbrauch zu erleichtern. |
| `SASD-REL-040` | Recommended- und Production-Releases MÜSSEN aus dokumentierten Quellen und Schritten reproduzierbar erzeugbar sein. |
| `SASD-REL-041` | Buildwerkzeuge, Abhängigkeiten und relevante Konfiguration MÜSSEN versioniert oder anderweitig nachvollziehbar festgelegt sein. |
| `SASD-REL-042` | Production-Artefakte MÜSSEN automatisiert oder durch einen kontrollierten, protokollierten Prozess erzeugt werden. |
| `SASD-REL-043` | Releaseartefakte SOLLTEN Prüfsummen besitzen, wenn sie als Dateien verteilt werden. |
| `SASD-REL-044` | Signaturen oder Provenance-Nachweise SOLLTEN für sicherheitsrelevante oder extern verteilte Production-Artefakte verwendet werden. |
| `SASD-REL-045` | Der veröffentlichte Quellstand, die erzeugten Artefakte und Release Notes MÜSSEN dieselbe Version repräsentieren. |
| `SASD-REL-050` | Releaseabhängigkeiten MÜSSEN hinsichtlich bekannter kritischer Schwachstellen und Lizenzrisiken geprüft werden. |
| `SASD-REL-051` | Production-Releases MÜSSEN soweit technisch möglich eine SBOM oder gleichwertige Komponentenliste bereitstellen. |
| `SASD-REL-052` | Die SBOM MUSS zum veröffentlichten Artefakt und nicht nur zu einem beliebigen Entwicklungsstand passen. |
| `SASD-REL-053` | Drittanbieterartefakte MÜSSEN Herkunft und Version erkennen lassen. |
| `SASD-REL-060` | Änderungen an Daten, Konfigurationen, Schnittstellen oder Betriebsumgebungen MÜSSEN auf Migrationsbedarf geprüft werden. |
| `SASD-REL-061` | Notwendige Migrationsschritte MÜSSEN vor dem Release dokumentiert und entsprechend dem Risiko getestet werden. |
| `SASD-REL-062` | Breaking Changes MÜSSEN eindeutig gekennzeichnet werden. |
| `SASD-REL-063` | Datenmigrationen SOLLTEN idempotent, wiederaufnehmbar oder anderweitig gegen Teilfehler abgesichert sein. |
| `SASD-REL-064` | Ein Rückweg MUSS definiert sein, wenn eine Migration nicht sicher rückgängig gemacht werden kann. |
| `SASD-REL-070` | Deployment-Schritte MÜSSEN für Recommended und Production dokumentiert sein. |
| `SASD-REL-071` | Production-Releases MÜSSEN einen Rollback-, Recovery- oder Schadensbegrenzungsplan besitzen. |
| `SASD-REL-072` | Rollback-Pläne MÜSSEN Daten- und Schemaänderungen berücksichtigen. |
| `SASD-REL-073` | Kritische Releases SOLLTEN schrittweise, beobachtbar oder mit begrenztem Nutzerkreis eingeführt werden. |
| `SASD-REL-074` | Nach der Einführung MUSS geprüft werden, ob der erwartete Betriebszustand erreicht wurde. |
| `SASD-REL-080` | Offizielle Veröffentlichungsorte MÜSSEN benannt werden. |
| `SASD-REL-081` | Veraltete oder unsichere Releases MÜSSEN als solche gekennzeichnet oder zurückgezogen werden. |
| `SASD-REL-082` | Production-Releases und zugehörige Nachweise MÜSSEN für einen angemessenen Zeitraum aufbewahrt werden. |
| `SASD-REL-083` | Ein Release MUSS Supportstatus oder Wartungserwartung erkennen lassen, wenn mehrere Versionen parallel existieren. |

## [Maintenance](MAINTENANCE.md)

| ID | Anforderung |
|---|---|
| `SASD-MNT-001` | Jedes Projekt MUSS einen verantwortlichen Maintainer oder einen ausdrücklich unbetreuten Status besitzen. |
| `SASD-MNT-002` | Unterstützte Versionen, Plattformen und Laufzeitumgebungen MÜSSEN auffindbar dokumentiert sein. |
| `SASD-MNT-003` | Ein Projekt DARF NICHT den Eindruck aktiver Wartung erwecken, wenn keine Wartung mehr vorgesehen ist. |
| `SASD-MNT-004` | Production-Projekte MÜSSEN Vertretung, Übergabe oder Eskalationsweg für kritische Wartungsaufgaben berücksichtigen. |
| `SASD-MNT-010` | Nutzer MÜSSEN wissen, wie Fehler oder Sicherheitsprobleme gemeldet werden können, soweit das Projekt verteilt oder betrieben wird. |
| `SASD-MNT-011` | Fehler MÜSSEN nach Auswirkung, Dringlichkeit, Sicherheitsrelevanz und Reproduzierbarkeit priorisiert werden. |
| `SASD-MNT-012` | Supportzusagen DÜRFEN NICHT gemacht werden, wenn sie organisatorisch nicht erfüllbar sind. |
| `SASD-MNT-013` | Bekannte Workarounds SOLLTEN dokumentiert und als temporär oder dauerhaft erkennbar sein. |
| `SASD-MNT-020` | Abhängigkeiten und Zielplattformen MÜSSEN regelmäßig auf Supportstatus und relevante Sicherheitsprobleme geprüft werden. |
| `SASD-MNT-021` | Updatehäufigkeit MUSS Risiko, Änderungsrate und Betriebsrelevanz berücksichtigen. |
| `SASD-MNT-022` | Updates MÜSSEN vor produktiver Einführung angemessen getestet werden. |
| `SASD-MNT-023` | Automatische Updates DÜRFEN NICHT ohne geeignete Kontrolle, Rückfallmöglichkeit und Integritätsprüfung eingesetzt werden. |
| `SASD-MNT-024` | Nicht mehr unterstützte Laufzeiten oder Abhängigkeiten MÜSSEN einen Upgrade-, Ablöse- oder Risikoakzeptanzplan erhalten. |
| `SASD-MNT-030` | Unterstützte Konfigurationen MÜSSEN dokumentiert sein. |
| `SASD-MNT-031` | Production-Konfiguration SOLLTE versioniert, deklarativ oder anderweitig nachvollziehbar verwaltet werden. |
| `SASD-MNT-032` | Manuelle Änderungen an produktiven Umgebungen MÜSSEN dokumentiert und soweit möglich in die verwaltete Konfiguration zurückgeführt werden. |
| `SASD-MNT-033` | Konfigurationsdrift SOLLTE regelmäßig erkannt und bewertet werden. |
| `SASD-MNT-034` | Geheimnisse DÜRFEN NICHT als normale Konfigurationswerte exportiert, versioniert oder protokolliert werden. |
| `SASD-MNT-040` | Ein Projekt MUSS einen angemessenen Weg zur Diagnose typischer Fehler besitzen. |
| `SASD-MNT-041` | Recommended-Projekte SOLLTEN strukturierte Logs, Statusinformationen oder Diagnosepakete bereitstellen. |
| `SASD-MNT-042` | Production-Systeme MÜSSEN kritische Zustände überwachen und zuständige Personen oder Systeme informieren. |
| `SASD-MNT-043` | Diagnoseinformationen MÜSSEN Schutzbedarf und Datenschutz berücksichtigen. |
| `SASD-MNT-044` | Uhrzeit, Version, Umgebung und relevante Korrelation SOLLTEN in Diagnoseinformationen nachvollziehbar sein. |
| `SASD-MNT-050` | Nicht leicht reproduzierbare Daten und Konfigurationen MÜSSEN entsprechend ihrer Bedeutung gesichert werden. |
| `SASD-MNT-051` | Backupumfang, Häufigkeit, Aufbewahrung und Verantwortlichkeit MÜSSEN dokumentiert sein. |
| `SASD-MNT-052` | Production-Projekte MÜSSEN Recovery Point Objective und Recovery Time Objective oder gleichwertige Wiederherstellungsziele festlegen, wenn Ausfall oder Datenverlust erheblich wäre. |
| `SASD-MNT-053` | Wiederherstellungsverfahren MÜSSEN getestet werden; bei Production regelmäßig und nach wesentlichen Änderungen. |
| `SASD-MNT-054` | Backups MÜSSEN vor unberechtigtem Zugriff, Manipulation und unbeabsichtigtem Löschen geschützt werden. |
| `SASD-MNT-055` | Ein Backup MUSS unabhängig vom primären Ausfallpfad verfügbar sein, wenn sonst ein gemeinsamer Fehler beide Kopien gefährdet. |
| `SASD-MNT-060` | Migrationen MÜSSEN versioniert und auf den Zielstand zurückführbar sein. |
| `SASD-MNT-061` | Vor risikoreichen Migrationen MUSS ein validiertes Backup oder eine gleichwertige Recovery-Möglichkeit existieren. |
| `SASD-MNT-062` | Migrationen MÜSSEN auf Teilfehler, Wiederaufnahme und Kompatibilität geprüft werden. |
| `SASD-MNT-063` | Datenverlust oder irreversible Transformationen MÜSSEN ausdrücklich freigegeben und dokumentiert werden. |
| `SASD-MNT-064` | Nach der Migration MUSS Integrität anhand definierter Kriterien geprüft werden. |
| `SASD-MNT-070` | Kritische Vorfälle MÜSSEN stabilisiert, dokumentiert und hinsichtlich Ursache sowie Folgemaßnahmen bewertet werden. |
| `SASD-MNT-071` | Wiederkehrende Fehler SOLLTEN einer Ursachenanalyse statt ausschließlich wiederholter Symptombehandlung unterzogen werden. |
| `SASD-MNT-072` | Production-Projekte MÜSSEN einen grundlegenden Incident-Ablauf mit Rollen, Kommunikation und Eskalation besitzen. |
| `SASD-MNT-073` | Nach relevanten Vorfällen SOLLTEN Lessons Learned und vorbeugende Maßnahmen dokumentiert werden. |
| `SASD-MNT-080` | Die Ablösung von Funktionen, Schnittstellen oder Versionen MUSS rechtzeitig und verständlich kommuniziert werden. |
| `SASD-MNT-081` | Ein Deprecation-Hinweis MUSS Ersatz, Frist oder bekannte Migration nennen, soweit verfügbar. |
| `SASD-MNT-082` | End of Life MUSS letzten Supportstand, Sicherheitsfolgen und Nachfolgeoptionen nennen. |
| `SASD-MNT-083` | Datenexport und Migration SOLLTEN vor Abschaltung ermöglicht werden, wenn Nutzer eigene relevante Daten besitzen. |
| `SASD-MNT-084` | Nicht mehr benötigte Zugänge, Secrets, Deployments, Domains und Automatisierungen MÜSSEN kontrolliert deaktiviert werden. |
| `SASD-MNT-090` | Archivierte Projekte MÜSSEN Status, letzte Version, Lizenz und bekannte Einschränkungen sichtbar behalten. |
| `SASD-MNT-091` | Quellstand, Dokumentation und wesentliche Entscheidungen SOLLTEN gemeinsam archiviert werden. |
| `SASD-MNT-092` | Archivierung DARF NICHT als Ersatz für notwendige Datenlöschung oder Geheimnisrotation verwendet werden. |
| `SASD-MNT-093` | Historische Build- oder Laufzeitabhängigkeiten SOLLTEN dokumentiert werden, wenn spätere Reproduzierbarkeit wichtig ist. |

## [Knowledge Management](KNOWLEDGE-MANAGEMENT.md)

| ID | Anforderung |
|---|---|
| `SASD-KM-001` | Ein Projekt MUSS benennen, wo verbindliches Projektwissen gespeichert wird. |
| `SASD-KM-002` | Chats, E-Mails und persönliche Notizen DÜRFEN NICHT die einzige Quelle für wesentliche Anforderungen, Entscheidungen oder Betriebsabläufe sein. |
| `SASD-KM-003` | Relevantes Wissen aus flüchtigen Kommunikationskanälen MUSS zeitnah in die dauerhafte Projektdokumentation übertragen werden. |
| `SASD-KM-004` | Widersprüchliche Wissensquellen MÜSSEN aufgelöst oder hinsichtlich ihrer Autorität gekennzeichnet werden. |
| `SASD-KM-010` | Wesentliche technische Entscheidungen MÜSSEN mit Kontext, Entscheidung, Alternativen und Konsequenzen dokumentiert werden. |
| `SASD-KM-011` | ADRs oder gleichwertige Entscheidungsnachweise MÜSSEN stabil referenzierbar sein. |
| `SASD-KM-012` | Ersetzte Entscheidungen MÜSSEN erhalten und als superseded gekennzeichnet werden. |
| `SASD-KM-013` | Entscheidungen DÜRFEN NICHT nachträglich so verändert werden, dass ihr ursprünglicher Kontext verloren geht. |
| `SASD-KM-014` | Wiederkehrende Entscheidungsgründe SOLLTEN in Prinzipien, Guidelines oder Templates überführt werden. |
| `SASD-KM-020` | Wiederkehrende Betriebs-, Installations-, Diagnose- und Wiederherstellungsaufgaben MÜSSEN in angemessenem Umfang dokumentiert werden. |
| `SASD-KM-021` | Production-Projekte MÜSSEN Runbooks oder gleichwertige Betriebsanweisungen für kritische Abläufe besitzen. |
| `SASD-KM-022` | Troubleshooting-Dokumentation SOLLTE Symptome, Prüfschritte, typische Ursachen, sichere Maßnahmen und Eskalationspunkte enthalten. |
| `SASD-KM-023` | Lokale, nicht reproduzierbare Expertenkenntnisse MÜSSEN priorisiert dokumentiert werden, wenn ihr Verlust den Betrieb oder die Wartung gefährden würde. |
| `SASD-KM-030` | Projektspezifische Begriffe, Abkürzungen und Domänenkonzepte SOLLTEN in einem Glossar oder an einer zentralen Stelle erklärt werden. |
| `SASD-KM-031` | Ein Begriff MUSS konsistent verwendet werden, wenn unterschiedliche Bedeutungen zu Fehlern führen könnten. |
| `SASD-KM-032` | Veraltete Begriffe SOLLTEN mit ihrem Nachfolger oder einer Migrationsnotiz versehen werden. |
| `SASD-KM-040` | Nach wesentlichen Releases, Migrationen, Vorfällen oder gescheiterten Ansätzen SOLLTEN Lessons Learned erfasst werden. |
| `SASD-KM-041` | Lessons Learned SOLLTEN Beobachtung, Ursache, Auswirkung und konkrete Verbesserung unterscheiden. |
| `SASD-KM-042` | Wiederverwendbare Erkenntnisse SOLLTEN in Standards, Checklisten, Templates oder Automatisierung überführt werden. |
| `SASD-KM-043` | Lessons Learned DÜRFEN NICHT zur persönlichen Schuldzuweisung verwendet werden. |
| `SASD-KM-050` | Externe Quellen, auf denen wesentliche Entscheidungen beruhen, SOLLTEN mit Titel, Herausgeber, Version oder Datum und Zugriffspfad referenziert werden. |
| `SASD-KM-051` | Kopierte Inhalte MÜSSEN Lizenz und Urheberrecht beachten. |
| `SASD-KM-052` | Kritisches Wissen SOLLTE nicht ausschließlich von einem veränderlichen externen Link abhängen. |
| `SASD-KM-053` | Veraltete Referenzen MÜSSEN bei relevanten Reviews aktualisiert oder gekennzeichnet werden. |
| `SASD-KM-060` | Wiederverwendbare oder entscheidungsrelevante Prompts SOLLTEN versioniert und mit Zweck, Eingaben und erwarteter Prüfung dokumentiert werden. |
| `SASD-KM-061` | Ein Prompt DARF NICHT als Ersatz für die fachliche Regel oder Entscheidung dienen. |
| `SASD-KM-062` | Ergebnisse aus KI-Systemen MÜSSEN vor Übernahme in die Source of Truth geprüft werden. |
| `SASD-KM-063` | Flüchtige Prompts ohne langfristigen Nutzen MÜSSEN nicht vollständig archiviert werden. |
| `SASD-KM-070` | Recommended- und Production-Projekte MÜSSEN einen Einstiegspfad für neue Entwickler oder Betreiber bereitstellen. |
| `SASD-KM-071` | Production-Projekte MÜSSEN kritische Verantwortlichkeiten, Zugänge, Systeme, Eskalationen und Wiederherstellungswissen übergabefähig dokumentieren. |
| `SASD-KM-072` | Eine Übergabe MUSS offene Risiken, technische Schulden und bekannte Einschränkungen benennen. |
| `SASD-KM-073` | Ein Projekt SOLLTE regelmäßig prüfen, ob eine fachkundige fremde Person den Einstieg mit der vorhandenen Dokumentation bewältigen kann. |
| `SASD-KM-080` | Wissen MUSS aktualisiert werden, wenn eine Änderung seine Richtigkeit oder Anwendbarkeit beeinflusst. |
| `SASD-KM-081` | Dokumente SOLLTEN einen Owner oder einen erkennbaren Pflegekontext besitzen. |
| `SASD-KM-082` | Veraltetes Wissen MUSS aktualisiert, als historisch gekennzeichnet oder archiviert werden. |
| `SASD-KM-083` | Historische Entscheidungen und Lessons Learned SOLLTEN erhalten bleiben, wenn sie spätere Entwicklungen erklären. |
| `SASD-KM-084` | Archivierung MUSS Sicherheits-, Datenschutz- und Aufbewahrungsanforderungen berücksichtigen. |

## [Ai Assisted Development](AI-ASSISTED-DEVELOPMENT.md)

| ID | Anforderung |
|---|---|
| `SASD-AI-001` | Für jedes übernommene KI-Ergebnis MUSS eine menschlich verantwortliche Person oder Rolle benannt oder ableitbar sein. |
| `SASD-AI-002` | KI-generierte Inhalte MÜSSEN vor Übernahme entsprechend ihrem Risiko fachlich geprüft werden. |
| `SASD-AI-003` | Ein KI-System DARF NICHT eigenständig ein Production-Release, eine irreversible Migration oder eine sicherheitskritische Änderung freigeben. |
| `SASD-AI-004` | Entscheidungen MÜSSEN anhand von Anforderungen und nachvollziehbaren Gründen getroffen werden, nicht allein aufgrund der überzeugenden Formulierung eines Modells. |
| `SASD-AI-005` | Unsicherheit, fehlende Prüfung oder ungeklärte Annahmen MÜSSEN sichtbar bleiben. |
| `SASD-AI-010` | Einsatzfälle MÜSSEN nach möglichem Schaden bei falschem Ergebnis bewertet werden. |
| `SASD-AI-011` | Hochriskante Ergebnisse MÜSSEN durch Primärquellen, Tests, Reviews oder praktische Verifikation bestätigt werden. |
| `SASD-AI-012` | KI SOLLTE für wiederholbare Routinearbeiten genutzt werden, wenn die resultierenden Artefakte zuverlässig geprüft werden können. |
| `SASD-AI-013` | KI SOLLTE NICHT als einzige Grundlage für Rechts-, Sicherheits-, Medizin-, Finanz- oder andere hochkritische Entscheidungen verwendet werden. |
| `SASD-AI-020` | Vor der Übermittlung von Kontext MUSS geprüft werden, ob Geheimnisse, personenbezogene Daten, vertrauliche Kundendaten oder geschütztes Material enthalten sind. |
| `SASD-AI-021` | Geheimnisse und produktive Zugangsdaten DÜRFEN NICHT an externe KI-Dienste übertragen werden. |
| `SASD-AI-022` | Personenbezogene und vertrauliche Daten MÜSSEN minimiert, anonymisiert oder durch eine ausdrücklich freigegebene, geeignete Umgebung geschützt werden. |
| `SASD-AI-023` | Projektdaten DÜRFEN NICHT allein aus Bequemlichkeit vollständig übertragen werden, wenn ein kleinerer Kontext genügt. |
| `SASD-AI-024` | Richtlinien und Vertragsbedingungen des verwendeten KI-Dienstes MÜSSEN für sensible oder geschäftliche Nutzung bewertet werden. |
| `SASD-AI-030` | Ein Prompt SOLLTE Ziel, Kontext, Constraints, erwartetes Ausgabeformat und Prüfkriterien klar beschreiben. |
| `SASD-AI-031` | Kritische Annahmen SOLLTEN ausdrücklich benannt werden, statt dem Modell ihre Erfindung zu überlassen. |
| `SASD-AI-032` | Wiederverwendbare Prompts SOLLTEN versioniert und mit Zweck, Variablen, Voraussetzungen und erwarteter Prüfung gespeichert werden. |
| `SASD-AI-033` | Ein Prompt DARF NICHT die normative Projektdokumentation ersetzen. |
| `SASD-AI-034` | Große Aufgaben SOLLTEN in prüfbare Arbeitspakete zerlegt werden, wenn dadurch Fehler leichter erkannt werden. |
| `SASD-AI-040` | Externe Fakten, Versionen, Schnittstellen, Gesetze und Sicherheitsbehauptungen MÜSSEN bei relevanter Änderungs- oder Fehlerrate anhand geeigneter Quellen verifiziert werden. |
| `SASD-AI-041` | Technische Implementierungsentscheidungen SOLLTEN vorrangig gegen offizielle Dokumentation, Spezifikationen oder Quellcode geprüft werden. |
| `SASD-AI-042` | Nicht verifizierbare Quellenangaben oder Zitate DÜRFEN NICHT als belegt übernommen werden. |
| `SASD-AI-043` | Zusammenfassungen MÜSSEN wesentliche Einschränkungen und Unsicherheiten der Ausgangsquelle erhalten. |
| `SASD-AI-050` | KI-generierter Code MUSS denselben Coding-, Review-, Test-, Lizenz- und Sicherheitsanforderungen wie manuell erstellter Code erfüllen. |
| `SASD-AI-051` | Übernommener Code MUSS verstanden werden, soweit dies für sichere Wartung und Freigabe erforderlich ist. |
| `SASD-AI-052` | Abhängigkeiten, APIs und Konfigurationswerte MÜSSEN auf Existenz, Version, Lizenz und angemessene Verwendung geprüft werden. |
| `SASD-AI-053` | Sicherheitskritische Logik, Kryptographie, Authentifizierung, Berechtigungen und Datenmigrationen MÜSSEN vertieft geprüft werden. |
| `SASD-AI-054` | KI-generierte Tests DÜRFEN NICHT lediglich die generierte Implementierung wiederholen; sie müssen Anforderungen und unabhängige Erwartungen prüfen. |
| `SASD-AI-055` | Unnötige Abstraktionen, erfundene Anforderungen und nicht verwendete Bestandteile MÜSSEN entfernt werden. |
| `SASD-AI-060` | Übernommene Inhalte MÜSSEN hinsichtlich Lizenz, Urheberrecht, Vertraulichkeit und Herkunft bewertet werden. |
| `SASD-AI-061` | Erkennbar fremde längere Code- oder Textpassagen DÜRFEN NICHT ohne Prüfung der Nutzungsrechte übernommen werden. |
| `SASD-AI-062` | KI-Nutzung DARF NICHT dazu verwendet werden, Lizenz- oder Vertraulichkeitsregeln zu umgehen. |
| `SASD-AI-063` | Production-Projekte SOLLTEN verwendete Werkzeuge und besondere IP-Risiken in ihrer Compliance- oder Projektdokumentation benennen. |
| `SASD-AI-070` | KI-Reviews KÖNNEN menschliche Reviews ergänzen, DÜRFEN aber bei hohem Risiko nicht die einzige Prüfung sein. |
| `SASD-AI-071` | Ergebnisse MÜSSEN praktisch getestet werden, wenn eine Ausführung oder Simulation möglich und für die Freigabe relevant ist. |
| `SASD-AI-072` | Sicherheitsbehauptungen MÜSSEN durch geeignete Analyse, Tests oder fachliche Prüfung belegt werden. |
| `SASD-AI-073` | Wiederkehrende Modellfehler SOLLTEN in Prompts, Checklisten oder Tooling berücksichtigt werden. |
| `SASD-AI-080` | Agentische Werkzeuge MÜSSEN mit minimal notwendigen Berechtigungen und klaren Arbeitsgrenzen betrieben werden. |
| `SASD-AI-081` | Schreibzugriff auf Repository, Cloud, Datenbanken oder Produktivsysteme MUSS ausdrücklich freigegeben und protokollierbar sein. |
| `SASD-AI-082` | Irreversible Aktionen MÜSSEN eine menschliche Bestätigung oder technisch gleichwertige Schutzbarriere besitzen. |
| `SASD-AI-083` | Toolausgaben und Seiteneffekte MÜSSEN vor der Freigabe geprüft werden. |
| `SASD-AI-084` | Ein Agent DARF NICHT selbstständig Schutzmechanismen, Prüfungen oder Freigaben deaktivieren, um ein Ziel schneller zu erreichen. |
| `SASD-AI-090` | Wesentliche KI-unterstützte Entscheidungen und Artefakte MÜSSEN so dokumentiert sein, dass Verantwortung und Prüfung nachvollziehbar bleiben. |
| `SASD-AI-091` | Production-Projekte SOLLTEN für sicherheits-, architektur- oder migrationskritische Ergebnisse Werkzeug, Datum, relevanten Kontext und Prüfnachweise festhalten. |
| `SASD-AI-092` | Nicht jeder flüchtige Prompt MUSS archiviert werden; wiederverwendbare und entscheidungsrelevante Prompts SOLLTEN erhalten bleiben. |
| `SASD-AI-093` | Ein KI-Chat DARF NICHT die einzige Historie einer Projektentscheidung bleiben. |
