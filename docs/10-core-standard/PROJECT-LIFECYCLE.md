---
title: "Projektlebenszyklus"
document-id: SASD-CORE-001
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
depends-on: [SASD-FND-002, SASD-FND-003, SASD-GOV-001, SASD-CORE-006]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Projektlebenszyklus

## 1. Zweck

Dieses Dokument definiert einen technologieunabhängigen Lebenszyklus für SASD-Projekte. Er beschreibt erforderliche Ergebnisse und Entscheidungspunkte, schreibt jedoch kein starres Wasserfallmodell vor.

## 2. Geltungsbereich

Der Lebenszyklus gilt für neue Projekte, wesentliche Erweiterungen und kontrollierte Modernisierungen bestehender Projekte. Phasen dürfen iterativ, überlappend oder mehrfach durchlaufen werden, solange Entscheidungen und Ergebnisse nachvollziehbar bleiben.

## 3. Lebenszyklusphasen

```text
Idee
  -> Initiierung und Klassifikation
  -> Exploration und Anforderungen
  -> Planung und Architektur
  -> Umsetzung
  -> Verifikation
  -> Release und Einführung
  -> Betrieb und Wartung
  -> Ablösung oder Archivierung
```

## 4. Normative Anforderungen

### 4.1 Allgemeine Steuerung

| ID | Anforderung |
|---|---|
| SASD-LC-001 | Jedes Projekt MUSS einen benannten Projektverantwortlichen besitzen. |
| SASD-LC-002 | Zweck, Scope, Qualitätsstufe, Status und nächster geplanter Meilenstein MÜSSEN auffindbar dokumentiert sein. |
| SASD-LC-003 | Phasen dürfen iterativ bearbeitet werden; wesentliche Entscheidungen und Freigaben MÜSSEN dennoch nachvollziehbar bleiben. |
| SASD-LC-004 | Ein Projekt MUSS offene Risiken, bekannte Einschränkungen und wesentliche technische Schulden sichtbar führen. |
| SASD-LC-005 | Ein Projekt DARF nicht veröffentlicht oder produktiv eingesetzt werden, wenn bekannte nicht akzeptierte Risiken den vorgesehenen Einsatz unvertretbar machen. |

### 4.2 Idee und Initiierung

Ziel ist die Klärung, ob ein Projekt begonnen werden soll.

| ID | Anforderung |
|---|---|
| SASD-LC-010 | Das zu lösende Problem, die erwartete Zielgruppe und der beabsichtigte Nutzen MÜSSEN beschrieben werden. |
| SASD-LC-011 | Scope und ausdrückliche Nicht-Ziele MÜSSEN mindestens kompakt dokumentiert werden. |
| SASD-LC-012 | Die primäre Qualitätsstufe und anwendbare Profile MÜSSEN gewählt werden. |
| SASD-LC-013 | Wesentliche Machbarkeits-, Rechts-, Sicherheits-, Datenschutz- und Betriebsrisiken SOLLTEN vor der Umsetzungsentscheidung identifiziert werden. |
| SASD-LC-014 | Doppelentwicklungen und bestehende geeignete Lösungen SOLLTEN geprüft werden, wenn die Recherche im Verhältnis zum Projektwert sinnvoll ist. |

**Phasenergebnis:** dokumentierter Projektauftrag oder begründete Entscheidung gegen die Umsetzung.

### 4.3 Exploration und Anforderungen

| ID | Anforderung |
|---|---|
| SASD-LC-020 | Anforderungen MÜSSEN so weit geklärt sein, dass der nächste Meilenstein prüfbar geplant werden kann. |
| SASD-LC-021 | Annahmen, Unsicherheiten und offene Fragen MÜSSEN von bestätigten Anforderungen unterscheidbar sein. |
| SASD-LC-022 | Akzeptanzkriterien MÜSSEN für wesentliche Funktionen und Qualitätsziele festgelegt werden. |
| SASD-LC-023 | Anforderungen SOLLTEN priorisiert werden. |
| SASD-LC-024 | Änderungen am Scope MÜSSEN hinsichtlich Aufwand, Architektur, Sicherheit, Tests, Dokumentation und Terminplanung bewertet werden. |

