---
title: "Sicherheitsstandard"
document-id: SASD-CORE-008
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
depends-on: [SASD-FND-003, SASD-GOV-001, SASD-CORE-002, SASD-CORE-003, SASD-CORE-006, SASD-CORE-007]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Sicherheitsstandard

## 1. Zweck

Dieses Dokument definiert grundlegende Anforderungen für sichere Entwicklung, Datenschutz, Abhängigkeiten, Software Supply Chain, Geheimnisse, Vorfälle und Wiederherstellung.

## 2. Geltungsbereich

Der Standard gilt für alle technischen Projekte. Die Tiefe der Maßnahmen richtet sich nach Schutzbedarf, Angriffsfläche und Qualitätsstufe. Dieses Dokument ersetzt keine projektspezifische Bedrohungsanalyse und keine gesetzlichen oder branchenspezifischen Vorgaben.

## 3. Sicherheitsgrundsätze

- Sicherheit beginnt bei Anforderungen und Architektur.
- Verantwortung bleibt bei Menschen und Projektverantwortlichen.
- Systeme werden mit möglichst geringen Rechten betrieben.
- Eingaben und externe Komponenten werden nicht blind vertraut.
- Sichere Standardwerte sind unsicheren Opt-in-Konfigurationen vorzuziehen.
- Sensible Daten werden minimiert und nur zweckgebunden verarbeitet.
- Sicherheitsmaßnahmen müssen wartbar und überprüfbar sein.

## 4. Normative Anforderungen

### 4.1 Schutzbedarf und Risiken

| ID | Anforderung |
|---|---|
| SASD-SEC-001 | Ein Projekt MUSS relevante Werte, Daten, Dienste und Vertrauensgrenzen identifizieren. |
| SASD-SEC-002 | Vertraulichkeit, Integrität und Verfügbarkeit MÜSSEN für wesentliche Assets bewertet werden. |
| SASD-SEC-003 | Recommended-Projekte MÜSSEN eine dokumentierte Sicherheitsrisikobetrachtung durchführen. |
| SASD-SEC-004 | Production-Projekte MÜSSEN ein Bedrohungsmodell oder eine gleichwertige strukturierte Analyse pflegen. |
| SASD-SEC-005 | Risiken MÜSSEN vermieden, reduziert, übertragen oder ausdrücklich akzeptiert werden. |

### 4.2 Sichere Anforderungen und Architektur

| ID | Anforderung |
|---|---|
| SASD-SEC-010 | Sicherheits- und Datenschutzanforderungen MÜSSEN als prüfbare Projektanforderungen behandelt werden. |
| SASD-SEC-011 | Sicherheitsrelevante Architekturentscheidungen MÜSSEN dokumentiert werden. |
| SASD-SEC-012 | Systeme MÜSSEN nach dem Prinzip geringstmöglicher Rechte entworfen und betrieben werden. |
| SASD-SEC-013 | Sicherheitskontrollen DÜRFEN NICHT allein auf verborgenem Code, geheimen URLs oder unbekannten Dateipfaden beruhen. |
| SASD-SEC-014 | Standardkonfigurationen SOLLTEN den sichersten praktikablen Zustand herstellen. |

### 4.3 Identitäten und Berechtigungen

| ID | Anforderung |
|---|---|
| SASD-SEC-020 | Identitäten MÜSSEN eindeutig und Berechtigungen nachvollziehbar sein, soweit das Projekt Authentifizierung oder Autorisierung benötigt. |
| SASD-SEC-021 | Geteilte privilegierte Konten SOLLTEN vermieden werden. |
| SASD-SEC-022 | Berechtigungen MÜSSEN regelmäßig und bei Rollenwechseln überprüft werden. |
| SASD-SEC-023 | Authentifizierungsdaten DÜRFEN NICHT unverschlüsselt oder unnötig dauerhaft gespeichert werden. |
| SASD-SEC-024 | Fehler- und Statusmeldungen DÜRFEN NICHT unnötig Informationen über Konten, Schlüssel oder interne Sicherheitsdetails preisgeben. |

### 4.4 Geheimnisse und Schlüssel

| ID | Anforderung |
|---|---|
| SASD-SEC-030 | Geheimnisse DÜRFEN NICHT in Quellcode, Dokumentation, Tests, Logs oder Repository-Historie eingecheckt werden. |
| SASD-SEC-031 | Geheimnisse MÜSSEN über geeignete Secret Stores, Umgebungsmechanismen oder geschützte Konfiguration bereitgestellt werden. |
| SASD-SEC-032 | Zugriff auf Geheimnisse MUSS auf notwendige Personen, Prozesse und Umgebungen begrenzt sein. |
| SASD-SEC-033 | Kompromittierte oder versehentlich veröffentlichte Geheimnisse MÜSSEN unverzüglich widerrufen oder rotiert werden. |
| SASD-SEC-034 | Schlüsselrotation, Ablauf und Wiederherstellung SOLLTEN für langlebige oder produktive Systeme vorgesehen werden. |
| SASD-SEC-035 | Beispielwerte MÜSSEN eindeutig nicht produktiv sein. |

