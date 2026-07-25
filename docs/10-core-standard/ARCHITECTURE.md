---
title: "Architekturstandard"
document-id: SASD-CORE-003
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
depends-on: [SASD-FND-003, SASD-GOV-001, SASD-CORE-002, SASD-CORE-006]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Architekturstandard

## 1. Zweck

Dieses Dokument definiert technologieunabhängige Anforderungen an Systemstruktur, Verantwortlichkeiten, Abhängigkeiten, Qualitätsattribute und Architekturentscheidungen.

## 2. Geltungsbereich

Der Standard gilt für Software, Infrastruktur, Datenplattformen, Automatisierungen und hybride technische Systeme. Er schreibt keinen bestimmten Architekturstil vor. Clean Architecture, Schichtenmodelle, modulare Monolithen, Services oder Skriptstrukturen sind Mittel zum Zweck und müssen zum Projekt passen.

## 3. Architekturprinzipien

- Architektur dient den Anforderungen und Risiken des Projekts.
- Komplexität muss begründet sein.
- Verantwortlichkeiten und Grenzen müssen erkennbar sein.
- Abhängigkeiten sollen bewusst, überprüfbar und austauschbar sein.
- Entscheidungen müssen mit dem tatsächlichen Projektstand übereinstimmen.
- Sicherheit, Betrieb und Wartung sind Architekturthemen.

## 4. Normative Anforderungen

### 4.1 Systemkontext

| ID | Anforderung |
|---|---|
| SASD-ARCH-001 | Zweck, Systemgrenze, Nutzergruppen und wesentliche externe Systeme MÜSSEN erkennbar sein. |
| SASD-ARCH-002 | Ein Systemkontext MUSS Ein- und Ausgaben, Datenquellen, Integrationen und Vertrauensgrenzen in angemessenem Umfang zeigen. |
| SASD-ARCH-003 | Annahmen über Netzwerk, Identitäten, Dateisysteme, Laufzeitumgebungen oder externe Dienste SOLLTEN dokumentiert werden. |
| SASD-ARCH-004 | Nicht zum Projekt gehörende Verantwortlichkeiten SOLLTEN ausdrücklich abgegrenzt werden, wenn Verwechslungen wahrscheinlich sind. |

### 4.2 Komponenten und Verantwortlichkeiten

| ID | Anforderung |
|---|---|
| SASD-ARCH-010 | Wesentliche Komponenten, Module oder Arbeitsbereiche MÜSSEN eine klar beschriebene Verantwortung besitzen. |
| SASD-ARCH-011 | Eine Komponente SOLLTE einen kohärenten Zweck besitzen und nicht zu einer unkontrollierten Sammlung fachfremder Funktionen werden. |
| SASD-ARCH-012 | Gemeinsam genutzte Funktionen MÜSSEN hinsichtlich Ownership, Stabilität und Abhängigkeiten betrachtet werden. |
| SASD-ARCH-013 | Architekturgrenzen MÜSSEN im Code, in der Konfiguration oder in der Repository-Struktur soweit möglich erkennbar sein. |
| SASD-ARCH-014 | Eine zusätzliche Schicht, ein Service oder ein Framework SOLLTE nur eingeführt werden, wenn der Nutzen die zusätzliche Komplexität rechtfertigt. |

### 4.3 Abhängigkeiten

| ID | Anforderung |
|---|---|
| SASD-ARCH-020 | Abhängigkeiten zwischen wesentlichen Komponenten MÜSSEN bekannt und nachvollziehbar sein. |
| SASD-ARCH-021 | Zirkuläre Abhängigkeiten SOLLTEN vermieden werden. Unvermeidbare Zyklen MÜSSEN begründet und kontrolliert werden. |
| SASD-ARCH-022 | Fachliche Kernlogik SOLLTE nicht unnötig an Benutzeroberfläche, konkrete Persistenz oder externe Dienste gekoppelt sein. |
| SASD-ARCH-023 | Abhängigkeiten zu externen Produkten, APIs und Diensten MÜSSEN hinsichtlich Ausfall, Versionierung, Lizenz, Sicherheit und Austauschbarkeit bewertet werden. |
| SASD-ARCH-024 | Nicht verwendete oder unbegründete Abhängigkeiten MÜSSEN entfernt werden. |

