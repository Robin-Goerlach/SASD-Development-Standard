---
title: "Fehler- und Ausnahmebehandlung in .NET"
document-id: SASD-PROF-DOTNET-004
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
depends-on: [SASD-PROF-DOTNET-001, SASD-PROF-DOTNET-003, SASD-CORE-006, SASD-CORE-007, SASD-CORE-008]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Fehler- und Ausnahmebehandlung in .NET

## 1. Zweck

Dieses Dokument trennt erwartete fachliche Ergebnisse, Validierungsfehler, Abbruch und außergewöhnliche technische Fehler. Es definiert Fehlergrenzen, sichere Benutzerkommunikation, Exception-Übersetzung, Retries und Prozessstabilität.

## 2. Geltungsbereich

Die Regeln gelten für synchrone und asynchrone .NET-Anwendungen, Bibliotheken, Hintergrunddienste und Integrationsgrenzen.

## 3. Normative Anforderungen

| ID | Anforderung |
|---|---|
| SASD-DOTNET-REQ-301 | Fehlerzustände MÜSSEN danach modelliert werden, ob sie erwartete fachliche Ergebnisse, Validierungsfehler, Abbruch oder außergewöhnliche technische Fehler darstellen. |
| SASD-DOTNET-REQ-302 | Exceptions SOLLTEN für außergewöhnliche Fehler verwendet werden und DÜRFEN NICHT als reguläre Verzweigungslogik für häufig erwartete Ergebnisse missbraucht werden. |
| SASD-DOTNET-REQ-303 | Erwartete fachliche Nicht-Erfolgsfälle SOLLTEN durch eindeutige Rückgabemodelle, Result-Typen oder domänenspezifische Ergebnisse ausgedrückt werden. |
| SASD-DOTNET-REQ-304 | Öffentliche Grenzen MÜSSEN ungültige Eingaben früh und mit verständlicher Fehlerklassifikation zurückweisen. |
| SASD-DOTNET-REQ-305 | Argumentprüfungen SOLLTEN geeignete Standardausnahmen oder Guard-Methoden verwenden. |
| SASD-DOTNET-REQ-306 | Eigene Exception-Typen SOLLTEN nur eingeführt werden, wenn Aufrufer den Fehlertyp sinnvoll unterscheiden oder behandeln müssen. |
| SASD-DOTNET-REQ-307 | Exception-Namen MÜSSEN auf `Exception` enden und eine fachlich eindeutige Bedeutung besitzen. |
| SASD-DOTNET-REQ-308 | Beim Übersetzen einer Exception MUSS die ursprüngliche Exception als Inner Exception erhalten bleiben, sofern keine Sicherheits- oder Datenschutzgründe dagegensprechen. |
| SASD-DOTNET-REQ-309 | Eine gefangene Exception MUSS mit `throw;` erneut ausgelöst werden, wenn der ursprüngliche Stacktrace erhalten bleiben soll; `throw ex;` DARF NICHT verwendet werden. |
| SASD-DOTNET-REQ-310 | `catch (Exception)` SOLLTE nur an klaren Fehlergrenzen oder für Cleanup und Kontextanreicherung verwendet werden. |
| SASD-DOTNET-REQ-311 | Eine Exception DARF NICHT stillschweigend verworfen werden. |
| SASD-DOTNET-REQ-312 | Ein Catch-Block MUSS den Fehler behandeln, übersetzen, protokollieren oder bewusst weiterwerfen; leere Catch-Blöcke sind unzulässig. |
| SASD-DOTNET-REQ-313 | Eine Exception SOLLTE nur einmal auf der verantwortlichen Grenze mit vollständigem Kontext protokolliert werden, um redundante Fehlerlogs zu vermeiden. |
| SASD-DOTNET-REQ-314 | Benutzernachrichten DÜRFEN NICHT ungefiltert interne Exceptiontexte, Stacktraces, Pfade, SQL, Tokens oder Geheimnisse offenlegen. |
| SASD-DOTNET-REQ-315 | Benutzerorientierte Fehler MÜSSEN eine verständliche Handlungsmöglichkeit oder einen Supportverweis bieten, soweit dies möglich ist. |
| SASD-DOTNET-REQ-316 | Technische Diagnoseinformationen SOLLTEN über Korrelation, Ereignis-ID oder Fehlerreferenz mit der Benutzermeldung verknüpft werden. |
| SASD-DOTNET-REQ-317 | `OperationCanceledException` und `TaskCanceledException` MÜSSEN als Abbruch und nicht automatisch als Anwendungsfehler behandelt werden, wenn das zugehörige Token abgebrochen wurde. |
| SASD-DOTNET-REQ-318 | Abbruchsignale SOLLTEN bis zur verantwortlichen Grenze weitergegeben werden. |
| SASD-DOTNET-REQ-319 | Timeouts MÜSSEN von expliziten Benutzerabbrüchen unterscheidbar sein, wenn unterschiedliche Reaktionen erforderlich sind. |
| SASD-DOTNET-REQ-320 | Wiederholungsversuche SOLLTEN nur für als transient klassifizierte Fehler eingesetzt werden. |
| SASD-DOTNET-REQ-321 | Retries MÜSSEN begrenzt sein und SOLLTEN Backoff, Jitter und Abbruch unterstützen. |
| SASD-DOTNET-REQ-322 | Ein Retry DARF NICHT für eine nicht-idempotente Operation eingesetzt werden, sofern Duplikate oder Teilwirkungen nicht sicher beherrscht werden. |
| SASD-DOTNET-REQ-323 | Transaktionen und Ressourcen MÜSSEN bei Fehlern in einem definierten Zustand beendet oder zurückgerollt werden. |
| SASD-DOTNET-REQ-324 | Cleanup-Code MUSS verhindern, dass die ursprüngliche Exception unbeabsichtigt verdeckt wird. |
| SASD-DOTNET-REQ-325 | Konstruktoren SOLLTEN keine vermeidbaren langlaufenden, externen oder fehleranfälligen Operationen durchführen. |
| SASD-DOTNET-REQ-326 | Hintergrundtasks MÜSSEN beobachtet werden; unbeobachtete Fire-and-Forget-Tasks DÜRFEN NICHT ohne kontrollierte Lebenszyklus- und Fehlerbehandlung gestartet werden. |
| SASD-DOTNET-REQ-327 | Anwendungsweite Fehlergrenzen MÜSSEN den Prozesszustand berücksichtigen und DÜRFEN eine möglicherweise korrupte Anwendung nicht blind weiterlaufen lassen. |
| SASD-DOTNET-REQ-328 | Fatal eingestufte Fehler MÜSSEN zu einer kontrollierten Beendigung, sicheren Degradierung oder Isolation führen. |
| SASD-DOTNET-REQ-329 | Fehlercodes und Result-Typen MÜSSEN stabil und dokumentiert sein, wenn externe Systeme oder persistierte Workflows davon abhängen. |
| SASD-DOTNET-REQ-330 | Fehlerpfade MÜSSEN risikobasiert getestet werden, einschließlich ungültiger Eingaben, I/O-Fehler, Timeout, Abbruch und Teilfehler. |

