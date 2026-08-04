using System.IO.Compression;
using System.Security.Cryptography;
using System.Text;
using System.Text.Json;

namespace Sasd.PromptManager.Application.PromptPackages;

/// <summary>
/// Liest und validiert das portable Austauschformat <c>sasd-prompt-package/1.0</c>.
/// </summary>
/// <remarks>
/// Vor der fachlichen Verarbeitung werden Archivgrenzen, Pfade und SHA-256-Prüfsummen geprüft.
/// Dadurch gelangen weder unvollständige Pakete noch manipulierte Promptdateien in den Importplan.
/// </remarks>
public sealed class SasdPromptPackageReader
{
    private const string SupportedFormat = "sasd-prompt-package/1.0";
    private const long MaximumArchiveBytes = 50L * 1024L * 1024L;
    private const long MaximumExpandedBytes = 100L * 1024L * 1024L;
    private const long MaximumSingleFileBytes = 4L * 1024L * 1024L;
    private const int MaximumEntryCount = 1000;
    private static readonly JsonSerializerOptions JsonOptions = new() { PropertyNameCaseInsensitive = false };

    /// <summary>Liest ein ZIP-Paket oder ein bereits entpacktes Paketverzeichnis.</summary>
    public SasdPromptPackage Read(string packagePath)
    {
        if (string.IsNullOrWhiteSpace(packagePath))
        {
            throw new ArgumentException("Ein Paketpfad ist erforderlich.", nameof(packagePath));
        }

        string fullPath = Path.GetFullPath(packagePath);
        using IPackageContent content = Directory.Exists(fullPath)
            ? new DirectoryPackageContent(fullPath)
            : CreateZipContent(fullPath);

        string manifestPath = FindSingleManifest(content.Paths);
        string packageDirectory = GetDirectory(manifestPath);
        string packageRoot = GetPackageRoot(manifestPath);

        SasdPromptPackageManifest manifest = Deserialize<SasdPromptPackageManifest>(content.ReadText(manifestPath), manifestPath);
        ValidateManifest(manifest);

        string catalogPath = CombinePackagePath(packageDirectory, manifest.Catalog);
        string categoriesPath = CombinePackagePath(packageDirectory, manifest.Categories);
        string checksumsPath = CombinePackagePath(packageDirectory, "checksums.json");

        SasdPromptCatalog catalog = Deserialize<SasdPromptCatalog>(content.ReadText(catalogPath), catalogPath);
        SasdPromptPackageCategories categories = Deserialize<SasdPromptPackageCategories>(content.ReadText(categoriesPath), categoriesPath);
        SasdPromptPackageChecksums checksums = Deserialize<SasdPromptPackageChecksums>(content.ReadText(checksumsPath), checksumsPath);

        ValidateIdentity(manifest, catalog, checksums);
        ValidateChecksums(content, packageRoot, checksums);

        var categoryIds = categories.Categories.Select(category => category.Id).ToHashSet(StringComparer.OrdinalIgnoreCase);
        if (categoryIds.Count != categories.Categories.Count)
        {
            throw new InvalidDataException("Das Paket enthält doppelte Kategorie-IDs.");
        }

        var promptIds = new HashSet<string>(StringComparer.OrdinalIgnoreCase);
        var prompts = new List<SasdPromptPackagePrompt>(catalog.Prompts.Count);
        foreach (SasdPromptCatalogEntry entry in catalog.Prompts)
        {
            ValidateCatalogEntry(entry, manifest, categoryIds, promptIds);
            string sourcePath = CombinePackagePath(packageRoot, entry.SourceFile);
            byte[] bytes = content.ReadBytes(sourcePath);
            ValidateHash(sourcePath, bytes, entry.Sha256);
            string markdown = DecodeUtf8(bytes, sourcePath);
            ValidateFrontMatter(markdown, entry);
            prompts.Add(new SasdPromptPackagePrompt(entry, RemoveFrontMatter(markdown).Trim()));
        }

        if (catalog.PromptCount != prompts.Count)
        {
            throw new InvalidDataException($"Der Katalog meldet {catalog.PromptCount} Prompts, enthält aber {prompts.Count} Einträge.");
        }

        return new SasdPromptPackage(manifest, catalog, categories.Categories.OrderBy(c => c.Order).ToArray(), prompts, fullPath, packageRoot);
    }

