using System.IO.Compression;
using System.Security.Cryptography;
using System.Text;
using System.Text.Json;
using Sasd.PromptManager.Application.PromptPackages;

namespace Sasd.PromptManager.Domain.Tests.PromptPackages;

public sealed class SasdPromptPackageReaderTests
{
    [Fact]
    public void Read_ValidDirectory_ReturnsPromptPackage()
    {
        using var fixture = PromptPackageFixture.Create();
        SasdPromptPackage package = new SasdPromptPackageReader().Read(fixture.RootDirectory);
        Assert.Equal("test-package", package.Manifest.PackageId);
        Assert.Single(package.Prompts);
        Assert.Contains("# Testprompt", package.Prompts[0].Content);
        Assert.DoesNotContain("prompt-id:", package.Prompts[0].Content);
    }

    [Fact]
    public void Read_ValidZip_ReturnsPromptPackage()
    {
        using var fixture = PromptPackageFixture.Create();
        string zip = fixture.CreateZip();
        SasdPromptPackage package = new SasdPromptPackageReader().Read(zip);
        Assert.Single(package.Prompts);
    }

    [Fact]
    public void Read_ManipulatedPrompt_RejectsChecksumMismatch()
    {
        using var fixture = PromptPackageFixture.Create();
        File.AppendAllText(fixture.PromptFile, "\nManipulation", Encoding.UTF8);
        InvalidDataException exception = Assert.Throws<InvalidDataException>(() => new SasdPromptPackageReader().Read(fixture.RootDirectory));
        Assert.Contains("SHA-256", exception.Message);
    }

    [Fact]
    public void Read_ZipWithTraversalPath_RejectsArchive()
    {
        using var fixture = PromptPackageFixture.Create();
        string zip = Path.Combine(fixture.TempDirectory, "unsafe.zip");
        using (var archive = ZipFile.Open(zip, ZipArchiveMode.Create))
        {
            ZipArchiveEntry entry = archive.CreateEntry("../outside.txt");
            using var writer = new StreamWriter(entry.Open());
            writer.Write("unsafe");
        }
        Assert.Throws<InvalidDataException>(() => new SasdPromptPackageReader().Read(zip));
    }

    private sealed class PromptPackageFixture : IDisposable
    {
        private PromptPackageFixture(string tempDirectory, string rootDirectory, string promptFile)
        { TempDirectory = tempDirectory; RootDirectory = rootDirectory; PromptFile = promptFile; }
        public string TempDirectory { get; }
        public string RootDirectory { get; }
        public string PromptFile { get; }

        public static PromptPackageFixture Create()
        {
            string temp = Path.Combine(Path.GetTempPath(), "sasd-prompt-package-tests", Guid.NewGuid().ToString("N"));
            string root = Path.Combine(temp, "test-root");
            string packageDir = Path.Combine(root, "prompts", "packages", "test-package");
            string promptDir = Path.Combine(root, "prompts", "review");
            Directory.CreateDirectory(packageDir);
            Directory.CreateDirectory(promptDir);
            string promptFile = Path.Combine(promptDir, "TEST-PROMPT.md");
            string prompt = "---\nprompt-id: \"SASD-PROMPT-TEST-001\"\npackage-id: \"test-package\"\n---\n\n# Testprompt\n\nPrüfe {{project_name}}.\n";
            File.WriteAllText(promptFile, prompt, new UTF8Encoding(false));
            string hash = Sha(promptFile);
            File.WriteAllText(Path.Combine(packageDir, "manifest.json"), JsonSerializer.Serialize(new {
                schema_version="1.0", format="sasd-prompt-package/1.0", package_id="test-package", name="Test", version="1.0.0", status="candidate", standard_version="1.0", authoritative_language="de", license="MIT", catalog="catalog.json", variables="variables.json", categories="categories.json", workflow="workflow.json"
            }), new UTF8Encoding(false));
            File.WriteAllText(Path.Combine(packageDir, "catalog.json"), JsonSerializer.Serialize(new {
                schema_version="1.0", package_id="test-package", package_version="1.0.0", prompt_count=1,
                prompts=new[]{new { prompt_id="SASD-PROMPT-TEST-001", title="Testprompt", summary="Test", version="1.0.0", status="Candidate", category="review", language="de", variables=Array.Empty<string>(), tags=new[]{"test"}, quality_levels=new[]{"Minimum"}, profiles=new[]{"Core"}, source_file="prompts/review/TEST-PROMPT.md", sha256=hash }}
            }), new UTF8Encoding(false));
            File.WriteAllText(Path.Combine(packageDir, "categories.json"), JsonSerializer.Serialize(new { schema_version="1.0", categories=new[]{new { id="review", title="Reviews", description="Reviewprompts", order=1 }} }), new UTF8Encoding(false));
            File.WriteAllText(Path.Combine(packageDir, "variables.json"), "{\"schema_version\":\"1.0\",\"variables\":[]}", new UTF8Encoding(false));
            File.WriteAllText(Path.Combine(packageDir, "workflow.json"), "{\"schema_version\":\"1.0\",\"stages\":[]}", new UTF8Encoding(false));
            var checksumFiles = new List<object>();
            foreach (string file in Directory.EnumerateFiles(root, "*", SearchOption.AllDirectories).OrderBy(x=>x))
            {
                string rel = Path.GetRelativePath(root,file).Replace('\\','/');
                if (rel.EndsWith("checksums.json")) continue;
                checksumFiles.Add(new { path=rel, sha256=Sha(file) });
            }
            File.WriteAllText(Path.Combine(packageDir, "checksums.json"), JsonSerializer.Serialize(new { schema_version="1.0", package_id="test-package", package_version="1.0.0", file_count=checksumFiles.Count, files=checksumFiles }), new UTF8Encoding(false));
            return new PromptPackageFixture(temp, root, promptFile);
        }
        public string CreateZip()
        {
            string zip=Path.Combine(TempDirectory,"package.zip");
            ZipFile.CreateFromDirectory(RootDirectory,zip,CompressionLevel.Fastest,includeBaseDirectory:true);
            return zip;
        }
        private static string Sha(string file)=>Convert.ToHexString(SHA256.HashData(File.ReadAllBytes(file))).ToLowerInvariant();
        public void Dispose(){ if(Directory.Exists(TempDirectory)) Directory.Delete(TempDirectory,true); }
    }
}
