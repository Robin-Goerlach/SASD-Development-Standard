---
title: "Projektarchivierung"
document-id: SASD-PROC-007
document-type: normative
status: Proposed
version: 0.6.0
standard-version: "1.0"
language: de
authoritative: true
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-CORE-011, SASD-CORE-012, SASD-CORE-008, SASD-GOV-007]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Projektarchivierung

## 1. Zweck

Dieser Prozess ermöglicht eine geordnete Stilllegung, ohne Nutzer, Daten, Infrastrukturkosten, Sicherheitsrisiken oder notwendiges Wissen zurückzulassen.

## 2. Geltungsbereich

Der Prozess gilt für beendete, abgelöste, aufgegebene oder aus Sicherheits- und Wartungsgründen stillzulegende Projekte, Dienste, Repositories und technische Artefaktsammlungen.

## 3. Auslöser und Startbedingungen

- ein Projektziel ist abgeschlossen und keine weitere Pflege vorgesehen
- ein Nachfolgeprodukt ersetzt das Projekt
- Wartung ist nicht mehr verantwortbar oder wirtschaftlich
- Sicherheits-, Lizenz- oder Betriebsrisiken erzwingen die Stilllegung

## 4. Benötigte Eingaben

- Archivierungsentscheidung und Grund
- Liste von Nutzern, Abhängigkeiten und Verantwortlichen
- Daten-, Backup- und Aufbewahrungsübersicht
- Infrastruktur-, Domain-, Zugangsdaten- und Drittanbieterinventar
- Repository-, Release- und Wissensstand

## 5. Rollen und Verantwortlichkeiten

| Rolle | Verantwortung |
|---|---|
| Projekt-/Produktverantwortlicher | entscheidet über Ende, Kommunikation und verbleibende Pflichten |
| Maintainer | sichert Repository, Dokumentation und technischen Abschluss |
| Daten-/Security-Verantwortlicher | behandelt Daten, Schlüssel, Zugänge und Risiken |
| Betriebsverantwortlicher | schaltet Dienste, Monitoring und Kosten kontrolliert ab |
| Reviewer | prüft Vollständigkeit und verbleibende Risiken |

Eine Person darf mehrere Rollen übernehmen. Die Kombination von Rollen hebt jedoch keine Nachweis-, Selbstreview- oder Freigabepflichten auf.

## 6. Prozessablauf

1. Archivierungsgrund, Scope und Verantwortliche beschließen.
2. Nutzer, Abhängigkeiten, Daten, Infrastruktur und Pflichten inventarisieren.
3. Migration, Export, Aufbewahrung und Löschung durchführen.
4. Dienste, Zugänge, Kosten und Monitoring kontrolliert stilllegen.
5. Repository, Releases, Dokumentation und Wissen archivierungsfähig machen.
6. Nutzer und Nachfolgewege kommunizieren.
7. Abschlussprüfung durchführen und Archivstatus setzen.

## 7. Normative Anforderungen

### Archivierungsentscheidung

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-600 | Die Stilllegung eines gepflegten Projekts MUSS als ausdrückliche Entscheidung dokumentiert werden. |
| SASD-PROC-REQ-601 | Der Archivierungsgrund MUSS zwischen Abschluss, Ablösung, fehlender Wartbarkeit, Sicherheitsrisiko und Aufgabe des Nutzens unterscheiden. |
| SASD-PROC-REQ-602 | Betroffene Nutzer, Betreiber und abhängige Projekte MÜSSEN vor der Stilllegung identifiziert werden. |
| SASD-PROC-REQ-603 | Eine Archivierung DARF NICHT als Ersatz für die Behandlung weiterhin bestehender rechtlicher oder sicherheitsbezogener Pflichten verwendet werden. |
| SASD-PROC-REQ-604 | Das Zieldatum und der verantwortliche Eigentümer der Archivierung MÜSSEN festgelegt werden. |

### Nutzer und Abhängigkeiten

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-605 | Aktive Nutzer MÜSSEN angemessen über Ende, Supportstatus und Alternativen informiert werden. |
| SASD-PROC-REQ-606 | Abhängige Systeme, Automatisierungen und Dokumente MÜSSEN auf verbleibende Verweise geprüft werden. |
| SASD-PROC-REQ-607 | Ein Nachfolgeprojekt MUSS eindeutig verlinkt werden, sofern es existiert. |
| SASD-PROC-REQ-608 | Nicht ersetzte Funktionen oder Datenzugänge MÜSSEN als verbleibendes Risiko dokumentiert werden. |
| SASD-PROC-REQ-609 | Externe Veröffentlichungen SOLLTEN mit einem klaren Archivierungs- oder End-of-Life-Hinweis versehen werden. |

