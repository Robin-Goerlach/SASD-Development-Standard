---
title: "Projektklassifikation"
document-id: SASD-PROC-002
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
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-CORE-006, SASD-FND-002, SASD-GOV-006]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Projektklassifikation

## 1. Zweck

Dieser Prozess bestimmt die angemessene Qualitätsstufe, die anwendbaren Profile, die strukturelle Größe und die Risikomerkmale eines Projekts. Er verhindert, dass Aufwand allein nach Codeumfang oder Teamgröße bemessen wird.

## 2. Geltungsbereich

Der Prozess gilt für neue Projekte, wesentliche Erweiterungen, Übernahmen bestehender Repositories, Pilotmigrationen und den Übergang eines Prototyps in dauerhafte Nutzung.

## 3. Auslöser und Startbedingungen

- eine neue Projektidee soll umgesetzt werden
- ein bestehendes Projekt wird übernommen oder wesentlich erweitert
- Nutzerkreis, Datenarten, Verteilung oder Betriebsmodell ändern sich
- ein Projekt wechselt von Experiment zu langfristiger oder produktiver Nutzung

## 4. Benötigte Eingaben

- Projektidee oder vorhandener Projektstand
- bekannter Scope und erkennbare Nicht-Ziele
- Informationen zu Nutzern, Daten, Integrationen und Betrieb
- bekannte rechtliche, vertragliche oder organisatorische Vorgaben
- vorläufige Risiko- und Lebensdauereinschätzung

## 5. Rollen und Verantwortlichkeiten

| Rolle | Verantwortung |
|---|---|
| Projektverantwortlicher | führt die Klassifikation durch und verantwortet das Ergebnis |
| Fachverantwortlicher | bewertet Zweck, Nutzer und fachliche Auswirkungen |
| Technischer Verantwortlicher | bewertet Struktur, Technologien, Integrationen und Betrieb |
| Security-/Datenschutzrolle | prüft sensible Daten, Exponierung und Schutzbedarf, soweit erforderlich |
| Reviewer | prüft Nachvollziehbarkeit und Angemessenheit |

Eine Person darf mehrere Rollen übernehmen. Die Kombination von Rollen hebt jedoch keine Nachweis-, Selbstreview- oder Freigabepflichten auf.

## 6. Prozessablauf

1. Projektgegenstand und beabsichtigten Lebenszyklus beschreiben.
2. Strukturelle Größe unabhängig von Kritikalität bestimmen.
3. Risikomerkmale und externe Verpflichtungen erfassen.
4. Qualitätsstufe anhand des höchsten angemessenen Schutz- und Wartungsbedarfs wählen.
5. Core und anwendbare Profile auswählen.
6. Erforderliche Artefakte und zulässige Zusammenfassungen festlegen.
7. Ergebnis prüfen, offene Fragen zuweisen und Klassifikation freigeben.

## 7. Normative Anforderungen

### Klassifikationsgrundlagen

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-100 | Jedes neue oder wesentlich veränderte Projekt MUSS vor der Umsetzungsfreigabe klassifiziert werden. |
| SASD-PROC-REQ-101 | Die Klassifikation MUSS Projektgröße, Qualitätsstufe, Risikomerkmale und anwendbare Profile getrennt ausweisen. |
| SASD-PROC-REQ-102 | Die Teamgröße DARF NICHT allein über die erforderliche Qualitätsstufe entscheiden. |
| SASD-PROC-REQ-103 | Ein kleines Projekt mit hoher Kritikalität MUSS strengere Maßnahmen erhalten können als ein großes, risikoarmes Lernprojekt. |
| SASD-PROC-REQ-104 | Die Klassifikation MUSS auf nachvollziehbaren Fakten und ausdrücklich gekennzeichneten Annahmen beruhen. |
| SASD-PROC-REQ-105 | Unbekannte risikorelevante Eigenschaften SOLLTEN als offene Klärung dokumentiert und nicht stillschweigend als unkritisch bewertet werden. |

### Projektgröße und Lebensdauer

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-106 | Die strukturelle Projektgröße MUSS mindestens als Small, Medium oder Large erfasst werden. |
| SASD-PROC-REQ-107 | Die Größenbewertung SOLLTE Umfang, Komponentenanzahl, Integrationen, Datenmodell, Betriebsaufwand und erwartete Änderungsrate berücksichtigen. |
| SASD-PROC-REQ-108 | Die erwartete Lebensdauer MUSS als Experiment, befristetes Vorhaben oder langfristig gepflegtes Produkt dokumentiert werden. |
| SASD-PROC-REQ-109 | Ein Prototyp, der produktiv weiterverwendet wird, MUSS neu klassifiziert werden. |
| SASD-PROC-REQ-110 | Projektgröße KANN die Artefakttiefe beeinflussen, DARF aber Sicherheits- oder Betriebsrisiken nicht herabstufen. |

