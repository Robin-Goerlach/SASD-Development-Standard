using System.Diagnostics;
using System.Reflection;
using System.Runtime.InteropServices;
using System.Security.Cryptography;
using System.Text.Json;
using TaskHostLocal.WinForms.Database;
using TaskHostLocal.WinForms.Models;
using TaskHostLocal.WinForms.Repositories;
using TaskHostLocal.WinForms.Services;

namespace TaskHostLocal.WinForms.Verification;

/// <summary>
/// Führt einen kopflosen Lauf gegen den produktiven Datenbank-, Repository- und Servicecode aus.
/// </summary>
internal static class SelfCheckRunner
{
    private static readonly JsonSerializerOptions JsonOptions = new()
    {
        WriteIndented = true,
        PropertyNamingPolicy = JsonNamingPolicy.CamelCase
    };

    /// <summary>
    /// Liest die Kommandozeilenparameter, führt den Selbsttest aus und liefert einen Prozess-Exitcode.
    /// </summary>
    public static int Execute(string[] args)
    {
        SelfCheckOptions options;

        try
        {
            options = SelfCheckOptions.Parse(args);
        }
        catch (Exception exception)
        {
            TryWriteArgumentFailure(args, exception);
            return 2;
        }

        var report = Run(options);
        return report.Success ? 0 : 1;
    }

    /// <summary>
    /// Führt den Selbsttest mit bereits validierten Optionen aus.
    /// </summary>
    internal static SelfCheckReport Run(SelfCheckOptions options)
    {
        ArgumentNullException.ThrowIfNull(options);

        var report = new SelfCheckReport
        {
            StartedUtc = DateTime.UtcNow,
            ApplicationVersion = Assembly.GetExecutingAssembly().GetName().Version?.ToString() ?? "unknown",
            RuntimeVersion = Environment.Version.ToString(),
            OperatingSystem = RuntimeInformation.OSDescription,
            ProcessArchitecture = RuntimeInformation.ProcessArchitecture.ToString(),
            UsedTemporaryDatabase = options.UsesTemporaryDatabase
        };

        var backupDirectory = Path.Combine(
            Path.GetDirectoryName(options.DatabasePath) ?? Path.GetTempPath(),
            "backup");

        try
        {
            var connectionFactory = new DbConnectionFactory(options.DatabasePath);
            var initializer = new DatabaseInitializer(connectionFactory);
            var listRepository = new ListRepository(connectionFactory);
            var taskRepository = new TaskRepository(connectionFactory);
            var listService = new ListService(listRepository, taskRepository);
            var taskService = new TaskService(taskRepository);
            var backupService = new BackupService(connectionFactory);

            RunStep(report, "database-initialization", () => initializer.EnsureDatabase());
            RunStep(report, "sqlite-integrity", () => VerifyDatabaseIntegrity(connectionFactory));
            RunStep(report, "schema-version", () => VerifySchemaVersion(connectionFactory));
            RunStep(report, "default-list", () => VerifyDefaultList(listService));
            RunStep(report, "repository-and-service-crud", () => VerifyCrud(listService, taskService));
            RunStep(report, "backup", () => VerifyBackup(backupService, backupDirectory));
            RunStep(report, "repeat-initialization", () => initializer.EnsureDatabase());
            RunStep(report, "foreign-key-check", () => VerifyForeignKeys(connectionFactory));

            report.DatabaseSha256 = ComputeSha256(options.DatabasePath);
            report.Success = report.Steps.All(step => string.Equals(step.Status, "Passed", StringComparison.Ordinal));
        }
        catch (Exception exception)
        {
            report.Success = false;
            report.ErrorType = exception.GetType().FullName;
            report.ErrorMessage = exception.Message;
        }
        finally
        {
            report.CompletedUtc = DateTime.UtcNow;
            WriteReport(report, options.ReportPath);

            if (options.UsesTemporaryDatabase && !options.KeepTemporaryDatabase)
            {
                TryDeleteDirectory(Path.GetDirectoryName(options.DatabasePath));
            }
        }

        return report;
    }

    private static void VerifyDatabaseIntegrity(DbConnectionFactory connectionFactory)
    {
        using var connection = connectionFactory.CreateOpenConnection();
        using var command = connection.CreateCommand();
        command.CommandText = "PRAGMA integrity_check;";
        var result = Convert.ToString(command.ExecuteScalar());

        if (!string.Equals(result, "ok", StringComparison.OrdinalIgnoreCase))
        {
            throw new InvalidOperationException($"SQLite integrity_check meldet: {result ?? "kein Ergebnis"}.");
        }
    }

    private static void VerifySchemaVersion(DbConnectionFactory connectionFactory)
    {
        using var connection = connectionFactory.CreateOpenConnection();
        using var command = connection.CreateCommand();
        command.CommandText = "PRAGMA user_version;";
        var version = Convert.ToInt32(command.ExecuteScalar());

        if (version != DatabaseInitializer.CurrentSchemaVersion)
        {
            throw new InvalidOperationException(
                $"Erwartete Schemaversion {DatabaseInitializer.CurrentSchemaVersion}, gefunden {version}.");
        }
    }

    private static void VerifyDefaultList(ListService listService)
    {
        var lists = listService.GetAllLists();
        if (lists.Count != 1 || !string.Equals(lists[0].Name, "Eingang", StringComparison.Ordinal))
        {
            throw new InvalidOperationException("Die erwartete einzelne Standardliste 'Eingang' wurde nicht gefunden.");
        }
    }

