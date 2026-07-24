---
title: "Qualitätsstufen"
document-id: SASD-CORE-006
document-type: normative
status: Draft
version: 0.2.0
standard-version: "1.0"
language: de
authoritative: true
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core]
depends-on: [SASD-FND-002, SASD-FND-003, SASD-GOV-001, SASD-GOV-006, SASD-GOV-007]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Qualitätsstufen

## 1. Zweck

Dieses Dokument definiert die Qualitätsstufen **SASD Minimum**, **SASD Recommended** und **SASD Production**. Die Stufen skalieren den Umfang von Dokumentation, Prüfung, Sicherheit, Nachweisen und Betriebsfähigkeit, ohne die grundlegenden Qualitätsprinzipien des Standards aufzugeben.

## 2. Geltungsbereich

Die Qualitätsstufe gilt für das gesamte Projekt. Einzelne Risikobereiche dürfen auf eine höhere Stufe angehoben werden. Eine niedrigere Behandlung einzelner Bereiche als die primäre Projektstufe ist nur über eine dokumentierte Abweichung zulässig.

Die Qualitätsstufe ersetzt keine gesetzlichen, vertraglichen, regulatorischen oder fachlichen Anforderungen.

## 3. Grundmodell

### 3.1 SASD Minimum

SASD Minimum ist für kleine Werkzeuge, Lernprojekte, Experimente und zeitlich begrenzte Prototypen vorgesehen. Die Stufe verlangt ein nachvollziehbares Projektfundament, reproduzierbare Nutzung und eine grundlegende Sicherheits- und Qualitätsprüfung, vermeidet jedoch unnötige Prozesslast.

### 3.2 SASD Recommended

SASD Recommended ist die Standardstufe für reguläre SASD-Projekte, öffentliche Repositories und Anwendungen, die längerfristig gepflegt oder von anderen Personen verstanden werden sollen.

### 3.3 SASD Production

SASD Production ist für geschäftskritische, sicherheitssensitive, kundennahe, öffentlich betriebene oder anderweitig folgenreiche Systeme vorgesehen. Die Stufe verlangt belastbare Nachweise, reproduzierbare Releases, Betriebs- und Wiederherstellungsfähigkeit sowie eine vertiefte Sicherheitsbetrachtung.

## 4. Normative Anforderungen

### 4.1 Auswahl und Dokumentation

| ID | Anforderung |
|---|---|
| SASD-QL-001 | Jedes Projekt MUSS genau eine primäre Qualitätsstufe benennen. |
| SASD-QL-002 | Die gewählte Qualitätsstufe MUSS im README oder in einer eindeutig verlinkten Compliance-Datei dokumentiert sein. |
| SASD-QL-003 | Die Auswahl MUSS anhand von Projektrisiko, geplanter Lebensdauer, Nutzerkreis, Datenarten, Betriebsrelevanz und Änderungswahrscheinlichkeit begründet werden. |
| SASD-QL-004 | Ein Projekt DARF seine Qualitätsstufe nicht allein deshalb niedriger wählen, weil Anforderungen noch nicht umgesetzt wurden. Fehlende Umsetzung ist als Lücke, technische Schuld oder Abweichung zu dokumentieren. |
| SASD-QL-005 | Änderungen der Qualitätsstufe MÜSSEN mit Datum, Begründung und Auswirkungen auf offene Maßnahmen dokumentiert werden. |

### 4.2 Risikobasierte Hochstufung

| ID | Anforderung |
|---|---|
| SASD-QL-006 | Ein Projekt MUSS mindestens die Sicherheitsanforderungen von SASD Production anwenden, wenn ein Fehler voraussichtlich erhebliche Schäden an Vertraulichkeit, Integrität, Verfügbarkeit, Gesundheit, Finanzen oder gesetzlichen Rechten verursachen kann. |
| SASD-QL-007 | Ein Projekt, das reale Zugangsdaten, personenbezogene Daten, Zahlungsdaten oder produktive Systeme verarbeitet, MUSS die betreffenden Bereiche mindestens auf Production-Niveau behandeln. |
| SASD-QL-008 | Ein öffentlich betriebener Dienst SOLLTE als SASD Production klassifiziert werden. Eine niedrigere Einstufung benötigt eine dokumentierte Risikobegründung. |
| SASD-QL-009 | Ein Prototyp mit realen produktiven Daten DARF nicht allein wegen seines experimentellen Charakters als risikolos behandelt werden. |

