---
title: "Lebenszyklus von Desktopanwendungen"
document-id: SASD-PROF-DESKTOP-004
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
applies-to-profiles: [Desktop]
depends-on: [SASD-PROF-DESKTOP-001, SASD-PROF-DESKTOP-002, SASD-PROF-DOTNET-004, SASD-PROF-DOTNET-005, SASD-PROF-DOTNET-006, SASD-PROF-DOTNET-007, SASD-PROF-DOTNET-008, SASD-CORE-008, SASD-CORE-010, SASD-CORE-011]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Lebenszyklus von Desktopanwendungen

## 1. Zweck

Dieses Dokument definiert Start, Initialisierung, Instanzmodell, Datenpfade, Migration, Fehlergrenzen, Crash Recovery, Shutdown, Publishing, Installation, Updates, Signierung, Deinstallation und Supportdiagnose.

## 2. Geltungsbereich

Die Regeln gelten für installierte und portable Desktopanwendungen, lokale Daten, Updatekomponenten, Installer, Paketierung und die Zusammenarbeit mit dem Betriebssystem.

## 3. Normative Anforderungen

| ID | Anforderung |
|---|---|
| SASD-DESKTOP-REQ-301 | Der Anwendungsstart MUSS einen klaren Composition Root oder gleichwertigen Bootstrap-Bereich besitzen. |
| SASD-DESKTOP-REQ-302 | Startup-Code MUSS Konfiguration, Logging, Datenmigration, Abhängigkeiten und Hauptfenster in einer nachvollziehbaren Reihenfolge initialisieren. |
| SASD-DESKTOP-REQ-303 | WinForms-Anwendungen auf modernem .NET SOLLTEN `ApplicationConfiguration.Initialize()` oder einen dokumentierten gleichwertigen Bootstrap verwenden. |
| SASD-DESKTOP-REQ-304 | WPF-Anwendungen MÜSSEN Verantwortlichkeiten von `App`, Startup und Hauptfenster eindeutig definieren. |
| SASD-DESKTOP-REQ-305 | Eine Anwendung MUSS bei Startfehlern zwischen reparierbarer Konfiguration, fehlender Abhängigkeit, Datenmigrationsfehler und fatalem Fehler unterscheiden. |
| SASD-DESKTOP-REQ-306 | Startfehler MÜSSEN eine sichere Benutzermeldung und eine auffindbare technische Diagnose erzeugen. |
| SASD-DESKTOP-REQ-307 | Langlaufende Initialisierung SOLLTE Fortschritt, Abbruch oder eine responsive Startansicht bereitstellen. |
| SASD-DESKTOP-REQ-308 | Die Hauptoberfläche DARF NICHT als betriebsbereit erscheinen, solange erforderliche Initialisierungsschritte unvollständig sind. |
| SASD-DESKTOP-REQ-309 | Single-Instance-Verhalten MUSS ausdrücklich entschieden und dokumentiert werden. |
| SASD-DESKTOP-REQ-310 | Eine Single-Instance-Implementierung MUSS parallele Starts, verwaiste Sperren und sichere Übergabe von Startargumenten berücksichtigen. |
| SASD-DESKTOP-REQ-311 | Mehrinstanzbetrieb MUSS Konflikte bei Dateien, Datenbanken, Ports, Einstellungen und Updates beherrschen. |
| SASD-DESKTOP-REQ-312 | Startargumente, Dateizuordnungen und Protokollaktivierungen MÜSSEN validiert werden und DÜRFEN keine ungeprüften Befehle oder Pfade ausführen. |
| SASD-DESKTOP-REQ-313 | Benutzerbezogene Daten SOLLTEN unter einem geeigneten lokalen oder roamingfähigen Anwendungsdatenpfad gespeichert werden. |
| SASD-DESKTOP-REQ-314 | Maschinenweite Daten DÜRFEN NICHT ohne echten gemeinsamen Bedarf und passende Berechtigungen gespeichert werden. |
| SASD-DESKTOP-REQ-315 | Temporäre Dateien MÜSSEN in geeigneten temporären Pfaden angelegt, eindeutig benannt und nach Möglichkeit bereinigt werden. |
| SASD-DESKTOP-REQ-316 | Cache-Daten MÜSSEN von maßgeblichen Benutzerdaten unterscheidbar und ohne Datenverlust neu erzeugbar sein. |
| SASD-DESKTOP-REQ-317 | Logdateien MÜSSEN einen dokumentierten Pfad, Rotation oder Begrenzung und Datenschutzregeln besitzen. |
| SASD-DESKTOP-REQ-318 | Konfigurations- und Datenmigrationen MÜSSEN versioniert, wiederholbar oder transaktional und gegen Teilfehler abgesichert sein. |
| SASD-DESKTOP-REQ-319 | Eine Migration DARF NICHT eine ältere nutzbare Datenbasis ohne vorherige Sicherung oder begründete irreversible Freigabe zerstören. |
| SASD-DESKTOP-REQ-320 | Datenformate MÜSSEN Vorwärts- und Rückwärtskompatibilität oder explizite Inkompatibilitätsgrenzen dokumentieren. |
| SASD-DESKTOP-REQ-321 | Unbehandelte UI-, Task- und Prozessausnahmen MÜSSEN an definierten Fehlergrenzen erfasst und klassifiziert werden. |
| SASD-DESKTOP-REQ-322 | Eine globale Fehlergrenze DARF NICHT den Prozess nach potenziell korrumpierendem Fehler blind weiterlaufen lassen. |
| SASD-DESKTOP-REQ-323 | Crashdiagnose MUSS mindestens Produktversion, Zeitpunkt, Fehlerreferenz und relevante, datenschutzkonforme technische Informationen enthalten. |
| SASD-DESKTOP-REQ-324 | Crashberichte oder Telemetrie DÜRFEN NICHT ohne transparente Information und erforderliche Rechtsgrundlage übertragen werden. |
| SASD-DESKTOP-REQ-325 | Autosave und Wiederherstellung SOLLTEN für lange oder wertvolle Bearbeitungsvorgänge risikobasiert vorgesehen werden. |
| SASD-DESKTOP-REQ-326 | Wiederherstellungsdaten MÜSSEN von regulär gespeicherten Daten unterscheidbar sein und DÜRFEN einen neueren gültigen Stand nicht ungefragt überschreiben. |
| SASD-DESKTOP-REQ-327 | Das Anwendungsshutdown MUSS laufende Operationen, ungespeicherte Änderungen, Hintergrunddienste und Ressourcenfreigabe in definierter Reihenfolge behandeln. |
| SASD-DESKTOP-REQ-328 | Ein Benutzerabbruch des Shutdowns MUSS möglich sein, wenn andernfalls ungespeicherte Daten ohne freigegebene Autosave-Strategie verloren gingen. |
| SASD-DESKTOP-REQ-329 | Hintergrundoperationen MÜSSEN beim Shutdown kontrolliert abgebrochen, abgeschlossen oder in einen sicheren Zustand überführt werden. |
| SASD-DESKTOP-REQ-330 | Der Shutdown DARF NICHT unbegrenzt auf blockierte externe Operationen warten. |
| SASD-DESKTOP-REQ-331 | Erzwungene Beendigung und Betriebssystemshutdown MÜSSEN hinsichtlich Datenintegrität und Wiederanlauf risikobasiert getestet werden. |
| SASD-DESKTOP-REQ-332 | Tray- und Hintergrundbetrieb MÜSSEN eindeutig zwischen Fenster schließen und Anwendung beenden unterscheiden. |
| SASD-DESKTOP-REQ-333 | Eine im Hintergrund weiterlaufende Anwendung MUSS für den Benutzer erkennbar und zuverlässig beendbar sein. |
| SASD-DESKTOP-REQ-334 | Geplante Hintergrundaufgaben MÜSSEN Lebensdauer, Fehlerbehandlung, Ressourcenverbrauch und Shutdownintegration dokumentieren. |
| SASD-DESKTOP-REQ-335 | Das Publish-Modell MUSS framework-dependent, self-contained, Single File, ReadyToRun, Trimming oder andere Optionen ausdrücklich festlegen. |
| SASD-DESKTOP-REQ-336 | Single-File-, Trimming- und AOT-Optionen DÜRFEN NICHT aktiviert werden, ohne UI-Framework, Reflection, Ressourcen, native Bibliotheken und Diagnose zu testen. |
| SASD-DESKTOP-REQ-337 | Für jede unterstützte Architektur MUSS ein passendes Artefakt erzeugt oder eine belastbare Kompatibilitätsaussage dokumentiert werden. |
| SASD-DESKTOP-REQ-338 | Die Installationsform MUSS zwischen per-user, per-machine, portable, MSIX, MSI, ClickOnce, App Installer oder anderer Verteilung unterscheiden. |
| SASD-DESKTOP-REQ-339 | Die Wahl zwischen paketierter und nicht paketierter Anwendung MUSS anhand von Identität, Update, Integrationspunkten, Berechtigungen und Zielumgebung begründet werden. |
| SASD-DESKTOP-REQ-340 | Ein Installer MUSS vorhandene Versionen, Reparatur, Upgrade und Deinstallation definiert behandeln. |
| SASD-DESKTOP-REQ-341 | Eine Deinstallation DARF NICHT Benutzerdaten ohne ausdrückliche, verständliche Auswahl löschen. |
| SASD-DESKTOP-REQ-342 | Dateizuordnungen, Autostart, Dienste, Registryeinträge und Shellintegration MÜSSEN bei Installation und Deinstallation nachvollziehbar verwaltet werden. |
| SASD-DESKTOP-REQ-343 | Updatequellen MÜSSEN authentisch, verschlüsselt und gegen Manipulation geschützt sein. |
| SASD-DESKTOP-REQ-344 | Ein Update MUSS Version, Kompatibilität, laufende Instanz, Datenmigration und erforderlichen Neustart berücksichtigen. |
| SASD-DESKTOP-REQ-345 | Production-Anwendungen SOLLTEN einen getesteten Rollback- oder Wiederherstellungsweg für fehlgeschlagene Updates besitzen. |
| SASD-DESKTOP-REQ-346 | Automatische Updates MÜSSEN Zeitpunkt, Benutzerkontrolle, Bandbreite, Fehler und Wiederaufnahme transparent behandeln. |
| SASD-DESKTOP-REQ-347 | Sicherheitsupdates SOLLTEN gegenüber Funktionsupdates priorisiert und getrennt bewertbar sein. |
| SASD-DESKTOP-REQ-348 | Code Signing MUSS private Schlüssel außerhalb des Repositories schützen und einen kontrollierten Signierprozess verwenden. |
| SASD-DESKTOP-REQ-349 | Signierte Artefakte MÜSSEN nach der Signierung unverändert bleiben und vor Veröffentlichung verifiziert werden. |
| SASD-DESKTOP-REQ-350 | Die Anwendung MUSS ihren Versionsstand, Commit- oder Buildbezug und Releasekanal für Supportzwecke ermitteln lassen. |
| SASD-DESKTOP-REQ-351 | Ein Release MUSS auf einem sauberen Zielsystem oder einer repräsentativen isolierten Umgebung installiert und gestartet werden. |
| SASD-DESKTOP-REQ-352 | Der Release-Smoke-Test MUSS Installation oder Entpacken, Start, Kernablauf, Persistenz, Shutdown und erneuten Start umfassen. |
| SASD-DESKTOP-REQ-353 | Updates MÜSSEN mindestens von der letzten unterstützten Version auf die neue Version geprüft werden. |
| SASD-DESKTOP-REQ-354 | Deinstallation und Neuinstallation SOLLTEN bei Recommended und MÜSSEN bei Production risikobasiert geprüft werden. |
| SASD-DESKTOP-REQ-355 | Betriebs- und Supportdokumentation MUSS Pfade, Logs, Konfiguration, Backup, Diagnose und bekannte Wiederherstellungsmaßnahmen nennen. |
| SASD-DESKTOP-REQ-356 | Die Anwendung MUSS auch bei vollem Datenträger, fehlenden Berechtigungen, beschädigter Konfiguration und nicht erreichbaren Diensten einen definierten Fehlerzustand besitzen. |
| SASD-DESKTOP-REQ-357 | Supportdaten SOLLTEN automatisiert sammelbar sein, MÜSSEN aber vor Export sensible Informationen erkennbar behandeln. |
| SASD-DESKTOP-REQ-358 | Das Ende des Supports einer Desktopversion MUSS dokumentiert und den betroffenen Benutzern angemessen kommuniziert werden. |
| SASD-DESKTOP-REQ-359 | Legacy-Desktopanwendungen MÜSSEN einen Wartungsentscheid für Weiterbetrieb, Modernisierung, Isolation oder Ablösung besitzen. |
| SASD-DESKTOP-REQ-360 | Ein Desktoprelease DARF NICHT veröffentlicht werden, wenn bekannte Datenverlust-, Start-, Update- oder Deinstallationsfehler ohne freigegebene Ausnahme bestehen. |

