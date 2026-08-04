using Sasd.PromptManager.Application.Categories;
using Sasd.PromptManager.Application.PromptPackages;
using Sasd.PromptManager.Application.Projects;
using Sasd.PromptManager.Application.Prompts;
using Sasd.PromptManager.Domain.Prompts;
using Sasd.PromptManager.Domain.Projects;

namespace Sasd.PromptManager.Domain.Tests.PromptPackages;

public sealed class SasdPromptPackageImportServiceTests
{
    [Fact]
    public void Execute_NewCandidatePrompt_CreatesNeedsReviewPromptAndBackup()
    {
        var promptRepository = new InMemoryPromptRepository();
        var categoryRepository = new InMemoryCategoryRepository();
        var promptService = new PromptService(promptRepository, new EmptyProjectRepository(), categoryRepository);
        var categoryService = new CategoryService(categoryRepository, promptRepository);
        var service = new SasdPromptPackageImportService(promptService, categoryService);
        SasdPromptPackage package = CreatePackage();
        SasdPromptPackageImportPlan plan = service.CreatePlan(package, SasdPromptPackageDuplicatePolicy.Skip);
        string root = Path.Combine(Path.GetTempPath(), "sasd-pm-import-tests", Guid.NewGuid().ToString("N"));
        string data = Path.Combine(root, "data");
        Directory.CreateDirectory(data);
        File.WriteAllText(Path.Combine(data, "prompts.json"), "[]");
        try
        {
            SasdPromptPackageImportResult result = service.Execute(plan, data);
            Assert.True(result.Succeeded);
            Assert.Equal(1, result.Created);
            Prompt imported = Assert.Single(promptRepository.GetAll());
            Assert.Equal(PromptStatus.NeedsReview, imported.Status);
            Assert.Equal(PromptType.Review, imported.Type);
            Assert.Contains("Prompt-ID=SASD-PROMPT-TEST-001", imported.Source);
            Assert.NotNull(imported.CategoryId);
            Assert.True(File.Exists(Path.Combine(result.BackupDirectory, "prompts.json")));
        }
        finally
        {
            if (Directory.Exists(root)) Directory.Delete(root, true);
        }
    }

    [Fact]
    public void CreatePlan_ExistingStableIdWithSkip_DoesNotPlanSecondCreate()
    {
        var promptRepository = new InMemoryPromptRepository();
        var categoryRepository = new InMemoryCategoryRepository();
        var promptService = new PromptService(promptRepository, new EmptyProjectRepository(), categoryRepository);
        var categoryService = new CategoryService(categoryRepository, promptRepository);
        var service = new SasdPromptPackageImportService(promptService, categoryService);
        promptService.CreatePrompt("Vorhanden", "Text", source: "SASD Prompt Package test-package@1.0.0; Prompt-ID=SASD-PROMPT-TEST-001; Source=test.md");

        SasdPromptPackageImportPlan plan = service.CreatePlan(CreatePackage(), SasdPromptPackageDuplicatePolicy.Skip);

        SasdPromptPackageImportPlanItem item = Assert.Single(plan.Items);
        Assert.Equal(SasdPromptPackageImportAction.Skip, item.Action);
        Assert.NotNull(item.ExistingPromptId);
    }

    private static SasdPromptPackage CreatePackage()
    {
        var manifest = new SasdPromptPackageManifest
        {
            SchemaVersion = "1.0", Format = "sasd-prompt-package/1.0", PackageId = "test-package",
            Name = "Test", Version = "1.0.0", Status = "candidate", StandardVersion = "1.0",
            AuthoritativeLanguage = "de", License = "MIT"
        };
        var metadata = new SasdPromptCatalogEntry
        {
            PromptId = "SASD-PROMPT-TEST-001", Title = "Reviewprompt", Summary = "Prüft etwas.",
            Version = "1.0.0", Status = "Candidate", Category = "review", Language = "de",
            Tags = new[] { "review" }, QualityLevels = new[] { "Minimum" }, Profiles = new[] { "Core" },
            SourceFile = "prompts/review/TEST.md", Sha256 = new string('0', 64)
        };
        var catalog = new SasdPromptCatalog
        {
            SchemaVersion = "1.0", PackageId = "test-package", PackageVersion = "1.0.0",
            PromptCount = 1, Prompts = new[] { metadata }
        };
        var categories = new[] { new SasdPromptPackageCategory { Id = "review", Title = "Reviews", Description = "Reviewprompts", Order = 1 } };
        return new SasdPromptPackage(manifest, catalog, categories, new[] { new SasdPromptPackagePrompt(metadata, "# Reviewprompt\n\nPrüfe das Projekt.") }, "memory", "");
    }

    private sealed class InMemoryPromptRepository : IPromptRepository
    {
        private readonly List<Prompt> _items = new();
        public void Add(Prompt prompt) => _items.Add(prompt);
        public void Update(Prompt prompt) { }
        public void Delete(Guid promptId) => _items.RemoveAll(item => item.Id == promptId);
        public Prompt? FindById(Guid promptId) => _items.FirstOrDefault(item => item.Id == promptId);
        public IReadOnlyList<Prompt> GetAll() => _items;
        public IReadOnlyList<Prompt> GetByProjectId(Guid projectId) => _items.Where(item => item.ProjectId == projectId).ToArray();
    }

    private sealed class InMemoryCategoryRepository : ICategoryRepository
    {
        private readonly List<PromptCategory> _items = new();
        public void Add(PromptCategory category) => _items.Add(category);
        public void Update(PromptCategory category) { }
        public void Delete(Guid categoryId) => _items.RemoveAll(item => item.Id == categoryId);
        public PromptCategory? FindById(Guid categoryId) => _items.FirstOrDefault(item => item.Id == categoryId);
        public PromptCategory? FindByName(string name) => _items.FirstOrDefault(item => string.Equals(item.Name, name, StringComparison.OrdinalIgnoreCase));
        public IReadOnlyList<PromptCategory> GetAll() => _items;
    }

    private sealed class EmptyProjectRepository : IProjectRepository
    {
        public void Add(PromptProject project) => throw new NotSupportedException();
        public void Update(PromptProject project) => throw new NotSupportedException();
        public void Delete(Guid projectId) => throw new NotSupportedException();
        public PromptProject? FindById(Guid projectId) => null;
        public PromptProject? FindByName(string name) => null;
        public IReadOnlyList<PromptProject> GetAll() => Array.Empty<PromptProject>();
    }
}