    private static IPackageContent CreateZipContent(string fullPath)
    {
        if (!File.Exists(fullPath)) throw new FileNotFoundException("Das Promptpaket wurde nicht gefunden.", fullPath);
        var info = new FileInfo(fullPath);
        if (info.Length > MaximumArchiveBytes) throw new InvalidDataException("Das Promptpaket überschreitet die zulässige ZIP-Größe von 50 MiB.");
        return new ZipPackageContent(fullPath);
    }

    private static string FindSingleManifest(IReadOnlyCollection<string> paths)
    {
        string[] candidates = paths
            .Where(path => path.EndsWith("/manifest.json", StringComparison.OrdinalIgnoreCase)
                && (path.StartsWith("prompts/packages/", StringComparison.OrdinalIgnoreCase)
                    || path.Contains("/prompts/packages/", StringComparison.OrdinalIgnoreCase)))
            .ToArray();
        if (candidates.Length != 1)
        {
            throw new InvalidDataException($"Es wurde genau ein Paketmanifest erwartet, gefunden: {candidates.Length}.");
        }
        return candidates[0];
    }

    private static string GetPackageRoot(string manifestPath)
    {
        const string marker = "prompts/packages/";
        int index = manifestPath.IndexOf(marker, StringComparison.OrdinalIgnoreCase);
        if (index < 0) throw new InvalidDataException("Das Paketmanifest liegt nicht unter prompts/packages/.");
        return manifestPath[..index].TrimEnd('/');
    }

    private static string GetDirectory(string path)
    {
        int index = path.LastIndexOf('/');
        return index < 0 ? string.Empty : path[..index];
    }

    private static string CombinePackagePath(string parent, string child)
    {
        string normalizedChild = NormalizeRelativePath(child);
        return string.IsNullOrEmpty(parent) ? normalizedChild : $"{parent}/{normalizedChild}";
    }

    private static string NormalizeRelativePath(string value)
    {
        if (string.IsNullOrWhiteSpace(value)) throw new InvalidDataException("Ein leerer Paketpfad ist nicht zulässig.");
        string path = value.Replace('\\', '/').Trim();
        if (path.StartsWith('/') || path.Contains(':')) throw new InvalidDataException($"Absoluter Paketpfad ist nicht zulässig: {value}");
        string[] parts = path.Split('/', StringSplitOptions.RemoveEmptyEntries);
        if (parts.Any(part => part is "." or "..")) throw new InvalidDataException($"Unsicherer Paketpfad: {value}");
        return string.Join('/', parts);
    }

    private static void ValidateManifest(SasdPromptPackageManifest manifest)
    {
        if (manifest.SchemaVersion != "1.0" || manifest.Format != SupportedFormat)
            throw new InvalidDataException($"Nicht unterstütztes Promptpaketformat: {manifest.Format} / {manifest.SchemaVersion}.");
        if (string.IsNullOrWhiteSpace(manifest.PackageId) || string.IsNullOrWhiteSpace(manifest.Version))
            throw new InvalidDataException("Paket-ID und Paketversion sind erforderlich.");
    }

    private static void ValidateIdentity(SasdPromptPackageManifest manifest, SasdPromptCatalog catalog, SasdPromptPackageChecksums checksums)
    {
        if (!string.Equals(catalog.PackageId, manifest.PackageId, StringComparison.Ordinal)
            || !string.Equals(checksums.PackageId, manifest.PackageId, StringComparison.Ordinal)
            || !string.Equals(catalog.PackageVersion, manifest.Version, StringComparison.Ordinal)
            || !string.Equals(checksums.PackageVersion, manifest.Version, StringComparison.Ordinal))
        {
            throw new InvalidDataException("Paketmanifest, Katalog und Prüfsummen verwenden unterschiedliche Identitäten oder Versionen.");
        }
        if (checksums.FileCount != checksums.Files.Count)
            throw new InvalidDataException("Die angegebene Anzahl der Prüfsummendateien stimmt nicht mit der Liste überein.");
    }

