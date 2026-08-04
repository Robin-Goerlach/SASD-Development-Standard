using Sasd.PromptManager.Application.Categories;
using Sasd.PromptManager.Application.Logging;
using Sasd.PromptManager.Application.Prompts;
using Sasd.PromptManager.Domain.Prompts;

namespace Sasd.PromptManager.Application.PromptPackages;

/// <summary>
/// Plant und importiert geprüfte SASD-Promptpakete über die vorhandenen Application Services.
/// </summary>
public sealed class SasdPromptPackageImportService
{
    private readonly PromptService _prompts;
    private readonly CategoryService _categories;
    private readonly IApplicationLogger _logger;

    public SasdPromptPackageImportService(PromptService prompts, CategoryService categories, IApplicationLogger? logger = null)
    {
        _prompts = prompts ?? throw new ArgumentNullException(nameof(prompts));
        _categories = categories ?? throw new ArgumentNullException(nameof(categories));
        _logger = logger ?? NullApplicationLogger.Instance;
    }

    /// <summary>Erzeugt eine nebenwirkungsfreie Importvorschau.</summary>
    public SasdPromptPackageImportPlan CreatePlan(SasdPromptPackage package, SasdPromptPackageDuplicatePolicy duplicatePolicy)
    {
        ArgumentNullException.ThrowIfNull(package);
        IReadOnlyList<Prompt> existingPrompts = _prompts.GetAllPrompts(includeArchived: true);
        var items = new List<SasdPromptPackageImportPlanItem>(package.Prompts.Count);
        foreach (SasdPromptPackagePrompt packagedPrompt in package.Prompts)
        {
            Prompt? existing = FindByStablePromptId(existingPrompts, packagedPrompt.Metadata.PromptId);
            SasdPromptPackageImportAction action;
            string reason;
            if (existing is null)
            {
                action = SasdPromptPackageImportAction.Create;
                reason = "Stabile Prompt-ID ist noch nicht vorhanden.";
            }
            else if (duplicatePolicy == SasdPromptPackageDuplicatePolicy.Update)
            {
                action = SasdPromptPackageImportAction.Update;
                reason = "Vorhandener Prompt wird als neue Version aktualisiert.";
            }
            else if (duplicatePolicy == SasdPromptPackageDuplicatePolicy.CreateCopy)
            {
                action = SasdPromptPackageImportAction.Create;
                reason = "Vorhandene Prompt-ID wird zusätzlich als gekennzeichnete Kopie importiert.";
            }
            else
            {
                action = SasdPromptPackageImportAction.Skip;
                reason = "Vorhandener Prompt bleibt unverändert.";
            }
            items.Add(new(packagedPrompt.Metadata.PromptId, packagedPrompt.Metadata.Title, packagedPrompt.Metadata.Category, action, existing?.Id, reason));
        }
        return new SasdPromptPackageImportPlan(package, duplicatePolicy, items);
    }

    /// <summary>Führt einen zuvor erzeugten Plan aus und legt davor eine Datensicherung an.</summary>
    public SasdPromptPackageImportResult Execute(SasdPromptPackageImportPlan plan, string dataDirectory)
    {
        ArgumentNullException.ThrowIfNull(plan);
        string backupDirectory = CreatePreImportBackup(dataDirectory, plan.Package.Manifest);
        int created = 0, updated = 0, skipped = 0;
        var messages = new List<string>();

        try
        {
            var categoryById = EnsureCategories(plan.Package);
            foreach (SasdPromptPackageImportPlanItem item in plan.Items)
            {
                SasdPromptPackagePrompt source = plan.Package.Prompts.Single(prompt => prompt.Metadata.PromptId == item.PromptId);
                if (item.Action == SasdPromptPackageImportAction.Skip)
                {
                    skipped++;
                    continue;
                }

                Guid? categoryId = categoryById.TryGetValue(source.Metadata.Category, out PromptCategory? category) ? category.Id : null;
                PromptType type = MapPromptType(source.Metadata.Category);
                PromptStatus status = MapPromptStatus(source.Metadata.Status);
                IReadOnlyList<string> tags = BuildTags(source.Metadata, plan.Package.Manifest);
                string title = item.Action == SasdPromptPackageImportAction.Create && item.ExistingPromptId is not null
                    ? $"{source.Metadata.Title} ({plan.Package.Manifest.Version})"
                    : source.Metadata.Title;
                string sourceText = BuildSource(source.Metadata, plan.Package.Manifest);
                string notes = BuildNotes(source.Metadata, plan.Package.Manifest, item.Action == SasdPromptPackageImportAction.Create && item.ExistingPromptId is not null);

                if (item.Action == SasdPromptPackageImportAction.Update && item.ExistingPromptId is Guid existingId)
                {
                    _prompts.UpdatePromptFromEditor(
                        promptId: existingId,
                        title: title,
                        content: source.Content,
                        description: source.Metadata.Summary,
                        projectId: null,
                        categoryId: categoryId,
                        type: type,
                        status: status,
                        confidentiality: PromptConfidentiality.Internal,
                        expectedResult: string.Empty,
                        language: source.Metadata.Language,
                        styleProfile: "SASD Development Standard",
                        source: sourceText,
                        notes: notes,
                        tagNames: tags,
                        changeNote: $"Promptpaket {plan.Package.Manifest.PackageId} {plan.Package.Manifest.Version} importiert");
                    updated++;
                }
                else
                {
                    _prompts.CreatePromptWithTags(
                        title: title,
                        content: source.Content,
                        description: source.Metadata.Summary,
                        projectId: null,
                        categoryId: categoryId,
                        type: type,
                        status: status,
                        confidentiality: PromptConfidentiality.Internal,
                        expectedResult: string.Empty,
                        language: source.Metadata.Language,
                        styleProfile: "SASD Development Standard",
                        source: sourceText,
                        notes: notes,
                        tagNames: tags,
                        changeNote: $"Import aus Promptpaket {plan.Package.Manifest.PackageId} {plan.Package.Manifest.Version}");
                    created++;
                }
            }

            messages.Add($"Import abgeschlossen: {created} neu, {updated} aktualisiert, {skipped} übersprungen.");
            _logger.Info(messages[^1]);
            return new(true, created, updated, skipped, backupDirectory, messages);
        }
        catch (Exception ex)
        {
            string message = "Der Import wurde nach einem Fehler beendet. Bereits gespeicherte Änderungen können vorhanden sein; die Vorab-Sicherung kann zur Wiederherstellung verwendet werden.";
            messages.Add(message);
            messages.Add(ex.Message);
            _logger.Error(message, ex);
            return new(false, created, updated, skipped, backupDirectory, messages);
        }
    }

