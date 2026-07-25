---
title: "Qualitätsstufen und Anwendbarkeit"
document-id: SASD-CORE-006
document-type: normative
status: Approved
version: 0.9.0
standard-version: "1.0"
approval-bundle: SASD-NORMATIVE-BASELINE-0.9.0
approval-review-state: approved
language: de
authoritative: true
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
approved-on: 2026-07-24
approval-record: SASD-REF-BASELINE-007
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core]
depends-on: [SASD-FND-002, SASD-FND-003, SASD-GOV-001, SASD-GOV-006, SASD-GOV-007]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Qualitätsstufen und Anwendbarkeit

## 1. Zweck

Dieses Dokument definiert die Qualitätsstufen **SASD Minimum**, **SASD Recommended** und **SASD Production**. Es legt außerdem verbindlich fest, wie Anforderungen, Bedingungen, Qualitätsmatrizen, Profile und projektspezifische Abweichungen zusammenwirken.

Die Stufen skalieren Dokumentation, Prüfung, Sicherheit, Nachweise und Betriebsfähigkeit, ohne die grundlegenden Qualitätsprinzipien des Standards aufzugeben.

## 2. Geltungsbereich

Die Qualitätsstufe gilt grundsätzlich für das gesamte Projekt. Einzelne Risikobereiche dürfen auf eine höhere Stufe angehoben werden. Eine niedrigere Behandlung einzelner Bereiche als die primäre Projektstufe ist nur über eine dokumentierte Abweichung zulässig.

Die Qualitätsstufe ersetzt keine gesetzlichen, vertraglichen, regulatorischen oder fachlichen Anforderungen.

## 3. Grundmodell

### 3.1 SASD Minimum

SASD Minimum ist für kleine Werkzeuge, Lernprojekte, Experimente und zeitlich begrenzte Prototypen vorgesehen. Die Stufe verlangt ein nachvollziehbares Projektfundament, reproduzierbare Nutzung und eine grundlegende Sicherheits- und Qualitätsprüfung, vermeidet jedoch unnötige Prozesslast.

Mehrere Dokumentrollen KÖNNEN in einem README oder einer kompakten Projektübersicht zusammengeführt werden, sofern die erforderlichen Inhalte auffindbar bleiben.

### 3.2 SASD Recommended

SASD Recommended ist die Standardstufe für reguläre SASD-Projekte, öffentliche Repositories und Anwendungen, die längerfristig gepflegt oder von anderen Personen verstanden werden sollen.

Die Stufe verlangt strukturierte Anforderungen, Architektur, risikobasierte Tests, nachvollziehbare Releases und dokumentierte Wartungs- und Sicherheitsentscheidungen.

### 3.3 SASD Production

SASD Production ist für geschäftskritische, sicherheitssensitive, kundennahe, öffentlich betriebene oder anderweitig folgenreiche Systeme vorgesehen. Die Stufe verlangt belastbare Nachweise, reproduzierbare Releases, Betriebs- und Wiederherstellungsfähigkeit sowie eine vertiefte Sicherheitsbetrachtung.

Production bedeutet nicht Fehlerfreiheit. Die Stufe verlangt, dass Risiken, Kontrollen, Freigaben und Wiederherstellungsmaßnahmen dem möglichen Schaden angemessen sind.

## 4. Normative Anforderungen

### 4.1 Auswahl und Dokumentation

| ID | Anforderung |
|---|---|
| SASD-QL-001 | Jedes Projekt MUSS genau eine primäre Qualitätsstufe benennen. |
| SASD-QL-002 | Die gewählte Qualitätsstufe MUSS im README oder in einer eindeutig verlinkten Compliance-Datei dokumentiert sein. |
| SASD-QL-003 | Die Auswahl MUSS anhand von Projektrisiko, geplanter Lebensdauer, Nutzerkreis, Datenarten, Betriebsrelevanz und Änderungswahrscheinlichkeit begründet werden. |
| SASD-QL-004 | Ein Projekt DARF NICHT allein deshalb eine niedrigere Qualitätsstufe wählen, weil Anforderungen noch nicht umgesetzt wurden. Fehlende Umsetzung MUSS als Lücke, technische Schuld oder Abweichung dokumentiert werden. |
| SASD-QL-005 | Änderungen der Qualitätsstufe MÜSSEN mit Datum, Begründung und Auswirkungen auf offene Maßnahmen dokumentiert werden. |

