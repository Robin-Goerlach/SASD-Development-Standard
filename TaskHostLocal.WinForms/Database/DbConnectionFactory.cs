using Microsoft.Data.Sqlite;

namespace TaskHostLocal.WinForms.Database;

/// <summary>
/// Erstellt SQLite-Verbindungen und kapselt den Speicherort der lokalen Datenbank.
/// </summary>
public sealed class DbConnectionFactory
{
    private const string VendorFolderName = "SASD";
    private const string ApplicationFolderName = "TaskHostLocal";
    private const string DatabaseFileName = "taskhost.db";

    /// <summary>
    /// Verzeichnis, in dem die lokale SQLite-Datenbank abgelegt wird.
    /// </summary>
    public string DataDirectory { get; }

    /// <summary>
    /// Vollständiger Pfad zur lokalen SQLite-Datenbankdatei.
    /// </summary>
    public string DatabasePath { get; }

    /// <summary>
    /// Initialisiert eine neue Factory mit dem produktiven Datenbankpfad unter
    /// <c>%AppData%\SASD\TaskHostLocal</c>.
    /// </summary>
    public DbConnectionFactory()
        : this(GetDefaultDatabasePath())
    {
    }

    /// <summary>
    /// Initialisiert eine Factory mit einem expliziten Datenbankpfad.
    /// Dieser Konstruktor ermöglicht isolierte Integrationstests mit temporären Datenbanken.
    /// </summary>
    /// <param name="databasePath">Vollständiger oder relativer Pfad zur SQLite-Datei.</param>
    /// <exception cref="ArgumentException">Der Pfad ist leer.</exception>
    public DbConnectionFactory(string databasePath)
    {
        ArgumentException.ThrowIfNullOrWhiteSpace(databasePath);

        DatabasePath = Path.GetFullPath(databasePath);
        DataDirectory = Path.GetDirectoryName(DatabasePath)
            ?? throw new ArgumentException("Für den Datenbankpfad konnte kein Verzeichnis ermittelt werden.", nameof(databasePath));
    }

    /// <summary>
    /// Erstellt eine geöffnete SQLite-Verbindung mit aktivierten Fremdschlüsseln.
    /// </summary>
    public SqliteConnection CreateOpenConnection()
    {
        Directory.CreateDirectory(DataDirectory);

        var connectionStringBuilder = new SqliteConnectionStringBuilder
        {
            DataSource = DatabasePath,
            Mode = SqliteOpenMode.ReadWriteCreate,
            ForeignKeys = true
        };

        var connection = new SqliteConnection(connectionStringBuilder.ToString());
        connection.Open();

        // Ein kurzes Busy-Timeout verhindert unnötige Sofortfehler, wenn SQLite die Datei
        // beispielsweise während eines sehr kurzen Backup- oder Schreibvorgangs gesperrt sieht.
        using var command = connection.CreateCommand();
        command.CommandText = "PRAGMA busy_timeout = 5000;";
        command.ExecuteNonQuery();

        return connection;
    }

    private static string GetDefaultDatabasePath()
    {
        var appData = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
        return Path.Combine(appData, VendorFolderName, ApplicationFolderName, DatabaseFileName);
    }
}
