namespace TaskHostLocal.WinForms.Verification;

/// <summary>
/// Konfiguration des kopflosen TaskHost-Local-Selbsttests.
/// </summary>
internal sealed class SelfCheckOptions
{
    private const string SelfCheckSwitch = "--self-check";
    private const string DatabaseSwitch = "--database";
    private const string ReportSwitch = "--report";
    private const string KeepDatabaseSwitch = "--keep-database";

    /// <summary>
    /// Vollständiger Pfad der isolierten SQLite-Datenbank.
    /// </summary>
    public required string DatabasePath { get; init; }

    /// <summary>
    /// Vollständiger Pfad des JSON-Berichts.
    /// </summary>
    public required string ReportPath { get; init; }

    /// <summary>
    /// Gibt an, ob eine automatisch erzeugte temporäre Datenbank nach dem Test erhalten bleibt.
    /// </summary>
    public bool KeepTemporaryDatabase { get; init; }

    /// <summary>
    /// Gibt an, ob der Datenbankpfad automatisch für diesen Test erzeugt wurde.
    /// </summary>
    public bool UsesTemporaryDatabase { get; init; }

    /// <summary>
    /// Prüft, ob der kopflose Selbsttest angefordert wurde.
    /// </summary>
    public static bool IsSelfCheckRequested(IEnumerable<string> args)
    {
        ArgumentNullException.ThrowIfNull(args);
        return args.Any(argument => string.Equals(argument, SelfCheckSwitch, StringComparison.OrdinalIgnoreCase));
    }

    /// <summary>
    /// Liest die unterstützten Kommandozeilenparameter.
    /// </summary>
    /// <exception cref="ArgumentException">Parameter fehlen, sind unbekannt oder besitzen keinen Wert.</exception>
    public static SelfCheckOptions Parse(string[] args)
    {
        ArgumentNullException.ThrowIfNull(args);

        if (!IsSelfCheckRequested(args))
        {
            throw new ArgumentException($"Der Parameter '{SelfCheckSwitch}' fehlt.", nameof(args));
        }

        string? databasePath = null;
        string? reportPath = null;
        var keepTemporaryDatabase = false;

        for (var index = 0; index < args.Length; index++)
        {
            var argument = args[index];

            if (string.Equals(argument, SelfCheckSwitch, StringComparison.OrdinalIgnoreCase))
            {
                continue;
            }

            if (string.Equals(argument, KeepDatabaseSwitch, StringComparison.OrdinalIgnoreCase))
            {
                keepTemporaryDatabase = true;
                continue;
            }

            if (string.Equals(argument, DatabaseSwitch, StringComparison.OrdinalIgnoreCase))
            {
                databasePath = ReadValue(args, ref index, DatabaseSwitch);
                continue;
            }

            if (string.Equals(argument, ReportSwitch, StringComparison.OrdinalIgnoreCase))
            {
                reportPath = ReadValue(args, ref index, ReportSwitch);
                continue;
            }

            throw new ArgumentException($"Unbekannter Self-Check-Parameter: '{argument}'.", nameof(args));
        }

        var usesTemporaryDatabase = string.IsNullOrWhiteSpace(databasePath);
        databasePath ??= Path.Combine(
            Path.GetTempPath(),
            "SASD",
            "TaskHostLocal",
            "self-check",
            Guid.NewGuid().ToString("N"),
            "taskhost-self-check.db");

        reportPath ??= Path.Combine(
            Environment.CurrentDirectory,
            "verification-results",
            "self-check-report.json");

        return new SelfCheckOptions
        {
            DatabasePath = Path.GetFullPath(databasePath),
            ReportPath = Path.GetFullPath(reportPath),
            KeepTemporaryDatabase = keepTemporaryDatabase,
            UsesTemporaryDatabase = usesTemporaryDatabase
        };
    }

    private static string ReadValue(string[] args, ref int index, string parameterName)
    {
        if (index + 1 >= args.Length || args[index + 1].StartsWith("--", StringComparison.Ordinal))
        {
            throw new ArgumentException($"Der Parameter '{parameterName}' benötigt einen Wert.", nameof(args));
        }

        index++;
        return args[index];
    }
}