### Qualitätsstufe

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-111 | SASD Recommended SOLLTE die Standardauswahl für langfristig gepflegte oder öffentlich bereitgestellte Projekte sein. |
| SASD-PROC-REQ-112 | SASD Minimum DARF NICHT gewählt werden, wenn die reduzierte Tiefe mit Zweck, Risiko, Lebensdauer oder Verteilung unvereinbar ist. |
| SASD-PROC-REQ-113 | SASD Production MUSS geprüft werden, wenn externe Nutzer, kritische Geschäftsabläufe, sensible Daten oder verbindliche Betriebszusagen betroffen sind. |
| SASD-PROC-REQ-114 | Die gewählte Qualitätsstufe MUSS mit einer kurzen Begründung dokumentiert werden. |
| SASD-PROC-REQ-115 | Bei konkurrierenden Kriterien MUSS die strengere angemessene Qualitätsstufe gewählt oder eine dokumentierte Ausnahme beschlossen werden. |
| SASD-PROC-REQ-116 | Eine Herabstufung der Qualitätsstufe MUSS begründet, genehmigt und auf ihre Risiken geprüft werden. |
| SASD-PROC-REQ-117 | Eine höhere Qualitätsstufe KANN freiwillig gewählt werden, ohne dass das Projekt seine Größenklassifikation ändert. |

### Risikomerkmale

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-118 | Die Klassifikation MUSS mindestens Datenvertraulichkeit, Datenintegrität, Verfügbarkeit und Wiederherstellbarkeit bewerten. |
| SASD-PROC-REQ-119 | Die Klassifikation MUSS externe Erreichbarkeit, Verteilung an Dritte und privilegierte Systemzugriffe erfassen. |
| SASD-PROC-REQ-120 | Die Klassifikation MUSS rechtliche, regulatorische, vertragliche und lizenzbezogene Anforderungen berücksichtigen. |
| SASD-PROC-REQ-121 | Abhängigkeiten von einzelnen Personen, externen Diensten oder nicht reproduzierbaren Umgebungen MÜSSEN als Kontinuitätsrisiken erfasst werden. |
| SASD-PROC-REQ-122 | Mögliche Auswirkungen fehlerhafter Ergebnisse auf Menschen, Finanzen, Betrieb oder Reputation MÜSSEN bewertet werden. |
| SASD-PROC-REQ-123 | Der Einsatz von Kryptographie, Zugangsdaten oder personenbezogenen Daten MUSS als gesondertes Risikomerkmal dokumentiert werden. |
| SASD-PROC-REQ-124 | KI-generierte oder KI-gestützte Ergebnisse MÜSSEN bei sicherheits-, rechts- oder geschäftskritischen Entscheidungen als Prüfbedarf berücksichtigt werden. |

### Profile und Projektart

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-125 | Der Core Standard MUSS für jedes klassifizierte SASD-Projekt als Ausgangsbasis ausgewählt werden. |
| SASD-PROC-REQ-126 | Anwendbare Technologie- und Projektprofile MÜSSEN anhand der tatsächlich eingesetzten Technologien und Betriebsformen bestimmt werden. |
| SASD-PROC-REQ-127 | Mehrere Profile KÖNNEN gleichzeitig gelten und MÜSSEN dann gemeinsam betrachtet werden. |
| SASD-PROC-REQ-128 | Nicht anwendbare Profile SOLLTEN ausdrücklich ausgeschlossen werden, wenn ihre Anwendung sonst naheliegend wäre. |
| SASD-PROC-REQ-129 | Profilkonflikte MÜSSEN nach der im Qualitätsstufenmodell definierten Vorrangregel aufgelöst werden. |

### Dokumentationstiefe und Artefakte

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-130 | Die Klassifikation MUSS den erwarteten Dokumentationsumfang und die zulässige Zusammenlegung von Artefakten festlegen. |
| SASD-PROC-REQ-131 | Für Small-Projekte KÖNNEN Projektbrief, Scope, Risiken und Architekturübersicht in einem kompakten Dokument zusammengeführt werden. |
| SASD-PROC-REQ-132 | Recommended-Projekte SOLLTEN Anforderungen, Architektur, Teststrategie, Roadmap und Wartung nachvollziehbar trennen oder eindeutig gliedern. |
| SASD-PROC-REQ-133 | Production-Projekte MÜSSEN sicherheits-, release-, betriebs- und wiederherstellungsrelevante Nachweise separat prüfbar halten. |
| SASD-PROC-REQ-134 | Die Zusammenlegung von Dokumenten DARF NICHT dazu führen, dass Verantwortlichkeiten oder Entscheidungen unauffindbar werden. |

