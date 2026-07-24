---
title: "Teststandard"
document-id: SASD-CORE-009
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
depends-on: [SASD-FND-003, SASD-GOV-001, SASD-CORE-002, SASD-CORE-003, SASD-CORE-006, SASD-CORE-007, SASD-CORE-008]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Teststandard

## 1. Zweck

Dieses Dokument definiert risikobasierte Anforderungen an Teststrategie, Testarten, Testdaten, Umgebungen, Fehlerbehandlung und Verifikationsnachweise.

## 2. Geltungsbereich

Tests umfassen automatisierte und manuelle Prüfungen von Software, Infrastruktur, Konfiguration, Datenmigration, Dokumentation, Deployment und Betriebsverfahren. Der Standard schreibt keine starre Testpyramide oder Mindestanzahl von Tests vor.

## 3. Testgrundsätze

- Tests dienen Anforderungen und Risiken, nicht bloßen Kennzahlen.
- Kritische Fehler sollen möglichst früh und auf der günstigsten geeigneten Ebene erkannt werden.
- Automatisierung wird dort eingesetzt, wo Wiederholung, Geschwindigkeit oder Fehlerrisiko sie rechtfertigen.
- Manuelle Tests bleiben zulässig, müssen aber bei Freigaberelevanz reproduzierbar beschrieben sein.
- Flaky Tests sind Fehler im Testsystem und dürfen nicht als normaler Zustand akzeptiert werden.

## 4. Normative Anforderungen

### 4.1 Teststrategie

| ID | Anforderung |
|---|---|
| SASD-TEST-001 | Jedes Projekt MUSS festlegen, wie die wesentlichen Anforderungen und Risiken verifiziert werden. |
| SASD-TEST-002 | Recommended- und Production-Projekte MÜSSEN eine dokumentierte, risikobasierte Teststrategie besitzen. |
| SASD-TEST-003 | Die Teststrategie MUSS Testziele, Testarten, Umgebungen, Verantwortlichkeiten, relevante Daten und Freigabekriterien benennen. |
| SASD-TEST-004 | Testaufwand MUSS sich an Auswirkung und Eintrittswahrscheinlichkeit möglicher Fehler orientieren. |
| SASD-TEST-005 | Code Coverage oder andere Kennzahlen DÜRFEN NICHT allein als Beweis ausreichender Qualität verwendet werden. |

### 4.2 Testarten

Ein Projekt wählt passende Testarten. Dazu können gehören:

- Unit- oder Komponententests,
- Integrations- und Vertragstests,
- System- und End-to-End-Tests,
- Akzeptanz- und explorative Tests,
- Installations-, Upgrade- und Migrationstests,
- Sicherheits- und Missbrauchstests,
- Performance-, Last- und Stabilitätstests,
- Backup- und Wiederherstellungstests,
- statische Prüfungen und Architekturtests,
- Dokumentations- und Bedienbarkeitstests.

| ID | Anforderung |
|---|---|
| SASD-TEST-010 | Kritische Geschäfts-, Daten- und Sicherheitslogik MUSS auf einer geeigneten Ebene geprüft werden. |
| SASD-TEST-011 | Integrationen zu Datenbanken, Dateisystemen, Netzwerken, APIs oder externen Diensten MÜSSEN entsprechend ihrem Risiko getestet oder simuliert werden. |
| SASD-TEST-012 | Öffentliche Schnittstellen SOLLTEN durch Vertrags- oder Kompatibilitätstests geschützt werden. |
| SASD-TEST-013 | Production-Projekte MÜSSEN Installations-, Upgrade-, Migration- und Wiederherstellungswege prüfen, soweit anwendbar. |
| SASD-TEST-014 | Sicherheitsrelevante Fehlbedienung und Missbrauchsfälle SOLLTEN ausdrücklich getestet werden. |

### 4.3 Zuordnung zu Anforderungen

