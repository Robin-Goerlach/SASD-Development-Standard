---
title: "Release-Candidate-Plan für Version 1.0"
document-id: SASD-REF-RC-001
document-type: informative
status: Draft
version: 0.12.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-25
applies-to-quality-levels: [Recommended, Production]
applies-to-profiles: [Core]
depends-on: [SASD-FND-007, SASD-GOV-004, SASD-CORE-010, SASD-PROC-006, SASD-REF-BASELINE-007, SASD-REF-PILOT-007, SASD-REF-CI-003]
---

# Release-Candidate-Plan für Version 1.0

## 1. Zweck

Dieses Dokument beschreibt den kontrollierten Übergang von der freigegebenen normativen Baseline `0.9.0` zum ersten Release Candidate `1.0.0-rc.1`.

Der Plan trennt ausdrücklich:

1. **inhaltliche Freigabe** der normativen Dokumente,
2. **technische Release-Readiness** des Repository-Stands,
3. **Erzeugung** reproduzierbarer Releaseartefakte,
4. **Verifikation** der erzeugten Artefakte,
5. **Maintainer-Entscheidung** zur Veröffentlichung,
6. **Git-Tag und GitHub Release**.

Keiner dieser Schritte darf durch das bloße Vorhandensein von Skripten, Vorlagen oder Workflowdateien als abgeschlossen gelten.

## 2. Vorgesehene Releaseidentität

| Eigenschaft | Wert |
|---|---|
| Standardversion | `1.0.0-rc.1` |
| Dokumentbasis | Approved Baseline `0.9.0` |
| Autoritative Sprache | Deutsch |
| Vorgesehener Git-Tag | `v1.0.0-rc.1` |
| GitHub-Status | Pre-release |
| Releaseart | Release Candidate |

## 3. Freigabeumfang

Der Release Candidate umfasst:

- die 46 Approved normativen Dokumente,
- Foundation und Governance,
- Core Standard,
- C#/.NET-Profil,
- Desktopprofil,
- operative Prozesse,
- Vorlagen, Checklisten und Prompts,
- Validierungs- und Releasewerkzeuge,
- dokumentierte Referenzpilot-Baselines,
- Changelog, Release Notes, Known Issues und Release Record,
- reproduzierbare Markdown- und Source-Archive mit SHA-256-Prüfsummen.

Nicht Bestandteil des Release Candidate sind:

- stabile Version `1.0.0`,
- spätere Linux-, Datenbank-, Container- oder Kubernetes-Profile,
- eine Behauptung vollständiger technischer Verifikation aller drei Pilotprojekte,
- Word- und PDF-Ausgaben als bereits abgeschlossenes Ergebnis,
- Zertifizierung fremder Projekte.

## 4. Releasephasen

### Phase RC-0 – Vorbereitung

- Releaseplan, Blockerregister und Known-Issues-Entwurf anlegen.
- Release Notes und Release Record vorbereiten.
- deterministische Paket- und Prüfsummenwerkzeuge bereitstellen.
- manuell auslösbaren Preview-Workflow bereitstellen.
- Release-Readiness automatisiert und nachvollziehbar berichten.

### Phase RC-1 – Evidenz schließen

- erfolgreichen Ubuntu- und Windows-Lauf für den vorgesehenen Releasecommit nachweisen,
- `SASD merge gate` für exakt denselben Commit nachweisen,
- Ruleset aktivieren oder eine dokumentierte Maintainer-Entscheidung zur Verschiebung treffen,
- mindestens einen praktisch ausgeführten Pilotdurchlauf verifizieren,
- offene Blocker schließen oder als genehmigte, befristete Releaseentscheidung dokumentieren.

### Phase RC-2 – Paket erzeugen

- sauberen Checkout des vorgesehenen Releasecommits verwenden,
- Quality Gates ausführen,
- Readiness mit `--require-ready` prüfen,
- deterministische Source- und Markdown-Archive erzeugen,
- Manifest und SHA-256-Prüfsummen erzeugen,
- Archive mit dem unabhängigen Verifier prüfen.

