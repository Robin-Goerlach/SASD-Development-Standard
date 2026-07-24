# Release-Readiness-Checkliste

## Identität und Scope

- [ ] Version, Releaseart, Commit und Tag sind festgelegt.
- [ ] Scope, bekannte Einschränkungen und Kompatibilitätswirkung sind dokumentiert.
- [ ] Blockierende Issues sind geschlossen oder formell behandelt.
- [ ] Changelog, Release Notes und Nutzerhinweise sind aktuell.

## Build, Tests und Artefakte

- [ ] Release-Build wurde aus sauberem Stand erzeugt.
- [ ] Automatisierte Tests sind erfolgreich.
- [ ] Manuelle Smoke-/Abnahmetests sind dokumentiert.
- [ ] Unterstützte Plattformen und Installationswege wurden geprüft.
- [ ] Artefakte wurden nach dem Build nicht verändert.
- [ ] Namen, Versionen und Prüfsummen sind konsistent.

## Sicherheit, Daten und Betrieb

- [ ] Kritische Security-Findings sind geschlossen oder Notfallausnahme ist genehmigt.
- [ ] Abhängigkeiten und Lizenzen wurden geprüft.
- [ ] Artefakte enthalten keine Secrets oder vertraulichen Testdaten.
- [ ] Migration, Backup und Rollback wurden getestet oder nachvollziehbar geprüft.
- [ ] Support-, Diagnose- und Einführungsinformationen sind vorhanden.

## Freigabe und Nachprüfung

- [ ] Review und Releasefreigabe sind dokumentiert.
- [ ] Tag zeigt auf den freigegebenen Quellstand.
- [ ] Veröffentlichungskanal ist geschützt.
- [ ] Download, Integrität und Installation wurden nach Veröffentlichung geprüft.
- [ ] Monitoring oder Nutzerfeedback für unmittelbare Probleme ist organisiert.