| ID | Anforderung |
|---|---|
| SASD-TEST-020 | Freigaberelevante Tests MÜSSEN auf eine Anforderung, ein Risiko, einen Fehler oder einen technischen Vertrag zurückführbar sein. |
| SASD-TEST-021 | Wesentliche Anforderungen DÜRFEN NICHT ohne definierten Verifikationsweg als erfüllt markiert werden. |
| SASD-TEST-022 | Für Production MUSS nachvollziehbar sein, welche Testnachweise den freigegebenen Lieferumfang abdecken. |
| SASD-TEST-023 | Ein Regressionstest SOLLTE ergänzt werden, wenn ein Fehler mit vertretbarem Aufwand automatisiert reproduzierbar ist. |

### 4.4 Automatisierung und Reproduzierbarkeit

| ID | Anforderung |
|---|---|
| SASD-TEST-030 | Automatisierte Tests MÜSSEN reproduzierbar ausführbar und ihre Voraussetzungen dokumentiert sein. |
| SASD-TEST-031 | Tests SOLLTEN unabhängig voneinander und ohne unbeabsichtigte Reihenfolgeabhängigkeit ausführbar sein. |
| SASD-TEST-032 | Wiederholbare Pflichtprüfungen SOLLTEN in CI oder einen gleichwertigen automatisierten Ablauf integriert werden. |
| SASD-TEST-033 | Production-Releases MÜSSEN aus einem identifizierbaren Prüflauf mit nachvollziehbarer Konfiguration freigegeben werden. |
| SASD-TEST-034 | Externe Dienste SOLLTEN in Tests kontrolliert ersetzt oder über dedizierte Testumgebungen angebunden werden. |
| SASD-TEST-035 | Ein Test DARF NICHT unbemerkt produktive Daten, Dienste oder kostenpflichtige Ressourcen verändern. |

### 4.5 Testdaten

| ID | Anforderung |
|---|---|
| SASD-TEST-040 | Testdaten MÜSSEN für den jeweiligen Testzweck repräsentativ und kontrollierbar sein. |
| SASD-TEST-041 | Produktive personenbezogene oder vertrauliche Daten DÜRFEN NICHT ohne ausdrückliche Freigabe und Schutzmaßnahmen als Testdaten verwendet werden. |
| SASD-TEST-042 | Sensible Testdaten MÜSSEN geschützt, minimiert und nach der vorgesehenen Nutzung gelöscht werden. |
| SASD-TEST-043 | Grenzwerte, ungültige Eingaben, leere Daten und relevante Fehlerfälle SOLLTEN berücksichtigt werden. |
| SASD-TEST-044 | Zufallsbasierte Tests MÜSSEN bei Fehlern einen reproduzierbaren Seed oder gleichwertigen Wiederholungsweg liefern. |

### 4.6 Testumgebungen

| ID | Anforderung |
|---|---|
| SASD-TEST-050 | Unterschiede zwischen Test- und Zielumgebung MÜSSEN bekannt sein, wenn sie das Ergebnis beeinflussen können. |
| SASD-TEST-051 | Production-Projekte SOLLTEN eine produktionsnahe Umgebung für kritische Integrations-, Deployment- und Migrationstests besitzen. |
| SASD-TEST-052 | Testumgebungen MÜSSEN mit kontrollierter Konfiguration und angemessenen Berechtigungen betrieben werden. |
| SASD-TEST-053 | Testartefakte und Umgebungen SOLLTEN nach Abschluss bereinigt werden, sofern sie nicht als Nachweis aufbewahrt werden. |

### 4.7 Fehler und Flaky Tests