### 4.4 Daten und Zustände

| ID | Anforderung |
|---|---|
| SASD-ARCH-030 | Wesentliche Datenobjekte, Zuständigkeiten, Speicherorte und Lebenszyklen MÜSSEN dokumentiert sein. |
| SASD-ARCH-031 | Datenflüsse über Vertrauens- oder Systemgrenzen MÜSSEN identifizierbar sein. |
| SASD-ARCH-032 | Integritäts-, Vertraulichkeits-, Aufbewahrungs- und Löschanforderungen MÜSSEN in Architekturentscheidungen berücksichtigt werden. |
| SASD-ARCH-033 | Datenformate und Schnittstellen SOLLTEN versioniert oder migrationsfähig gestaltet sein, wenn sie längerfristig gespeichert oder extern genutzt werden. |
| SASD-ARCH-034 | Versteckte globale Zustände und nicht dokumentierte Seiteneffekte SOLLTEN vermieden werden. |

### 4.5 Qualitätsattribute

| ID | Anforderung |
|---|---|
| SASD-ARCH-040 | Relevante Qualitätsattribute MÜSSEN priorisiert und durch Architekturmaßnahmen unterstützt werden. |
| SASD-ARCH-041 | Zielkonflikte, beispielsweise zwischen Sicherheit, Bedienbarkeit, Performance und Einfachheit, MÜSSEN bei wesentlichen Entscheidungen dokumentiert werden. |
| SASD-ARCH-042 | Architekturentscheidungen DÜRFEN NICHT ausschließlich auf hypothetische Skalierungs- oder Erweiterungsanforderungen gestützt werden. |
| SASD-ARCH-043 | Für Production MÜSSEN Ausfallmodi, Wiederherstellung, Beobachtbarkeit und Kapazitätsgrenzen betrachtet werden. |
| SASD-ARCH-044 | Barrierefreiheit und Internationalisierung SOLLTEN berücksichtigt werden, wenn Nutzeroberflächen oder öffentliche Inhalte entstehen. |

### 4.6 Sicherheit und Datenschutz

| ID | Anforderung |
|---|---|
| SASD-ARCH-050 | Vertrauensgrenzen, Identitäten, Berechtigungen und sensible Daten MÜSSEN in der Architektur berücksichtigt werden. |
| SASD-ARCH-051 | Sicherheitskontrollen SOLLTEN möglichst nahe an der zu schützenden Grenze und zusätzlich durch übergreifende Schutzmaßnahmen umgesetzt werden. |
| SASD-ARCH-052 | Sicherheitsrelevante Entscheidungen DÜRFEN NICHT allein auf Geheimhaltung der Architektur beruhen. |
| SASD-ARCH-053 | Externe Eingaben MÜSSEN als nicht vertrauenswürdig behandelt werden, bis sie angemessen validiert wurden. |
| SASD-ARCH-054 | Datenschutz durch Datenminimierung, Zweckbindung und begrenzte Aufbewahrung MUSS berücksichtigt werden, wenn personenbezogene Daten verarbeitet werden. |

### 4.7 Laufzeit, Deployment und Betrieb

| ID | Anforderung |
|---|---|
| SASD-ARCH-060 | Unterstützte Laufzeit- und Zielumgebungen MÜSSEN dokumentiert sein. |
| SASD-ARCH-061 | Deployment-Einheiten, Konfigurationsquellen und externe Voraussetzungen MÜSSEN für Recommended und Production beschrieben werden. |
| SASD-ARCH-062 | Konfiguration MUSS von Geheimnissen unterscheidbar und soweit sinnvoll von der Implementierung getrennt sein. |
| SASD-ARCH-063 | Für Production MÜSSEN Überwachung, Diagnose, Backup und Wiederherstellung architektonisch berücksichtigt werden. |
| SASD-ARCH-064 | Lokale Entwicklungs-, Test- und Produktivumgebungen SOLLTEN in relevanten Eigenschaften vergleichbar oder Unterschiede ausdrücklich dokumentiert sein. |

### 4.8 Architekturentscheidungen