**Phasenergebnis:** priorisierte und prüfbare Grundlage für Architektur und Umsetzung.

### 4.4 Planung und Architektur

| ID | Anforderung |
|---|---|
| SASD-LC-030 | Das Projekt MUSS in nachvollziehbare Meilensteine oder Lieferabschnitte gegliedert werden. |
| SASD-LC-031 | Die Architektur MUSS für die gewählte Qualitätsstufe ausreichend dokumentiert sein. |
| SASD-LC-032 | Wesentliche technische Entscheidungen MÜSSEN mit Kontext und Begründung festgehalten werden. |
| SASD-LC-033 | Abhängigkeiten, externe Dienste, Datenflüsse und Betriebsannahmen SOLLTEN vor der Implementierung risikoreicher Teile geklärt werden. |
| SASD-LC-034 | Für wesentliche Risiken SOLLTEN Prototypen oder technische Spikes verwendet werden, bevor große irreversible Investitionen erfolgen. |

**Phasenergebnis:** umsetzbare Architektur, Meilensteinplan und bekannte Risiken.

### 4.5 Umsetzung

| ID | Anforderung |
|---|---|
| SASD-LC-040 | Änderungen MÜSSEN auf nachvollziehbare Anforderungen, Fehler, Wartungsziele oder technische Entscheidungen zurückführbar sein. |
| SASD-LC-041 | Implementierung, Tests und Dokumentation SOLLTEN innerhalb desselben Meilensteins gemeinsam gepflegt werden. |
| SASD-LC-042 | Wiederholbare Prüfungen SOLLTEN automatisiert werden, sobald manueller Aufwand oder Fehlerrisiko dies rechtfertigen. |
| SASD-LC-043 | Temporäre Umgehungen MÜSSEN als solche gekennzeichnet und mit einer Nachverfolgung versehen werden. |
| SASD-LC-044 | Geheimnisse, produktive Zugangsdaten und unnötige personenbezogene Daten DÜRFEN NICHT in Quellcode, Tests oder Repository-Historie eingecheckt werden. |

**Phasenergebnis:** integrierter, dokumentierter und prüfbarer Projektstand.

### 4.6 Verifikation

| ID | Anforderung |
|---|---|
| SASD-LC-050 | Vor einem Release MUSS geprüft werden, ob die Akzeptanzkriterien des Lieferumfangs erfüllt sind. |
| SASD-LC-051 | Bekannte Fehler und Einschränkungen MÜSSEN bewertet und für Nutzer oder Betreiber angemessen dokumentiert werden. |
| SASD-LC-052 | Sicherheits-, Datenschutz-, Installations-, Upgrade- und Wiederherstellungsrisiken MÜSSEN entsprechend dem Projektkontext geprüft werden. |
| SASD-LC-053 | Fehlgeschlagene Pflichtprüfungen DÜRFEN NICHT ohne dokumentierte Freigabe ignoriert werden. |
| SASD-LC-054 | Die Definition of Done MUSS für den Releaseumfang erfüllt oder mit genehmigten Abweichungen versehen sein. |

**Phasenergebnis:** begründete Releasefreigabe oder dokumentierte Rückgabe an Planung und Umsetzung.

### 4.7 Release und Einführung

| ID | Anforderung |
|---|---|
| SASD-LC-060 | Ein Release MUSS eindeutig versioniert oder anderweitig unverwechselbar identifizierbar sein. |
| SASD-LC-061 | Release Notes oder ein Changelog MÜSSEN wesentliche Änderungen, bekannte Einschränkungen und notwendige Migrationsschritte nennen. |
| SASD-LC-062 | Veröffentlichung und Deployment MÜSSEN für Recommended und Production nachvollziehbar reproduzierbar sein. |
| SASD-LC-063 | Für Production MUSS ein Rollback-, Wiederherstellungs- oder anderweitiger Schadensbegrenzungsweg vor der Einführung festgelegt sein. |
| SASD-LC-064 | Veröffentlicht werden DARF nur ein Zustand, der den dokumentierten Freigabekriterien entspricht. |

**Phasenergebnis:** identifizierbares, dokumentiertes und unterstützbares Release.

