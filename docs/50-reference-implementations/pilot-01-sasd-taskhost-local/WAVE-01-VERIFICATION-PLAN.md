---
title: "Pilot 01 Wave 01 Verifikationsplan"
document-id: SASD-REF-PILOT-112
document-type: informative
status: Draft
version: 0.8.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Recommended]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-REF-PILOT-107, SASD-REF-PILOT-111, SASD-PROC-004]
---

# Wave 01 Verifikationsplan – SASD TaskHost Local

## 1. Ziel

Dieser Plan überführt das vorbereitete Artefakt in einen identifizierten, geprüften Ziel-Repository-Stand. Er ist keine Aufforderung, fehlgeschlagene Prüfungen zu überspringen oder bestehende Nutzerdaten ungesichert zu verwenden.

## 2. Vorbedingungen

- sauberer lokaler Clone des Ziel-Repositories,
- keine uncommitted Änderungen oder bewusst gesicherter Arbeitsstand,
- Windows mit .NET-Desktopunterstützung,
- Sicherung einer vorhandenen TaskHost-Datenbank außerhalb des Repositories,
- Prüfung der vorbereiteten MIT-Lizenzentscheidung,
- SHA-256-Abgleich des Updatepakets.

## 3. Einspielnachweis

Zu erfassen:

```text
Baseline commit:
Arbeitsbranch:
Artefakt-SHA-256:
Datum:
Bearbeiter:
Ergebnis von git status vor Einspielung:
Ergebnis von git diff --stat nach Einspielung:
```

## 4. Automatisierte Verifikation

Aus dem Repository-Stamm:

```powershell
python .    oolingalidate-wave-01.py
powershell -ExecutionPolicy Bypass -File .\scriptserify-wave-01.ps1
```

Zusätzlich mindestens erfassen:

```powershell
dotnet --info
dotnet restore .\TaskHostLocal.sln
dotnet build .\TaskHostLocal.sln -c Release --no-restore
dotnet test .\TaskHostLocal.sln -c Release --no-build
```

Für jeden Befehl werden Exitcode, Datum, SDK-Version und relevante Ausgabe dokumentiert.

## 5. Datenbank- und Startverifikation

### Frische Datenbank

1. sicherstellen, dass eine separate Testumgebung verwendet wird,
2. Anwendung starten,
3. Standardliste und leere Aufgabenansicht prüfen,
4. Liste und Aufgabe anlegen,
5. Anwendung schließen und erneut öffnen,
6. Persistenz prüfen.

### Kopie einer bestehenden Datenbank

1. vorhandene Datenbank mit dem Skript sichern,
2. ausschließlich mit einer Testkopie arbeiten,
3. Anwendung starten,
4. Datenbestand und Schema prüfen,
5. eine nicht destruktive Änderung durchführen,
6. erneut starten und Persistenz prüfen.

### Fehlerfall

- Schreibschutz oder absichtlich ungültigen Testpfad verwenden,
- Diagnosemeldung und Logpfad prüfen,
- sicherstellen, dass keine echte Datenbank gelöscht oder überschrieben wird.

## 6. CI-Verifikation

Nach Commit und Push erfassen:

- vollständige Commit-ID,
- Workflow-Name und Run-ID,
- Ergebnis von Restore, Build, Test und Audit,
- hochgeladene Testartefakte,
- offene Warnungen,
- gegebenenfalls Fehlerursache und Folgecommit.

Die Existenz von `.github/workflows/ci.yml` genügt nicht als CI-Nachweis.

## 7. Akzeptanzkriterien

- [ ] Ziel-Commit eindeutig identifiziert
- [ ] statischer Wave-Validator erfolgreich
- [ ] Restore erfolgreich
- [ ] Release-Build erfolgreich
- [ ] alle automatisierten Tests erfolgreich
- [ ] Start mit frischer Datenbank erfolgreich
- [ ] Start mit gesicherter Testkopie erfolgreich
- [ ] keine unerwartete Datenlöschung oder destruktive Migration
- [ ] Diagnosepfad praktisch geprüft
- [ ] CI-Lauf erfolgreich
- [ ] Lizenzentscheidung bestätigt
- [ ] Gap Register und Evidenzzuordnung aktualisiert
- [ ] Wellenreview abgeschlossen

## 8. Stop-Kriterien

Verifikation wird gestoppt, wenn:

- Build oder Tests fehlschlagen,
- Datenintegrität nicht beurteilt werden kann,
- eine Migration bestehende Daten verändert, ohne dass dies geplant war,
- der Startfehler weiterhin auftritt und seine Ursache unklar bleibt,
- das Update nur durch Löschen der Nutzerdaten funktioniert,
- Lizenz- oder Eigentümerentscheidung nicht bestätigt ist.

## 9. Ergebnisrecord

Das Ergebnis wird mit der Vorlage `templates/documents/PILOT-VERIFICATION-RECORD-TEMPLATE.md` erfasst. Erst bei vollständig erfüllten Kriterien darf `verification_state` auf `Passed` und der Pilotstatus auf `Wave Validated` gesetzt werden.