    private static void ValidateChecksums(IPackageContent content, string packageRoot, SasdPromptPackageChecksums checksums)
    {
        var seen = new HashSet<string>(StringComparer.OrdinalIgnoreCase);
        foreach (SasdPromptPackageChecksumEntry entry in checksums.Files)
        {
            string relative = NormalizeRelativePath(entry.Path);
            if (!seen.Add(relative)) throw new InvalidDataException($"Doppelter Prüfsummeneintrag: {relative}");
            string fullPath = CombinePackagePath(packageRoot, relative);
            byte[] bytes = content.ReadBytes(fullPath);
            ValidateHash(fullPath, bytes, entry.Sha256);
        }
    }

    private static void ValidateCatalogEntry(SasdPromptCatalogEntry entry, SasdPromptPackageManifest manifest, HashSet<string> categoryIds, HashSet<string> promptIds)
    {
        if (string.IsNullOrWhiteSpace(entry.PromptId) || !promptIds.Add(entry.PromptId))
            throw new InvalidDataException($"Leere oder doppelte Prompt-ID: {entry.PromptId}");
        if (string.IsNullOrWhiteSpace(entry.Title) || string.IsNullOrWhiteSpace(entry.SourceFile))
            throw new InvalidDataException($"Prompt {entry.PromptId} besitzt keinen Titel oder keine Quelldatei.");
        if (!string.Equals(entry.Version, manifest.Version, StringComparison.Ordinal))
            throw new InvalidDataException($"Prompt {entry.PromptId} verwendet die unerwartete Version {entry.Version}.");
        if (!categoryIds.Contains(entry.Category))
            throw new InvalidDataException($"Prompt {entry.PromptId} verweist auf die unbekannte Kategorie {entry.Category}.");
    }

    private static void ValidateHash(string path, byte[] bytes, string expected)
    {
        if (string.IsNullOrWhiteSpace(expected) || expected.Length != 64)
            throw new InvalidDataException($"Ungültige SHA-256-Angabe für {path}.");
        string actual = Convert.ToHexString(SHA256.HashData(bytes)).ToLowerInvariant();
        if (!string.Equals(actual, expected, StringComparison.OrdinalIgnoreCase))
            throw new InvalidDataException($"SHA-256-Prüfung fehlgeschlagen: {path}.");
    }

    private static void ValidateFrontMatter(string markdown, SasdPromptCatalogEntry entry)
    {
        IReadOnlyDictionary<string, string> metadata = ParseFrontMatter(markdown);
        if (!metadata.TryGetValue("prompt-id", out string? promptId) || !string.Equals(promptId, entry.PromptId, StringComparison.Ordinal))
            throw new InvalidDataException($"Front Matter und Katalog widersprechen sich bei {entry.PromptId}.");
        if (!metadata.TryGetValue("package-id", out string? packageId) || string.IsNullOrWhiteSpace(packageId))
            throw new InvalidDataException($"Prompt {entry.PromptId} enthält keine package-id.");
    }

    private static IReadOnlyDictionary<string, string> ParseFrontMatter(string markdown)
    {
        string normalized = markdown.ReplaceLineEndings("\n");
        if (!normalized.StartsWith("---\n", StringComparison.Ordinal)) throw new InvalidDataException("Eine Promptdatei enthält kein YAML-Front-Matter.");
        int end = normalized.IndexOf("\n---\n", 4, StringComparison.Ordinal);
        if (end < 0) throw new InvalidDataException("Das YAML-Front-Matter ist nicht abgeschlossen.");
        var result = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
        foreach (string line in normalized[4..end].Split('\n'))
        {
            int separator = line.IndexOf(':');
            if (separator <= 0) continue;
            string key = line[..separator].Trim();
            string value = line[(separator + 1)..].Trim().Trim('"');
            result[key] = value;
        }
        return result;
    }

    private static string RemoveFrontMatter(string markdown)
    {
        string normalized = markdown.ReplaceLineEndings("\n");
        int end = normalized.IndexOf("\n---\n", 4, StringComparison.Ordinal);
        return end < 0 ? normalized : normalized[(end + 5)..];
    }