    private static void VerifyCrud(ListService listService, TaskService taskService)
    {
        var list = listService.CreateList("SASD Self-Check");
        listService.RenameList(list, "SASD Self-Check Renamed");

        var task = taskService.CreateTask(new TaskItem
        {
            ListId = list.Id,
            Title = "Self-check task",
            Description = "Temporary verification data",
            DueDate = DateTime.Today.AddDays(1),
            Priority = 2
        });

        var loaded = taskService.GetTasksForList(list);
        if (loaded.Count != 1 || loaded[0].Id != task.Id)
        {
            throw new InvalidOperationException("Die angelegte Testaufgabe konnte nicht eindeutig geladen werden.");
        }

        var searchResult = taskService.SearchTasks("Temporary verification");
        if (searchResult.All(item => item.Id != task.Id))
        {
            throw new InvalidOperationException("Die Testaufgabe wurde über die Beschreibung nicht gefunden.");
        }

        task.Title = "Self-check task updated";
        task.Description = "Temporary verification data updated";
        taskService.UpdateTask(task);
        taskService.ToggleCompletion(task);

        var updated = taskService.GetTasksForList(list).Single(item => item.Id == task.Id);
        if (!updated.IsCompleted || !string.Equals(updated.Title, task.Title, StringComparison.Ordinal))
        {
            throw new InvalidOperationException("Aktualisierung oder Erledigt-Status wurde nicht gespeichert.");
        }

        taskService.DeleteTask(updated);
        listService.DeleteList(list);

        if (listService.GetAllLists().Count != 1)
        {
            throw new InvalidOperationException("Temporäre Self-Check-Daten wurden nicht vollständig bereinigt.");
        }
    }

    private static void VerifyBackup(BackupService backupService, string backupDirectory)
    {
        Directory.CreateDirectory(backupDirectory);
        var backupPath = backupService.CreateBackup(backupDirectory);

        if (!File.Exists(backupPath) || new FileInfo(backupPath).Length == 0)
        {
            throw new InvalidOperationException("Der Backup-Service hat keine nichtleere Sicherungsdatei erzeugt.");
        }

        var backupFactory = new DbConnectionFactory(backupPath);
        VerifyDatabaseIntegrity(backupFactory);
    }

    private static void VerifyForeignKeys(DbConnectionFactory connectionFactory)
    {
        using var connection = connectionFactory.CreateOpenConnection();
        using var command = connection.CreateCommand();
        command.CommandText = "PRAGMA foreign_key_check;";
        using var reader = command.ExecuteReader();

        if (reader.Read())
        {
            throw new InvalidOperationException("SQLite meldet eine Fremdschlüsselverletzung.");
        }
    }

    private static void RunStep(SelfCheckReport report, string name, Action action)
    {
        var stopwatch = Stopwatch.StartNew();

        try
        {
            action();
            stopwatch.Stop();
            report.Steps.Add(new SelfCheckStep
            {
                Name = name,
                Status = "Passed",
                DurationMilliseconds = stopwatch.ElapsedMilliseconds
            });
        }
        catch (Exception exception)
        {
            stopwatch.Stop();
            report.Steps.Add(new SelfCheckStep
            {
                Name = name,
                Status = "Failed",
                DurationMilliseconds = stopwatch.ElapsedMilliseconds,
                Message = exception.Message
            });
            throw;
        }
    }

    private static string ComputeSha256(string path)
    {
        using var stream = File.OpenRead(path);
        return Convert.ToHexString(SHA256.HashData(stream)).ToLowerInvariant();
    }

    private static void WriteReport(SelfCheckReport report, string reportPath)
    {
        var reportDirectory = Path.GetDirectoryName(reportPath)
            ?? throw new ArgumentException("Der Berichtspfad besitzt kein Verzeichnis.", nameof(reportPath));

        Directory.CreateDirectory(reportDirectory);
        var temporaryPath = reportPath + ".tmp";
        var json = JsonSerializer.Serialize(report, JsonOptions);
        File.WriteAllText(temporaryPath, json);
        File.Move(temporaryPath, reportPath, overwrite: true);
    }

    private static void TryWriteArgumentFailure(string[] args, Exception exception)
    {
        try
        {
            var reportIndex = Array.FindIndex(
                args,
                argument => string.Equals(argument, "--report", StringComparison.OrdinalIgnoreCase));

            if (reportIndex < 0 || reportIndex + 1 >= args.Length)
            {
                return;
            }

            var report = new SelfCheckReport
            {
                StartedUtc = DateTime.UtcNow,
                CompletedUtc = DateTime.UtcNow,
                Success = false,
                ApplicationVersion = Assembly.GetExecutingAssembly().GetName().Version?.ToString() ?? "unknown",
                RuntimeVersion = Environment.Version.ToString(),
                OperatingSystem = RuntimeInformation.OSDescription,
                ProcessArchitecture = RuntimeInformation.ProcessArchitecture.ToString(),
                ErrorType = exception.GetType().FullName,
                ErrorMessage = exception.Message
            };

            WriteReport(report, Path.GetFullPath(args[reportIndex + 1]));
        }
        catch
        {
            // Ein Fehler beim Schreiben des Argumentfehlerberichts darf den Exitcode nicht verändern.
        }
    }

    private static void TryDeleteDirectory(string? directory)
    {
        if (string.IsNullOrWhiteSpace(directory) || !Directory.Exists(directory))
        {
            return;
        }

        try
        {
            Directory.Delete(directory, recursive: true);
        }
        catch
        {
            // Temporäre Dateien dürfen die fachliche Self-Check-Aussage nicht nachträglich verfälschen.
        }
    }
}
