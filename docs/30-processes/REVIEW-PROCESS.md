---
title: "Reviewprozess"
document-id: SASD-PROC-004
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
depends-on: [SASD-CORE-007, SASD-CORE-009, SASD-CORE-013, SASD-GOV-006]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Reviewprozess

## 1. Zweck

Dieser Prozess definiert nachvollziehbare Dokument-, Architektur-, Code-, Security-, Test- und Release-Reviews. Er verbindet automatisierte Prüfungen mit risikobasierter menschlicher Beurteilung.

## 2. Geltungsbereich

Der Prozess gilt für Änderungen an normativen Dokumenten, Architektur, Quellcode, Konfiguration, Datenmodellen, Sicherheitsmaßnahmen, Releases und wesentlichen Betriebsabläufen.

## 3. Auslöser und Startbedingungen

- ein prüfbares Dokument oder Änderungspaket ist fertiggestellt
- ein Meilenstein oder Release benötigt Freigabe
- eine risikoreiche Architektur- oder Sicherheitsänderung wird vorgeschlagen
- ein Vorfall oder wiederkehrender Fehler erfordert systematische Nachbetrachtung

## 4. Benötigte Eingaben

- klar abgegrenzter Reviewgegenstand
- zugehörige Anforderungen und Entscheidungen
- automatisierte Prüfergebnisse
- Risiken, bekannte Einschränkungen und offene Fragen
- Definition of Done oder spezifische Freigabekriterien

## 5. Rollen und Verantwortlichkeiten

| Rolle | Verantwortung |
|---|---|
| Autor/Umsetzer | stellt prüfbaren Stand und Kontext bereit |
| Reviewer | prüft unabhängig und dokumentiert Findings |
| Fach-/Security-Spezialist | bewertet besondere Risiken |
| Freigabeverantwortlicher | entscheidet über Annahme, Nacharbeit oder Ausnahme |

Eine Person darf mehrere Rollen übernehmen. Die Kombination von Rollen hebt jedoch keine Nachweis-, Selbstreview- oder Freigabepflichten auf.

## 6. Prozessablauf

1. Reviewziel, Umfang und Kriterien festlegen.
2. Automatisierte Prüfungen und vorbereitende Selbstprüfung durchführen.
3. Artefakte, Anforderungen, Entscheidungen und Risiken prüfen.
4. Findings eindeutig erfassen und klassifizieren.
5. Findings beheben, begründet ablehnen oder als Ausnahme behandeln.
6. Behobene Punkte verifizieren.
7. Reviewabschluss, offene Risiken und Freigabe dokumentieren.

## 7. Normative Anforderungen

### Reviewplanung

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-300 | Jedes Review MUSS Ziel, Gegenstand, Prüftiefe und Abschlusskriterien benennen. |
| SASD-PROC-REQ-301 | Der Reviewumfang MUSS zur Qualitätsstufe, Änderungsgröße und zum Risiko passen. |
| SASD-PROC-REQ-302 | Reviewer MÜSSEN Zugriff auf die für ihre Bewertung erforderlichen Artefakte und Kontextinformationen erhalten. |
| SASD-PROC-REQ-303 | Ein Review DARF NICHT durch unnötig große Änderungspakete faktisch unprüfbar gemacht werden. |
| SASD-PROC-REQ-304 | Große Änderungen SOLLTEN in logisch prüfbare Einheiten zerlegt werden. |
| SASD-PROC-REQ-305 | Zeitkritische Reviews MÜSSEN verbleibende Prüflücken ausdrücklich dokumentieren. |

### Reviewarten

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-306 | Dokumente MÜSSEN auf Vollständigkeit, Widerspruchsfreiheit, Verständlichkeit und Aktualität geprüft werden. |
| SASD-PROC-REQ-307 | Architekturreviews MÜSSEN Anforderungen, Abhängigkeiten, Risiken, Datenflüsse und Betriebsfolgen berücksichtigen. |
| SASD-PROC-REQ-308 | Codereviews MÜSSEN Korrektheit, Wartbarkeit, Sicherheit und Testauswirkungen bewerten. |
| SASD-PROC-REQ-309 | Securityreviews MÜSSEN von Personen mit angemessener Fachkenntnis durchgeführt oder unterstützt werden. |
| SASD-PROC-REQ-310 | Release-Reviews MÜSSEN Nachweise statt nur Aussagen über Build, Tests und Artefakte prüfen. |
| SASD-PROC-REQ-311 | Post-Incident-Reviews SOLLTEN Ursachen, beitragende Faktoren und systemische Verbesserungen betrachten, nicht Schuldzuweisungen. |