### 4.2 Risikobasierte Hochstufung

| ID | Anforderung |
|---|---|
| SASD-QL-006 | Ein Projekt MUSS mindestens die Sicherheitsanforderungen von SASD Production anwenden, wenn ein Fehler voraussichtlich erhebliche Schäden an Vertraulichkeit, Integrität, Verfügbarkeit, Gesundheit, Finanzen oder gesetzlichen Rechten verursachen kann. |
| SASD-QL-007 | Ein Projekt, das reale Zugangsdaten, personenbezogene Daten, Zahlungsdaten oder produktive Systeme verarbeitet, MUSS die betreffenden Bereiche mindestens auf Production-Niveau behandeln. |
| SASD-QL-008 | Ein öffentlich betriebener Dienst SOLLTE als SASD Production klassifiziert werden. Eine niedrigere Einstufung benötigt eine dokumentierte Risikobegründung. |
| SASD-QL-009 | Ein Prototyp mit realen produktiven Daten DARF NICHT allein wegen seines experimentellen Charakters als risikolos behandelt werden. |

### 4.3 Bereichsweise Anhebung

| ID | Anforderung |
|---|---|
| SASD-QL-010 | Ein Projekt KANN einzelne Bereiche wie Sicherheit, Tests, Dokumentation oder Betrieb auf eine höhere Stufe anheben. |
| SASD-QL-011 | Bereichsweise Anhebungen MÜSSEN in der Compliance-Erklärung benannt werden. |
| SASD-QL-012 | Abhängige Anforderungen MÜSSEN gemeinsam betrachtet werden. Eine Production-Sicherheitsstufe ohne angemessene Test- und Wartungsnachweise ist nicht ausreichend. |

### 4.4 Anwendbarkeit einzelner Anforderungen

| ID | Anforderung |
|---|---|
| SASD-QL-013 | Eine Anforderung MUSS für alle in ihren Dokumentmetadaten genannten Qualitätsstufen angewendet werden, sofern ihr Wortlaut oder eine Qualitätsstufenmatrix die Anwendbarkeit nicht ausdrücklich einschränkt oder skaliert. |
| SASD-QL-014 | Bedingungen wie „bei Verteilung“, „bei Betrieb“, „soweit anwendbar“ oder „wenn sensible Daten verarbeitet werden“ MÜSSEN anhand der tatsächlichen Projekteigenschaften bewertet werden. |
| SASD-QL-015 | Eine dokumenteigene Qualitätsstufenmatrix KANN den Verbindlichkeitsgrad einer beschriebenen Maßnahme für eine konkrete Stufe präzisieren. Für diese Maßnahme und Stufe MUSS die Matrix gegenüber einer allgemeineren Formulierung desselben Dokuments vorrangig angewendet werden. |
| SASD-QL-016 | Eine MUSS- oder DARF-NICHT-Anforderung ohne einschränkende Bedingung oder abweichende Qualitätsstufenregel gilt für Minimum, Recommended und Production. |
| SASD-QL-017 | Eine als nicht anwendbar bewertete MUSS- oder DARF-NICHT-Anforderung MUSS mit einer kurzen, überprüfbaren Begründung in der Compliance-Bewertung gekennzeichnet werden. |
| SASD-QL-018 | Eine SOLLTE- oder SOLLTE-NICHT-Anforderung, der ein Projekt nicht folgt, SOLLTE mit der fachlichen Begründung dokumentiert werden, wenn die Abweichung Sicherheit, Wartbarkeit, Reproduzierbarkeit oder Nachweisführung beeinflusst. |
| SASD-QL-019 | Nachweise MÜSSEN dem Risiko, der Projektgröße und der Qualitätsstufe angemessen sein. Ein kleineres Projekt DARF denselben Inhalt kompakter dokumentieren, aber nicht ersatzlos weglassen. |

