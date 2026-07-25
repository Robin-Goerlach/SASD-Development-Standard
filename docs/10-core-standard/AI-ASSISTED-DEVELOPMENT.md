---
title: "KI-gestützte Entwicklung"
document-id: SASD-CORE-013
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
depends-on: [SASD-FND-003, SASD-GOV-001, SASD-CORE-002, SASD-CORE-004, SASD-CORE-006, SASD-CORE-007, SASD-CORE-008, SASD-CORE-009, SASD-CORE-012]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# KI-gestützte Entwicklung

## 1. Zweck

Dieses Dokument definiert einen verantwortungsvollen, nachvollziehbaren und sicheren Einsatz von KI-Systemen bei Recherche, Planung, Architektur, Implementierung, Dokumentation, Test, Review und Betrieb.

## 2. Geltungsbereich

Der Standard gilt für generative KI, Coding Assistants, Chatbots, agentische Systeme und andere Werkzeuge, deren Ergebnisse in ein Projekt einfließen. KI ist ein Hilfsmittel; Verantwortung und Freigabe verbleiben bei Menschen.

## 3. Grundsätze

- KI-Ergebnisse sind Vorschläge, keine autoritative Wahrheit.
- Der Nutzer bleibt verantwortlich für Anforderungen, Entscheidungen, Code und Releases.
- Kontext wird minimiert und nach Schutzbedarf ausgewählt.
- Ergebnisse werden entsprechend Risiko und Qualitätsstufe geprüft.
- Reproduzierbare Prompts und wichtige Entscheidungen werden dauerhaft gesichert.
- KI-Unterstützung darf Reviews und Tests ergänzen, aber nicht blind ersetzen.

## 4. Normative Anforderungen

### 4.1 Verantwortung und Freigabe

| ID | Anforderung |
|---|---|
| SASD-AI-001 | Für jedes übernommene KI-Ergebnis MUSS eine menschlich verantwortliche Person oder Rolle benannt oder ableitbar sein. |
| SASD-AI-002 | KI-generierte Inhalte MÜSSEN vor Übernahme entsprechend ihrem Risiko fachlich geprüft werden. |
| SASD-AI-003 | Ein KI-System DARF NICHT eigenständig ein Production-Release, eine irreversible Migration oder eine sicherheitskritische Änderung freigeben. |
| SASD-AI-004 | Entscheidungen MÜSSEN anhand von Anforderungen und nachvollziehbaren Gründen getroffen werden, nicht allein aufgrund der überzeugenden Formulierung eines Modells. |
| SASD-AI-005 | Unsicherheit, fehlende Prüfung oder ungeklärte Annahmen MÜSSEN sichtbar bleiben. |

### 4.2 Geeignete Einsatzfälle

KI KANN unter anderem eingesetzt werden für:

- Strukturierung und Ideensammlung,
- Formulierungs- und Dokumentationsentwürfe,
- Code- und Testentwürfe,
- Review-Hinweise,
- Fehlerhypothesen und Troubleshooting-Pläne,
- Übersetzung und Zusammenfassung,
- Generierung wiederholbarer Projektartefakte.

| ID | Anforderung |
|---|---|
| SASD-AI-010 | Einsatzfälle MÜSSEN nach möglichem Schaden bei falschem Ergebnis bewertet werden. |
| SASD-AI-011 | Hochriskante Ergebnisse MÜSSEN durch Primärquellen, Tests, Reviews oder praktische Verifikation bestätigt werden. |
| SASD-AI-012 | KI SOLLTE für wiederholbare Routinearbeiten genutzt werden, wenn die resultierenden Artefakte zuverlässig geprüft werden können. |
| SASD-AI-013 | KI SOLLTE NICHT als einzige Grundlage für Rechts-, Sicherheits-, Medizin-, Finanz- oder andere hochkritische Entscheidungen verwendet werden. |

### 4.3 Kontext, Datenschutz und Geheimnisse

| ID | Anforderung |
|---|---|
| SASD-AI-020 | Vor der Übermittlung von Kontext MUSS geprüft werden, ob Geheimnisse, personenbezogene Daten, vertrauliche Kundendaten oder geschütztes Material enthalten sind. |
| SASD-AI-021 | Geheimnisse und produktive Zugangsdaten DÜRFEN NICHT an externe KI-Dienste übertragen werden. |
| SASD-AI-022 | Personenbezogene und vertrauliche Daten MÜSSEN minimiert, anonymisiert oder durch eine ausdrücklich freigegebene, geeignete Umgebung geschützt werden. |
| SASD-AI-023 | Projektdaten DÜRFEN NICHT allein aus Bequemlichkeit vollständig übertragen werden, wenn ein kleinerer Kontext genügt. |
| SASD-AI-024 | Richtlinien und Vertragsbedingungen des verwendeten KI-Dienstes MÜSSEN für sensible oder geschäftliche Nutzung bewertet werden. |

