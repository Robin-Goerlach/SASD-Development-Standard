using Microsoft.Data.Sqlite;
using TaskHostLocal.WinForms.Database;

namespace TaskHostLocal.Tests.Infrastructure;

/// <summary>
/// Verwaltet pro Test eine vollständig isolierte SQLite-Datei im temporären Verzeichnis.
/// </summary>
internal sealed class TemporaryDatabase : IDisposable
{
    private readonly string _directoryPath;

    public TemporaryDatabase(bool initialize = true)
    {
        _directoryPath = Path.Combine(Path.GetTempPath(), "SASD", "TaskHostLocal.Tests", Guid.NewGuid().ToString("N"));
        var databasePath = Path.Combine(_directoryPath, "taskhost-test.db");

        ConnectionFactory = new DbConnectionFactory(databasePath);

        if (initialize)
        {
            new DatabaseInitializer(ConnectionFactory).EnsureDatabase();
        }
    }

    public DbConnectionFactory ConnectionFactory { get; }

    public SqliteConnection OpenConnection() => ConnectionFactory.CreateOpenConnection();

    public void Dispose()
    {
        // Freigegebene Verbindungen werden nicht gepoolt festgehalten, bevor das Testverzeichnis gelöscht wird.
        SqliteConnection.ClearAllPools();

        if (Directory.Exists(_directoryPath))
        {
            Directory.Delete(_directoryPath, recursive: true);
        }
    }
}
