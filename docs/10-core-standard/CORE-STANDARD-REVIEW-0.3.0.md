---
title: "Core Standard Review 0.3.0"
document-id: SASD-REF-004
document-type: informative
status: Draft
version: 0.1.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core]
depends-on: [SASD-CORE-001, SASD-CORE-002, SASD-CORE-003, SASD-CORE-004, SASD-CORE-005, SASD-CORE-006, SASD-CORE-007, SASD-CORE-008, SASD-CORE-009, SASD-CORE-010, SASD-CORE-011, SASD-CORE-012, SASD-CORE-013, SASD-GOV-006, SASD-GOV-007]
normative-keywords: []
---

# Core Standard Review 0.3.0

## 1. Reviewziel

Der Review prüfte den vollständigen technologieunabhängigen Core Standard auf:

- interne Widersprüche,
- unnötige oder identische Doppelanforderungen,
- angemessene Abstufung von Minimum, Recommended und Production,
- eindeutige Anwendbarkeit bedingter Anforderungen,
- konsistente Compliance-Begriffe,
- praktische Nutzung durch Einzelentwickler,
- maschinelle Grundprüfbarkeit.

## 2. Umfang

Geprüft wurden 13 Core-Dokumente mit ursprünglich 531 Anforderungs-IDs sowie die angrenzenden Governance-Dokumente zu normativer Sprache, Ausnahmen und Compliance.

Die Prüfung umfasste:

- Metadaten- und Linkvalidierung,
- Eindeutigkeit von Anforderungs-IDs,
- Vergleich identischer und stark ähnlicher Anforderungstexte,
- Vergleich aller Qualitätsstufenmatrizen,
- Prüfung der Dokumentzuständigkeiten,
- Anwendung auf typische kleine, mittlere und risikoreiche Projektszenarien.

## 3. Wesentliche Befunde und Korrekturen

### 3.1 Identische Doppelanforderung

`SASD-LC-023` und `SASD-REQ-050` verlangten wortgleich die Priorisierung von Anforderungen.

**Korrektur:** `SASD-REQ-050` bleibt die fachliche Priorisierungsregel. `SASD-LC-023` beschreibt nun den Zeitpunkt und verlangt, dass die Meilensteinpriorität vor Beginn erkennbar ist.

### 3.2 Uneinheitliche Gesamtstatus

Der Core verwendete teilweise `Compliant`, während Governance `Aligned` vorsah.

**Korrektur:** Einheitliches Statusmodell:

- `Not Assessed`,
- `Assessment in Progress`,
- `Partially Aligned`,
- `Aligned with Exceptions`,
- `Aligned`.

Der Begriff Alignment vermeidet den Eindruck einer externen Zertifizierung.

### 3.3 Unklare Skalierung einzelner Anforderungen

Anforderungstabellen und Qualitätsmatrizen konnten unterschiedlich streng wirken, ohne dass ihr Verhältnis ausdrücklich geregelt war.

**Korrektur:** `QUALITY-LEVELS.md` definiert nun:

- Standardanwendbarkeit,
- Bedingungen und `Not Applicable`,
- Vorrang dokumenteigener Qualitätsmatrizen,
- Vererbung höherer Stufen,
- Profilverschärfungen,
- Rollenbündelung bei Einzelentwicklern.

### 3.4 Absichtliche Querschnittsregeln

Mehrere Themen erscheinen berechtigt in verschiedenen Dokumenten, beispielsweise Secrets, ADRs, Restore-Tests und Provenance. Die Aussagen besitzen unterschiedliche Kontrollzwecke und wurden nicht entfernt.

**Korrektur:** `CORE-RESPONSIBILITY-MAP.md` dokumentiert die primäre Zuständigkeit und zulässige Abgrenzung.

### 3.5 Praxistauglichkeit für Einzelentwickler