## 4. Empfohlenes Fehlerflussmodell

```text
Eingabegrenze
  -> Validierung / erwartetes Result
  -> Application- oder Domain-Fehler
  -> technische Adapterfehler
  -> verantwortliche Fehlergrenze
  -> sichere Benutzer- oder Protokollreaktion
```

## 5. Zuordnung zu Qualitätsstufen

| Bereich | Minimum | Recommended | Production |
|---|---|---|---|
| Eingabevalidierung | MUSS | MUSS | MUSS |
| zentrale Fehlergrenze | bei ausführbarer App SOLLTE | MUSS | MUSS |
| Result-/Fehlermodell | bei fachlichen Fällen SOLLTE | MUSS | stabil dokumentiert MUSS |
| Retry-Policy | nur wenn nötig | dokumentiert MUSS | getestet und überwacht MUSS |
| Korrelation | KANN | SOLLTE | MUSS für Support und Betrieb |
| Fehlerpfadtests | kritische Pfade MUSS | risikobasiert MUSS | systematisch MUSS |
| sichere Benutzermeldung | MUSS | MUSS | MUSS |

## 6. Verantwortlichkeiten

Entwickler modellieren Fehler an der richtigen Ebene. Adapter übersetzen technische Fehler nur, wenn ein stabiler Vertrag entsteht. Hosts definieren letzte Fehlergrenzen. Reviewer prüfen insbesondere stille Fehler, Doppel-Logging, falsche Retries und Informationslecks.

## 7. Nachweise und Prüfkriterien

Nachweise sind Fehlertypen, Result-Verträge, globale Handler, Retry-Konfiguration, Fehlerreferenzen, Logs und Tests der Fehlerpfade.

## 8. Ausnahmen und Abweichungen

Frameworks dürfen bestimmte Exception- oder Handlerformen erzwingen. Die Abweichung MUSS dennoch sichere Meldung, Logging, Cleanup und Testbarkeit gewährleisten.

## 9. Verwandte Dokumente

- [Logging](LOGGING.md)
- [Testing](DOTNET-TESTING.md)
- [Core Security](../../10-core-standard/SECURITY.md)
