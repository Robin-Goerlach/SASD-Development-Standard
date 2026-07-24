---
title: "Releaseprozess"
document-id: SASD-PROC-006
document-type: normative
status: Proposed
version: 0.6.0
standard-version: "1.0"
language: de
authoritative: true
owner: SASD Development Standard Maintainer
last-updated: 2026-07-24
applies-to-quality-levels: [Minimum, Recommended, Production]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-CORE-010, SASD-CORE-008, SASD-CORE-009, SASD-PROC-004]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# Releaseprozess

## 1. Zweck

Dieser Prozess stellt sicher, dass ein überprüfter Quellstand in nachvollziehbare, sichere und supportfähige Releaseartefakte überführt, freigegeben, veröffentlicht und nachkontrolliert wird.

## 2. Geltungsbereich

Der Prozess gilt für öffentliche, interne und produktive Software-Releases sowie für versionierte Infrastruktur-, Konfigurations- oder Dokumentationspakete. Die Tiefe richtet sich nach Qualitätsstufe und Verteilungsrisiko.

## 3. Auslöser und Startbedingungen

- ein Meilenstein ist zur Veröffentlichung vorgesehen
- ein Patch oder Hotfix muss bereitgestellt werden
- eine neue unterstützte Plattform oder ein neues Paketformat wird veröffentlicht
- ein interner, externer oder produktiver Rollout benötigt Freigabe

## 4. Benötigte Eingaben

- festgelegter Release-Scope und Quellstand
- erfolgreiche Build-, Test- und Reviewnachweise
- Changelog und Release Notes
- Sicherheits-, Lizenz- und Abhängigkeitsbewertung
- Migrations-, Rollback- und Supportinformationen

## 5. Rollen und Verantwortlichkeiten

| Rolle | Verantwortung |
|---|---|
| Release Owner | koordiniert Scope, Nachweise und Freigabe |
| Build-/Packaging-Verantwortlicher | erzeugt unveränderte Artefakte |
| Reviewer/QA | prüft Tests, Dokumentation und Readiness |
| Security-/Betriebsrolle | prüft Risiken, Migration und Einführung |
| Freigabeverantwortlicher | genehmigt oder stoppt die Veröffentlichung |

Eine Person darf mehrere Rollen übernehmen. Die Kombination von Rollen hebt jedoch keine Nachweis-, Selbstreview- oder Freigabepflichten auf.

## 6. Prozessablauf

1. Releaseart, Scope, Version und Quellstand festlegen.
2. Readiness-Nachweise und bekannte Risiken zusammenführen.
3. Sauberen Release-Build und Artefakte erzeugen.
4. Tests, Security, Abhängigkeiten, Dokumentation und Migration prüfen.
5. Releasefreigabe dokumentieren.
6. Tag, Release Notes und unveränderte Artefakte veröffentlichen.
7. Veröffentlichung und Einführung verifizieren.
8. Nachwirkungen überwachen und Release abschließen.

## 7. Normative Anforderungen

### Releaseidentität und Scope

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-500 | Jedes veröffentlichte Release MUSS eine eindeutige Version oder anderweitig eindeutige Releasekennung besitzen. |
| SASD-PROC-REQ-501 | Der Release-Scope MUSS die enthaltenen Änderungen, behobenen Fehler und bekannten Einschränkungen benennen. |
| SASD-PROC-REQ-502 | Änderungen außerhalb des freigegebenen Scopes DÜRFEN NICHT unbemerkt in das Release aufgenommen werden. |
| SASD-PROC-REQ-503 | Releaseart und erwartete Kompatibilitätswirkung MÜSSEN vor der Freigabe festgelegt werden. |
| SASD-PROC-REQ-504 | Ein Hotfix MUSS auf den kleinsten vertretbaren Scope begrenzt werden. |
| SASD-PROC-REQ-505 | Interne Builds MÜSSEN von freigegebenen Releases unterscheidbar sein. |

### Readiness und Änderungsstand

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-506 | Der zu veröffentlichende Commit oder Artefaktstand MUSS eindeutig festgelegt und unverändert prüfbar sein. |
| SASD-PROC-REQ-507 | Alle anwendbaren Releasekriterien MÜSSEN vor der Freigabe gegen diesen Stand geprüft werden. |
| SASD-PROC-REQ-508 | Blockierende Issues MÜSSEN geschlossen, verschoben oder formell eskaliert sein. |
| SASD-PROC-REQ-509 | Bekannte Risiken und Ausnahmen MÜSSEN in der Releaseentscheidung sichtbar sein. |
| SASD-PROC-REQ-510 | Die Dokumentation MUSS zum veröffentlichten Funktions- und Konfigurationsstand passen. |
| SASD-PROC-REQ-511 | Das Changelog MUSS die für Nutzer und Maintainer relevanten Änderungen enthalten. |
| SASD-PROC-REQ-512 | Migrations- oder Upgradehinweise MÜSSEN vor der Veröffentlichung verfügbar sein, wenn Nutzermaßnahmen erforderlich sind. |

