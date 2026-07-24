---
title: "Qualitätsstandard"
document-id: SASD-CORE-007
document-type: normative
status: Proposed
version: 0.3.0
standard-version: "1.0"
language: de
authoritative: true
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core]
depends-on: [SASD-FND-003, SASD-GOV-001, SASD-CORE-002, SASD-CORE-003, SASD-CORE-006, SASD-CORE-009]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Qualitätsstandard

## 1. Zweck

Dieses Dokument definiert allgemeine Qualitätsziele, Definition of Done, Review, statische Prüfung, technische Schulden und kontinuierliche Verbesserung.

## 2. Geltungsbereich

Der Standard gilt für Quellcode, Infrastrukturdefinitionen, Skripte, Konfigurationen, Datenmodelle, Dokumentation und weitere wartbare Projektartefakte.

## 3. Qualitätsmodell

Qualität bedeutet nicht maximale Perfektion. Ein Projekt gilt als qualitativ angemessen, wenn seine Anforderungen, Risiken und Lebensdauer durch nachvollziehbare Maßnahmen unterstützt werden und bekannte Einschränkungen sichtbar bleiben.

Relevante Qualitätsattribute können sein:

- funktionale Korrektheit,
- Verständlichkeit und Wartbarkeit,
- Sicherheit und Datenschutz,
- Zuverlässigkeit und Wiederherstellbarkeit,
- Testbarkeit und Beobachtbarkeit,
- Performance und Ressourceneffizienz,
- Portabilität und Kompatibilität,
- Bedienbarkeit und Barrierefreiheit.

## 4. Normative Anforderungen

### 4.1 Qualitätsziele

| ID | Anforderung |
|---|---|
| SASD-QUAL-001 | Relevante Qualitätsattribute MÜSSEN aus Anforderungen und Risiken abgeleitet werden. |
| SASD-QUAL-002 | Qualitätsziele MÜSSEN soweit möglich beobachtbar oder prüfbar formuliert werden. |
| SASD-QUAL-003 | Zielkonflikte MÜSSEN bei wesentlichen Entscheidungen dokumentiert werden. |
| SASD-QUAL-004 | Ein Projekt DARF NICHT Qualitätsmaßnahmen allein nach leicht messbaren Kennzahlen ausrichten. Kennzahlen MÜSSEN dem Projektziel dienen. |

### 4.2 Definition of Done

| ID | Anforderung |
|---|---|
| SASD-QUAL-010 | Recommended- und Production-Projekte MÜSSEN eine Definition of Done für Änderungen oder Meilensteine besitzen. |
| SASD-QUAL-011 | Die Definition of Done MUSS mindestens Implementierung, Tests, Dokumentation, Sicherheitsauswirkungen, offene Risiken und Integrationsfähigkeit berücksichtigen. |
| SASD-QUAL-012 | Eine Änderung DARF NICHT als abgeschlossen gelten, wenn bekannte Pflichtprüfungen ohne dokumentierte Ausnahme fehlschlagen. |
| SASD-QUAL-013 | Für Minimum MUSS zumindest festgelegt sein, wann ein geplanter Lieferumfang als nutzbar und geprüft gilt. |

### 4.3 Lesbarkeit und Wartbarkeit

| ID | Anforderung |
|---|---|
| SASD-QUAL-020 | Projektartefakte MÜSSEN verständlich benannt und strukturiert sein. |
| SASD-QUAL-021 | Unnötige Duplizierung SOLLTE vermieden werden; erzwungene Abstraktion ohne stabilen gemeinsamen Zweck SOLLTE ebenfalls vermieden werden. |
| SASD-QUAL-022 | Komplexe oder nicht offensichtliche Logik MUSS durch Struktur, Benennung, Tests oder erklärende Dokumentation verständlich gemacht werden. |
| SASD-QUAL-023 | Tote, nicht erreichbare oder nicht mehr verwendete Artefakte MÜSSEN entfernt oder ausdrücklich begründet werden. |
| SASD-QUAL-024 | Öffentliche Verträge und Kompatibilitätsgrenzen MÜSSEN stabil oder klar versioniert sein. |

