using System.Text.Json.Serialization;
using Sasd.PromptManager.Domain.Prompts;

namespace Sasd.PromptManager.Application.PromptPackages;

/// <summary>
/// Verhalten beim erneuten Import einer bereits bekannten stabilen Prompt-ID.
/// </summary>
public enum SasdPromptPackageDuplicatePolicy
{
    /// <summary>Vorhandenen Prompt unverändert lassen.</summary>
    Skip = 0,
    /// <summary>Vorhandenen Prompt kontrolliert aktualisieren und eine neue Prompt-Version anlegen.</summary>
    Update = 1,
    /// <summary>Zusätzliche Kopie anlegen. Die stabile ID bleibt in den Metadaten sichtbar.</summary>
    CreateCopy = 2
}

/// <summary>Geplante oder ausgeführte Einzelaktion eines Paketimports.</summary>
public enum SasdPromptPackageImportAction
{
    Create = 0,
    Update = 1,
    Skip = 2
}

/// <summary>Manifest des portablen Formats <c>sasd-prompt-package/1.0</c>.</summary>
public sealed class SasdPromptPackageManifest
{
    [JsonPropertyName("schema_version")] public string SchemaVersion { get; init; } = "";
    [JsonPropertyName("format")] public string Format { get; init; } = "";
    [JsonPropertyName("package_id")] public string PackageId { get; init; } = "";
    [JsonPropertyName("name")] public string Name { get; init; } = "";
    [JsonPropertyName("version")] public string Version { get; init; } = "";
    [JsonPropertyName("status")] public string Status { get; init; } = "";
    [JsonPropertyName("standard_version")] public string StandardVersion { get; init; } = "";
    [JsonPropertyName("authoritative_language")] public string AuthoritativeLanguage { get; init; } = "";
    [JsonPropertyName("maintainer")] public string Maintainer { get; init; } = "";
    [JsonPropertyName("license")] public string License { get; init; } = "";
    [JsonPropertyName("description")] public string Description { get; init; } = "";
    [JsonPropertyName("catalog")] public string Catalog { get; init; } = "";
    [JsonPropertyName("variables")] public string Variables { get; init; } = "";
    [JsonPropertyName("categories")] public string Categories { get; init; } = "";
    [JsonPropertyName("workflow")] public string Workflow { get; init; } = "";
}

/// <summary>Eintrag des maschinenlesbaren Promptkatalogs.</summary>
public sealed class SasdPromptCatalogEntry
{
    [JsonPropertyName("prompt_id")] public string PromptId { get; init; } = "";
    [JsonPropertyName("title")] public string Title { get; init; } = "";
    [JsonPropertyName("summary")] public string Summary { get; init; } = "";
    [JsonPropertyName("version")] public string Version { get; init; } = "";
    [JsonPropertyName("status")] public string Status { get; init; } = "";
    [JsonPropertyName("category")] public string Category { get; init; } = "";
    [JsonPropertyName("language")] public string Language { get; init; } = "";
    [JsonPropertyName("variables")] public IReadOnlyList<string> Variables { get; init; } = Array.Empty<string>();
    [JsonPropertyName("tags")] public IReadOnlyList<string> Tags { get; init; } = Array.Empty<string>();
    [JsonPropertyName("quality_levels")] public IReadOnlyList<string> QualityLevels { get; init; } = Array.Empty<string>();
    [JsonPropertyName("profiles")] public IReadOnlyList<string> Profiles { get; init; } = Array.Empty<string>();
    [JsonPropertyName("source_file")] public string SourceFile { get; init; } = "";
    [JsonPropertyName("sha256")] public string Sha256 { get; init; } = "";
}