### 4.5 Eingaben, Ausgaben und Datenverarbeitung

| ID | Anforderung |
|---|---|
| SASD-SEC-040 | Externe Eingaben MÜSSEN entsprechend ihrem Kontext validiert werden. |
| SASD-SEC-041 | Ausgaben MÜSSEN kontextgerecht kodiert oder geschützt werden, wenn sie in Interpreter, Abfragen, Shells, Markup oder andere ausführende Kontexte gelangen. |
| SASD-SEC-042 | Datenmengen und Datentypen MÜSSEN auf den erforderlichen Zweck begrenzt werden. |
| SASD-SEC-043 | Dateipfade, Uploads, Archive und Deserialisierung MÜSSEN gegen projektrelevante Missbrauchsfälle abgesichert werden. |
| SASD-SEC-044 | Sicherheitsrelevante Validierung DARF NICHT ausschließlich in einer leicht umgehbaren Benutzerschnittstelle stattfinden. |

### 4.6 Kryptographie

| ID | Anforderung |
|---|---|
| SASD-SEC-050 | Eigene kryptographische Algorithmen oder Protokolle DÜRFEN NICHT entwickelt werden, wenn etablierte und geeignete Verfahren verfügbar sind. |
| SASD-SEC-051 | Kryptographische Verfahren MÜSSEN dem Schutzbedarf und aktuellen fachlichen Empfehlungen entsprechen. |
| SASD-SEC-052 | Schlüssel, Nonces, Initialisierungsvektoren und Zufallswerte MÜSSEN mit geeigneten kryptographischen Mechanismen erzeugt und verwaltet werden. |
| SASD-SEC-053 | Verschlüsselung DARF NICHT als Ersatz für Zugriffskontrolle, Datenminimierung oder sichere Schlüsselverwaltung betrachtet werden. |
| SASD-SEC-054 | Passwörter MÜSSEN mit einem geeigneten passwortspezifischen Hashverfahren gespeichert werden, wenn das Projekt Passwörter selbst verwaltet. |

### 4.7 Abhängigkeiten und Supply Chain

| ID | Anforderung |
|---|---|
| SASD-SEC-060 | Direkte Abhängigkeiten MÜSSEN identifizierbar und versionierbar sein. |
| SASD-SEC-061 | Herkunft, Wartungsstatus, Lizenz und Sicherheitslage neuer kritischer Abhängigkeiten MÜSSEN bewertet werden. |
| SASD-SEC-062 | Bekannte kritische Schwachstellen MÜSSEN zeitnah bewertet und behandelt werden. |
| SASD-SEC-063 | Automatisierte Builds MÜSSEN kontrollierte Quellen und so wenig Berechtigungen wie möglich verwenden. |
| SASD-SEC-064 | Externe Buildschritte, Plugins und CI-Actions MÜSSEN auf Herkunft, Berechtigungen und unveränderliche Versionierung geprüft werden. |
| SASD-SEC-065 | Production-Projekte MÜSSEN eine Software Bill of Materials oder eine gleichwertige Komponentenübersicht für veröffentlichte Artefakte erzeugen, soweit technisch möglich. |
| SASD-SEC-066 | Releaseartefakte SOLLTEN auf Quellstand und Buildprozess zurückführbar sein. |

### 4.8 Datenschutz

| ID | Anforderung |
|---|---|
| SASD-SEC-070 | Personenbezogene Daten MÜSSEN ausschließlich für einen dokumentierten Zweck und in erforderlichem Umfang verarbeitet werden. |
| SASD-SEC-071 | Aufbewahrungs- und Löschregeln MÜSSEN festgelegt werden, wenn personenbezogene oder vertrauliche Daten gespeichert werden. |
| SASD-SEC-072 | Test- und Entwicklungsdaten SOLLTEN anonymisiert, synthetisch oder anderweitig geschützt sein. |
| SASD-SEC-073 | Produktive Daten DÜRFEN NICHT ohne ausdrückliche Freigabe und Schutzmaßnahmen in Entwicklungs- oder KI-Systeme übertragen werden. |
| SASD-SEC-074 | Nutzer MÜSSEN über relevante Datenverarbeitung informiert werden, soweit dies rechtlich oder funktional erforderlich ist. |

### 4.9 Logging und Monitoring

