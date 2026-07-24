---
title: "Wartungsstandard"
document-id: SASD-CORE-011
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
depends-on: [SASD-FND-003, SASD-GOV-001, SASD-CORE-006, SASD-CORE-008, SASD-CORE-009, SASD-CORE-010, SASD-CORE-012]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Wartungsstandard

## 1. Zweck

Dieses Dokument definiert Anforderungen an Ownership, Support, Updates, Diagnose, Backup, Wiederherstellung, Migration, End of Life und Archivierung.

## 2. Geltungsbereich

Wartung beginnt mit dem ersten nutzbaren Projektstand und endet erst mit kontrollierter Ablösung oder Archivierung. Auch nicht dauerhaft betriebene Werkzeuge benötigen einen erkennbaren Wartungsstatus.

## 3. Normative Anforderungen

### 3.1 Ownership und Wartungsstatus

| ID | Anforderung |
|---|---|
| SASD-MNT-001 | Jedes Projekt MUSS einen verantwortlichen Maintainer oder einen ausdrücklich unbetreuten Status besitzen. |
| SASD-MNT-002 | Unterstützte Versionen, Plattformen und Laufzeitumgebungen MÜSSEN auffindbar dokumentiert sein. |
| SASD-MNT-003 | Ein Projekt DARF NICHT den Eindruck aktiver Wartung erwecken, wenn keine Wartung mehr vorgesehen ist. |
| SASD-MNT-004 | Production-Projekte MÜSSEN Vertretung, Übergabe oder Eskalationsweg für kritische Wartungsaufgaben berücksichtigen. |

### 3.2 Support und Fehlerannahme

| ID | Anforderung |
|---|---|
| SASD-MNT-010 | Nutzer MÜSSEN wissen, wie Fehler oder Sicherheitsprobleme gemeldet werden können, soweit das Projekt verteilt oder betrieben wird. |
| SASD-MNT-011 | Fehler MÜSSEN nach Auswirkung, Dringlichkeit, Sicherheitsrelevanz und Reproduzierbarkeit priorisiert werden. |
| SASD-MNT-012 | Supportzusagen DÜRFEN NICHT gemacht werden, wenn sie organisatorisch nicht erfüllbar sind. |
| SASD-MNT-013 | Bekannte Workarounds SOLLTEN dokumentiert und als temporär oder dauerhaft erkennbar sein. |

### 3.3 Updates und Abhängigkeiten

| ID | Anforderung |
|---|---|
| SASD-MNT-020 | Abhängigkeiten und Zielplattformen MÜSSEN regelmäßig auf Supportstatus und relevante Sicherheitsprobleme geprüft werden. |
| SASD-MNT-021 | Updatehäufigkeit MUSS Risiko, Änderungsrate und Betriebsrelevanz berücksichtigen. |
| SASD-MNT-022 | Updates MÜSSEN vor produktiver Einführung angemessen getestet werden. |
| SASD-MNT-023 | Automatische Updates DÜRFEN NICHT ohne geeignete Kontrolle, Rückfallmöglichkeit und Integritätsprüfung eingesetzt werden. |
| SASD-MNT-024 | Nicht mehr unterstützte Laufzeiten oder Abhängigkeiten MÜSSEN einen Upgrade-, Ablöse- oder Risikoakzeptanzplan erhalten. |

### 3.4 Konfiguration und Umgebungsdrift

| ID | Anforderung |
|---|---|
| SASD-MNT-030 | Unterstützte Konfigurationen MÜSSEN dokumentiert sein. |
| SASD-MNT-031 | Production-Konfiguration SOLLTE versioniert, deklarativ oder anderweitig nachvollziehbar verwaltet werden. |
| SASD-MNT-032 | Manuelle Änderungen an produktiven Umgebungen MÜSSEN dokumentiert und soweit möglich in die verwaltete Konfiguration zurückgeführt werden. |
| SASD-MNT-033 | Konfigurationsdrift SOLLTE regelmäßig erkannt und bewertet werden. |
| SASD-MNT-034 | Geheimnisse DÜRFEN NICHT als normale Konfigurationswerte exportiert, versioniert oder protokolliert werden. |

### 3.5 Diagnose und Beobachtbarkeit

| ID | Anforderung |
|---|---|
| SASD-MNT-040 | Ein Projekt MUSS einen angemessenen Weg zur Diagnose typischer Fehler besitzen. |
| SASD-MNT-041 | Recommended-Projekte SOLLTEN strukturierte Logs, Statusinformationen oder Diagnosepakete bereitstellen. |
| SASD-MNT-042 | Production-Systeme MÜSSEN kritische Zustände überwachen und zuständige Personen oder Systeme informieren. |
| SASD-MNT-043 | Diagnoseinformationen MÜSSEN Schutzbedarf und Datenschutz berücksichtigen. |
| SASD-MNT-044 | Uhrzeit, Version, Umgebung und relevante Korrelation SOLLTEN in Diagnoseinformationen nachvollziehbar sein. |

### 3.6 Backup und Wiederherstellung

| ID | Anforderung |
|---|---|
| SASD-MNT-050 | Nicht leicht reproduzierbare Daten und Konfigurationen MÜSSEN entsprechend ihrer Bedeutung gesichert werden. |
| SASD-MNT-051 | Backupumfang, Häufigkeit, Aufbewahrung und Verantwortlichkeit MÜSSEN dokumentiert sein. |
| SASD-MNT-052 | Production-Projekte MÜSSEN Recovery Point Objective und Recovery Time Objective oder gleichwertige Wiederherstellungsziele festlegen, wenn Ausfall oder Datenverlust erheblich wäre. |
| SASD-MNT-053 | Wiederherstellungsverfahren MÜSSEN getestet werden; bei Production regelmäßig und nach wesentlichen Änderungen. |
| SASD-MNT-054 | Backups MÜSSEN vor unberechtigtem Zugriff, Manipulation und unbeabsichtigtem Löschen geschützt werden. |
| SASD-MNT-055 | Ein Backup MUSS unabhängig vom primären Ausfallpfad verfügbar sein, wenn sonst ein gemeinsamer Fehler beide Kopien gefährdet. |

