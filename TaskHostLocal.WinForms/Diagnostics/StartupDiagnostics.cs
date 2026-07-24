using System.Reflection;
using System.Runtime.InteropServices;
using System.Text;

namespace TaskHostLocal.WinForms.Diagnostics;

/// <summary>
/// Schreibt bei einem fehlgeschlagenen Programmstart ein lokales Diagnoseprotokoll.
/// Inhaltsdaten aus Aufgaben oder Listen werden nicht protokolliert.
/// </summary>
internal static class StartupDiagnostics
{
    /// <summary>
    /// Versucht, einen Diagnosebericht zu schreiben. Ein Fehler beim Protokollieren darf
    /// den ursprünglichen Startfehler nicht überdecken.
    /// </summary>
    /// <returns>Vollständiger Protokollpfad oder <see langword="null"/>.</returns>
    public static string? TryWrite(Exception exception, string? databasePath)
    {
        ArgumentNullException.ThrowIfNull(exception);

        try
        {
            var localAppData = Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData);
            var logDirectory = Path.Combine(localAppData, "SASD", "TaskHostLocal", "logs");
            Directory.CreateDirectory(logDirectory);

            var fileName = $"startup-{DateTime.UtcNow:yyyyMMdd-HHmmss}.log";
            var logPath = Path.Combine(logDirectory, fileName);

            var report = new StringBuilder()
                .AppendLine("SASD TaskHost Local - Startup Diagnostic")
                .AppendLine($"UTC time: {DateTime.UtcNow:O}")
                .AppendLine($"Application version: {Assembly.GetExecutingAssembly().GetName().Version}")
                .AppendLine($".NET runtime: {Environment.Version}")
                .AppendLine($"Operating system: {RuntimeInformation.OSDescription}")
                .AppendLine($"Process architecture: {RuntimeInformation.ProcessArchitecture}")
                .AppendLine($"Database path: {databasePath ?? "not yet available"}")
                .AppendLine()
                .AppendLine(exception.ToString())
                .ToString();

            File.WriteAllText(logPath, report, Encoding.UTF8);
            return logPath;
        }
        catch
        {
            return null;
        }
    }
}