### Daten und Aufbewahrung

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-610 | Projekt- und Nutzerdaten MÜSSEN nach dokumentierten Aufbewahrungs-, Export- und Löschregeln behandelt werden. |
| SASD-PROC-REQ-611 | Vor der Löschung benötigter Daten MUSS ihre erfolgreiche Übernahme oder ein genehmigter Verzicht bestätigt werden. |
| SASD-PROC-REQ-612 | Backups MÜSSEN entsprechend Schutzbedarf, Aufbewahrungsfrist und späterer Wiederherstellbarkeit behandelt werden. |
| SASD-PROC-REQ-613 | Personenbezogene oder vertrauliche Daten DÜRFEN NICHT allein wegen einer Repository-Archivierung unbegrenzt aufbewahrt werden. |
| SASD-PROC-REQ-614 | Datenformate und benötigte Lesewerkzeuge SOLLTEN dokumentiert werden, wenn spätere Auskunft oder Wiederherstellung erforderlich sein kann. |
| SASD-PROC-REQ-615 | Kryptographische Schlüssel für archivierte Daten MÜSSEN entweder sicher weiterverwahrt oder die Daten kontrolliert unbrauchbar gemacht werden. |

### Infrastruktur und Zugänge

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-616 | Nicht mehr benötigte Dienste, Jobs, Domains, Tokens und Zugangsdaten MÜSSEN kontrolliert deaktiviert oder widerrufen werden. |
| SASD-PROC-REQ-617 | Cloud-, Hosting- und Drittanbieterkosten SOLLTEN nach erfolgreicher Stilllegung beendet werden. |
| SASD-PROC-REQ-618 | Gemeinsam genutzte Infrastruktur DARF NICHT durch unkoordinierte Archivierung beeinträchtigt werden. |
| SASD-PROC-REQ-619 | Monitoring und Alerts MÜSSEN angepasst werden, damit weder blinde Flecken noch dauerhafte Fehlalarme entstehen. |
| SASD-PROC-REQ-620 | Verbleibende öffentliche Endpunkte MÜSSEN entfernt, umgeleitet oder mit sicherem End-of-Life-Verhalten versehen werden. |
| SASD-PROC-REQ-621 | Signier-, Deployment- und Administrationsrechte MÜSSEN nach dem Prinzip minimaler verbleibender Berechtigung reduziert werden. |

### Repository und Wissen

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-622 | Das Repository MUSS einen abschließenden Statushinweis mit Archivierungsdatum, Grund und Supportstatus erhalten. |
| SASD-PROC-REQ-623 | Der letzte unterstützte Stand MUSS durch Tag oder gleichwertige unveränderliche Referenz auffindbar sein. |
| SASD-PROC-REQ-624 | Build-, Installations-, Daten- und Wiederherstellungsinformationen MÜSSEN soweit erforderlich für spätere Nachvollziehbarkeit erhalten bleiben. |
| SASD-PROC-REQ-625 | Offene Sicherheitsprobleme MÜSSEN vor öffentlicher Archivierung bewertet und angemessen kommuniziert oder vertraulich behandelt werden. |
| SASD-PROC-REQ-626 | Issues und Roadmap MÜSSEN so geschlossen oder gekennzeichnet werden, dass keine fortgesetzte aktive Pflege suggeriert wird. |
| SASD-PROC-REQ-627 | Wichtige Entscheidungen und Lessons Learned SOLLTEN vor der Archivierung in dauerhafte Wissensartefakte überführt werden. |
| SASD-PROC-REQ-628 | Nicht reproduzierbare Binärartefakte SOLLTEN zusammen mit Herkunft, Version und Prüfsumme archiviert werden, wenn sie für Wiederherstellung benötigt werden. |

### Wiederaufnahme und Wiederherstellung

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-629 | Es MUSS festgelegt werden, ob das Projekt dauerhaft beendet oder grundsätzlich reaktivierbar ist. |
| SASD-PROC-REQ-630 | Für reaktivierbare Production-Projekte MUSS ein minimaler Wiederherstellungsweg dokumentiert und geschützt aufbewahrt werden. |
| SASD-PROC-REQ-631 | Voraussetzungen für eine Wiederaufnahme MÜSSEN benannt werden, einschließlich Eigentümer, Daten, Zugänge und Toolchain. |
| SASD-PROC-REQ-632 | Eine spätere Reaktivierung MUSS eine neue Klassifikation und Sicherheitsbewertung auslösen. |
| SASD-PROC-REQ-633 | Archivierte Abhängigkeiten DÜRFEN NICHT ungeprüft als weiterhin sicher oder unterstützt angenommen werden. |

