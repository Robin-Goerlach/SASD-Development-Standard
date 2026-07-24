using TaskHostLocal.WinForms.Database;
using TaskHostLocal.WinForms.Diagnostics;
using TaskHostLocal.WinForms.Repositories;
using TaskHostLocal.WinForms.Services;

namespace TaskHostLocal.WinForms;

/// <summary>
/// Einstiegspunkt der Anwendung.
/// </summary>
internal static class Program
{
    /// <summary>
    /// Startet TaskHost Local und erzeugt bei einem fehlgeschlagenen Start einen
    /// lokalen Diagnosebericht ohne Aufgabeninhalte.
    /// </summary>
    [STAThread]
    private static void Main()
    {
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
        }
    }
}
