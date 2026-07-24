using System.Text.Json;
using TaskHostLocal.WinForms.Verification;

namespace TaskHostLocal.Tests.Verification;

/// <summary>
/// Integrationstests für den kopflosen produktiven Selbsttest.
/// </summary>
public sealed class SelfCheckRunnerTests : IDisposable
{
    private readonly string _directory = Path.Combine(
        Path.GetTempPath(),
        "SASD",
        "TaskHostLocal.Tests",
        Guid.NewGuid().ToString("N"));

    /// <summary>
    /// Prüft den vollständigen Self-Check gegen eine isolierte SQLite-Datei.
    /// </summary>
    [Fact]
    public void Run_WithTemporaryDatabase_CompletesAllStepsAndWritesJsonReport()
    {
        var databasePath = Path.Combine(_directory, "self-check.db");
        var reportPath = Path.Combine(_directory, "self-check.json");
        var options = new SelfCheckOptions
        {
            DatabasePath = databasePath,
            ReportPath = reportPath,
            KeepTemporaryDatabase = true,
            UsesTemporaryDatabase = true
        };

        var report = SelfCheckRunner.Run(options);

        Assert.True(report.Success);
        Assert.Equal(8, report.Steps.Count);
        Assert.All(report.Steps, step => Assert.Equal("Passed", step.Status));
        Assert.True(File.Exists(databasePath));
        Assert.True(File.Exists(reportPath));
        Assert.False(string.IsNullOrWhiteSpace(report.DatabaseSha256));

        using var json = JsonDocument.Parse(File.ReadAllText(reportPath));
        Assert.True(json.RootElement.GetProperty("success").GetBoolean());
        Assert.Equal(8, json.RootElement.GetProperty("steps").GetArrayLength());
    }

    /// <summary>
    /// Prüft, dass unbekannte Parameter nicht stillschweigend akzeptiert werden.
    /// </summary>
    [Fact]
    public void Parse_WithUnknownArgument_ThrowsArgumentException()
    {
        var exception = Assert.Throws<ArgumentException>(
            () => SelfCheckOptions.Parse(["--self-check", "--unknown"]));

        Assert.Contains("Unbekannter", exception.Message);
    }

    /// <inheritdoc />
    public void Dispose()
    {
        if (Directory.Exists(_directory))
        {
            Directory.Delete(_directory, recursive: true);
        }
    }
}