## 4. Referenz-Lebenszyklus

```text
Start
  -> Bootstrap und Konfiguration
  -> Logging und Diagnose
  -> Instanzprüfung
  -> Datenprüfung und Migration
  -> Hauptoberfläche
  -> laufende Operationen und Autosave
  -> Shutdown-Anforderung
  -> Speichern / Abbruch / Cleanup
  -> Prozessende
```

## 5. Deployment-Entscheidung

| Modell | Vorteil | besonderes Risiko |
|---|---|---|
| framework-dependent | kleineres Artefakt, zentrale Runtimeupdates | Runtime muss vorhanden sein |
| self-contained | kontrollierte Runtime, einfacher Zielbetrieb | größere Artefakte, Runtime muss mit Anwendung aktualisiert werden |
| Single File | einfache Verteilung | native Dateien, Reflection und Diagnose prüfen |
| MSIX / paketiert | Identität, sauberes Installations- und Updatemodell | Signierung, Plattform- und Unternehmensrichtlinien |
| MSI / klassischer Installer | etablierte Unternehmensverteilung | Upgrade- und Custom-Action-Komplexität |
| portable / xcopy | geringe Installationshürde | Datenpfade, Updates, Rechte und Mehrbenutzerbetrieb |

## 6. Zuordnung zu Qualitätsstufen