### 4.4 Automatisierte und statische Prüfungen

| ID | Anforderung |
|---|---|
| SASD-QUAL-030 | Build- oder Validierungswarnungen MÜSSEN bewertet werden und DÜRFEN NICHT dauerhaft unbegründet ignoriert werden. |
| SASD-QUAL-031 | Formatierung und einfache Qualitätsregeln SOLLTEN automatisiert und repositoryweit konsistent angewendet werden. |
| SASD-QUAL-032 | Recommended-Projekte SOLLTEN statische Analyse, Linting oder vergleichbare Prüfungen einsetzen. |
| SASD-QUAL-033 | Production-Projekte MÜSSEN relevante automatisierbare Qualitäts- und Sicherheitsprüfungen in die Integrations- oder Releasepipeline einbinden. |
| SASD-QUAL-034 | Unterdrückungen von Warnungen MÜSSEN lokal, begründet und so eng wie möglich sein. |
| SASD-QUAL-035 | Qualitätsprüfungen DÜRFEN NICHT so konfiguriert werden, dass ein grüner Status durch pauschales Deaktivieren wesentlicher Regeln entsteht. |

### 4.5 Reviews

| ID | Anforderung |
|---|---|
| SASD-QUAL-040 | Änderungen mit erhöhtem Risiko MÜSSEN einer strukturierten Prüfung unterzogen werden. |
| SASD-QUAL-041 | Reviews MÜSSEN Anforderungen, Korrektheit, Verständlichkeit, Tests, Sicherheit, Dokumentation und Auswirkungen berücksichtigen. |
| SASD-QUAL-042 | Einpersonenprojekte KÖNNEN Peer Review durch eine dokumentierte Selbstprüfung, zeitversetzte Prüfung oder geeignete Werkzeuge ergänzen. |
| SASD-QUAL-043 | Reviewumfang MUSS risikobasiert sein; rein formale Freigaben ohne inhaltliche Prüfung sind nicht ausreichend. |
| SASD-QUAL-044 | Findings MÜSSEN nach Risiko eingeordnet und entweder behoben, akzeptiert oder nachverfolgt werden. |

### 4.6 Technische Schulden

| ID | Anforderung |
|---|---|
| SASD-QUAL-050 | Bewusst eingegangene technische Schulden MÜSSEN mit Auswirkung, Begründung und geplanter Behandlung dokumentiert werden. |
| SASD-QUAL-051 | Kritische technische Schulden DÜRFEN NICHT unbegrenzt ohne erneute Risikobewertung verschoben werden. |
| SASD-QUAL-052 | TODO-, FIXME- oder ähnliche Markierungen SOLLTEN auf ein nachverfolgbares Arbeitselement verweisen, wenn sie nicht unmittelbar behoben werden. |
| SASD-QUAL-053 | Refactoring SOLLTE kontinuierlich und in kontrollierten Schritten erfolgen. |
| SASD-QUAL-054 | Refactoring MUSS durch angemessene Tests, Reviews oder Vergleichsnachweise abgesichert werden. |

### 4.7 Abhängigkeiten und Kompatibilität

| ID | Anforderung |
|---|---|
| SASD-QUAL-060 | Abhängigkeiten MÜSSEN einen erkennbaren Nutzen besitzen und aktiv gepflegt oder vertretbar stabil sein. |
| SASD-QUAL-061 | Versionen und Kompatibilitätsgrenzen SOLLTEN reproduzierbar festgelegt werden. |
| SASD-QUAL-062 | Veraltete, nicht unterstützte oder bekannte kritische Abhängigkeiten MÜSSEN bewertet und mit einem Maßnahmenplan versehen werden. |
| SASD-QUAL-063 | Ein Upgrade MUSS hinsichtlich Verhalten, Daten, Sicherheit, Build, Tests und Deployment geprüft werden. |

