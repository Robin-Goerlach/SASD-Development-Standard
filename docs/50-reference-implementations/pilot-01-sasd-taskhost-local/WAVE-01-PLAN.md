---
title: "Pilot 01 Wave 01 – Stabilisierung und Engineering-Basis"
document-id: SASD-REF-PILOT-107
document-type: informative
status: Draft
version: 0.8.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-REF-PILOT-106, SASD-PROC-004, SASD-PROF-DOTNET-008, SASD-PROF-DESKTOP-004]
---

# Wave 01 – Stabilisierung und Engineering-Basis

## 1. Ziel

Wave 01 stellt eine startfähige, reproduzierbar baubare und minimal regressionsgeschützte Baseline her. Sie vermeidet Funktionsausbau und größere Architekturänderungen.


## 1.1 Aktueller Ausführungsstand

```text
Implementierungszustand: Artifact Prepared
Verifikationszustand: Pending
Ziel-Commit: noch nicht vorhanden
```

Die Arbeitspakete sind in einem statisch geprüften Overlay vorbereitet. Die Akzeptanzkriterien bleiben bis zur Ausführung des [Verifikationsplans](WAVE-01-VERIFICATION-PLAN.md) offen.

## 2. Arbeitspakete

### WP-01 Baseline und Schutz

- Arbeitsbranch anlegen.
- aktuellen Commit und lokale SDK-Version erfassen.
- vorhandene lokale Datenbank und Backups außerhalb des Repositories sichern.
- Restore und Release-Build ausführen.
- Startfehler mit frischer und bestehender Datenbank reproduzieren.
- keine echten Aufgabendaten in Logs, Screenshots oder Tests verwenden.

**Nachweis:** Baseline-Protokoll mit Befehlen, Exitcodes und Ergebnis.

### WP-02 SQLite-Startfehler

- fehlerhafte SQL-Anweisung exakt identifizieren.
- Schemaerstellung und DML unterscheiden.
- SQL nur im Database-/Repository-Bereich korrigieren.
- Initialisierung in einer kontrollierten Transaktion ausführen, soweit sinnvoll.
- Verhalten für neue und vorhandene Datenbank prüfen.
- Fehler nicht durch pauschales Löschen der Nutzerdaten umgehen.

**Nachweis:** dokumentierte Ursache, Codeänderung, manueller Starttest.

### WP-03 Minimale Regressionstests

Ein Testprojekt `TaskHostLocal.Tests` oder entsprechend der bestehenden Namenskonvention hinzufügen. Mindestens prüfen:

- leere temporäre Datenbank kann initialisiert werden,
- erwartete Tabellen/Strukturen entstehen,
- erneute Initialisierung ist idempotent oder kontrolliert,
- eine einfache Repository-Operation funktioniert,
- Tests verwenden ausschließlich temporäre Dateien und fiktive Daten.

**Nachweis:** erfolgreicher `dotnet test`-Lauf.

### WP-04 Toolchain und Codequalitätsbasis

- `global.json` mit tatsächlich unterstützter SDK-Version hinzufügen,
- `.editorconfig` aus dem SASD-.NET-Profil proportional übernehmen,
- `Directory.Build.props` für Nullable, Analyzer und Metadaten ergänzen,
- Warnungen zunächst sichtbar machen; bestehende Warnungen nicht blind als Fehler eskalieren,
- NuGet-Paketstand und Schwachstellen prüfen,
- Paketupdate nur mit Build- und Testnachweis durchführen.

**Nachweis:** sauber dokumentierter Release-Build und Paketreview.

### WP-05 Continuous Integration

Windows-Workflow hinzufügen, der:

1. Repository auscheckt,
2. festgelegtes .NET-SDK installiert,
3. Restore ausführt,
4. Release-Build ausführt,
5. Tests ausführt.

Actions sollten für eine dauerhafte Fassung auf geprüfte Commit-SHAs gepinnt werden. Ein Publish- oder Release-Schritt ist noch nicht Teil dieser Welle.

**Nachweis:** erfolgreicher Workflow-Lauf.

### WP-06 Lizenz, Security und Alignment

- Lizenzentscheidung bewusst treffen; MIT ist für das kleine lokale Open-Source-Werkzeug eine plausible, aber nicht automatisch vorausgesetzte Wahl,
- `LICENSE` hinzufügen,
- `SECURITY.md` mit privatem Meldeweg und unterstützten Versionen ergänzen,
- `docs/standards/SASD-ALIGNMENT.md` anlegen,
- anwendbare Profile, Qualitätsstufe, offene Gaps und Ausnahmen dokumentieren,
- README-Projektstatus nach erfolgreichem Start aktualisieren.

**Nachweis:** Dateien und nachvollziehbare Entscheidung.

### WP-07 Review und Abschluss

- Build, Tests und Start erneut ausführen,
- manuellen MVP-Testplan soweit möglich durchführen,
- Gap Register aktualisieren,
- keine unnötige Projektaufteilung eingeführt,
- Wave-Review mit Blocker/Major/Minor/Observation durchführen,
- Lessons Learned für den SASD-Standard erfassen.

## 3. Empfohlene Commitfolge im Ziel-Repository

```text
fix(database): repair SQLite schema initialization

test(database): add initialization regression coverage

build: add shared .NET build and SDK configuration

ci: add Windows build and test workflow

docs: add license security and SASD alignment records
```

Die tatsächliche Aufteilung darf kleiner oder größer sein, solange Fehlerkorrektur, Tests, Buildbasis und Dokumentation nachvollziehbar bleiben.

## 4. Akzeptanzkriterien

- [ ] `dotnet restore` erfolgreich
- [ ] `dotnet build -c Release` erfolgreich
- [ ] `dotnet test -c Release` erfolgreich
- [ ] Anwendung startet mit neuer Datenbank ohne SQLite-Syntaxfehler
- [ ] Anwendung startet mit gesicherter Testkopie einer bestehenden Datenbank
- [ ] keine echten Nutzerdaten in Tests oder Repository
- [ ] CI erfolgreich
- [ ] Lizenz entschieden und dokumentiert
- [ ] Security-Meldeweg dokumentiert
- [ ] SASD-Alignment-Dokument vorhanden
- [ ] Gap Register und Review aktualisiert
- [ ] keine unbegründete Architekturvergrößerung

## 5. Stop-Kriterien

Die Welle wird gestoppt und neu geplant, wenn:

- eine Datenmigration Nutzerdaten gefährdet,
- die Ursache des SQL-Fehlers unklar bleibt,
- Tests nur mit echten Daten funktionieren,
- ein Paketupdate inkompatible Datenänderungen erzwingt,
- die Lösung eine grundlegende Neuentwicklung erfordern würde.