| Bereich | Minimum | Recommended | Production |
|---|---|---|---|
| Start/Shutdown | dokumentierter Pfad MUSS | Fehler- und Abbruchfälle MÜSSEN | Recovery und erzwungener Shutdown MÜSSEN |
| Datenpfade | getrennt MUSS | Migration und Backup SOLLTEN | Migration, Backup und Restore MÜSSEN |
| Crashdiagnose | Log und Version MÜSSEN | Fehlerreferenz SOLLTE | datenschutzkonformes Supportpaket SOLLTE |
| Publishing | reproduzierbar MUSS | skript- oder CI-fähig MUSS | signiert und freigegeben MUSS |
| Update | manuell beschrieben MUSS | Upgradepfad MUSS | Authentizität, Rollback und Kanalstrategie MÜSSEN |
| Installation | Kernpfad geprüft MUSS | Upgrade und Deinstallation SOLLTEN | saubere Zielsystemmatrix MUSS |
| Support | Pfade und Logs MÜSSEN | Troubleshooting SOLLTE | Lebenszyklus und EOL MÜSSEN |

## 7. Verantwortlichkeiten

Entwickler verantworten Bootstrap, Datenintegrität und Shutdown. Releaseverantwortliche definieren Publish-, Signier-, Installer- und Updateprozess. Betrieb oder Support pflegen Diagnose- und Wiederherstellungswissen. Security Reviewer prüfen Updatequelle, Signierschlüssel, Startargumente und sensible Supportdaten.