### 4.4 Prompt- und Kontextqualität

| ID | Anforderung |
|---|---|
| SASD-AI-030 | Ein Prompt SOLLTE Ziel, Kontext, Constraints, erwartetes Ausgabeformat und Prüfkriterien klar beschreiben. |
| SASD-AI-031 | Kritische Annahmen SOLLTEN ausdrücklich benannt werden, statt dem Modell ihre Erfindung zu überlassen. |
| SASD-AI-032 | Wiederverwendbare Prompts SOLLTEN versioniert und mit Zweck, Variablen, Voraussetzungen und erwarteter Prüfung gespeichert werden. |
| SASD-AI-033 | Ein Prompt DARF NICHT die normative Projektdokumentation ersetzen. |
| SASD-AI-034 | Große Aufgaben SOLLTEN in prüfbare Arbeitspakete zerlegt werden, wenn dadurch Fehler leichter erkannt werden. |

### 4.5 Quellen und Faktentreue

| ID | Anforderung |
|---|---|
| SASD-AI-040 | Externe Fakten, Versionen, Schnittstellen, Gesetze und Sicherheitsbehauptungen MÜSSEN bei relevanter Änderungs- oder Fehlerrate anhand geeigneter Quellen verifiziert werden. |
| SASD-AI-041 | Technische Implementierungsentscheidungen SOLLTEN vorrangig gegen offizielle Dokumentation, Spezifikationen oder Quellcode geprüft werden. |
| SASD-AI-042 | Nicht verifizierbare Quellenangaben oder Zitate DÜRFEN NICHT als belegt übernommen werden. |
| SASD-AI-043 | Zusammenfassungen MÜSSEN wesentliche Einschränkungen und Unsicherheiten der Ausgangsquelle erhalten. |

### 4.6 KI-generierter Code und Konfiguration

| ID | Anforderung |
|---|---|
| SASD-AI-050 | KI-generierter Code MUSS denselben Coding-, Review-, Test-, Lizenz- und Sicherheitsanforderungen wie manuell erstellter Code erfüllen. |
| SASD-AI-051 | Übernommener Code MUSS verstanden werden, soweit dies für sichere Wartung und Freigabe erforderlich ist. |
| SASD-AI-052 | Abhängigkeiten, APIs und Konfigurationswerte MÜSSEN auf Existenz, Version, Lizenz und angemessene Verwendung geprüft werden. |
| SASD-AI-053 | Sicherheitskritische Logik, Kryptographie, Authentifizierung, Berechtigungen und Datenmigrationen MÜSSEN vertieft geprüft werden. |
| SASD-AI-054 | KI-generierte Tests DÜRFEN NICHT lediglich die generierte Implementierung wiederholen; sie müssen Anforderungen und unabhängige Erwartungen prüfen. |
| SASD-AI-055 | Unnötige Abstraktionen, erfundene Anforderungen und nicht verwendete Bestandteile MÜSSEN entfernt werden. |

### 4.7 Lizenz und geistiges Eigentum

| ID | Anforderung |
|---|---|
| SASD-AI-060 | Übernommene Inhalte MÜSSEN hinsichtlich Lizenz, Urheberrecht, Vertraulichkeit und Herkunft bewertet werden. |
| SASD-AI-061 | Erkennbar fremde längere Code- oder Textpassagen DÜRFEN NICHT ohne Prüfung der Nutzungsrechte übernommen werden. |
| SASD-AI-062 | KI-Nutzung DARF NICHT dazu verwendet werden, Lizenz- oder Vertraulichkeitsregeln zu umgehen. |
| SASD-AI-063 | Production-Projekte SOLLTEN verwendete Werkzeuge und besondere IP-Risiken in ihrer Compliance- oder Projektdokumentation benennen. |

### 4.8 Reviews und Tests

| ID | Anforderung |
|---|---|
| SASD-AI-070 | KI-Reviews KÖNNEN menschliche Reviews ergänzen, DÜRFEN aber bei hohem Risiko nicht die einzige Prüfung sein. |
| SASD-AI-071 | Ergebnisse MÜSSEN praktisch getestet werden, wenn eine Ausführung oder Simulation möglich und für die Freigabe relevant ist. |
| SASD-AI-072 | Sicherheitsbehauptungen MÜSSEN durch geeignete Analyse, Tests oder fachliche Prüfung belegt werden. |
| SASD-AI-073 | Wiederkehrende Modellfehler SOLLTEN in Prompts, Checklisten oder Tooling berücksichtigt werden. |