### Build und Artefakte

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-513 | Releaseartefakte MÜSSEN durch einen dokumentierten oder automatisierten Buildprozess erzeugt werden. |
| SASD-PROC-REQ-514 | Der Build MUSS aus einem sauberen Checkout oder einer gleichwertig kontrollierten Umgebung reproduzierbar angestoßen werden können. |
| SASD-PROC-REQ-515 | Releaseartefakte DÜRFEN NICHT manuell nach dem geprüften Build verändert werden. |
| SASD-PROC-REQ-516 | Artefaktnamen MÜSSEN Produkt, Version und gegebenenfalls Plattform eindeutig erkennen lassen. |
| SASD-PROC-REQ-517 | Prüfsummen SOLLTEN für herunterladbare Releaseartefakte bereitgestellt werden. |
| SASD-PROC-REQ-518 | Production-Artefakte MÜSSEN angemessen signiert oder auf andere Weise gegen unbemerkte Manipulation geschützt werden, soweit die Plattform dies unterstützt. |
| SASD-PROC-REQ-519 | Debug-Symbole und Diagnoseartefakte MÜSSEN gemäß Schutz- und Supportbedarf getrennt behandelt werden. |

### Tests und Qualität

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-520 | Alle für das Release vorgeschriebenen automatisierten Tests MÜSSEN erfolgreich sein. |
| SASD-PROC-REQ-521 | Manuelle Smoke- oder Abnahmetests MÜSSEN für die unterstützten Hauptszenarien durchgeführt werden. |
| SASD-PROC-REQ-522 | Fehlgeschlagene oder übersprungene Tests MÜSSEN vor Freigabe bewertet und dokumentiert werden. |
| SASD-PROC-REQ-523 | Regressionen mit hoher Auswirkung MÜSSEN die Freigabe blockieren. |
| SASD-PROC-REQ-524 | Unterstützte Plattformen, Installationswege und Upgradepfade MÜSSEN entsprechend der Qualitätsstufe geprüft werden. |
| SASD-PROC-REQ-525 | Performance- oder Lasttests MÜSSEN durchgeführt werden, wenn das Release leistungsrelevante Risiken verändert. |
| SASD-PROC-REQ-526 | Die Releaseprüfung SOLLTE die Definition of Done und nicht nur den erfolgreichen Build berücksichtigen. |

### Sicherheit und Abhängigkeiten

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-527 | Offene kritische Sicherheitsbefunde MÜSSEN die Veröffentlichung blockieren, sofern keine ausdrücklich genehmigte Notfallausnahme besteht. |
| SASD-PROC-REQ-528 | Abhängigkeiten MÜSSEN auf bekannte relevante Schwachstellen und unerwartete Änderungen geprüft werden. |
| SASD-PROC-REQ-529 | Secrets und vertrauliche Testdaten DÜRFEN NICHT in Releaseartefakten, Logs oder Metadaten enthalten sein. |
| SASD-PROC-REQ-530 | Lizenz- und Herkunftsanforderungen für enthaltene Drittkomponenten MÜSSEN erfüllt sein. |
| SASD-PROC-REQ-531 | Sicherheitsrelevante Änderungen MÜSSEN in angemessener Weise kommuniziert werden, ohne ausnutzbare Details unnötig vorzeitig offenzulegen. |
| SASD-PROC-REQ-532 | Release-Zugangsdaten und Signierschlüssel MÜSSEN geschützt und auf notwendige Rollen begrenzt sein. |

### Daten, Migration und Rollback

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-533 | Daten- oder Schemaänderungen MÜSSEN mit getesteter Migrationsstrategie veröffentlicht werden. |
| SASD-PROC-REQ-534 | Vor irreversiblen Migrationen MUSS eine geprüfte Sicherungs- oder Wiederherstellungsoption bestehen. |
| SASD-PROC-REQ-535 | Rollbackfähigkeit und ihre Grenzen MÜSSEN vor Freigabe dokumentiert werden. |
| SASD-PROC-REQ-536 | Ein Release DARF NICHT als rückrollbar bezeichnet werden, wenn Datenänderungen den Rückweg verhindern. |
| SASD-PROC-REQ-537 | Kompatibilitätsgrenzen zwischen alten und neuen Versionen MÜSSEN dokumentiert werden. |
| SASD-PROC-REQ-538 | Production-Releases MÜSSEN einen Abbruch- oder Rollback-Entscheidungspunkt für die Einführung besitzen. |