### 4.8 Betrieb und Wartung

| ID | Anforderung |
|---|---|
| SASD-LC-070 | Verantwortlichkeit für Wartung, Sicherheitsupdates und Nutzerkommunikation MUSS geklärt sein. |
| SASD-LC-071 | Fehler, Sicherheitsprobleme und Änderungswünsche MÜSSEN nach Risiko und Auswirkung priorisiert werden. |
| SASD-LC-072 | Abhängigkeiten und Laufzeitumgebungen SOLLTEN regelmäßig auf Supportstatus und Risiken geprüft werden. |
| SASD-LC-073 | Betriebs- und Wiederherstellungswissen MUSS in angemessenem Umfang dokumentiert werden. |
| SASD-LC-074 | Lessons Learned SOLLTEN nach wesentlichen Releases oder Vorfällen in Projekt oder Standard zurückgeführt werden. |

### 4.9 Ablösung und Archivierung

| ID | Anforderung |
|---|---|
| SASD-LC-080 | Das Ende aktiver Wartung MUSS klar kommuniziert werden. |
| SASD-LC-081 | Datenexport, Migration, Deinstallation und Aufbewahrung MÜSSEN entsprechend dem Projektkontext geregelt sein. |
| SASD-LC-082 | Archivierte Repositories MÜSSEN Status, letzte unterstützte Version und bekannte Risiken sichtbar nennen. |
| SASD-LC-083 | Geheimnisse und nicht benötigte sensible Daten MÜSSEN vor Archivierung entfernt oder sicher behandelt werden. |
| SASD-LC-084 | Historische Releases und Entscheidungen SOLLTEN erhalten bleiben, soweit keine rechtlichen oder sicherheitsbezogenen Gründe dagegensprechen. |

## 5. Phasengates nach Qualitätsstufe

| Gate | Minimum | Recommended | Production |
|---|---|---|---|
| Startentscheidung | kompakter Projektauftrag | dokumentierter Projektauftrag | geprüfter Auftrag mit Risiko- und Betriebsbetrachtung |
| Umsetzungsstart | Ziel und nächster Meilenstein | Anforderungen und Architekturgrundlage | freigegebene Anforderungen, Architektur und Risikomaßnahmen |
| Releasefreigabe | Nutzung geprüft | definierte DoD und Testnachweise | formale Freigabe, Security-, Betriebs- und Recovery-Nachweise |
| Wartungsübergang | Zuständigkeit benannt | Wartungs- und Updateweg dokumentiert | Betriebsmodell, Monitoring, Backup und Incident-Verfahren geprüft |
| Archivierung | Status und Nutzungshinweis | Migrations- und Archivhinweis | kontrollierter EOL-Prozess und Datenbehandlung |

## 6. Verantwortlichkeiten

Einzelentwickler dürfen mehrere Rollen übernehmen. Die Rollen bleiben dennoch fachlich unterscheidbar:

- **Projektverantwortlicher:** Scope, Prioritäten, Qualitätsstufe und Freigabe.
- **Maintainer:** technische Pflege, Releases und Wartung.
- **Reviewer:** unabhängige oder strukturierte Selbstprüfung.
- **Betreiber:** produktive Umgebung, Überwachung und Wiederherstellung.

## 7. Nachweise und Prüfkriterien

Geeignete Nachweise sind Projektcharta, Roadmap, Anforderungen, Architektur, ADRs, Testberichte, Release Notes, Changelog, Compliance-Erklärung, Wartungsplan und Archivhinweis.

## 8. Ausnahmen und Abweichungen

Ein Projekt darf Phasen zusammenfassen, aber DARF erforderliche Ergebnisse nicht stillschweigend auslassen. Abweichungen werden nach [EXCEPTIONS.md](../40-governance/EXCEPTIONS.md) dokumentiert.

## 9. Verwandte Dokumente

- [Anforderungsmanagement](REQUIREMENTS.md)
- [Architekturstandard](ARCHITECTURE.md)
- [Teststandard](TESTING.md)
- [Release-Standard](RELEASES.md)
- [Wartungsstandard](MAINTENANCE.md)
