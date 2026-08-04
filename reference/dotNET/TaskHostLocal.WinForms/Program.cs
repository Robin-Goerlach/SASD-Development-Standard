using TaskHostLocal.WinForms.Database;
using TaskHostLocal.WinForms.Diagnostics;
using TaskHostLocal.WinForms.Repositories;
using TaskHostLocal.WinForms.Services;
using TaskHostLocal.WinForms.Verification;

namespace TaskHostLocal.WinForms;

/// <summary>
/// Einstiegspunkt der Anwendung.
/// </summary>
internal static class Program
{
    /// <summary>
    /// Startet entweder den kopflosen Verifikationsmodus oder die grafische Anwendung.
    /// </summary>
    /// <param name="args">Optionale Kommandozeilenparameter.</param>
    /// <returns>Prozess-Exitcode. Null bedeutet Erfolg.</returns>
    [STAThread]
    private static int Main(string[] args)
    {
        if (SelfCheckOptions.IsSelfCheckRequested(args))
        {
            // Der Self-Check startet bewusst keine Windows-Forms-Oberfläche. Dadurch kann
            // derselbe produktive Build in CI und auf einem lokalen Windows-System geprüft werden.
            return SelfCheckRunner.Execute(args);
        }

        ApplicationConfiguration.Initialize();

        DbConnectionFactory? connectionFactory = null;

        try
        {
            // Für das kleine MVP werden die Abhängigkeiten weiterhin bewusst direkt
            // zusammengesetzt. Ein DI-Container wäre in dieser Projektgröße kein Mehrwert.
            connectionFactory = new DbConnectionFactory();
            var databaseInitializer = new DatabaseInitializer(connectionFactory);
            databaseInitializer.EnsureDatabase();

            var listRepository = new ListRepository(connectionFactory);
            var taskRepository = new TaskRepository(connectionFactory);

            var listService = new ListService(listRepository, taskRepository);
            var taskService = new TaskService(taskRepository);
            var backupService = new BackupService(connectionFactory);

            Application.Run(new MainForm(listService, taskService, backupService));
            return 0;
        }
        catch (Exception exception)
        {
            var diagnosticPath = StartupDiagnostics.TryWrite(exception, connectionFactory?.DatabasePath);
            var diagnosticHint = diagnosticPath is null
                ? "Es konnte kein Diagnoseprotokoll geschrieben werden."
                : $"Diagnoseprotokoll:\n{diagnosticPath}";

            MessageBox.Show(
                "TaskHost Local konnte nicht gestartet werden.\n\n" +
                "Die vorhandene Datenbank wurde nicht automatisch gelöscht oder überschrieben.\n\n" +
                diagnosticHint,
                "TaskHost Local – Startfehler",
                MessageBoxButtons.OK,
                MessageBoxIcon.Error);

            return 1;
        }
    }
}