### Unabhängigkeit und Einzelentwicklung

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-312 | Recommended-Projekte SOLLTEN für risikoreiche Änderungen einen zweiten menschlichen Reviewer einbeziehen. |
| SASD-PROC-REQ-313 | Production-Projekte MÜSSEN für kritische Sicherheits-, Daten- oder Betriebsänderungen angemessene unabhängige Prüfung vorsehen. |
| SASD-PROC-REQ-314 | Bei Einzelentwicklung MUSS ein strukturierter Selbstreview zeitlich oder kontextuell von der Erstellung getrennt werden. |
| SASD-PROC-REQ-315 | Ein Selbstreview MUSS eine Checkliste oder eine gleichwertige systematische Prüfmethode verwenden. |
| SASD-PROC-REQ-316 | KI-basierte Reviews KÖNNEN zusätzliche Hinweise liefern, DÜRFEN aber erforderliche menschliche Freigaben nicht ersetzen. |
| SASD-PROC-REQ-317 | Der Autor DARF NICHT eigene offene Zweifel oder bekannte Schwachstellen aus dem Reviewkontext entfernen. |

### Durchführung

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-318 | Reviewer MÜSSEN Anforderungen und Entscheidungen von persönlichen Stilpräferenzen unterscheiden. |
| SASD-PROC-REQ-319 | Feststellungen MÜSSEN auf konkrete Stellen, Anforderungen, Risiken oder reproduzierbare Beobachtungen verweisen. |
| SASD-PROC-REQ-320 | Automatisierte Prüfungen SOLLTEN vor dem manuellen Review ausgeführt werden, damit menschliche Aufmerksamkeit auf nicht automatisierbare Fragen gerichtet wird. |
| SASD-PROC-REQ-321 | Der Review MUSS geänderte Dokumentation, Tests, Konfiguration und Betriebsfolgen gemeinsam mit dem Code berücksichtigen. |
| SASD-PROC-REQ-322 | Unklare Anforderungen MÜSSEN als Klärungsbedarf und nicht als stillschweigende Reviewer-Annahme behandelt werden. |
| SASD-PROC-REQ-323 | Sicherheitsrelevante Details DÜRFEN NICHT unnötig in öffentlichen Reviewkommentaren offengelegt werden. |
| SASD-PROC-REQ-324 | Reviewer SOLLTEN zwischen verbindlichem Änderungsbedarf und optionaler Verbesserung unterscheiden. |

### Finding-Klassifikation

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-325 | Reviewfeststellungen MÜSSEN mindestens als Blocker, Major, Minor oder Observation klassifizierbar sein. |
| SASD-PROC-REQ-326 | Ein Blocker MUSS vor Freigabe behoben oder formell eskaliert werden. |
| SASD-PROC-REQ-327 | Major Findings MÜSSEN vor Freigabe behoben oder durch eine genehmigte Ausnahme abgedeckt sein. |
| SASD-PROC-REQ-328 | Minor Findings KÖNNEN nachverfolgt werden, wenn ihr Risiko und ein Zieltermin dokumentiert sind. |
| SASD-PROC-REQ-329 | Observations DÜRFEN NICHT als versteckte Pflichtanforderungen verwendet werden. |
| SASD-PROC-REQ-330 | Die Schweregrade MÜSSEN nach Auswirkung und Eintrittswahrscheinlichkeit und nicht nach persönlicher Präferenz vergeben werden. |