| ID | Anforderung |
|---|---|
| SASD-ARCH-070 | Wesentliche, schwer umkehrbare oder risikoreiche Architekturentscheidungen MÜSSEN als ADR oder gleichwertiger Entscheidungsnachweis dokumentiert werden. |
| SASD-ARCH-071 | Ein Entscheidungsnachweis MUSS mindestens Kontext, Entscheidung, Alternativen und Konsequenzen enthalten. |
| SASD-ARCH-072 | Ersetzte Entscheidungen MÜSSEN als superseded gekennzeichnet werden und auf ihre Nachfolge verweisen. |
| SASD-ARCH-073 | Architekturentscheidungen DÜRFEN NICHT rückwirkend verfälscht werden. Neue Erkenntnisse werden durch neue oder aktualisierte Entscheidungen dokumentiert. |
| SASD-ARCH-074 | Architektur und Implementierung MÜSSEN regelmäßig auf erkennbare Abweichungen geprüft werden. |

### 4.9 Evolution und technische Schulden

| ID | Anforderung |
|---|---|
| SASD-ARCH-080 | Bekannte Architekturabweichungen und technische Schulden MÜSSEN sichtbar und priorisierbar sein. |
| SASD-ARCH-081 | Erweiterungspunkte SOLLTEN nur dort geschaffen werden, wo reale oder hinreichend wahrscheinliche Änderungen erwartet werden. |
| SASD-ARCH-082 | Refactoring MUSS durch Tests oder andere angemessene Verifikationsmaßnahmen abgesichert werden. |
| SASD-ARCH-083 | Ein Architekturwechsel MUSS Migration, Kompatibilität, Daten und Rückfallmöglichkeiten berücksichtigen. |

## 5. Dokumentation nach Qualitätsstufe

| Artefakt | Minimum | Recommended | Production |
|---|---|---|---|
| Systemübersicht | einfache Beschreibung MUSS | Kontextdiagramm oder gleichwertig MUSS | geprüfter Kontext mit Vertrauensgrenzen MUSS |
| Komponenten | wichtigste Bereiche SOLLTE | Verantwortlichkeiten und Abhängigkeiten MUSS | zusätzlich Laufzeit- und Ausfallverhalten MUSS |
| ADRs | für kritische Entscheidungen SOLLTE | wesentliche Entscheidungen MUSS | wesentliche und sicherheitsrelevante Entscheidungen MUSS |
| Datenflüsse | bei Relevanz SOLLTE | externe und sensible Flüsse MUSS | vollständige kritische Flüsse und Aufbewahrung MUSS |
| Deployment | Nutzungsschritte MUSS | Deployment-Sicht MUSS | Betriebs-, Monitoring- und Recovery-Sicht MUSS |
| Architekturreview | KANN | vor großen Meilensteinen SOLLTE | vor Releases und wesentlichen Änderungen MUSS |

## 6. Verantwortlichkeiten

Der Projektverantwortliche stellt sicher, dass Architektur dem Scope entspricht. Entwickler halten Implementierung und Dokumentation konsistent. Reviewer prüfen Zielkonflikte, Risiken und unnötige Komplexität. Betreiber bringen Betriebsanforderungen ein.

## 7. Nachweise und Prüfkriterien

Geeignete Nachweise sind Architekturübersicht, Kontext- und Komponentendiagramme, ADRs, Datenflussdarstellungen, Deployment-Dokumentation, Architekturtests und Reviewprotokolle.

## 8. Ausnahmen und Abweichungen

Ein kleines Projekt darf Architektur in README oder einer einzelnen Datei dokumentieren. Es DARF jedoch nicht auf eine verständliche Systemgrenze, Hauptverantwortlichkeiten und kritische Entscheidungen verzichten.

## 9. Verwandte Dokumente

- [Anforderungsmanagement](REQUIREMENTS.md)
- [Sicherheitsstandard](SECURITY.md)
- [Dokumentationsstandard](DOCUMENTATION.md)
- [Wissensmanagement](KNOWLEDGE-MANAGEMENT.md)
- [ADR-Template](../../templates/architecture-decisions/ADR-TEMPLATE.md)