/// <summary>Container des Promptkatalogs.</summary>
public sealed class SasdPromptCatalog
{
    [JsonPropertyName("schema_version")] public string SchemaVersion { get; init; } = "";
    [JsonPropertyName("package_id")] public string PackageId { get; init; } = "";
    [JsonPropertyName("package_version")] public string PackageVersion { get; init; } = "";
    [JsonPropertyName("prompt_count")] public int PromptCount { get; init; }
    [JsonPropertyName("prompts")] public IReadOnlyList<SasdPromptCatalogEntry> Prompts { get; init; } = Array.Empty<SasdPromptCatalogEntry>();
}

/// <summary>Kategorieeintrag des Pakets.</summary>
public sealed class SasdPromptPackageCategory
{
    [JsonPropertyName("id")] public string Id { get; init; } = "";
    [JsonPropertyName("title")] public string Title { get; init; } = "";
    [JsonPropertyName("description")] public string Description { get; init; } = "";
    [JsonPropertyName("order")] public int Order { get; init; }
}

/// <summary>Container der Paketkategorien.</summary>
public sealed class SasdPromptPackageCategories
{
    [JsonPropertyName("schema_version")] public string SchemaVersion { get; init; } = "";
    [JsonPropertyName("categories")] public IReadOnlyList<SasdPromptPackageCategory> Categories { get; init; } = Array.Empty<SasdPromptPackageCategory>();
}

/// <summary>Prüfsummeneintrag des Pakets.</summary>
public sealed class SasdPromptPackageChecksumEntry
{
    [JsonPropertyName("path")] public string Path { get; init; } = "";
    [JsonPropertyName("sha256")] public string Sha256 { get; init; } = "";
}

/// <summary>Container der Paketprüfsummen.</summary>
public sealed class SasdPromptPackageChecksums
{
    [JsonPropertyName("schema_version")] public string SchemaVersion { get; init; } = "";
    [JsonPropertyName("package_id")] public string PackageId { get; init; } = "";
    [JsonPropertyName("package_version")] public string PackageVersion { get; init; } = "";
    [JsonPropertyName("file_count")] public int FileCount { get; init; }
    [JsonPropertyName("files")] public IReadOnlyList<SasdPromptPackageChecksumEntry> Files { get; init; } = Array.Empty<SasdPromptPackageChecksumEntry>();
}

/// <summary>Vollständig gelesener Prompt einschließlich bereinigtem Markdown-Inhalt.</summary>
public sealed record SasdPromptPackagePrompt(SasdPromptCatalogEntry Metadata, string Content);

/// <summary>Geprüftes, vollständig in den Speicher eingelesenes Promptpaket.</summary>
public sealed record SasdPromptPackage(
    SasdPromptPackageManifest Manifest,
    SasdPromptCatalog Catalog,
    IReadOnlyList<SasdPromptPackageCategory> Categories,
    IReadOnlyList<SasdPromptPackagePrompt> Prompts,
    string SourcePath,
    string PackageRoot);

/// <summary>Ein Eintrag der Importvorschau.</summary>
public sealed record SasdPromptPackageImportPlanItem(
    string PromptId,
    string Title,
    string Category,
    SasdPromptPackageImportAction Action,
    Guid? ExistingPromptId,
    string Reason);

/// <summary>Unveränderliche Vorschau eines Imports.</summary>
public sealed record SasdPromptPackageImportPlan(
    SasdPromptPackage Package,
    SasdPromptPackageDuplicatePolicy DuplicatePolicy,
    IReadOnlyList<SasdPromptPackageImportPlanItem> Items)
{
    public int CreateCount => Items.Count(item => item.Action == SasdPromptPackageImportAction.Create);
    public int UpdateCount => Items.Count(item => item.Action == SasdPromptPackageImportAction.Update);
    public int SkipCount => Items.Count(item => item.Action == SasdPromptPackageImportAction.Skip);
}

/// <summary>Ergebnis eines tatsächlich ausgeführten Imports.</summary>
public sealed record SasdPromptPackageImportResult(
    bool Succeeded,
    int Created,
    int Updated,
    int Skipped,
    string BackupDirectory,
    IReadOnlyList<string> Messages);