### Freigabe und Neubewertung

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-135 | Das Klassifikationsergebnis MUSS vor der Projektinitialisierung oder Migration freigegeben werden. |
| SASD-PROC-REQ-136 | Bei Einzelentwicklung MUSS die Freigabe mindestens durch einen zeitlich getrennten strukturierten Selbstreview erfolgen. |
| SASD-PROC-REQ-137 | Die Klassifikation MUSS bei wesentlichen Scope-, Daten-, Betriebs-, Nutzer- oder Sicherheitsänderungen erneut geprüft werden. |
| SASD-PROC-REQ-138 | Eine Neubewertung SOLLTE mindestens vor jedem Major Release und vor dem Übergang in produktiven Betrieb erfolgen. |
| SASD-PROC-REQ-139 | Änderungen der Klassifikation MÜSSEN mit Datum, Anlass und Auswirkungen dokumentiert werden. |
| SASD-PROC-REQ-140 | Offene Klassifikationsfragen MÜSSEN einen Verantwortlichen und einen Zieltermin erhalten. |
| SASD-PROC-REQ-141 | Das Ergebnis MUSS so gespeichert werden, dass spätere Entscheidungen auf die damals bekannten Grundlagen zurückgeführt werden können. |

## 8. Zuordnung zu Qualitätsstufen

| Qualitätsstufe | Mindesttiefe des Prozesses |
|---|---|
| **Minimum** | Kompakte Klassifikation mit Zweck, Größe, Lebensdauer, Risiken, Profilen und Begründung der Stufe. |
| **Recommended** | Vollständige Klassifikationsvorlage, dokumentierte Risikomerkmale, Artefaktplan und Review. |
| **Production** | Formale Schutzbedarfs- und Betriebsbewertung, unabhängige fachliche Prüfung sowie dokumentierte Freigabe. |

Die Qualitätsstufe bestimmt die erforderliche Tiefe, nicht den grundsätzlichen Zweck des Prozesses. Risikoreiche Eigenschaften können unabhängig von Projektgröße oder Teamgröße strengere Maßnahmen auslösen.

## 9. Ergebnisse und Nachweise

- ausgefüllter Projektklassifikationsnachweis
- gewählte Qualitätsstufe mit Begründung
- Liste anwendbarer Profile
- Risikomerkmale und offene Klärungen
- vorgesehener Artefakt- und Reviewumfang

## 10. Abschlusskriterien

Der Prozess gilt erst als abgeschlossen, wenn die anwendbaren Kriterien erfüllt und die Nachweise auffindbar sind:

- [ ] Projektgröße, Lebensdauer und Qualitätsstufe sind getrennt ausgewiesen.
- [ ] Core und anwendbare Profile sind bestimmt.
- [ ] Risikomerkmale und offene Fragen sind dokumentiert.
- [ ] Artefakttiefe und nächste Neubewertung sind festgelegt.
- [ ] Klassifikation ist geprüft und freigegeben.

## 11. Ausnahmen und Abweichungen

Ist eine belastbare Klassifikation wegen fehlender Informationen noch nicht möglich, darf ein zeitlich begrenzter vorläufiger Status verwendet werden. Dabei MUSS konservativ klassifiziert und der Klärungstermin dokumentiert werden.

Abweichungen von MUSS-Anforderungen werden gemäß [Ausnahmen](../40-governance/EXCEPTIONS.md) behandelt. Nicht anwendbare Anforderungen benötigen eine kurze, überprüfbare Begründung.

## 12. Verwandte Dokumente

- [Qualitätsstufen](../10-core-standard/QUALITY-LEVELS.md)
- [Projektlebenszyklus](../10-core-standard/PROJECT-LIFECYCLE.md)
- [Projektklassifikationsvorlage](../../templates/documents/PROJECT-CLASSIFICATION-TEMPLATE.md)
- [Klassifikationscheckliste](../../checklists/project-initiation/PROJECT-CLASSIFICATION-CHECKLIST.md)

---

**Anforderungsumfang:** 42 Prozessanforderungen in diesem Dokument.