| ID | Anforderung |
|---|---|
| SASD-TEST-060 | Fehlgeschlagene Tests MÜSSEN untersucht und dürfen nicht pauschal erneut ausgeführt werden, bis zufällig ein grüner Lauf entsteht. |
| SASD-TEST-061 | Flaky Tests MÜSSEN sichtbar gekennzeichnet, priorisiert und behoben oder kontrolliert quarantänisiert werden. |
| SASD-TEST-062 | Quarantänisierte Pflichtprüfungen MÜSSEN eine dokumentierte Risikoakzeptanz und Frist besitzen. |
| SASD-TEST-063 | Fehlerberichte SOLLTEN Reproduktionsschritte, erwartetes und tatsächliches Verhalten, Umgebung und relevante Protokolle enthalten. |
| SASD-TEST-064 | Kritische Defekte DÜRFEN NICHT ohne ausdrückliche Freigabe in ein Release übernommen werden. |

### 4.8 Manuelle Prüfungen

| ID | Anforderung |
|---|---|
| SASD-TEST-070 | Manuelle freigaberelevante Tests MÜSSEN mit Schritten, erwarteten Ergebnissen und Ergebnis dokumentiert werden. |
| SASD-TEST-071 | Explorative Tests SOLLTEN Fokus, Beobachtungen und gefundene Risiken festhalten. |
| SASD-TEST-072 | Benutzeroberflächen SOLLTEN auf Verständlichkeit, Fehlermeldungen, Tastaturbedienung und relevante Barrierefreiheit geprüft werden. |
| SASD-TEST-073 | Ein manueller Test SOLLTE automatisiert werden, wenn er häufig wiederholt wird und zuverlässig automatisierbar ist. |

### 4.9 Testnachweise und Aufbewahrung

| ID | Anforderung |
|---|---|
| SASD-TEST-080 | Releasefreigaben MÜSSEN auf die relevanten Prüfergebnisse verweisen. |
| SASD-TEST-081 | Testnachweise MÜSSEN Version, Zeitpunkt, Umgebung und Ergebnis erkennen lassen, wenn diese für die Bewertung notwendig sind. |
| SASD-TEST-082 | Production-Projekte MÜSSEN freigaberelevante Nachweise für einen angemessenen Zeitraum aufbewahren. |
| SASD-TEST-083 | Testberichte DÜRFEN NICHT sensible Daten oder Geheimnisse unnötig offenlegen. |

## 5. Zuordnung zu Qualitätsstufen

| Maßnahme | Minimum | Recommended | Production |
|---|---|---|---|
| dokumentierter Testansatz | kompakt MUSS | MUSS | MUSS |
| automatisierte Tests | kritische Logik SOLLTE | wesentliche Logik MUSS | umfassend risikobasiert MUSS |
| Integrationstests | bei relevanten Integrationen SOLLTE | MUSS | MUSS |
| manuelle Releaseprüfung | bei Bedarf MUSS | reproduzierbar MUSS | protokolliert MUSS |
| Security-Tests | Baseline SOLLTE | risikobasiert MUSS | Bedrohungsmodell-basiert MUSS |
| Upgrade/Recovery-Tests | KANN | bei Betrieb SOLLTE | MUSS |
| CI-Integration | KANN | SOLLTE | MUSS |
| Testnachweise | Ergebnis SOLLTE | MUSS | releasebezogen MUSS |

## 6. Verantwortlichkeiten

Entwickler erstellen und pflegen Tests. Projektverantwortliche priorisieren Testtiefe nach Risiko. Reviewer prüfen Testaussage und Lücken. Betreiber unterstützen Deployment-, Backup- und Recovery-Tests.

## 7. Nachweise und Prüfkriterien

Geeignete Nachweise sind Teststrategie, automatisierte Testergebnisse, manuelle Testprotokolle, Traceability, Fehlerberichte, Coverage als Zusatzinformation, Recovery-Berichte und Releasefreigabe.

## 8. Ausnahmen und Abweichungen

Nicht automatisierbare Tests sind zulässig. Die Abweichung MUSS erklären, wie das Risiko stattdessen kontrolliert und die Prüfung reproduziert wird.

## 9. Verwandte Dokumente

- [Anforderungsmanagement](REQUIREMENTS.md)
- [Qualitätsstandard](QUALITY.md)
- [Sicherheitsstandard](SECURITY.md)
- [Release-Standard](RELEASES.md)