## 8. Nachweise und Prüfkriterien

Nachweise sind Startupdiagramm, Datenpfadliste, Migrationsskripte, Installerkonfiguration, Publishprofile, Signierprotokoll, Release-Smoke-Test, Upgrade-/Rollbacktest, Supportanleitung und Versionsanzeige.

## 9. Ausnahmen und Abweichungen

Legacyinstaller, nicht signierte interne Builds oder manuelle Updates können zeitweise zulässig sein, benötigen aber Zielgruppe, Verteilungsweg, Risiko, Schutzmaßnahmen und Ablöseplan. Production-Ausnahmen für Updateauthentizität oder Datenmigration sind besonders zu begründen.

## 10. Verwandte Dokumente

- [Desktop Deployment Plan Template](../../../templates/documents/DESKTOP-DEPLOYMENT-PLAN-TEMPLATE.md)
- [Desktop Release Smoke Test](../../../checklists/releases/DESKTOP-RELEASE-SMOKE-TEST-CHECKLIST.md)
- [.NET Configuration](../dotnet/CONFIGURATION.md)
- [.NET Persistence](../dotnet/PERSISTENCE.md)
- [Core Releases](../../10-core-standard/RELEASES.md)
- [Core Maintenance](../../10-core-standard/MAINTENANCE.md)
