using Microsoft.Data.Sqlite;
using TaskHostLocal.Tests.Infrastructure;
using TaskHostLocal.WinForms.Database;

namespace TaskHostLocal.Tests.Database;

public sealed class DatabaseInitializerTests
{
    [Fact]
    public void EnsureDatabase_CreatesRequiredSchemaAndDefaultList()
    {
        using var database = new TemporaryDatabase(initialize: false);

        new DatabaseInitializer(database.ConnectionFactory).EnsureDatabase();

        using var connection = database.OpenConnection();
        Assert.Equal(1L, ExecuteScalar<long>(connection, "SELECT COUNT(*) FROM task_lists;"));
        Assert.Equal("Eingang", ExecuteScalar<string>(connection, "SELECT name FROM task_lists LIMIT 1;"));
        Assert.Equal(1L, ExecuteScalar<long>(connection, "SELECT COUNT(*) FROM sqlite_master WHERE type = 'table' AND name = 'tasks';"));
        Assert.Equal(1L, ExecuteScalar<long>(connection, "SELECT COUNT(*) FROM sqlite_master WHERE type = 'index' AND name = 'idx_tasks_status_due';"));
        Assert.Equal(DatabaseInitializer.CurrentSchemaVersion, ExecuteScalar<long>(connection, "PRAGMA user_version;"));
    }

    [Fact]
    public void EnsureDatabase_IsIdempotentAndDoesNotDuplicateDefaultList()
    {
        using var database = new TemporaryDatabase(initialize: false);
        var initializer = new DatabaseInitializer(database.ConnectionFactory);

        initializer.EnsureDatabase();
        initializer.EnsureDatabase();

        using var connection = database.OpenConnection();
        Assert.Equal(1L, ExecuteScalar<long>(connection, "SELECT COUNT(*) FROM task_lists WHERE name = 'Eingang';"));
    }

    [Fact]
    public void CreateOpenConnection_EnforcesForeignKeys()
    {
        using var database = new TemporaryDatabase();
        using var connection = database.OpenConnection();
        using var command = connection.CreateCommand();
        command.CommandText = """
            INSERT INTO tasks
                (list_id, title, priority, is_completed, created_at, updated_at)
            VALUES
                (999999, 'Ungültige Aufgabe', 0, 0, $createdAt, $updatedAt);
            """;
        command.Parameters.AddWithValue("$createdAt", DateTime.UtcNow.ToString("O"));
        command.Parameters.AddWithValue("$updatedAt", DateTime.UtcNow.ToString("O"));

        var exception = Assert.Throws<SqliteException>(() => command.ExecuteNonQuery());
        Assert.Equal(19, exception.SqliteErrorCode);
    }

    [Fact]
    public void EnsureDatabase_PreservesDataFromExistingMvpSchema()
    {
        using var database = new TemporaryDatabase(initialize: false);
        using (var connection = database.OpenConnection())
        {
            ExecuteNonQuery(connection, """
                CREATE TABLE task_lists (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    sort_order INTEGER NOT NULL DEFAULT 0,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                );
                """);

            ExecuteNonQuery(connection, """
                CREATE TABLE tasks (
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
                    FOREIGN KEY (list_id) REFERENCES task_lists(id)
                );
                """);

            ExecuteNonQuery(connection, """
                INSERT INTO task_lists (name, sort_order, created_at, updated_at)
                VALUES ('Bestehende Liste', 0, '2026-05-13T00:00:00Z', '2026-05-13T00:00:00Z');
                """);

            ExecuteNonQuery(connection, """
                INSERT INTO tasks (list_id, title, priority, is_completed, created_at, updated_at)
                VALUES (1, 'Bestehende Aufgabe', 0, 0, '2026-05-13T00:00:00Z', '2026-05-13T00:00:00Z');
                """);
        }

        new DatabaseInitializer(database.ConnectionFactory).EnsureDatabase();

        using var verificationConnection = database.OpenConnection();
        Assert.Equal(1L, ExecuteScalar<long>(verificationConnection, "SELECT COUNT(*) FROM tasks WHERE title = 'Bestehende Aufgabe';"));
        Assert.Equal(DatabaseInitializer.CurrentSchemaVersion, ExecuteScalar<long>(verificationConnection, "PRAGMA user_version;"));
    }

    private static void ExecuteNonQuery(SqliteConnection connection, string sql)
    {
        using var command = connection.CreateCommand();
        command.CommandText = sql;
        command.ExecuteNonQuery();
    }

    private static T ExecuteScalar<T>(SqliteConnection connection, string sql)
    {
        using var command = connection.CreateCommand();
        command.CommandText = sql;
        return (T)Convert.ChangeType(command.ExecuteScalar()!, typeof(T));
    }
}