| ID | Anforderung |
|---|---|
| SASD-SEC-080 | Sicherheitsrelevante Ereignisse SOLLTEN in angemessenem Umfang protokolliert werden. |
| SASD-SEC-081 | Logs DÜRFEN NICHT unnötig Geheimnisse, vollständige Zugangsdaten oder sensible Inhalte enthalten. |
| SASD-SEC-082 | Zugriff, Aufbewahrung und Löschung von Logs MÜSSEN dem Schutzbedarf entsprechen. |
| SASD-SEC-083 | Production-Systeme MÜSSEN kritische Sicherheits- und Verfügbarkeitsereignisse erkennbar machen. |
| SASD-SEC-084 | Zeitstempel und Ereigniskontext SOLLTEN eine nachträgliche Untersuchung unterstützen. |

### 4.10 Backups und Wiederherstellung

| ID | Anforderung |
|---|---|
| SASD-SEC-090 | Schutzwürdige oder nicht leicht reproduzierbare Daten MÜSSEN durch geeignete Backups oder Replikation abgesichert werden. |
| SASD-SEC-091 | Backups MÜSSEN mindestens denselben angemessenen Schutz wie die Primärdaten erhalten. |
| SASD-SEC-092 | Production-Wiederherstellungsverfahren MÜSSEN regelmäßig getestet werden. |
| SASD-SEC-093 | Recovery-Ziele SOLLTEN für geschäfts- oder betriebsrelevante Systeme festgelegt werden. |
| SASD-SEC-094 | Ein Backup DARF NICHT allein aufgrund seines erfolgreichen Erstellungsprotokolls als wiederherstellbar gelten. |

### 4.11 Schwachstellen und Vorfälle

| ID | Anforderung |
|---|---|
| SASD-SEC-100 | Ein öffentlicher oder verteilter Dienst MUSS einen geeigneten Weg zur vertraulichen Meldung von Schwachstellen anbieten. |
| SASD-SEC-101 | Sicherheitsmeldungen MÜSSEN nach Schwere, Ausnutzbarkeit und Auswirkung bewertet werden. |
| SASD-SEC-102 | Production-Projekte MÜSSEN Verantwortlichkeiten und grundlegende Schritte für Sicherheitsvorfälle dokumentieren. |
| SASD-SEC-103 | Behebung, Kommunikation, Rotation, Update und Lessons Learned MÜSSEN bei relevanten Vorfällen berücksichtigt werden. |
| SASD-SEC-104 | Sicherheitsdetails DÜRFEN NICHT unnötig veröffentlicht werden, solange dies Betroffene zusätzlich gefährden würde. |

## 5. Zuordnung zu Qualitätsstufen

| Maßnahme | Minimum | Recommended | Production |
|---|---|---|---|
| Security Baseline | MUSS | MUSS | MUSS |
| Risikoanalyse | kompakt SOLLTE | MUSS | MUSS |
| Threat Model | KANN | bei erhöhtem Risiko SOLLTE | MUSS |
| Secret Management | MUSS | MUSS | MUSS mit Rotation |
| Dependency Scanning | KANN | SOLLTE | MUSS |
| SBOM | KANN | bei Verteilung SOLLTE | MUSS soweit möglich |
| Security Review | kritische Bereiche SOLLTE | vor Releases SOLLTE | vor wesentlichen Releases MUSS |
| Incident-Verfahren | KANN | bei Betrieb SOLLTE | MUSS |
| Restore-Test | KANN | regelmäßig SOLLTE | regelmäßig MUSS |

## 6. Verantwortlichkeiten

Der Projektverantwortliche akzeptiert Restrisiken. Entwickler setzen Sicherheitsanforderungen um. Maintainer pflegen Abhängigkeiten und Sicherheitsupdates. Betreiber schützen Laufzeit, Backups und Logs. Reviewer prüfen risikoreiche Änderungen.

## 7. Nachweise und Prüfkriterien

Geeignete Nachweise sind Schutzbedarfsanalyse, Threat Model, Security-Checkliste, Abhängigkeitsbericht, SBOM, Secret-Scan, Security-Tests, Restore-Protokoll, Incident-Plan und dokumentierte Risikoakzeptanzen.

## 8. Ausnahmen und Abweichungen

Sicherheitsabweichungen MÜSSEN Risiko, betroffene Assets, Kompensationsmaßnahmen, Owner und Ablaufdatum benennen. Dauerhafte pauschale Ausnahmen sind unzulässig.

## 9. Verwandte Dokumente

- [Architekturstandard](ARCHITECTURE.md)
- [Teststandard](TESTING.md)
- [Wartungsstandard](MAINTENANCE.md)
- [KI-gestützte Entwicklung](AI-ASSISTED-DEVELOPMENT.md)
- [Security Baseline Checkliste](../../checklists/security/SECURITY-BASELINE-CHECKLIST.md)
