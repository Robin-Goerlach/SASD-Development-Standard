---
title: "Prozess für Architekturentscheidungen"
document-id: SASD-PROC-003
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
depends-on: [SASD-CORE-003, SASD-CORE-012, SASD-GOV-001]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Prozess für Architekturentscheidungen

## 1. Zweck

Dieser Prozess stellt sicher, dass bedeutende technische Entscheidungen mit Kontext, Alternativen, Konsequenzen und nachvollziehbarer Freigabe dokumentiert werden.

## 2. Geltungsbereich

Der Prozess gilt für Entscheidungen, die Architektur, Daten, Sicherheit, Integration, Technologie, Betrieb, Deployment oder langfristige Wartung wesentlich beeinflussen.

## 3. Auslöser und Startbedingungen

- mehrere tragfähige technische Optionen bestehen
- eine Entscheidung ist teuer oder schwer reversibel
- eine neue Abhängigkeit, Datenhaltung oder externe Integration wird eingeführt
- eine bestehende Architekturentscheidung wird infrage gestellt oder abgelöst

## 4. Benötigte Eingaben

- Entscheidungsproblem und Kontext
- Anforderungen und Randbedingungen
- realistische Alternativen
- Risiken, Kosten und Auswirkungen
- verfügbare Primärquellen, Prototypen oder Messergebnisse

## 5. Rollen und Verantwortlichkeiten

| Rolle | Verantwortung |
|---|---|
| ADR-Autor | bereitet Kontext, Optionen und Entscheidungsvorschlag auf |
| Entscheidungsverantwortlicher | akzeptiert, verwirft oder vertagt den Vorschlag |
| Fach-/Security-Reviewer | prüft betroffene Spezialaspekte |
| Umsetzungsverantwortlicher | führt Folgemaßnahmen aus und hält Verweise aktuell |

Eine Person darf mehrere Rollen übernehmen. Die Kombination von Rollen hebt jedoch keine Nachweis-, Selbstreview- oder Freigabepflichten auf.

## 6. Prozessablauf

1. Entscheidungsbedarf und ADR-Angemessenheit feststellen.
2. Kontext, Kriterien, Randbedingungen und Alternativen sammeln.
3. Optionen bewerten und Konsequenzen sichtbar machen.
4. ADR als Proposed zur Prüfung vorlegen.
5. Entscheidung akzeptieren, verwerfen oder vertagen.
6. Umsetzung und Folgemaßnahmen verknüpfen.
7. ADR bei geänderten Annahmen überprüfen und gegebenenfalls ablösen.

## 7. Normative Anforderungen

### Auslöser und Angemessenheit

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-200 | Eine Entscheidung mit langfristiger, schwer reversibler oder projektübergreifender Wirkung MUSS als ADR geprüft werden. |
| SASD-PROC-REQ-201 | Technologie-, Daten-, Integrations-, Sicherheits- und Deploymententscheidungen SOLLTEN als ADR erfasst werden, wenn mehrere tragfähige Alternativen bestehen. |
| SASD-PROC-REQ-202 | Triviale lokale Implementierungsdetails SOLLTEN NICHT als ADR dokumentiert werden. |
| SASD-PROC-REQ-203 | Ein ADR DARF NICHT verwendet werden, um fehlende Anforderungen oder unklare Verantwortlichkeiten zu verdecken. |
| SASD-PROC-REQ-204 | Die Entscheidungstiefe MUSS dem Risiko und der erwarteten Lebensdauer entsprechen. |

### Identität und Status

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-205 | Jeder ADR MUSS eine repositoryweit eindeutige, stabile Kennung besitzen. |
| SASD-PROC-REQ-206 | ADRs MÜSSEN mindestens die Zustände Proposed, Accepted, Rejected, Superseded und Deprecated unterstützen. |
| SASD-PROC-REQ-207 | Der aktuelle Status und das Entscheidungsdatum MÜSSEN im ADR sichtbar sein. |
| SASD-PROC-REQ-208 | Ein akzeptierter ADR DARF NICHT in seiner ursprünglichen Entscheidungsbegründung stillschweigend umgeschrieben werden. |
| SASD-PROC-REQ-209 | Sachliche Korrekturen an akzeptierten ADRs MÜSSEN als solche kenntlich gemacht werden. |
| SASD-PROC-REQ-210 | Eine abgelöste Entscheidung MUSS auf ihren Nachfolger verweisen. |

### Inhalt

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-211 | Ein ADR MUSS Kontext, Entscheidungsproblem, gewählte Option und wesentliche Konsequenzen enthalten. |
| SASD-PROC-REQ-212 | Relevante Alternativen MÜSSEN mit ihren wichtigsten Vor- und Nachteilen dargestellt werden. |
| SASD-PROC-REQ-213 | Annahmen, Randbedingungen und nicht verhandelbare Vorgaben MÜSSEN von Präferenzen unterscheidbar sein. |
| SASD-PROC-REQ-214 | Sicherheits-, Datenschutz-, Betriebs- und Wartungsauswirkungen MÜSSEN berücksichtigt werden, wenn sie betroffen sind. |
| SASD-PROC-REQ-215 | Bewusste Nachteile und technische Schulden MÜSSEN im ADR ausdrücklich benannt werden. |
| SASD-PROC-REQ-216 | Die Entscheidung MUSS so formuliert sein, dass ihre spätere Umsetzung und Prüfung möglich ist. |