### 4.5 Hierarchie und Konfliktbehandlung

| ID | Anforderung |
|---|---|
| SASD-QL-020 | Für eine höhere Qualitätsstufe MÜSSEN alle anwendbaren Anforderungen niedrigerer Stufen übernommen werden, sofern keine ausdrücklich strengere oder anders ausgestaltete Regel für die höhere Stufe besteht. |
| SASD-QL-021 | Profile KÖNNEN Core-Anforderungen konkretisieren oder verschärfen, DÜRFEN sie jedoch nicht stillschweigend abschwächen. |
| SASD-QL-022 | Gesetzliche, vertragliche, regulatorische und projektspezifisch freigegebene strengere Anforderungen MÜSSEN gegenüber einer weniger strengen SASD-Regel vorrangig angewendet werden. |
| SASD-QL-023 | Ein erkannter normativer Konflikt MUSS nach den Vorrangregeln der Inhaltsarchitektur bewertet und bis zur Klärung als offene Standard- oder Projektabweichung dokumentiert werden. |

### 4.6 Rollen bei Einzelentwicklern

| ID | Anforderung |
|---|---|
| SASD-QL-024 | Eine Person KANN mehrere oder alle Projektrollen übernehmen. Die Zusammenlegung von Rollen hebt keine fachliche Prüfung, Freigabe oder Nachweispflicht auf. |
| SASD-QL-025 | Wo kein unabhängiger Reviewer verfügbar ist, MUSS eine geforderte Prüfung als strukturierte Selbstprüfung durchgeführt und nachvollziehbar dokumentiert werden, sofern die betreffende Anforderung nicht ausdrücklich eine personelle Trennung verlangt. |
| SASD-QL-026 | Bei hohem oder kritischem Risiko SOLLTE trotz Einzelentwicklung eine unabhängige fachliche, sicherheitsbezogene oder rechtliche Prüfung eingeholt werden. |

## 5. Auswahlkriterien

Bei der Klassifikation werden mindestens folgende Fragen betrachtet:

| Kriterium | Minimum | Recommended | Production |
|---|---|---|---|
| Lebensdauer | kurz oder experimentell | längerfristig gepflegt | langfristig oder vertraglich zugesichert |
| Nutzerkreis | Entwickler selbst oder kleiner Lernkreis | mehrere Nutzer oder Open Source | externe Kunden, Öffentlichkeit oder operative Teams |
| Ausfallauswirkung | gering und leicht behebbar | spürbar, aber beherrschbar | erheblich, geschäfts- oder sicherheitskritisch |
| Daten | keine oder unkritische Testdaten | reguläre Projektdaten | sensible, personenbezogene oder geschäftskritische Daten |
| Betrieb | lokal und gelegentlich | regelmäßig genutzt | produktiv, automatisiert oder dauerhaft verfügbar |
| Wiederherstellung | erneute Erstellung vertretbar | Backup oder dokumentierte Wiederherstellung | getestete Wiederherstellung und definierte Ziele |
| Nachweisbedarf | gering | nachvollziehbar für Dritte | auditierbar oder vertraglich relevant |

Die Tabelle ist eine Entscheidungshilfe. Ein einziges hohes Risiko kann eine höhere Stufe oder eine bereichsweise Hochstufung rechtfertigen.

## 6. Mindestumfang je Qualitätsstufe

