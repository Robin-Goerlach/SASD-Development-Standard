---
title: "User Experience für Desktopanwendungen"
document-id: SASD-PROF-DESKTOP-003
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
depends-on: [SASD-PROF-DESKTOP-001, SASD-PROF-DESKTOP-002, SASD-PROF-DOTNET-004, SASD-PROF-DOTNET-005, SASD-CORE-006, SASD-CORE-007, SASD-CORE-008, SASD-CORE-009]
normative-keywords: [MUSS, DARF NICHT, SOLLTE, SOLLTE NICHT, KANN]
---

# User Experience für Desktopanwendungen

## 1. Zweck

Dieses Dokument definiert Mindestanforderungen für verständliche, konsistente, zugängliche und fehlertolerante Desktopoberflächen. Es behandelt Aufgabenfluss, Texte, Validierung, Dialoge, Tastaturbedienung, Accessibility, DPI, Layout, Zustände und Lokalisierung.

## 2. Geltungsbereich

Die Regeln gelten für sichtbare und assistiv zugängliche UI-Elemente, Dialoge, Tabellen, Formulare, Benachrichtigungen, Statusanzeigen, Einstellungen und zentrale Benutzerabläufe.

## 3. Normative Anforderungen

| ID | Anforderung |
|---|---|
| SASD-DESKTOP-REQ-201 | Die wichtigsten Benutzeraufgaben MÜSSEN mit möglichst wenigen klaren und konsistenten Schritten erreichbar sein. |
| SASD-DESKTOP-REQ-202 | Gleiche Aktionen, Begriffe, Icons und Tastenkürzel MÜSSEN innerhalb einer Anwendung konsistent verwendet werden. |
| SASD-DESKTOP-REQ-203 | Die Hauptansicht MUSS den aktuellen Kontext, den Arbeitsgegenstand und den Anwendungszustand verständlich erkennen lassen. |
| SASD-DESKTOP-REQ-204 | Beschriftungen MÜSSEN aus Sicht des Benutzers formuliert sein und SOLLTEN interne technische Begriffe vermeiden. |
| SASD-DESKTOP-REQ-205 | Steuerelemente MÜSSEN eindeutige sichtbare oder assistiv zugängliche Namen besitzen. |
| SASD-DESKTOP-REQ-206 | Pflichtfelder, erlaubte Formate und Einschränkungen SOLLTEN vor oder während der Eingabe erkennbar sein. |
| SASD-DESKTOP-REQ-207 | Validierungsfehler MÜSSEN in unmittelbarer Nähe der betroffenen Eingabe und zusätzlich in verständlicher Form verfügbar sein. |
| SASD-DESKTOP-REQ-208 | Ein Validierungsfehler DARF NICHT ausschließlich durch eine kurzzeitig angezeigte MessageBox kommuniziert werden. |
| SASD-DESKTOP-REQ-209 | Fehlermeldungen MÜSSEN beschreiben, was nicht funktioniert hat, welche Auswirkung besteht und was der Benutzer als Nächstes tun kann. |
| SASD-DESKTOP-REQ-210 | Technische Fehlerdetails SOLLTEN über eine optionale Diagnoseansicht oder Fehlerreferenz erreichbar sein, ohne die Hauptmeldung zu überladen. |
| SASD-DESKTOP-REQ-211 | Erfolgsmeldungen SOLLTEN nur angezeigt werden, wenn der Erfolg nicht bereits eindeutig aus dem neuen Zustand hervorgeht. |
| SASD-DESKTOP-REQ-212 | Blockierende Meldungsdialoge SOLLTEN sparsam verwendet werden und DÜRFEN nicht als allgemeiner Benachrichtigungskanal dienen. |
| SASD-DESKTOP-REQ-213 | Destruktive Aktionen MÜSSEN eindeutig benannt und von ungefährlichen Standardaktionen visuell und semantisch unterscheidbar sein. |
| SASD-DESKTOP-REQ-214 | Eine Bestätigungsabfrage MUSS die konkrete Auswirkung nennen und SOLLTE nur bei erheblichem oder schwer rückgängig zu machendem Risiko verwendet werden. |
| SASD-DESKTOP-REQ-215 | Wo sinnvoll SOLLTE eine rückgängig machbare Aktion einer häufigen Bestätigungsabfrage vorgezogen werden. |
| SASD-DESKTOP-REQ-216 | Die Standardaktion eines Dialogs MUSS sicher und erwartbar sein; eine destruktive Aktion DARF NICHT unbeabsichtigt die Standardbestätigung erhalten. |
| SASD-DESKTOP-REQ-217 | Abbrechen, Schließen und Verwerfen MÜSSEN klar unterscheidbar sein, wenn sie unterschiedliche Folgen haben. |
| SASD-DESKTOP-REQ-218 | Ungespeicherte Änderungen MÜSSEN vor Verlust geschützt oder durch eine dokumentierte Autosave-Strategie abgesichert werden. |
| SASD-DESKTOP-REQ-219 | Die Anwendung MUSS vollständig über die Tastatur bedienbar sein, soweit die eingesetzten Controls und Kernaufgaben dies ermöglichen. |
| SASD-DESKTOP-REQ-220 | Die Tab-Reihenfolge MUSS der visuellen und fachlichen Lesereihenfolge entsprechen. |
| SASD-DESKTOP-REQ-221 | Der Tastaturfokus MUSS sichtbar sein und DARF nicht durch Styling unsichtbar gemacht werden. |
| SASD-DESKTOP-REQ-222 | Nach Navigation, Dialogschluss und Validierungsfehler SOLLTE der Fokus an einer vorhersehbaren und hilfreichen Position stehen. |
| SASD-DESKTOP-REQ-223 | Tastenkürzel MÜSSEN dokumentiert und konfliktfrei sein, wenn sie für Kernfunktionen verwendet werden. |
| SASD-DESKTOP-REQ-224 | Standardkonventionen wie Kopieren, Einfügen, Rückgängig, Speichern, Suchen und Schließen SOLLTEN nicht ohne wichtigen Grund neu belegt werden. |
| SASD-DESKTOP-REQ-225 | Steuerelemente mit nicht selbsterklärendem Inhalt MÜSSEN geeignete Accessibility-Namen, Beschreibungen oder Labels bereitstellen. |
| SASD-DESKTOP-REQ-226 | Informationen DÜRFEN NICHT ausschließlich über Farbe, Position, Ton oder Animation vermittelt werden. |
| SASD-DESKTOP-REQ-227 | Text und wichtige Bedienelemente MÜSSEN einen ausreichenden visuellen Kontrast besitzen. |
| SASD-DESKTOP-REQ-228 | Die Benutzeroberfläche SOLLTE bei Windows-Kontrastdesigns und geänderten Systemfarben funktionsfähig und verständlich bleiben. |
| SASD-DESKTOP-REQ-229 | Benutzerdefinierte Controls MÜSSEN Accessibility, Tastaturbedienung, Fokus, Skalierung und Zustandsanzeige ausdrücklich berücksichtigen. |
| SASD-DESKTOP-REQ-230 | Animationen SOLLTEN funktional begründet, kurz und nicht störend sein; kritische Abläufe DÜRFEN NICHT von Animationen abhängen. |
| SASD-DESKTOP-REQ-231 | Blinkende oder stark bewegte Inhalte SOLLTEN vermieden werden und benötigen eine ausdrückliche UX- und Accessibility-Begründung. |
| SASD-DESKTOP-REQ-232 | Formulare und Fenster MÜSSEN bei den unterstützten DPI-Skalierungen ohne abgeschnittene Kerninhalte oder unzugängliche Aktionen funktionieren. |
| SASD-DESKTOP-REQ-233 | Layouts SOLLTEN flexible Container, Anchoring, Docking oder WPF-Layoutmechanismen statt starrer Pixelpositionierung verwenden. |
| SASD-DESKTOP-REQ-234 | Eine Anwendung MUSS mit der dokumentierten Mindestfenstergröße sinnvoll bedienbar sein. |
| SASD-DESKTOP-REQ-235 | Fenstergrößen und Positionen KÖNNEN wiederhergestellt werden, MÜSSEN aber bei geänderter Monitoranordnung in einen sichtbaren Bereich korrigiert werden. |
| SASD-DESKTOP-REQ-236 | Dialoge SOLLTEN sich sinnvoll relativ zu ihrem Besitzer öffnen und DÜRFEN nicht unbeabsichtigt außerhalb sichtbarer Arbeitsbereiche erscheinen. |
| SASD-DESKTOP-REQ-237 | Mehrmonitorbetrieb MUSS mindestens Wechsel des Hauptmonitors, unterschiedliche Skalierungen und entfernte Monitore berücksichtigen, sofern die Anwendung Fensterpositionen speichert. |
| SASD-DESKTOP-REQ-238 | Ladezustände MÜSSEN von leeren Ergebnissen und Fehlerzuständen unterscheidbar sein. |
| SASD-DESKTOP-REQ-239 | Leere Ansichten SOLLTEN erklären, warum keine Daten sichtbar sind und welche nächste Aktion möglich ist. |
| SASD-DESKTOP-REQ-240 | Fortschrittsanzeigen MÜSSEN zwischen bestimmtem und unbestimmtem Fortschritt unterscheiden, wenn eine belastbare Fortschrittsmessung möglich ist. |
| SASD-DESKTOP-REQ-241 | Eine Beschäftigtanzeige DARF den Benutzer nicht über einen weiter nutzbaren Teil der Anwendung täuschen; blockierte und verfügbare Bereiche MÜSSEN erkennbar sein. |
| SASD-DESKTOP-REQ-242 | Statusleisten und dauerhafte Statusbereiche SOLLTEN nur Informationen anzeigen, die zum aktuellen Arbeitskontext gehören. |
| SASD-DESKTOP-REQ-243 | Tabellen und Listen MÜSSEN Auswahl, Sortierung, Filterung und Bearbeitbarkeit eindeutig erkennen lassen. |
| SASD-DESKTOP-REQ-244 | Tabellen mit vielen Daten SOLLTEN Paging, Filter, Suche oder Virtualisierung passend zum Nutzungsszenario anbieten. |
| SASD-DESKTOP-REQ-245 | Spaltenüberschriften MÜSSEN fachlich verständlich sein; interne Feldnamen DÜRFEN NICHT ungeprüft angezeigt werden. |
| SASD-DESKTOP-REQ-246 | Datums-, Zeit-, Zahlen- und Währungsformate MÜSSEN zur ausgewählten Kultur oder ausdrücklich dokumentierten Fachkonvention passen. |
| SASD-DESKTOP-REQ-247 | Sortierung, Suche und Vergleiche MÜSSEN die relevante Kultur und Groß-/Kleinschreibung bewusst behandeln. |
| SASD-DESKTOP-REQ-248 | Benutzertexte DÜRFEN NICHT durch Stringverkettung erzeugt werden, wenn dadurch Grammatik oder Lokalisierung unzuverlässig wird. |
| SASD-DESKTOP-REQ-249 | Die Oberfläche MUSS längere übersetzte Texte und variable Zahlenformate berücksichtigen, wenn Lokalisierung vorgesehen ist. |
| SASD-DESKTOP-REQ-250 | Icons MÜSSEN bei unterschiedlichen Skalierungen scharf und in Bedeutung konsistent bleiben. |
| SASD-DESKTOP-REQ-251 | Ein Icon ohne Text SOLLTE einen Tooltip und einen assistiv zugänglichen Namen besitzen. |
| SASD-DESKTOP-REQ-252 | Tooltips DÜRFEN NICHT unverzichtbare Informationen enthalten, die auf anderem Weg nicht zugänglich sind. |
| SASD-DESKTOP-REQ-253 | Kontextmenüs SOLLTEN nur ergänzende oder redundante Aktionen anbieten; zentrale Funktionen MÜSSEN auch über einen sichtbaren oder tastaturzugänglichen Weg erreichbar sein. |
| SASD-DESKTOP-REQ-254 | Einstellungen MÜSSEN verständliche Standardwerte, Gültigkeitsbereiche und Auswirkungen besitzen. |
| SASD-DESKTOP-REQ-255 | Eine Änderung mit Neustarterfordernis MUSS vor dem Anwenden erkennbar sein. |
| SASD-DESKTOP-REQ-256 | Benutzer SOLLTEN geänderte UI-Einstellungen auf sinnvolle Standardwerte zurücksetzen können. |
| SASD-DESKTOP-REQ-257 | Die Anwendung SOLLTE einen klar erreichbaren Bereich für Version, Lizenz, Support- und Datenschutzinformationen besitzen. |
| SASD-DESKTOP-REQ-258 | Recommended- und Production-Projekte MÜSSEN zentrale Arbeitsabläufe mit repräsentativen Benutzern, Reviewern oder strukturierten heuristischen Tests prüfen. |
| SASD-DESKTOP-REQ-259 | Production-Anwendungen SOLLTEN kritische Accessibility-Szenarien mit mindestens Tastatur, Skalierung und einem geeigneten assistiven Prüfwerkzeug testen. |
| SASD-DESKTOP-REQ-260 | UX-Abweichungen und bekannte Einschränkungen MÜSSEN priorisiert, nachvollziehbar dokumentiert und bei Releases bewertet werden. |