### Behebung und Abschluss

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-331 | Jedes verbindliche Finding MUSS einen Status und einen Verantwortlichen erhalten. |
| SASD-PROC-REQ-332 | Behobene Findings MÜSSEN durch erneute Prüfung oder nachvollziehbaren Nachweis geschlossen werden. |
| SASD-PROC-REQ-333 | Das bloße Antworten auf einen Reviewkommentar DARF NICHT automatisch als Behebung gelten. |
| SASD-PROC-REQ-334 | Abgelehnte Findings MÜSSEN mit einer sachlichen Begründung dokumentiert werden. |
| SASD-PROC-REQ-335 | Wiederkehrende Findings SOLLTEN in Standards, Checklisten, Tests oder Tooling zurückgeführt werden. |
| SASD-PROC-REQ-336 | Der Reviewabschluss MUSS offene Risiken, Ausnahmen und Nacharbeiten zusammenfassen. |
| SASD-PROC-REQ-337 | Die Freigabe MUSS eindeutig erkennen lassen, wer was auf welcher Evidenzbasis genehmigt hat. |

### Reviewnachweise und Schutz

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-338 | Reviewnachweise MÜSSEN zusammen mit dem betroffenen Änderungsstand auffindbar sein. |
| SASD-PROC-REQ-339 | Vertrauliche Reviewartefakte MÜSSEN angemessen geschützt gespeichert werden. |
| SASD-PROC-REQ-340 | Personenbezogene oder sensible Inhalte SOLLTEN in Reviewnachweisen auf das notwendige Maß begrenzt werden. |
| SASD-PROC-REQ-341 | Produktionskritische Freigaben MÜSSEN gegen nachträgliche unbemerkte Änderung geschützt oder versioniert sein. |
| SASD-PROC-REQ-342 | Reviewmetriken KÖNNEN zur Prozessverbesserung genutzt werden, DÜRFEN aber nicht zu oberflächlichen Mengenkennzahlen verzerren. |
| SASD-PROC-REQ-343 | Der Reviewprozess SOLLTE regelmäßig auf unnötige Reibung und übersehene Risiken überprüft werden. |

## 8. Zuordnung zu Qualitätsstufen

| Qualitätsstufe | Mindesttiefe des Prozesses |
|---|---|
| **Minimum** | Strukturierter Selbstreview, relevante automatisierte Prüfungen und dokumentierte Blockerbehandlung. |
| **Recommended** | Risikobasierter Peer- oder zeitlich getrennter Selbstreview, Finding-Tracking und Abschlussnachweis. |
| **Production** | Unabhängige Spezialreviews für kritische Bereiche, formale Freigabe, geschützte Nachweise und strenge Blockerregeln. |

Die Qualitätsstufe bestimmt die erforderliche Tiefe, nicht den grundsätzlichen Zweck des Prozesses. Risikoreiche Eigenschaften können unabhängig von Projektgröße oder Teamgröße strengere Maßnahmen auslösen.

## 9. Ergebnisse und Nachweise

- Reviewprotokoll oder nachvollziehbare Reviewhistorie
- klassifizierte Findings
- Behebungs- und Verifikationsnachweise
- offene Risiken und Ausnahmen
- Freigabe- oder Ablehnungsentscheidung

## 10. Abschlusskriterien

Der Prozess gilt erst als abgeschlossen, wenn die anwendbaren Kriterien erfüllt und die Nachweise auffindbar sind:

- [ ] Reviewgegenstand und geprüfter Stand sind eindeutig.
- [ ] Blocker und Major Findings sind behandelt.
- [ ] Verbleibende Findings besitzen Status und Verantwortliche.
- [ ] Erforderliche Nachprüfung wurde durchgeführt.
- [ ] Freigabe und offene Risiken sind dokumentiert.

## 11. Ausnahmen und Abweichungen

Bei Notfalländerungen darf das vollständige Review nachgelagert werden, wenn eine minimale Risiko- und Rollbackprüfung vorab erfolgt. Das nachgelagerte Review MUSS terminiert und nachweisbar abgeschlossen werden.

Abweichungen von MUSS-Anforderungen werden gemäß [Ausnahmen](../40-governance/EXCEPTIONS.md) behandelt. Nicht anwendbare Anforderungen benötigen eine kurze, überprüfbare Begründung.

## 12. Verwandte Dokumente

- [Qualitätsstandard](../10-core-standard/QUALITY.md)
- [Teststandard](../10-core-standard/TESTING.md)
- [Reviewprotokoll-Vorlage](../../templates/documents/REVIEW-RECORD-TEMPLATE.md)
- [Review-Checkliste](../../checklists/development/REVIEW-EXECUTION-CHECKLIST.md)

---

**Anforderungsumfang:** 44 Prozessanforderungen in diesem Dokument.