    public static PromptType MapPromptType(string category) => category.ToLowerInvariant() switch
    {
        "architecture" => PromptType.Architecture,
        "development" => PromptType.Coding,
        "debugging" => PromptType.Debugging,
        "documentation" => PromptType.Documentation,
        "review" => PromptType.Review,
        _ => PromptType.General
    };

    public static PromptStatus MapPromptStatus(string status) => status.ToLowerInvariant() switch
    {
        "stable" => PromptStatus.Active,
        "candidate" => PromptStatus.NeedsReview,
        "draft" => PromptStatus.Draft,
        _ => PromptStatus.NeedsReview
    };

    private Dictionary<string, PromptCategory> EnsureCategories(SasdPromptPackage package)
    {
        var result = new Dictionary<string, PromptCategory>(StringComparer.OrdinalIgnoreCase);
        foreach (SasdPromptPackageCategory packageCategory in package.Categories)
        {
            PromptCategory category = _categories.FindCategoryByName(packageCategory.Title)
                ?? _categories.CreateCategory(packageCategory.Title, packageCategory.Description);
            result[packageCategory.Id] = category;
        }
        return result;
    }

    private static Prompt? FindByStablePromptId(IEnumerable<Prompt> prompts, string promptId)
    {
        string marker = $"Prompt-ID={promptId}";
        return prompts.FirstOrDefault(prompt => prompt.Source.Contains(marker, StringComparison.OrdinalIgnoreCase)
            || prompt.Notes.Contains($"Prompt-ID: {promptId}", StringComparison.OrdinalIgnoreCase));
    }

    private static IReadOnlyList<string> BuildTags(SasdPromptCatalogEntry entry, SasdPromptPackageManifest manifest)
    {
        return entry.Tags
            .Concat(new[] { "SASD", "PromptPackage", entry.Category, entry.PromptId, manifest.PackageId })
            .Where(value => !string.IsNullOrWhiteSpace(value))
            .Select(value => value.Trim())
            .Distinct(StringComparer.OrdinalIgnoreCase)
            .OrderBy(value => value, StringComparer.OrdinalIgnoreCase)
            .ToArray();
    }

    private static string BuildSource(SasdPromptCatalogEntry entry, SasdPromptPackageManifest manifest)
        => $"SASD Prompt Package {manifest.PackageId}@{manifest.Version}; Prompt-ID={entry.PromptId}; Source={entry.SourceFile}";

    private static string BuildNotes(SasdPromptCatalogEntry entry, SasdPromptPackageManifest manifest, bool isCopy)
    {
        string copyNote = isCopy ? "\nImportmodus: zusätzliche Kopie" : string.Empty;
        return $"Prompt-ID: {entry.PromptId}\nPaket: {manifest.PackageId} {manifest.Version}\nPaketstatus: {manifest.Status}\nPromptstatus: {entry.Status}\nQualitätsstufen: {string.Join(", ", entry.QualityLevels)}\nProfile: {string.Join(", ", entry.Profiles)}\nVariablen: {string.Join(", ", entry.Variables)}{copyNote}";
    }

    private static string CreatePreImportBackup(string dataDirectory, SasdPromptPackageManifest manifest)
    {
        if (string.IsNullOrWhiteSpace(dataDirectory) || !Directory.Exists(dataDirectory))
            throw new DirectoryNotFoundException("Das Prompt-Manager-Datenverzeichnis wurde nicht gefunden.");

        string safePackageId = string.Concat(manifest.PackageId.Select(character => Path.GetInvalidFileNameChars().Contains(character) ? '_' : character));
        string backupRoot = Path.Combine(Path.GetDirectoryName(Path.GetFullPath(dataDirectory))!, "backups", "prompt-package-imports");
        string backupDirectory = Path.Combine(backupRoot, $"{DateTimeOffset.Now:yyyyMMdd-HHmmss}-{safePackageId}-{manifest.Version}");
        Directory.CreateDirectory(backupDirectory);
        foreach (string file in Directory.EnumerateFiles(dataDirectory, "*.json", SearchOption.TopDirectoryOnly))
        {
            File.Copy(file, Path.Combine(backupDirectory, Path.GetFileName(file)), overwrite: false);
        }
        File.WriteAllText(Path.Combine(backupDirectory, "IMPORT-BACKUP.txt"),
            $"Package: {manifest.PackageId}\nVersion: {manifest.Version}\nCreated: {DateTimeOffset.Now:O}\nSource data directory: {Path.GetFullPath(dataDirectory)}\n", new System.Text.UTF8Encoding(false));
        return backupDirectory;
    }
}