## 4. Verpflichtende UI-Zustände

Eine datenorientierte Ansicht SOLLTE mindestens folgende Zustände bewusst darstellen:

1. Initialisierung oder Laden,
2. bereit mit Daten,
3. bereit ohne Daten,
4. Bearbeitung mit ungespeicherten Änderungen,
5. Validierungsfehler,
6. technischer Fehler,
7. nicht verfügbar oder fehlende Berechtigung.

Nicht jede Ansicht benötigt ein eigenes visuelles Element für jeden Zustand; der Zustand MUSS jedoch für den Benutzer eindeutig sein.

## 5. Zuordnung zu Qualitätsstufen

| Bereich | Minimum | Recommended | Production |
|---|---|---|---|
| Kernaufgaben | verständlich MUSS | heuristisch geprüft MUSS | mit repräsentativen Nutzern SOLLTE |
| Tastatur | Kernabläufe MUSS | vollständiger Review MUSS | Regression und assistiver Test MÜSSEN |
| Accessibility-Namen | wesentliche Controls MÜSSEN | alle nicht selbsterklärenden Controls MÜSSEN | automatisiert und manuell geprüft SOLLTEN |
| DPI | Hauptfenster SOLLTE | relevante Fenster MÜSSEN | definierte DPI-/Monitor-Matrix MUSS |
| Validierung | verständlich MUSS | inline und fokussiert MUSS | barrierefrei und systematisch getestet MUSS |
| Lokalisierung | bei Bedarf MUSS | Ressourcenmodell SOLLTE | Übersetzungs- und Layouttest MÜSSEN |
| UX-Nachweis | kurze Checkliste MUSS | Reviewbericht SOLLTE | dokumentierter Abnahmetest MUSS |