### Freigabe und Veröffentlichung

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-539 | Die Releasefreigabe MUSS durch eine benannte verantwortliche Rolle erfolgen. |
| SASD-PROC-REQ-540 | Der Freigabeverantwortliche MUSS Zugriff auf die relevanten Prüf- und Risikonachweise besitzen. |
| SASD-PROC-REQ-541 | Bei Einzelentwicklung MUSS ein zeitlich getrennter Release-Selbstreview dokumentiert werden. |
| SASD-PROC-REQ-542 | Der Release-Tag MUSS auf den freigegebenen Quellstand zeigen. |
| SASD-PROC-REQ-543 | Release Notes, Artefakte und Prüfsummen MÜSSEN konsistent dieselbe Version bezeichnen. |
| SASD-PROC-REQ-544 | Veröffentlichungskanäle MÜSSEN gegen versehentliche oder unautorisierte Releases geschützt werden. |
| SASD-PROC-REQ-545 | Ein Production-Release SOLLTE nach dem Vier-Augen-Prinzip freigegeben werden, soweit realistisch verfügbar. |

### Nachprüfung und Reaktion

| Anforderungs-ID | Anforderung |
|---|---|
| SASD-PROC-REQ-546 | Nach der Veröffentlichung MUSS geprüft werden, ob Artefakte erreichbar, installierbar und unverändert sind. |
| SASD-PROC-REQ-547 | Betriebene Releases MÜSSEN auf unmittelbare Fehlerindikatoren und kritische Nutzerprobleme überwacht werden. |
| SASD-PROC-REQ-548 | Ein fehlgeschlagenes Release MUSS nach dem vorbereiteten Rollback-, Stop- oder Hotfixverfahren behandelt werden. |
| SASD-PROC-REQ-549 | Releasebezogene Vorfälle MÜSSEN mit Ursache, Auswirkung und Folgemaßnahmen dokumentiert werden. |
| SASD-PROC-REQ-550 | Die tatsächlich veröffentlichte Version MUSS in Roadmap, Changelog oder Releasehistorie nachvollziehbar sein. |
| SASD-PROC-REQ-551 | Wiederkehrende Releaseprobleme SOLLTEN in Automatisierung, Checklisten oder Standardregeln zurückgeführt werden. |
| SASD-PROC-REQ-552 | Veraltete oder unsichere Releases SOLLTEN mit Supportstatus und empfohlenem Nachfolger gekennzeichnet werden. |

## 8. Zuordnung zu Qualitätsstufen

| Qualitätsstufe | Mindesttiefe des Prozesses |
|---|---|
| **Minimum** | Eindeutige Version, sauberer Build, Kernprüfungen, kurze Release Notes und Installations-Smoke-Test. |
| **Recommended** | Vollständige Readiness-Checkliste, reproduzierbare Artefakte, Prüfsummen, Changelog, Upgradehinweise und Nachprüfung. |
| **Production** | Formale Freigabe, Signierung oder gleichwertiger Schutz, Rollback-/Migrationskontrolle, unabhängige Reviews und Betriebsüberwachung. |

Die Qualitätsstufe bestimmt die erforderliche Tiefe, nicht den grundsätzlichen Zweck des Prozesses. Risikoreiche Eigenschaften können unabhängig von Projektgröße oder Teamgröße strengere Maßnahmen auslösen.

## 9. Ergebnisse und Nachweise

- freigegebener Quellstand und Tag
- Releaseartefakte und Prüfsummen
- Release Notes und Changelog
- Readiness- und Freigabenachweis
- Migrations- und Rollbackinformationen
- Verifikations- und Abschlussnachweis

## 10. Abschlusskriterien

Der Prozess gilt erst als abgeschlossen, wenn die anwendbaren Kriterien erfüllt und die Nachweise auffindbar sind:

- [ ] Version, Tag, Artefakte und Release Notes sind konsistent.
- [ ] Erforderliche Tests, Reviews und Securityprüfungen sind erfolgreich.
- [ ] Bekannte Risiken und Ausnahmen sind freigegeben.
- [ ] Installation oder Einführung wurde nachgeprüft.
- [ ] Support- und Rollbackinformationen sind verfügbar.
- [ ] Releasehistorie ist aktualisiert.

## 11. Ausnahmen und Abweichungen

Notfallreleases dürfen einzelne nichtkritische Nachweise nachgelagert erbringen, wenn Risiko, Genehmigung, Rückfalloption und Nachholtermin vor Veröffentlichung dokumentiert sind. Sicherheits- und Artefaktintegrität dürfen dabei nicht stillschweigend entfallen.

Abweichungen von MUSS-Anforderungen werden gemäß [Ausnahmen](../40-governance/EXCEPTIONS.md) behandelt. Nicht anwendbare Anforderungen benötigen eine kurze, überprüfbare Begründung.

## 12. Verwandte Dokumente

- [Core-Releases](../10-core-standard/RELEASES.md)
- [Release-Record-Vorlage](../../templates/documents/RELEASE-RECORD-TEMPLATE.md)
- [Release-Readiness-Checkliste](../../checklists/releases/RELEASE-READINESS-CHECKLIST.md)
- [Release Notes Template](../../templates/documents/RELEASE-NOTES-TEMPLATE.md)

---

**Anforderungsumfang:** 53 Prozessanforderungen in diesem Dokument.
