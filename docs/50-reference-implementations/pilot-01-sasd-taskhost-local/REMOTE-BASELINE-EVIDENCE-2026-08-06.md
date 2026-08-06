---
title: "Pilot 01 Remote-Baseline-Evidenz – SASD TaskHost Local"
document-id: SASD-REF-PILOT-114
document-type: informative
status: Draft
version: 0.1.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-08-06
applies-to-quality-levels: [Recommended]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-REF-PILOT-108, SASD-REF-PILOT-111, SASD-REF-RC-008]
---

# Pilot 01 Remote-Baseline-Evidenz – SASD TaskHost Local

## 1. Zweck

Dieses Dokument registriert den erfolgreichen, repositoryübergreifenden Remote-Baseline-Lauf für SASD TaskHost Local. Der Nachweis ist absichtlich enger als eine vollständige Pilotverifikation.

## 2. Identität des Nachweises

| Merkmal | Wert |
|---|---|
| Standard-Repository | `Robin-Goerlach/SASD-Development-Standard` |
| Standard-Commit | `d80baf0cccf66b5c940cfd7f05e399c83f880e1a` |
| Ziel-Repository | `https://github.com/Robin-Goerlach/SASD-TaskHost-Local` |
| Ziel-Commit | `2404feb0904b22274972b5803520e6d86a70047d` |
| GitHub-Actions-Workflow | `TaskHost Local reference baseline` |
| Run-ID | `31100169566` |
| Ergebnis | `success` |
| Betriebssystem | Microsoft Windows `10.0.26100`, X64 |
| Konfiguration | `Release` |
| Evidenzartefakt | `taskhost-baseline-standard-d80baf0cccf66b5c940cfd7f05e399c83f880e1a-target-2404feb0904b22274972b5803520e6d86a70047d` |
| Ausführungszeitraum UTC | 2026-08-06 12:09:16 bis 12:09:36 |

## 3. Automatisierte Schritte

| Schritt | Ergebnis | Exitcode | Dauer |
|---|---|---:|---:|
| `dotnet --info` | Passed | 0 | 2,753 s |
| `dotnet restore` | Passed | 0 | 6,433 s |
| `dotnet build` | Passed | 0 | 8,165 s |
| automatisierte Tests | NotAvailable | — | 0 s |
| NuGet-Audit | Passed | 0 | 1,639 s |
| `dotnet publish` | Passed | 0 | 0,802 s |

Im geprüften Zielcommit ist kein automatisiertes Testprojekt vorhanden. Dieser Zustand wurde als `NotAvailable` ausgewiesen und nicht als bestandener Testlauf interpretiert.

## 4. Erzeugte Evidenz

Das Workflowartefakt enthält:

- `verification-summary.json`,
- `verification-summary.md`,
- Protokolle für .NET-Informationen, Restore, Build, Audit und Publish,
- die veröffentlichte Windows-Anwendung einschließlich `TaskHostLocal.WinForms.exe`,
- die zur SQLite-Laufzeit erforderlichen verwalteten und nativen Abhängigkeiten.

Der Zielarbeitsbaum war vor dem Build nicht verändert. Standard- und Zielcommit sind sowohl in der Zusammenfassung als auch im Artefaktnamen festgehalten.

## 5. Bewertung

| Aussage | Bewertung |
|---|---|
| Öffentlicher Zielcommit reproduzierbar erreichbar | bestätigt |
| Restore und Release-Build unter Windows | bestätigt |
| NuGet-Audit ausgeführt | bestätigt |
| Publish-Artefakt erzeugt | bestätigt |
| Automatisierte Produkttests | nicht verfügbar |
| Headless-Laufzeit-Self-Check | nicht vorhanden beziehungsweise nicht ausgeführt |
| Manueller Windows-Smoke-Test | ausstehend |
| Wave-01-Integration im Ziel-Repository | ausstehend |
| Vollständige Pilotverifikation | ausstehend |

## 6. Schlussfolgerung

Die **Remote Technical Baseline** ist `Passed`. Die **Practical Standard Validation** und der Pilotstatus `verification_state: Passed` bleiben `Pending`.

Dieser Nachweis erhöht die technische Plausibilität des Standards und der Referenzarchitektur. Er rechtfertigt weder den Abschluss von `RC-RDY-003` noch die Freigabe eines Release Candidate oder der stabilen Version 1.0.

## 7. Zugehörige Dokumente

- [Evidenzzuordnung](EVIDENCE-MAP.md)
- [Wave-01-Verifikationsplan](WAVE-01-VERIFICATION-PLAN.md)
- [Pilotmanifest](pilot.json)
- [Spezifikationsbaseline und Validierungsübergabe](../../40-governance/VERSION-1.0-SPECIFICATION-BASELINE.md)