## 6. Verantwortlichkeiten

Produktverantwortliche definieren Benutzeraufgaben und Prioritäten. UI-Entwickler setzen Interaktion, Layout und Accessibility um. Reviewer prüfen Tastatur, Fokus, Texte, Fehlerzustände, DPI und irreversible Aktionen. Nutzerfeedback MUSS als Anforderung oder Verbesserung nachvollziehbar bewertet werden.

## 7. Nachweise und Prüfkriterien

Nachweise sind Aufgabenbeschreibungen, Screenshots, Tastaturläufe, Accessibility-Inspektionen, DPI-/Mehrmonitorprüfungen, UX-Testberichte, Fehlerzustandskataloge, Lokalisierungstests und dokumentierte bekannte Einschränkungen.

## 8. Ausnahmen und Abweichungen

Frameworkgrenzen oder Altcontrols können Accessibility und Skalierung einschränken. Abweichungen MÜSSEN betroffene Benutzer, Auswirkung, Workaround, Ersatzplanung und Priorität enthalten. Rein optische Präferenz ist keine ausreichende Begründung für eine Barrierefreiheitsabweichung.

## 9. Verwandte Dokumente

- [UI-Architektur](UI-ARCHITECTURE.md)
- [Desktop Release Smoke Test](../../../checklists/releases/DESKTOP-RELEASE-SMOKE-TEST-CHECKLIST.md)
- [Desktop UX Review](../../../checklists/development/DESKTOP-UX-REVIEW-CHECKLIST.md)
- [Core Quality](../../10-core-standard/QUALITY.md)
- [Core Security](../../10-core-standard/SECURITY.md)