### 3.7 Daten- und Schemamigration

| ID | Anforderung |
|---|---|
| SASD-MNT-060 | Migrationen MÜSSEN versioniert und auf den Zielstand zurückführbar sein. |
| SASD-MNT-061 | Vor risikoreichen Migrationen MUSS ein validiertes Backup oder eine gleichwertige Recovery-Möglichkeit existieren. |
| SASD-MNT-062 | Migrationen MÜSSEN auf Teilfehler, Wiederaufnahme und Kompatibilität geprüft werden. |
| SASD-MNT-063 | Datenverlust oder irreversible Transformationen MÜSSEN ausdrücklich freigegeben und dokumentiert werden. |
| SASD-MNT-064 | Nach der Migration MUSS Integrität anhand definierter Kriterien geprüft werden. |

### 3.8 Vorfälle und Problemmanagement

| ID | Anforderung |
|---|---|
| SASD-MNT-070 | Kritische Vorfälle MÜSSEN stabilisiert, dokumentiert und hinsichtlich Ursache sowie Folgemaßnahmen bewertet werden. |
| SASD-MNT-071 | Wiederkehrende Fehler SOLLTEN einer Ursachenanalyse statt ausschließlich wiederholter Symptombehandlung unterzogen werden. |
| SASD-MNT-072 | Production-Projekte MÜSSEN einen grundlegenden Incident-Ablauf mit Rollen, Kommunikation und Eskalation besitzen. |
| SASD-MNT-073 | Nach relevanten Vorfällen SOLLTEN Lessons Learned und vorbeugende Maßnahmen dokumentiert werden. |

### 3.9 Deprecation und End of Life

| ID | Anforderung |
|---|---|
| SASD-MNT-080 | Die Ablösung von Funktionen, Schnittstellen oder Versionen MUSS rechtzeitig und verständlich kommuniziert werden. |
| SASD-MNT-081 | Ein Deprecation-Hinweis MUSS Ersatz, Frist oder bekannte Migration nennen, soweit verfügbar. |
| SASD-MNT-082 | End of Life MUSS letzten Supportstand, Sicherheitsfolgen und Nachfolgeoptionen nennen. |
| SASD-MNT-083 | Datenexport und Migration SOLLTEN vor Abschaltung ermöglicht werden, wenn Nutzer eigene relevante Daten besitzen. |
| SASD-MNT-084 | Nicht mehr benötigte Zugänge, Secrets, Deployments, Domains und Automatisierungen MÜSSEN kontrolliert deaktiviert werden. |

### 3.10 Archivierung

| ID | Anforderung |
|---|---|
| SASD-MNT-090 | Archivierte Projekte MÜSSEN Status, letzte Version, Lizenz und bekannte Einschränkungen sichtbar behalten. |
| SASD-MNT-091 | Quellstand, Dokumentation und wesentliche Entscheidungen SOLLTEN gemeinsam archiviert werden. |
| SASD-MNT-092 | Archivierung DARF NICHT als Ersatz für notwendige Datenlöschung oder Geheimnisrotation verwendet werden. |
| SASD-MNT-093 | Historische Build- oder Laufzeitabhängigkeiten SOLLTEN dokumentiert werden, wenn spätere Reproduzierbarkeit wichtig ist. |

## 4. Zuordnung zu Qualitätsstufen

| Maßnahme | Minimum | Recommended | Production |
|---|---|---|---|
| Maintainer/Status | MUSS | MUSS | MUSS |
| Updateprüfung | bei Bedarf SOLLTE | regelmäßig MUSS | geplant und risikobasiert MUSS |
| Diagnose | grundlegende Fehlerausgabe MUSS | strukturierte Diagnose SOLLTE | Monitoring und Alerting MUSS |
| Backup | bei nicht reproduzierbaren Daten MUSS | MUSS | MUSS mit Schutz und Zielen |
| Restore-Test | KANN | regelmäßig SOLLTE | regelmäßig MUSS |
| Incident-Prozess | KANN | bei Betrieb SOLLTE | MUSS |
| EOL-Plan | bei Einstellung MUSS | MUSS | MUSS mit Migration und Kommunikation |

## 5. Verantwortlichkeiten

Maintainer pflegen Updates, Supportstatus und Abhängigkeiten. Betreiber verantworten Monitoring, Backup und Recovery. Projektverantwortliche akzeptieren Risiken und planen EOL. Nutzerkommunikation muss einer benannten Rolle zugeordnet sein.

## 6. Nachweise und Prüfkriterien

Geeignete Nachweise sind Wartungsplan, Supportmatrix, Dependency-Report, Monitoringübersicht, Backupplan, Restore-Protokolle, Runbook, Incident-Bericht, Deprecation- und EOL-Hinweise.

## 7. Ausnahmen und Abweichungen

Ein lokal genutztes Wegwerfwerkzeug benötigt keinen umfassenden Betriebsplan, MUSS aber Status, Nutzung und Verlustfolgen nachvollziehbar machen.

## 8. Verwandte Dokumente

- [Release-Standard](RELEASES.md)
- [Sicherheitsstandard](SECURITY.md)
- [Wissensmanagement](KNOWLEDGE-MANAGEMENT.md)
- [Projektarchivierung](../30-processes/PROJECT-ARCHIVAL.md)