    private static T Deserialize<T>(string json, string path)
    {
        try { return JsonSerializer.Deserialize<T>(json, JsonOptions) ?? throw new InvalidDataException($"Leere JSON-Datei: {path}"); }
        catch (JsonException ex) { throw new InvalidDataException($"Ungültige JSON-Datei: {path}", ex); }
    }

    private static string DecodeUtf8(byte[] bytes, string path)
    {
        try { return new UTF8Encoding(false, true).GetString(bytes); }
        catch (DecoderFallbackException ex) { throw new InvalidDataException($"Datei ist kein gültiges UTF-8: {path}", ex); }
    }

    private interface IPackageContent : IDisposable
    {
        IReadOnlyCollection<string> Paths { get; }
        byte[] ReadBytes(string path);
        string ReadText(string path) => DecodeUtf8(ReadBytes(path), path);
    }

    private sealed class DirectoryPackageContent : IPackageContent
    {
        private readonly string _root;
        private readonly Dictionary<string, string> _files;
        public DirectoryPackageContent(string root)
        {
            _root = Path.GetFullPath(root);
            _files = Directory.EnumerateFiles(_root, "*", SearchOption.AllDirectories)
                .ToDictionary(file => Path.GetRelativePath(_root, file).Replace('\\', '/'), file => file, StringComparer.OrdinalIgnoreCase);
            if (_files.Count > MaximumEntryCount) throw new InvalidDataException("Das Paket enthält zu viele Dateien.");
        }
        public IReadOnlyCollection<string> Paths => _files.Keys;
        public byte[] ReadBytes(string path)
        {
            string normalized = NormalizeRelativePath(path);
            if (!_files.TryGetValue(normalized, out string? file)) throw new InvalidDataException($"Paketdatei fehlt: {normalized}");
            var info = new FileInfo(file);
            if (info.Length > MaximumSingleFileBytes) throw new InvalidDataException($"Paketdatei ist zu groß: {normalized}");
            return File.ReadAllBytes(file);
        }
        public void Dispose() { }
    }

    private sealed class ZipPackageContent : IPackageContent
    {
        private readonly ZipArchive _archive;
        private readonly FileStream _stream;
        private readonly Dictionary<string, ZipArchiveEntry> _entries;
        public ZipPackageContent(string path)
        {
            _stream = File.OpenRead(path);
            _archive = new ZipArchive(_stream, ZipArchiveMode.Read, leaveOpen: false);
            _entries = new Dictionary<string, ZipArchiveEntry>(StringComparer.OrdinalIgnoreCase);
            try
            {
                if (_archive.Entries.Count > MaximumEntryCount) throw new InvalidDataException("Das ZIP enthält zu viele Einträge.");
                long expanded = 0;
                foreach (ZipArchiveEntry entry in _archive.Entries)
                {
                    if (string.IsNullOrEmpty(entry.Name)) continue;
                    string normalized = NormalizeRelativePath(entry.FullName);
                    if (entry.Length > MaximumSingleFileBytes) throw new InvalidDataException($"ZIP-Eintrag ist zu groß: {normalized}");
                    expanded += entry.Length;
                    if (expanded > MaximumExpandedBytes) throw new InvalidDataException("Das entpackte Paket überschreitet 100 MiB.");
                    if (!_entries.TryAdd(normalized, entry)) throw new InvalidDataException($"Doppelter ZIP-Pfad: {normalized}");
                }
            }
            catch
            {
                _archive.Dispose();
                _stream.Dispose();
                throw;
            }
        }
        public IReadOnlyCollection<string> Paths => _entries.Keys;
        public byte[] ReadBytes(string path)
        {
            string normalized = NormalizeRelativePath(path);
            if (!_entries.TryGetValue(normalized, out ZipArchiveEntry? entry)) throw new InvalidDataException($"Paketdatei fehlt: {normalized}");
            using Stream source = entry.Open();
            using var target = new MemoryStream((int)entry.Length);
            source.CopyTo(target);
            return target.ToArray();
        }
        public void Dispose() { _archive.Dispose(); _stream.Dispose(); }
    }
}