### Abschluss und Kontrolle

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-634 | Die Archivierung MUSS mit einer Checkliste oder einem gleichwertigen Abschlussnachweis dokumentiert werden. |
| SASD-PROC-REQ-635 | Nach Abschaltung MUSS geprüft werden, ob öffentliche Endpunkte, Kosten, Jobs und Zugänge tatsächlich beendet sind. |
| SASD-PROC-REQ-636 | Verbleibende Aufbewahrungs- und Löschtermine MÜSSEN Verantwortliche und Fälligkeit besitzen. |
| SASD-PROC-REQ-637 | Production-Archivierungen MÜSSEN eine unabhängige Prüfung der Daten- und Zugangsbehandlung erhalten. |
| SASD-PROC-REQ-638 | Die Abschlussentscheidung MUSS verbleibende Risiken und nicht erfüllte Punkte ausdrücklich benennen. |
| SASD-PROC-REQ-639 | Das Projekt DARF NICHT als archiviert gelten, bevor Repository, Daten, Infrastruktur, Nutzerkommunikation und Wissen konsistent behandelt wurden. |

## 8. Zuordnung zu Qualitätsstufen

| Qualitätsstufe | Mindesttiefe des Prozesses |
|---|---|
| **Minimum** | Abschlusshinweis, letzter Stand, grundlegende Daten-/Zugangsbereinigung und dokumentierte verbleibende Pflichten. |
| **Recommended** | Vollständiges Inventar, Nutzerkommunikation, Wissenssicherung, Infrastrukturprüfung und Archivierungsnachweis. |
| **Production** | Formale Daten-, Security- und Betriebsfreigabe, unabhängige Prüfung, Wiederherstellungs- oder Nachfolgekonzept und kontrollierte Aufbewahrung. |

Die Qualitätsstufe bestimmt die erforderliche Tiefe, nicht den grundsätzlichen Zweck des Prozesses. Risikoreiche Eigenschaften können unabhängig von Projektgröße oder Teamgröße strengere Maßnahmen auslösen.

## 9. Ergebnisse und Nachweise

- Archivierungsentscheidung
- Nutzer- und Abhängigkeitskommunikation
- Daten-, Aufbewahrungs- und Löschprotokoll
- Zugangs- und Infrastrukturabschluss
- archiviertes Repository mit Statushinweis
- Wiederaufnahme- oder Endgültigkeitsentscheidung
- Abschlussnachweis mit Restpflichten

## 10. Abschlusskriterien

Der Prozess gilt erst als abgeschlossen, wenn die anwendbaren Kriterien erfüllt und die Nachweise auffindbar sind:

- [ ] Nutzer und Abhängigkeiten sind behandelt.
- [ ] Daten und Backups folgen dokumentierten Regeln.
- [ ] Dienste, Zugänge, Jobs und Kosten sind geprüft.
- [ ] Repository und letzter unterstützter Stand sind auffindbar.
- [ ] Wissen und Wiederaufnahmebedingungen sind gesichert.
- [ ] Verbleibende Pflichten besitzen Verantwortliche und Termine.

## 11. Ausnahmen und Abweichungen

Kann eine vollständige Abschaltung wegen Aufbewahrungspflichten, Abhängigkeiten oder fehlender Zugriffsrechte nicht abgeschlossen werden, MUSS ein eingeschränkter Archivstatus mit Restmaßnahmen, Risiko und Verantwortlichem verwendet werden.

Abweichungen von MUSS-Anforderungen werden gemäß [Ausnahmen](../40-governance/EXCEPTIONS.md) behandelt. Nicht anwendbare Anforderungen benötigen eine kurze, überprüfbare Begründung.

## 12. Verwandte Dokumente

- [Wartungsstandard](../10-core-standard/MAINTENANCE.md)
- [Archivierungsnachweis](../../templates/documents/PROJECT-ARCHIVAL-RECORD-TEMPLATE.md)
- [Archivierungscheckliste](../../checklists/releases/PROJECT-ARCHIVAL-CHECKLIST.md)
- [Legacy-Migration](LEGACY-MIGRATION.md)

---

**Anforderungsumfang:** 40 Prozessanforderungen in diesem Dokument.
