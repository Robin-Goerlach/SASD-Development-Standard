---
title: "Logging und Diagnose in .NET"
document-id: SASD-PROF-DOTNET-005
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
applies-to-profiles: [DotNet]
depends-on: [SASD-PROF-DOTNET-001, SASD-PROF-DOTNET-004, SASD-CORE-006, SASD-CORE-008, SASD-CORE-011]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Logging und Diagnose in .NET

## 1. Zweck

Dieses Dokument definiert strukturiertes, datenschutzgerechtes und betrieblich nutzbares Logging für .NET-Anwendungen. Es trennt Diagnose, Monitoring und Auditierung und verhindert sensible oder unkontrollierte Protokollierung.

## 2. Geltungsbereich

Die Regeln gelten für lokale Anwendungen, Dienste, Bibliotheken und verteilte Systeme. Bibliotheken SOLLTEN keine globale Loggingkonfiguration erzwingen.

## 3. Normative Anforderungen

| ID | Anforderung |
|---|---|
| SASD-DOTNET-REQ-401 | Anwendungscode SOLLTE die abstrahierte .NET-Logging-API `ILogger` beziehungsweise `ILogger<T>` oder einen gleichwertigen Adapter verwenden. |
| SASD-DOTNET-REQ-402 | Logger SOLLTEN über Dependency Injection oder den Application Host bereitgestellt und DÜRFEN NICHT unkontrolliert pro Klasse neu konfiguriert werden. |
| SASD-DOTNET-REQ-403 | Logereignisse MÜSSEN einen angemessenen Level verwenden und DÜRFEN reguläre Zustände nicht als Fehler klassifizieren. |
| SASD-DOTNET-REQ-404 | `Trace` und `Debug` SOLLTEN detaillierter Diagnose dienen, `Information` regulären Meilensteinen, `Warning` beherrschbaren Abweichungen, `Error` fehlgeschlagenen Operationen und `Critical` systemgefährdenden Zuständen. |
| SASD-DOTNET-REQ-405 | Logs SOLLTEN strukturierte Message Templates mit benannten Eigenschaften verwenden statt relevante Werte ausschließlich in vorformatierten Text einzubetten. |
| SASD-DOTNET-REQ-406 | Property-Namen in Logs MÜSSEN innerhalb des Projekts konsistent sein, insbesondere für Operation, Entity, Correlation, User, Tenant und Duration. |
| SASD-DOTNET-REQ-407 | Exceptions MÜSSEN über den dafür vorgesehenen Loggerparameter übergeben werden, wenn Stacktrace und Exceptiontyp benötigt werden. |
| SASD-DOTNET-REQ-408 | Ein Fehler SOLLTE nur an der Ebene protokolliert werden, die ihn abschließend behandelt oder mit relevantem Kontext weitergibt. |
| SASD-DOTNET-REQ-409 | Secrets, Passwörter, Tokens, private Schlüssel und vollständige Verbindungszeichenfolgen DÜRFEN NICHT protokolliert werden. |
| SASD-DOTNET-REQ-410 | Personenbezogene oder vertrauliche Daten DÜRFEN NICHT ohne dokumentierte Notwendigkeit, Minimierung und Schutzmaßnahme protokolliert werden. |
| SASD-DOTNET-REQ-411 | Freitext-Eingaben und externe Payloads MÜSSEN vor Protokollierung hinsichtlich Umfang, Steuerzeichen, Injection und Sensitivität bewertet werden. |
| SASD-DOTNET-REQ-412 | Ein Projekt MUSS geeignete Redaction-, Maskierungs- oder Hashing-Regeln definieren, wenn sensible Identifikatoren für Diagnosezwecke benötigt werden. |
| SASD-DOTNET-REQ-413 | Länger laufende Operationen SOLLTEN eine Korrelations- oder Operations-ID besitzen, die über Prozess- und Integrationsgrenzen weitergegeben wird. |
| SASD-DOTNET-REQ-414 | Verteilte Anwendungen SOLLTEN standardisierte Trace- und Span-Kontexte verwenden. |
| SASD-DOTNET-REQ-415 | Start, kontrolliertes Ende, Version, Umgebung und wesentliche betriebliche Konfiguration SOLLTEN ohne Geheimnisse protokolliert werden. |
| SASD-DOTNET-REQ-416 | Fehlende oder ungültige kritische Konfiguration MUSS vor Aufnahme des regulären Betriebs sichtbar fehlschlagen. |
| SASD-DOTNET-REQ-417 | Hohe Ereignisraten MÜSSEN hinsichtlich Performance, Kosten und Informationswert begrenzt werden. |
| SASD-DOTNET-REQ-418 | Hot Paths SOLLTEN Source-Generated Logging oder gleichwertige performante Muster verwenden, wenn Messungen einen relevanten Nutzen zeigen. |
| SASD-DOTNET-REQ-419 | Logprovider, Ziel, Mindestlevel und Filter MÜSSEN konfigurierbar sein, ohne Codeänderungen zu erfordern. |
| SASD-DOTNET-REQ-420 | Lokale Dateilogs MÜSSEN Rotation, Größenbegrenzung, Zugriffsschutz und Aufbewahrung berücksichtigen. |
| SASD-DOTNET-REQ-421 | Produktionslogs MÜSSEN eine definierte Aufbewahrung und Löschung besitzen. |
| SASD-DOTNET-REQ-422 | Zeitstempel MÜSSEN eindeutig interpretierbar sein und SOLLTEN in UTC oder mit Offset gespeichert werden. |
| SASD-DOTNET-REQ-423 | Production-Logs SOLLTEN mindestens Anwendungsversion, Umgebung, Prozess- oder Instanzkennung und relevante Korrelationsdaten enthalten. |
| SASD-DOTNET-REQ-424 | Auditereignisse MÜSSEN von reinem Diagnoselogging unterschieden und gegen unbefugte Änderung oder Löschung angemessen geschützt werden. |
| SASD-DOTNET-REQ-425 | Logging DARF NICHT allein als Audit-, Monitoring- oder Fehlerbehandlungsstrategie betrachtet werden. |
| SASD-DOTNET-REQ-426 | Ein Support-Bundle SOLLTE nur freigegebene Diagnoseinformationen sammeln und MUSS vor Weitergabe sensible Daten minimieren. |
| SASD-DOTNET-REQ-427 | Logkonfiguration und Redaction-Regeln MÜSSEN risikobasiert getestet werden. |
| SASD-DOTNET-REQ-428 | Loggingfehler DÜRFEN die Hauptfunktion nicht unbegrenzt blockieren; Verlust- und Degradationsverhalten MÜSSEN für Production festgelegt sein. |