Die Pflichten waren grundsätzlich skalierbar, die erlaubte Zusammenlegung von Rollen und Dokumenten jedoch nicht zentral genug beschrieben.

**Korrektur:** Qualitätsstufenregeln und `SOLO-DEVELOPER-GUIDE.md` stellen klar:

- Inhalte dürfen kompakt zusammengeführt werden,
- eine Person darf mehrere Rollen übernehmen,
- Selbstreview bleibt strukturiert nachweisbar,
- hohe Risiken können unabhängige Expertise erfordern.

## 4. Proportionalitätsprüfung

| Szenario | Angemessene Anwendung | Review-Ergebnis |
|---|---|---|
| kleines lokales Hilfsprogramm ohne sensible Daten | Minimum; kompakte Inhalte im README; manuelle reproduzierbare Prüfung möglich | angemessen, sofern Scope, Nutzung, Security-Baseline und Wartungsstatus nicht fehlen |
| langfristig gepflegte öffentliche Desktopanwendung | Recommended; strukturierte Anforderungen, Architektur, Tests, Releases und Compliance-Erklärung | entspricht der vorgesehenen Standardstufe |
| Desktopanwendung mit Zugangsdaten oder personenbezogenen Daten | Recommended mit Production-Hochstufung für Security, Tests, Persistenz und Recovery; gegebenenfalls gesamthaft Production | bereichsweise Hochstufung ist erforderlich und jetzt eindeutig geregelt |
| öffentlich betriebener Dienst mit externen Nutzern | Production; Threat Model, CI-Nachweise, Monitoring, Incident und Recovery | Anforderungen sind anspruchsvoll, aber risikogerecht |
| reines Lernexperiment ohne Veröffentlichung | Minimum; keine simulierten Unternehmensprozesse | ausreichend schlank, sofern keine produktiven Daten oder Systeme beteiligt sind |

## 5. Umgang mit Überschneidungen

Als unnötiges Duplikat gilt eine Aussage, wenn:

- derselbe Gegenstand,
- derselbe Zeitpunkt,
- dieselbe Handlung,
- derselbe Verbindlichkeitsgrad,
- und derselbe Prüfnachweis

in mehreren Dokumenten gefordert werden.

Eine Querschnittsregel bleibt zulässig, wenn sie eine andere Kontrollhandlung beschreibt, beispielsweise Schutz, Ablage, Prüfung, Freigabe oder Aufbewahrung.

## 6. Automatisierte Prüfungen

Das Update ergänzt:

- `validate-core-consistency.py`,
- `generate-core-requirements-index.py`,
- `generate-core-quality-matrix.py`.

Damit werden unter anderem Dokumentstatus, Pflichtabschnitte, normative Schlüsselwörter, exakte Textduplikate, alte Compliance-Begriffe und Aktualität der erzeugten Übersichten geprüft.

## 7. Reviewentscheidung

Die 13 Core-Dokumente erfüllen die Kriterien für den Übergang von **Draft** zu **Proposed**:

- vorgesehene Inhalte sind vollständig,
- bekannte interne Konflikte wurden bereinigt,
- Zuständigkeiten und Anwendbarkeit sind definiert,
- offene Punkte sind auf Pilotierung und fachliche Freigabe begrenzt,
- maschinelle Konsistenzprüfungen sind vorhanden.

`Proposed` bedeutet ausdrücklich noch nicht `Approved`.

## 8. Offene Punkte vor Approved

Vor der Freigabe für Version 1.0 sind weiterhin erforderlich:

1. Anwendung auf mindestens drei Pilotprojekte,
2. Prüfung der tatsächlichen Arbeitslast je Qualitätsstufe,
3. Rückmeldung zu fehlenden oder unprüfbaren Nachweisen,
4. Abgleich mit dem C#/.NET- und Desktopprofil,
5. abschließende fachliche Prüfung sicherheitskritischer Aussagen,
6. dokumentierte Freigabe im Releaseprozess.
