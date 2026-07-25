---
title: "Pilot 02 Initial Lessons Learned – SASD Prompt Manager"
document-id: SASD-REF-PILOT-211
document-type: informative
status: Draft
version: 0.11.0
standard-version: "1.0"
language: de
authoritative: false
owner: SASD Development Standard Maintainer
last-updated: 2026-07-25
applies-to-quality-levels: [Recommended]
applies-to-profiles: [Core, DotNet, Desktop]
depends-on: [SASD-REF-PILOT-210, SASD-REF-PILOT-004]
---

# Initial Lessons Learned – SASD Prompt Manager

1. Eine gute Schichtenstruktur ersetzt keine schichtenübergreifende Test- und Build-Evidenz.
2. Ein mittleres Einzelentwicklerprojekt kann Recommended erfüllen, ohne Enterprise-Prozesse einzuführen.
3. Promptdaten benötigen eine eigene Vertraulichkeitsbetrachtung, weil Nutzer unbeabsichtigt Secrets speichern können.
4. Backup, Export und Import sind nicht nur Features, sondern zentrale Recovery-Nachweise.
5. Öffentliche Repository-Struktur reicht zur Pilotwahl, nicht für eine Alignment-Aussage.
