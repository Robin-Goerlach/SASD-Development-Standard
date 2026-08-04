using TaskHostLocal.Tests.Infrastructure;
using TaskHostLocal.WinForms.Services;

namespace TaskHostLocal.Tests.Services;

public sealed class BackupServiceTests
{
    [Fact]
    public void CreateBackup_CopiesInitializedDatabase()
    {
        using var database = new TemporaryDatabase();
        var targetDirectory = Path.Combine(
            Path.GetTempPath(),
            "SASD",
            "TaskHostLocal.BackupTests",
            Guid.NewGuid().ToString("N"));

        try
        {
            var service = new BackupService(database.ConnectionFactory);

            var backupPath = service.CreateBackup(targetDirectory);

            Assert.True(File.Exists(backupPath));
            Assert.True(new FileInfo(backupPath).Length > 0);
        }
        finally
        {
            if (Directory.Exists(targetDirectory))
            {
                Directory.Delete(targetDirectory, recursive: true);
            }
        }
    }
}