### 4.3 Bereichsweise Anhebung

| ID | Anforderung |
|---|---|
| SASD-QL-010 | Ein Projekt KANN einzelne Bereiche wie Sicherheit, Tests, Dokumentation oder Betrieb auf eine höhere Stufe anheben. |
| SASD-QL-011 | Bereichsweise Anhebungen MÜSSEN in der Compliance-Erklärung benannt werden. |
| SASD-QL-012 | Abhängige Anforderungen MÜSSEN gemeinsam betrachtet werden. Eine Production-Sicherheitsstufe ohne angemessene Test- und Wartungsnachweise ist nicht ausreichend. |

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

Die Tabelle ist eine Entscheidungshilfe. Ein einziges hohes Risiko kann eine höhere Stufe rechtfertigen.

## 6. Mindestumfang je Qualitätsstufe

| Bereich | Minimum | Recommended | Production |
|---|---|---|---|
| Projektziel und Scope | MUSS | MUSS | MUSS |
| README und Nutzung | MUSS | MUSS | MUSS |
| Anforderungen | kompakt MUSS | strukturiert MUSS | nachvollziehbar und freigegeben MUSS |
| Architektur | einfache Übersicht SOLLTE | dokumentiert MUSS | geprüft und entscheidungsbasiert MUSS |
| Tests | kritische Nutzung MUSS geprüft werden | risikobasierte Teststrategie MUSS | automatisierte und dokumentierte Freigaben MUSS |
| Sicherheit | Baseline MUSS | Risikoanalyse MUSS | Bedrohungsmodell und belastbare Nachweise MUSS |
| Releases | nachvollziehbarer Stand MUSS | versioniert und dokumentiert MUSS | reproduzierbar, prüfbar und rückrollbar MUSS |
| Wartung | Zuständigkeit MUSS | Wartungsplan SOLLTE | Betriebs-, Update- und Wiederherstellungsplan MUSS |
| Wissensmanagement | wesentliche Hinweise MUSS | ADRs und Übergabewissen SOLLTE | vollständige Betriebs- und Entscheidungsnachweise MUSS |
| Automatisierung | KANN | SOLLTE | für wiederholbare Prüfungen MUSS, soweit technisch möglich |

## 7. Compliance-Modell

Ein Projekt kann einen der folgenden Zustände angeben:

- **Compliant**: alle anwendbaren MUSS- und DARF-NICHT-Anforderungen sind erfüllt oder genehmigt abgedeckt.
- **Compliant with Exceptions**: Anforderungen sind über dokumentierte, befristete Ausnahmen abgedeckt.
- **Partially Aligned**: der Standard wird angewendet, aber wesentliche Pflichtanforderungen sind noch offen.
- **Not Assessed**: es wurde noch keine strukturierte Bewertung durchgeführt.

Ein Projekt DARF sich nicht als vollständig compliant bezeichnen, solange unbekannte oder nicht bewertete Pflichtbereiche bestehen.

## 8. Verantwortlichkeiten

Der Projektverantwortliche MUSS die Qualitätsstufe auswählen und Änderungen genehmigen. Bei einem Einzelentwickler kann dieselbe Person alle Rollen übernehmen, SOLLTE aber die Auswahl anhand der Projektklassifikations- und Compliance-Checklisten nachvollziehen.

## 9. Nachweise und Prüfkriterien

Geeignete Nachweise sind:

- Eintrag im README oder `docs/SASD-COMPLIANCE.md`,
- ausgefüllte Projektklassifikation,
- Liste bereichsweiser Hochstufungen,
- dokumentierte Abweichungen,
- Verweise auf erforderliche Artefakte und Prüfergebnisse.

## 10. Ausnahmen und Abweichungen

Abweichungen werden nach [EXCEPTIONS.md](../40-governance/EXCEPTIONS.md) behandelt. Eine Abweichung DARF die Projektstufe nicht faktisch entwerten.

## 11. Verwandte Dokumente

- [Projektklassifikation](../30-processes/PROJECT-CLASSIFICATION.md)
- [Compliance](../40-governance/COMPLIANCE.md)
- [Qualitätsstandard](QUALITY.md)
- [Sicherheitsstandard](SECURITY.md)
- [Teststandard](TESTING.md)