### 4.9 Agentische und autonome Werkzeuge

| ID | Anforderung |
|---|---|
| SASD-AI-080 | Agentische Werkzeuge MÜSSEN mit minimal notwendigen Berechtigungen und klaren Arbeitsgrenzen betrieben werden. |
| SASD-AI-081 | Schreibzugriff auf Repository, Cloud, Datenbanken oder Produktivsysteme MUSS ausdrücklich freigegeben und protokollierbar sein. |
| SASD-AI-082 | Irreversible Aktionen MÜSSEN eine menschliche Bestätigung oder technisch gleichwertige Schutzbarriere besitzen. |
| SASD-AI-083 | Toolausgaben und Seiteneffekte MÜSSEN vor der Freigabe geprüft werden. |
| SASD-AI-084 | Ein Agent DARF NICHT selbstständig Schutzmechanismen, Prüfungen oder Freigaben deaktivieren, um ein Ziel schneller zu erreichen. |

### 4.10 Nachvollziehbarkeit

| ID | Anforderung |
|---|---|
| SASD-AI-090 | Wesentliche KI-unterstützte Entscheidungen und Artefakte MÜSSEN so dokumentiert sein, dass Verantwortung und Prüfung nachvollziehbar bleiben. |
| SASD-AI-091 | Production-Projekte SOLLTEN für sicherheits-, architektur- oder migrationskritische Ergebnisse Werkzeug, Datum, relevanten Kontext und Prüfnachweise festhalten. |
| SASD-AI-092 | Nicht jeder flüchtige Prompt MUSS archiviert werden; wiederverwendbare und entscheidungsrelevante Prompts SOLLTEN erhalten bleiben. |
| SASD-AI-093 | Ein KI-Chat DARF NICHT die einzige Historie einer Projektentscheidung bleiben. |

## 5. Prüftiefe nach Risikoklasse

| Risikoklasse | Beispiel | Mindestprüfung |
|---|---|---|
| niedrig | Formulierung, Gliederung, einfache Beispiele | Plausibilitätsprüfung |
| mittel | regulärer Code, Tests, Konfiguration, Architekturentwurf | Review, Build und passende Tests |
| hoch | Security, Auth, Datenmigration, Deployment, rechtliche Aussagen | Primärquellen, vertiefter Review, Tests und ausdrückliche Freigabe |
| kritisch | irreversible Production-Aktion, Schlüsselverwaltung, erhebliche Schäden | menschliche Kontrolle, getrennte Freigabe und Recovery-Plan |

## 6. Zuordnung zu Qualitätsstufen

| Maßnahme | Minimum | Recommended | Production |
|---|---|---|---|
| menschliche Verantwortung | MUSS | MUSS | MUSS |
| fachliche Prüfung | risikobasiert MUSS | MUSS | vertieft MUSS |
| Promptversionierung | KANN | für Wiederverwendung SOLLTE | für kritische Abläufe MUSS |
| Werkzeug-/Kontextdokumentation | KANN | bei wichtigen Ergebnissen SOLLTE | bei kritischen Ergebnissen MUSS |
| Schutz sensibler Daten | MUSS | MUSS | MUSS mit freigegebener Umgebung |
| Agentenberechtigungen | minimal MUSS | kontrolliert MUSS | minimal, protokolliert und freigegeben MUSS |
| unabhängiger Review | KANN | bei hohem Risiko SOLLTE | bei kritischen Änderungen MUSS |

## 7. Verantwortlichkeiten

Nutzer des KI-Systems prüfen Kontext und Ergebnis. Projektverantwortliche definieren zulässige Werkzeuge und Risikogrenzen. Reviewer bewerten unabhängige Korrektheit. Security- oder Datenschutzverantwortliche genehmigen sensible Nutzung, soweit vorhanden.

## 8. Nachweise und Prüfkriterien

Geeignete Nachweise sind Prompt-Metadaten, Reviewkommentare, Testprotokolle, Quellen, Toolkonfiguration, Berechtigungsübersicht, Compliance-Eintrag und dokumentierte Freigabe.

## 9. Ausnahmen und Abweichungen

Eine Ausnahme von Datenschutz-, Geheimnis- oder Freigaberegeln ist nur mit dokumentierter Rechtsgrundlage, Risikobewertung, Schutzmaßnahmen und verantwortlicher Genehmigung zulässig.

## 10. Verwandte Dokumente

- [Sicherheitsstandard](SECURITY.md)
- [Qualitätsstandard](QUALITY.md)
- [Teststandard](TESTING.md)
- [Wissensmanagement](KNOWLEDGE-MANAGEMENT.md)
- [Prompt-Metadaten-Template](../../templates/prompts/PROMPT-METADATA-TEMPLATE.md)
