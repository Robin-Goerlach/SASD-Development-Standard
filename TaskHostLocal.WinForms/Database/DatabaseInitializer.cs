using Microsoft.Data.Sqlite;

namespace TaskHostLocal.WinForms.Database;

/// <summary>
/// Legt die SQLite-Datenbankstruktur transaktional an und prüft die für das MVP
/// erforderlichen Datenbankobjekte.
/// </summary>
public sealed class DatabaseInitializer
{
    /// <summary>
    /// Aktuelle interne Version des SQLite-Schemas.
    /// </summary>
    public const int CurrentSchemaVersion = 1;

    private readonly DbConnectionFactory _connectionFactory;

    /// <summary>
    /// Erstellt einen neuen Initializer.
    /// </summary>
    public DatabaseInitializer(DbConnectionFactory connectionFactory)
    {
        _connectionFactory = connectionFactory ?? throw new ArgumentNullException(nameof(connectionFactory));
    }

    /// <summary>
    /// Stellt sicher, dass Tabellen, Indizes, Schemaversion und Standardliste vorhanden sind.
    /// Die Methode ist idempotent und darf bei jedem Programmstart ausgeführt werden.
    /// </summary>
    public void EnsureDatabase()
    {
        using var connection = _connectionFactory.CreateOpenConnection();
        using var transaction = connection.BeginTransaction();

        ExecuteNonQuery(connection, transaction, """
            CREATE TABLE IF NOT EXISTS task_lists (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                sort_order INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            );
            """);

        ExecuteNonQuery(connection, transaction, """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                list_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                description TEXT NULL,
                due_date TEXT NULL,
                priority INTEGER NOT NULL DEFAULT 0,
                is_completed INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                completed_at TEXT NULL,
                FOREIGN KEY (list_id) REFERENCES task_lists(id) ON DELETE RESTRICT
            );
            """);

        ExecuteNonQuery(connection, transaction, """
            CREATE INDEX IF NOT EXISTS idx_tasks_list_id ON tasks(list_id);
            """);

        ExecuteNonQuery(connection, transaction, """
            CREATE INDEX IF NOT EXISTS idx_tasks_due_date ON tasks(due_date);
            """);

        ExecuteNonQuery(connection, transaction, """
            CREATE INDEX IF NOT EXISTS idx_tasks_status_due
            ON tasks(is_completed, due_date, priority, updated_at);
            """);

        ExecuteNonQuery(connection, transaction, $"PRAGMA user_version = {CurrentSchemaVersion};");
        EnsureDefaultList(connection, transaction);
        transaction.Commit();

        VerifyRequiredObjects(connection);
    }

    private static void EnsureDefaultList(SqliteConnection connection, SqliteTransaction transaction)
    {
        using var countCommand = connection.CreateCommand();
        countCommand.Transaction = transaction;
        countCommand.CommandText = "SELECT COUNT(*) FROM task_lists;";
        var count = Convert.ToInt64(countCommand.ExecuteScalar());

        if (count > 0)
        {
            return;
        }

        var now = DateTime.UtcNow.ToString("O");

        using var insertCommand = connection.CreateCommand();
        insertCommand.Transaction = transaction;
        insertCommand.CommandText = """
            INSERT INTO task_lists (name, sort_order, created_at, updated_at)
            VALUES ($name, $sortOrder, $createdAt, $updatedAt);
            """;
        insertCommand.Parameters.AddWithValue("$name", "Eingang");
        insertCommand.Parameters.AddWithValue("$sortOrder", 0);
        insertCommand.Parameters.AddWithValue("$createdAt", now);
        insertCommand.Parameters.AddWithValue("$updatedAt", now);
        insertCommand.ExecuteNonQuery();
    }

    private static void VerifyRequiredObjects(SqliteConnection connection)
    {
        string[] requiredObjects =
        [
            "task_lists",
            "tasks",
            "idx_tasks_list_id",
            "idx_tasks_due_date",
            "idx_tasks_status_due"
        ];

        using var command = connection.CreateCommand();
        command.CommandText = """
            SELECT COUNT(*)
            FROM sqlite_master
            WHERE name = $name
              AND type IN ('table', 'index');
            """;
        var nameParameter = command.Parameters.Add("$name", SqliteType.Text);

        foreach (var objectName in requiredObjects)
        {
            nameParameter.Value = objectName;
            var exists = Convert.ToInt64(command.ExecuteScalar()) == 1;
            if (!exists)
            {
                throw new InvalidOperationException(
                    $"Die SQLite-Initialisierung ist unvollständig. Das Objekt '{objectName}' fehlt.");
            }
        }
    }

    private static void ExecuteNonQuery(
        SqliteConnection connection,
        SqliteTransaction transaction,
        string sql)
    {
        using var command = connection.CreateCommand();
        command.Transaction = transaction;
        command.CommandText = sql;
        command.ExecuteNonQuery();
    }
}