## 4. Ereignisgestaltung

Ein gutes Ereignis beantwortet möglichst:

- Was ist geschehen?
- In welcher Operation und Version?
- Welches fachliche oder technische Objekt war betroffen?
- War der Vorgang erfolgreich, abgebrochen oder fehlgeschlagen?
- Welche sichere Korrelation ermöglicht weitere Diagnose?

## 5. Zuordnung zu Qualitätsstufen

| Bereich | Minimum | Recommended | Production |
|---|---|---|---|
| strukturierte API | SOLLTE | MUSS | MUSS |
| Level und Filter | MUSS | MUSS | MUSS |
| Secret- und Datenschutz | MUSS | MUSS | MUSS, getestet |
| Korrelation | KANN | SOLLTE | MUSS bei mehrstufigen Vorgängen |
| Rotation/Aufbewahrung | bei Dateilog MUSS | MUSS | MUSS mit Löschkonzept |
| Audittrennung | bei Auditbedarf MUSS | MUSS | geschützt MUSS |
| Support-Bundle | KANN | SOLLTE bei Desktop/Service | MUSS, wenn Supportprozess dies benötigt |
| Telemetrieausfall | KANN | Verhalten SOLLTE | Verhalten MUSS definiert sein |

## 6. Verantwortlichkeiten

Entwickler definieren Ereignisse und Datenminimierung. Betreiber konfigurieren Provider, Filter, Aufbewahrung und Zugriffe. Security- und Datenschutzverantwortliche prüfen sensible Felder. Maintainer dokumentieren Diagnose- und Supportwege.

## 7. Nachweise und Prüfkriterien

Nachweise sind Loggingkonfiguration, Beispielereignisse, Redaction-Tests, Rotation und Aufbewahrung, Zugriffsregeln, Support-Bundle-Inhalt und Betriebsdokumentation.

## 8. Ausnahmen und Abweichungen

Ein alternatives Loggingframework ist zulässig, wenn strukturierte Ereignisse, Abstraktion, Filterung, Datenschutz, Korrelation und Tests gleichwertig erfüllt werden.

## 9. Verwandte Dokumente

- [Error Handling](ERROR-HANDLING.md)
- [Configuration](CONFIGURATION.md)
- [Core Security](../../10-core-standard/SECURITY.md)
- [Core Maintenance](../../10-core-standard/MAINTENANCE.md)
