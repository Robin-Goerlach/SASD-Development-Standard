---
title: "Normative Sprache"
document-id: SASD-GOV-001
document-type: normative
status: Proposed
version: 0.2.0
standard-version: "1.0"
language: de
authoritative: true
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-FND-004]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Normative Sprache

## 1. Zweck

Dieses Dokument legt fest, wie Verbindlichkeit im SASD Development Standard ausgedrückt und interpretiert wird. Die Schlüsselwörter werden bewusst in Großbuchstaben geschrieben.

## 2. Schlüsselwörter

### MUSS

**MUSS** bezeichnet eine verpflichtende Anforderung. Ein Projekt erfüllt die Anforderung oder dokumentiert eine genehmigte Abweichung. Ohne Erfüllung oder genehmigte Abweichung besteht keine vollständige Compliance für den betroffenen Bereich.

### DARF NICHT

**DARF NICHT** bezeichnet ein verbindliches Verbot. Eine Ausnahme erfordert eine dokumentierte Risikoabwägung und Genehmigung nach `EXCEPTIONS.md`.

### SOLLTE

**SOLLTE** bezeichnet eine starke Empfehlung. Eine Abweichung ist zulässig, muss aber nachvollziehbar begründet werden, wenn sie die Wartbarkeit, Sicherheit, Reproduzierbarkeit oder Nachweisführung beeinflusst.

### SOLLTE NICHT

**SOLLTE NICHT** bezeichnet eine Praxis, die in der Regel vermieden wird. Eine abweichende Nutzung benötigt eine nachvollziehbare Begründung.

### KANN

**KANN** bezeichnet eine optionale Möglichkeit. Die Umsetzung oder Nichtumsetzung beeinflusst die Compliance nicht, sofern keine andere Anforderung daraus eine Pflicht ableitet.

## 3. Grammatische Varianten in der deutschen Fassung

Die Metadaten verwenden die kanonischen Singularformen `MUSS`, `DARF NICHT`, `SOLLTE`, `SOLLTE NICHT` und `KANN`. In deutschen Sätzen besitzen die folgenden großgeschriebenen Flexionsformen dieselbe normative Bedeutung:

| Kanonische Form | Gleichwertige grammatische Form |
|---|---|
| MUSS | MÜSSEN |
| DARF NICHT | DÜRFEN NICHT |
| SOLLTE | SOLLTEN |
| SOLLTE NICHT | SOLLTEN NICHT |
| KANN | KÖNNEN |

Kleingeschriebene Verwendungen sind nur dann normativ, wenn der unmittelbare Kontext eindeutig auf eine bereits identifizierte normative Anforderung verweist. Neue Anforderungen SOLLTEN die großgeschriebenen Formen verwenden.

## 4. Nicht normative Formulierungen

Formulierungen wie „beispielsweise“, „typischerweise“, „könnte“, „möglich“, „Hinweis“ oder „Empfehlung“ setzen ohne ein normatives Schlüsselwort keine eigenständige Verpflichtung.

Informative Beispiele dürfen Anforderungen erläutern, aber nicht erweitern.

## 5. Anforderungen und Qualitätsstufen

Eine Anforderung kann für eine oder mehrere Qualitätsstufen gelten. Die Zuordnung MUSS im Dokument oder in einer eindeutig referenzierten Anforderungstabelle erfolgen.

Beispiel:

| Anforderung | Minimum | Recommended | Production |
|---|---:|---:|---:|
| README vorhanden | MUSS | MUSS | MUSS |
| automatisierter Releaseprozess | KANN | SOLLTE | MUSS |

## 6. Anforderungen und Profile

Ein Profil darf eine allgemeine Anforderung präzisieren oder verschärfen. Es DARF sie nur dann abweichend regeln, wenn:

1. die Abweichung ausdrücklich gekennzeichnet ist,
2. die fachliche Notwendigkeit erklärt wird,
3. der Geltungsbereich eindeutig ist,
4. keine stillschweigende Abschwächung entsteht.

## 7. Nachweisbarkeit

Jede MUSS- oder DARF-NICHT-Anforderung SOLLTE einen prüfbaren Nachweis besitzen. Beispiele sind:

- Datei oder Dokument,
- Testausgabe,
- Buildprotokoll,
- Konfigurationsdatei,
- Reviewprotokoll,
- Architekturentscheidung,
- Freigabe oder dokumentierte Abweichung.

## 8. Sprachfassungen

In der englischen Ausgabe entsprechen die Begriffe:

| Deutsch | Englisch |
|---|---|
| MUSS | MUST |
| DARF NICHT | MUST NOT |
| SOLLTE | SHOULD |
| SOLLTE NICHT | SHOULD NOT |
| KANN | MAY |

Bis zu einer anderslautenden Governance-Entscheidung ist die deutsche Fassung autoritativ.
