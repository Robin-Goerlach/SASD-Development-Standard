# Checkliste: Definition of Done

Diese Baseline wird projektspezifisch ergänzt. Nicht anwendbare Punkte werden ausdrücklich gekennzeichnet statt stillschweigend ausgelassen.

## Zweck und Umfang

- [ ] Änderung ist einer Anforderung, einem Fehler, einer Wartungsaufgabe oder einer Entscheidung zugeordnet.
- [ ] Scope und Nicht-Ziele der Änderung sind klar.
- [ ] Akzeptanzkriterien sind erfüllt.

## Umsetzung

- [ ] Implementierung, Konfiguration und Datenänderungen sind vollständig.
- [ ] Namen, Struktur und Verantwortlichkeiten sind verständlich.
- [ ] Keine unbegründeten temporären Workarounds oder toten Artefakte verbleiben.
- [ ] Kompatibilität, Migration und Rückwärtsfolgen wurden bewertet.

## Qualität und Tests

- [ ] Build oder entsprechende Validierung ist erfolgreich.
- [ ] Relevante Unit-, Integrations-, System- und manuelle Tests sind erfolgreich.
- [ ] Neue oder behobene Fehler besitzen geeignete Regressionstests, soweit sinnvoll.
- [ ] Warnungen und statische Findings sind bewertet.
- [ ] Flaky oder quarantänisierte Tests sind dokumentiert und nachverfolgt.

## Sicherheit und Datenschutz

- [ ] Externe Eingaben und Berechtigungen sind angemessen behandelt.
- [ ] Keine Geheimnisse oder produktiven Zugangsdaten wurden eingecheckt.
- [ ] Abhängigkeiten und neue Drittkomponenten sind geprüft.
- [ ] Logging und Fehlerausgaben legen keine unnötigen sensiblen Daten offen.
- [ ] Sicherheits- und Datenschutzrisiken sind behoben, akzeptiert oder nachverfolgt.

## Dokumentation und Wissen

- [ ] README, Anforderungen, Architektur, Konfiguration und Betriebsdokumentation sind aktualisiert.
- [ ] Wesentliche Entscheidungen sind als ADR oder gleichwertig dokumentiert.
- [ ] Changelog oder Release Notes sind vorbereitet, soweit relevant.
- [ ] Troubleshooting, Migration und bekannte Einschränkungen sind ergänzt.

## Integration und Freigabe

- [ ] Änderung ist in die Hauptlinie integrierbar.
- [ ] Pflichtprüfungen sind erfolgreich oder besitzen eine genehmigte Ausnahme.
- [ ] Review oder strukturierte Selbstprüfung ist abgeschlossen.
- [ ] Offene Risiken und technische Schulden sind sichtbar.
- [ ] Der freigegebene Stand ist eindeutig identifizierbar.