| Bereich | Minimum | Recommended | Production |
|---|---|---|---|
| Projektziel und Scope | MUSS | MUSS | MUSS |
| README und Nutzung | MUSS | MUSS | MUSS |
| Anforderungen | kompakt MUSS | strukturiert MUSS | nachvollziehbar und freigegeben MUSS |
| Architektur | einfache Übersicht SOLLTE | dokumentiert MUSS | geprüft und entscheidungsbasiert MUSS |
| Tests | kritische Nutzung MUSS geprüft werden | risikobasierte Teststrategie MUSS | automatisierte und dokumentierte Freigaben MÜSSEN vorhanden sein |
| Sicherheit | Baseline MUSS | Risikoanalyse MUSS | Bedrohungsmodell und belastbare Nachweise MÜSSEN vorhanden sein |
| Releases | nachvollziehbarer Stand MUSS | versioniert und dokumentiert MUSS | reproduzierbar, prüfbar und rückrollbar MUSS |
| Wartung | Zuständigkeit MUSS | Wartungsplan SOLLTE | Betriebs-, Update- und Wiederherstellungsplan MUSS |
| Wissensmanagement | wesentliche Hinweise MUSS | ADRs und Übergabewissen SOLLTEN vorhanden sein | vollständige Betriebs- und Entscheidungsnachweise MÜSSEN vorhanden sein |
| Automatisierung | KANN | SOLLTE | für wiederholbare Prüfungen MUSS sie soweit technisch möglich eingesetzt werden |

## 7. Compliance- und Bewertungsmodell

Ein Projekt verwendet einen der folgenden Zustände:

- **Not Assessed**: Es wurde noch keine strukturierte Bewertung durchgeführt.
- **Assessment in Progress**: Die Bewertung läuft; Ergebnisse sind unvollständig.
- **Partially Aligned**: Der Standard wird angewendet, aber anwendbare Pflichtanforderungen sind offen oder noch nicht abschließend bewertet.
- **Aligned with Exceptions**: Alle anwendbaren Pflichtanforderungen sind erfüllt oder durch gültige, dokumentierte Ausnahmen abgedeckt.
- **Aligned**: Alle anwendbaren MUSS- und DARF-NICHT-Anforderungen sind erfüllt; erforderliche Begründungen und Nachweise sind vorhanden.

Ein Projekt DARF sich nicht als `Aligned` bezeichnen, solange unbekannte, nicht bewertete oder offene Pflichtbereiche bestehen.

Formale Alignment-Aussagen beziehen sich immer auf eine **veröffentlichte Standardversion mit Approved-Dokumenten**. Gegen Draft- oder Proposed-Dokumente KANN nur eine Pilot- oder Vorabbewertung dokumentiert werden.

## 8. Verantwortlichkeiten

Der Projektverantwortliche MUSS die Qualitätsstufe auswählen und Änderungen genehmigen. Bei einem Einzelentwickler kann dieselbe Person alle Rollen übernehmen, MUSS die Auswahl und Selbstprüfung jedoch anhand der Projektklassifikations- und Compliance-Hilfsmittel nachvollziehbar machen.

## 9. Nachweise und Prüfkriterien

Geeignete Nachweise sind:

- Eintrag im README oder `docs/SASD-COMPLIANCE.md`,
- ausgefüllte Projektklassifikation,
- Liste bereichsweiser Hochstufungen,
- Requirement-Status- und Nachweismatrix,
- dokumentierte Abweichungen,
- Verweise auf erforderliche Artefakte und Prüfergebnisse.

## 10. Ausnahmen und Abweichungen

Abweichungen werden nach [EXCEPTIONS.md](../40-governance/EXCEPTIONS.md) behandelt. Eine Abweichung DARF die Projektstufe nicht faktisch entwerten oder gesetzliche, vertragliche oder regulatorische Pflichten ersetzen.

## 11. Verwandte Dokumente

- [Normative Sprache](../40-governance/NORMATIVE-LANGUAGE.md)
- [Compliance-Modell](../40-governance/COMPLIANCE.md)
- [Ausnahmen und Abweichungen](../40-governance/EXCEPTIONS.md)
- [Projektklassifikation](../30-processes/PROJECT-CLASSIFICATION.md)
- [Qualitätsstandard](QUALITY.md)
- [Sicherheitsstandard](SECURITY.md)
- [Leitfaden für Einzelentwickler](SOLO-DEVELOPER-GUIDE.md)