### Erstellung und Bewertung

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-217 | Der Autor MUSS vor der Entscheidung ausreichend Informationen für einen Vergleich der realistischen Optionen sammeln. |
| SASD-PROC-REQ-218 | Zeitlich begrenzte Experimente KÖNNEN zur Validierung einer ADR-Option eingesetzt werden. |
| SASD-PROC-REQ-219 | Bewertungskriterien SOLLTEN vor der endgültigen Auswahl festgelegt werden. |
| SASD-PROC-REQ-220 | Bei Production-relevanten Sicherheits- oder Datenentscheidungen MUSS geeignete unabhängige Fachprüfung eingeholt werden. |
| SASD-PROC-REQ-221 | KI KANN bei Recherche und Strukturierung unterstützen, DARF aber nicht als alleinige Entscheidungsinstanz oder Quelle verwendet werden. |
| SASD-PROC-REQ-222 | Unsichere externe Fakten MÜSSEN auf Primärquellen oder reproduzierbare Tests zurückgeführt werden. |

### Freigabe und Umsetzung

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-223 | Ein ADR MUSS vor oder spätestens mit der ersten irreversiblen Umsetzung akzeptiert werden. |
| SASD-PROC-REQ-224 | Die Freigabe MUSS zur Qualitätsstufe und zum Entscheidungsrisiko passen. |
| SASD-PROC-REQ-225 | Bei Einzelentwicklung MUSS zwischen Erstellung und Akzeptanz ein strukturierter Selbstreview erfolgen. |
| SASD-PROC-REQ-226 | Die Umsetzung SOLLTE auf den ADR verweisen, wenn der Zusammenhang sonst nicht auffindbar ist. |
| SASD-PROC-REQ-227 | Offene Umsetzungsfolgen MÜSSEN als Aufgaben, Risiken oder Folgemaßnahmen nachverfolgt werden. |
| SASD-PROC-REQ-228 | Ein akzeptierter ADR MUSS in einem ADR-Index oder einer gleichwertigen Navigation auffindbar sein. |

### Änderung und Ablösung

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-229 | Eine wesentlich geänderte Entscheidung MUSS durch einen neuen ADR dokumentiert werden. |
| SASD-PROC-REQ-230 | Der neue ADR MUSS den ersetzten ADR und den Grund der Änderung nennen. |
| SASD-PROC-REQ-231 | Ein ADR SOLLTE überprüft werden, wenn zentrale Annahmen, Technologie-Support oder Betriebsbedingungen entfallen. |
| SASD-PROC-REQ-232 | Nicht mehr relevante ADRs KÖNNEN als Deprecated markiert werden, dürfen aber nicht ohne Archivnachweis verschwinden. |
| SASD-PROC-REQ-233 | Die Historie abgelehnter Optionen SOLLTE erhalten bleiben, wenn sie spätere Wiederholungsdiskussionen verhindert. |
| SASD-PROC-REQ-234 | Widersprüche zwischen gültigen ADRs MÜSSEN vor dem nächsten betroffenen Release aufgelöst werden. |

## 8. Zuordnung zu Qualitätsstufen

| Qualitätsstufe | Mindesttiefe des Prozesses |
|---|---|
| **Minimum** | ADR nur für zentrale oder schwer reversible Entscheidungen; kompakte Alternativen- und Konsequenzdarstellung. |
| **Recommended** | ADR-Index, dokumentierte Kriterien, Review und Verknüpfung zu Umsetzung und Folgemaßnahmen. |
| **Production** | Formale Freigabe, Spezialreview bei Risiko, belastbare Evidenz und regelmäßige Prüfung kritischer Entscheidungen. |

Die Qualitätsstufe bestimmt die erforderliche Tiefe, nicht den grundsätzlichen Zweck des Prozesses. Risikoreiche Eigenschaften können unabhängig von Projektgröße oder Teamgröße strengere Maßnahmen auslösen.

## 9. Ergebnisse und Nachweise

- versionierter ADR
- Status- und Freigabeentscheidung
- ADR-Indexeintrag
- verknüpfte Umsetzungs- und Folgemaßnahmen
- gegebenenfalls Nachfolge-ADR

## 10. Abschlusskriterien

Der Prozess gilt erst als abgeschlossen, wenn die anwendbaren Kriterien erfüllt und die Nachweise auffindbar sind:

- [ ] Entscheidungsproblem und Kontext sind verständlich.
- [ ] Realistische Alternativen und Konsequenzen sind dokumentiert.
- [ ] Status und Freigabe sind eindeutig.
- [ ] Folgemaßnahmen sind zugewiesen.
- [ ] ADR ist auffindbar und mit relevanten Artefakten verknüpft.

## 11. Ausnahmen und Abweichungen

Akute Incident- oder Hotfix-Entscheidungen dürfen zunächst in einem Ereignisprotokoll festgehalten werden. Ein erforderlicher ADR MUSS anschließend innerhalb eines festgelegten Zeitraums nachgezogen werden.

Abweichungen von MUSS-Anforderungen werden gemäß [Ausnahmen](../40-governance/EXCEPTIONS.md) behandelt. Nicht anwendbare Anforderungen benötigen eine kurze, überprüfbare Begründung.

## 12. Verwandte Dokumente

- [Architekturstandard](../10-core-standard/ARCHITECTURE.md)
- [ADR-Vorlage](../../templates/architecture-decisions/ADR-TEMPLATE.md)
- [ADR-Index-Vorlage](../../templates/architecture-decisions/ADR-INDEX-TEMPLATE.md)
- [ADR-Review-Checkliste](../../checklists/development/ADR-REVIEW-CHECKLIST.md)

---

**Anforderungsumfang:** 35 Prozessanforderungen in diesem Dokument.
