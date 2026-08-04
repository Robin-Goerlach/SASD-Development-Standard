namespace TaskHostLocal.WinForms.Verification;

/// <summary>
/// Maschinenlesbarer Bericht des kopflosen Selbsttests.
/// </summary>
internal sealed class SelfCheckReport
{
    /// <summary>
    /// Versionskennung des Berichtsformats.
    /// </summary>
    public string SchemaVersion { get; init; } = "1.0";

    /// <summary>
    /// UTC-Zeitpunkt des Testbeginns.
    /// </summary>
    public DateTime StartedUtc { get; init; }

    /// <summary>
    /// UTC-Zeitpunkt des Testendes.
    /// </summary>
    public DateTime CompletedUtc { get; set; }

    /// <summary>
    /// Gesamtstatus des Selbsttests.
    /// </summary>
    public bool Success { get; set; }

    /// <summary>
    /// Produktversion des geprüften Builds.
    /// </summary>
    public string ApplicationVersion { get; init; } = string.Empty;

    /// <summary>
    /// Verwendete .NET-Laufzeit.
    /// </summary>
    public string RuntimeVersion { get; init; } = string.Empty;

    /// <summary>
    /// Betriebssystembeschreibung.
    /// </summary>
    public string OperatingSystem { get; init; } = string.Empty;

    /// <summary>
    /// Prozessarchitektur.
    /// </summary>
    public string ProcessArchitecture { get; init; } = string.Empty;

    /// <summary>
    /// Gibt an, ob eine isolierte temporäre Datenbank verwendet wurde.
    /// </summary>
    public bool UsedTemporaryDatabase { get; init; }

    /// <summary>
    /// SHA-256-Prüfsumme der geprüften Datenbank vor der optionalen Bereinigung.
    /// </summary>
    public string? DatabaseSha256 { get; set; }

    /// <summary>
    /// Ausgeführte Einzelschritte.
    /// </summary>
    public List<SelfCheckStep> Steps { get; } = [];

    /// <summary>
    /// Typ der aufgetretenen Ausnahme, sofern der Test fehlschlug.
    /// </summary>
    public string? ErrorType { get; set; }

    /// <summary>
    /// Bereinigte Fehlermeldung ohne Aufgabeninhalte.
    /// </summary>
    public string? ErrorMessage { get; set; }
}

/// <summary>
/// Ergebnis eines einzelnen Selbsttestschrittes.
/// </summary>
internal sealed class SelfCheckStep
{
    /// <summary>
    /// Stabiler Name des Prüfschritts.
    /// </summary>
    public required string Name { get; init; }

    /// <summary>
    /// Statuswert <c>Passed</c> oder <c>Failed</c>.
    /// </summary>
    public required string Status { get; init; }

    /// <summary>
    /// Laufzeit des Schritts in Millisekunden.
    /// </summary>
    public long DurationMilliseconds { get; init; }

    /// <summary>
    /// Kurzer technischer Hinweis ohne Nutzdaten.
    /// </summary>
    public string? Message { get; init; }
}
