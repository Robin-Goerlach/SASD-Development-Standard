# Verifikation des SASD-Promptpaket-Imports

## Automatisierte Prüfungen

```powershell
dotnet restore .\Sasd.PromptManager.sln
dotnet build .\Sasd.PromptManager.sln --configuration Release --no-restore
dotnet test .\Sasd.PromptManager.sln --configuration Release --no-build
```

Die Tests decken gültige Verzeichnisse und ZIPs, Prüfsummenmanipulation, ZIP-Path-Traversal sowie
die Status- und Typabbildung ab.

## Manueller Roundtrip mit Paket 0.13.0

1. Prompt Manager mit bestehenden Testdaten starten.
2. Vollständiges Backup exportieren.
3. `SASD-Development-Standard-Prompt-Package-0.13.0-candidate.zip` analysieren.
4. Erwartung: 39 Prompts, neun Kategorien, keine Integritätsfehler.
5. Standardstrategie `Skip` wählen und importieren.
6. Erwartung beim ersten Import: 39 neue Prompts.
7. Kategorien, Tags, Source, Notes, Variablen und `NeedsReview` stichprobenartig prüfen.
8. Dasselbe Paket erneut analysieren.
9. Erwartung: 39 vorhandene IDs und bei `Skip` keine Änderungen.
10. Einen Prompt im Paket in einer kontrollierten Testkopie ändern, Prüfsummen neu erzeugen und mit
    `Update` importieren. Versionshistorie prüfen.
11. Vorab-Sicherung lokalisieren und Wiederherstellbarkeit in einem separaten Testdatenverzeichnis prüfen.

## Noch nicht behauptete Nachweise

Das Repository-Update enthält Quellcode und Tests. Ein erfolgreicher Windows-Build, ein grüner
GitHub-Actions-Lauf und der manuelle 39-Prompt-Roundtrip müssen nach dem Commit separat ausgeführt
und dokumentiert werden.