### Phase RC-3 – Maintainer-Freigabe

- Release-Candidate-Checkliste abschließen,
- Release Record mit Commit, Workflow-Lauf, Artefakten und Known Issues vervollständigen,
- Maintainer-Entscheidung dokumentieren,
- annotierten Tag `v1.0.0-rc.1` auf genau den freigegebenen Commit setzen.

### Phase RC-4 – Veröffentlichung

- GitHub Pre-release aus dem bestehenden Tag erstellen,
- Release Notes veröffentlichen,
- die zuvor geprüften Artefakte unverändert hochladen,
- Prüfsummen veröffentlichen,
- Release nach Veröffentlichung erneut herunterladen und verifizieren.

### Phase RC-5 – Kandidatenprüfung

- Einstieg aus README und Dokumentation durchspielen,
- Artefakte in einer sauberen Umgebung prüfen,
- Feedback und Fehler als RC-Befunde erfassen,
- Word-/PDF-Publikationspfad praktisch testen,
- Entscheidung über `rc.2` oder stabile `1.0.0` treffen.

## 5. Release-Gates

| Gate | Bedeutung | Aktueller Zustand |
|---|---|---|
| G1 Normative Freigabe | alle erforderlichen normativen Dokumente Approved | Erfüllt |
| G2 Repository-Qualität | lokale und Remote-Quality-Gates erfolgreich | Remote-Nachweis offen |
| G3 Pilotpraxis | mindestens ein Pilotdurchlauf technisch verifiziert | Offen |
| G4 CI-Governance | Merge Gate nachgewiesen; Ruleset bewertet | Offen |
| G5 Releaseunterlagen | Notes, Record, Known Issues und Manifest vorbereitet | Mit diesem Update vorbereitet |
| G6 Reproduzierbare Artefakte | Paketbau und unabhängige Prüfung erfolgreich | Werkzeug vorbereitet; Ausführung offen |
| G7 Maintainer-Freigabe | dokumentierte Freigabe für exakten Commit | Offen |
| G8 Veröffentlichung | Tag und GitHub Pre-release veröffentlicht | Offen |

## 6. Zulässige Entscheidungen bei offenen Bedingungen

Ein Release-Blocker darf nicht durch Umbenennung oder bloße Notiz verschwinden. Eine offene Bedingung kann nur:

1. erfüllt,
2. als nicht anwendbar mit nachvollziehbarer Begründung bewertet,
3. durch eine genehmigte und befristete Releaseentscheidung akzeptiert,
4. oder durch Verschiebung des Release Candidate offen gehalten werden.

Die Freigabe eines Release Candidate trotz einer akzeptierten Abweichung muss im Release Record, in den Known Issues und in den Release Notes sichtbar sein.

## 7. Reproduzierbarkeit

Der Paketbau muss:

- Dateien in stabiler Reihenfolge verarbeiten,
- feste ZIP-Zeitstempel verwenden,
- generierte Laufzeitartefakte ausschließen,
- Pfade gegen Directory Traversal prüfen,
- Version und Commit in einem maschinenlesbaren Manifest festhalten,
- SHA-256-Prüfsummen erzeugen,
- bei identischem Quellstand identische Archive erzeugen.

## 8. Verwandte Dokumente

- [Release-Readiness](VERSION-1.0-RELEASE-CANDIDATE-READINESS.md)
- [Blockerregister](VERSION-1.0-RELEASE-CANDIDATE-BLOCKERS.md)
- [Release Notes Draft](VERSION-1.0-RELEASE-NOTES-DRAFT.md)
- [Release Record Draft](VERSION-1.0-RC1-RELEASE-RECORD-DRAFT.md)
- [Publikationsprofil](VERSION-1.0-PUBLICATION-PROFILE.md)
- [Version-1.0-Akzeptanzkriterien](../00-foundation/VERSION-1.0-ACCEPTANCE-CRITERIA.md)
- [Release-Standard](../10-core-standard/RELEASES.md)
- [Releaseprozess](../30-processes/RELEASE-PROCESS.md)