### 4.8 Beobachtbarkeit und Diagnose

| ID | Anforderung |
|---|---|
| SASD-QUAL-070 | Fehler MÜSSEN mit vertretbarem Aufwand diagnostizierbar sein. |
| SASD-QUAL-071 | Relevante Fehlerzustände MÜSSEN verständlich protokolliert oder dem Nutzer angemessen angezeigt werden. |
| SASD-QUAL-072 | Protokollierung DARF NICHT unnötig Geheimnisse oder personenbezogene Daten offenlegen. |
| SASD-QUAL-073 | Production-Systeme MÜSSEN für kritische Betriebszustände geeignete Überwachungs- und Diagnosemöglichkeiten besitzen. |

### 4.9 Kontinuierliche Verbesserung

| ID | Anforderung |
|---|---|
| SASD-QUAL-080 | Wiederkehrende Fehler und manuelle Problemstellen SOLLTEN als Verbesserungskandidaten behandelt werden. |
| SASD-QUAL-081 | Nach wesentlichen Vorfällen, Releases oder Migrationen SOLLTEN Lessons Learned festgehalten werden. |
| SASD-QUAL-082 | Qualitätsregeln MÜSSEN angepasst werden, wenn sie erkennbar keinen Nutzen liefern oder relevante Risiken nicht erfassen. |

## 5. Definition-of-Done-Baseline

Eine Änderung ist grundsätzlich erst fertig, wenn:

- Zweck und Anforderung klar sind,
- Implementierung und Konfiguration vollständig sind,
- relevante Tests erfolgreich sind,
- Dokumentation und Beispiele aktualisiert sind,
- Sicherheits- und Datenschutzfolgen bewertet sind,
- keine unbegründeten Pflichtwarnungen oder bekannten kritischen Fehler offen sind,
- Migration und Rückwärtskompatibilität berücksichtigt sind,
- die Änderung integrierbar und nachvollziehbar versioniert ist.

## 6. Zuordnung zu Qualitätsstufen

| Maßnahme | Minimum | Recommended | Production |
|---|---|---|---|
| Qualitätsziele | kritische Ziele SOLLTE | MUSS | MUSS mit Nachweisen |
| Definition of Done | kompakt MUSS | MUSS | MUSS und releasegebunden |
| Formatierung / Linting | KANN | SOLLTE | MUSS für relevante Artefakte |
| statische Analyse | KANN | SOLLTE | MUSS |
| Review | risikobasiert KANN | wesentliche Änderungen SOLLTE | wesentliche Änderungen MUSS |
| technische Schulden | kritische Lücken MUSS | MUSS | MUSS mit Frist/Risiko |
| Beobachtbarkeit | Fehlerausgabe MUSS | strukturierte Diagnose SOLLTE | Monitoring und Diagnose MUSS |

## 7. Verantwortlichkeiten

Projektverantwortliche setzen Qualitätsziele. Entwickler erfüllen Definition of Done und halten Schulden sichtbar. Reviewer bewerten Risiko und Verständlichkeit. Maintainer pflegen Prüfregeln und behandeln Findings.

## 8. Nachweise und Prüfkriterien

Geeignete Nachweise sind Definition of Done, CI-Protokolle, Analyzerberichte, Reviews, Testberichte, technische-Schulden-Register, Qualitätsmetriken und Lessons Learned.

## 9. Ausnahmen und Abweichungen

Eine Ausnahme von automatisierten Prüfungen MUSS den Grund, den Umfang, das Risiko und eine erneute Bewertung benennen.

## 10. Verwandte Dokumente

- [Qualitätsstufen](QUALITY-LEVELS.md)
- [Teststandard](TESTING.md)
- [Sicherheitsstandard](SECURITY.md)
- [Dokumentationsstandard](DOCUMENTATION.md)
