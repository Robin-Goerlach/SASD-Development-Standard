using System.Drawing;
using System.Windows.Forms;
using Sasd.PromptManager.Application.Categories;
using Sasd.PromptManager.Application.Logging;
using Sasd.PromptManager.Application.PromptPackages;
using Sasd.PromptManager.Application.Prompts;

namespace Sasd.PromptManager.App;

/// <summary>Zeigt Analyse, Vorschau und kontrollierten Import eines SASD-Promptpakets.</summary>
public sealed class SasdPromptPackageImportDialog : Form
{
    private readonly SasdPromptPackageReader _reader = new();
    private readonly SasdPromptPackageImportService _importService;
    private readonly IApplicationLogger _logger;
    private readonly string _dataDirectory;
    private readonly TextBox _pathTextBox = new() { Dock = DockStyle.Fill };
    private readonly Label _packageLabel = new() { AutoSize = true, Text = "Noch kein Paket analysiert." };
    private readonly Label _summaryLabel = new() { AutoSize = true, Text = "" };
    private readonly DataGridView _previewGrid = new() { Dock = DockStyle.Fill, ReadOnly = true, AllowUserToAddRows = false, AutoGenerateColumns = false, SelectionMode = DataGridViewSelectionMode.FullRowSelect };
    private readonly ComboBox _duplicatePolicyCombo = new() { DropDownStyle = ComboBoxStyle.DropDownList, Width = 220 };
    private readonly Button _importButton = new() { Text = "Importieren", Enabled = false, AutoSize = true };
    private SasdPromptPackage? _package;
    private SasdPromptPackageImportPlan? _plan;

    public SasdPromptPackageImportDialog(PromptService promptService, CategoryService categoryService, IApplicationLogger logger, string dataDirectory)
    {
        _importService = new SasdPromptPackageImportService(promptService, categoryService, logger);
        _logger = logger;
        _dataDirectory = dataDirectory;
        Text = "SASD-Promptpaket importieren";
        Width = 1050;
        Height = 720;
        StartPosition = FormStartPosition.CenterParent;
        MinimumSize = new Size(850, 560);
        BuildUi();
    }

    public bool ImportCompleted { get; private set; }
    public SasdPromptPackageImportResult? ImportResult { get; private set; }

    private void BuildUi()
    {
        _duplicatePolicyCombo.Items.Add(new PolicyItem("Vorhandene Prompt-IDs überspringen (empfohlen)", SasdPromptPackageDuplicatePolicy.Skip));
        _duplicatePolicyCombo.Items.Add(new PolicyItem("Vorhandene Prompts aktualisieren", SasdPromptPackageDuplicatePolicy.Update));
        _duplicatePolicyCombo.Items.Add(new PolicyItem("Zusätzliche Kopien anlegen", SasdPromptPackageDuplicatePolicy.CreateCopy));
        _duplicatePolicyCombo.SelectedIndex = 0;
        _duplicatePolicyCombo.SelectedIndexChanged += (_, _) => RefreshPlan();

        _previewGrid.Columns.Add(new DataGridViewTextBoxColumn { HeaderText = "Aktion", DataPropertyName = "Action", Width = 90 });
        _previewGrid.Columns.Add(new DataGridViewTextBoxColumn { HeaderText = "Prompt-ID", DataPropertyName = "PromptId", Width = 175 });
        _previewGrid.Columns.Add(new DataGridViewTextBoxColumn { HeaderText = "Titel", DataPropertyName = "Title", AutoSizeMode = DataGridViewAutoSizeColumnMode.Fill });
        _previewGrid.Columns.Add(new DataGridViewTextBoxColumn { HeaderText = "Kategorie", DataPropertyName = "Category", Width = 135 });
        _previewGrid.Columns.Add(new DataGridViewTextBoxColumn { HeaderText = "Begründung", DataPropertyName = "Reason", Width = 280 });

        var browseButton = new Button { Text = "ZIP wählen...", AutoSize = true };
        browseButton.Click += (_, _) => ChooseZip();
        var folderButton = new Button { Text = "Ordner wählen...", AutoSize = true };
        folderButton.Click += (_, _) => ChooseFolder();
        var analyseButton = new Button { Text = "Analysieren", AutoSize = true };
        analyseButton.Click += (_, _) => AnalysePackage();
        _importButton.Click += (_, _) => ImportPackage();
        var closeButton = new Button { Text = "Schließen", AutoSize = true, DialogResult = DialogResult.Cancel };

        var pathPanel = new TableLayoutPanel { Dock = DockStyle.Top, AutoSize = true, ColumnCount = 4, Padding = new Padding(10) };
        pathPanel.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 100));
        pathPanel.ColumnStyles.Add(new ColumnStyle(SizeType.AutoSize));
        pathPanel.ColumnStyles.Add(new ColumnStyle(SizeType.AutoSize));
        pathPanel.ColumnStyles.Add(new ColumnStyle(SizeType.AutoSize));
        pathPanel.Controls.Add(_pathTextBox, 0, 0);
        pathPanel.Controls.Add(browseButton, 1, 0);
        pathPanel.Controls.Add(folderButton, 2, 0);
        pathPanel.Controls.Add(analyseButton, 3, 0);

        var infoPanel = new FlowLayoutPanel { Dock = DockStyle.Top, AutoSize = true, FlowDirection = FlowDirection.TopDown, WrapContents = false, Padding = new Padding(10, 0, 10, 8) };
        infoPanel.Controls.Add(_packageLabel);
        infoPanel.Controls.Add(_summaryLabel);

        var policyPanel = new FlowLayoutPanel { Dock = DockStyle.Top, AutoSize = true, Padding = new Padding(10, 4, 10, 8) };
        policyPanel.Controls.Add(new Label { Text = "Bei vorhandener stabiler Prompt-ID:", AutoSize = true, Padding = new Padding(0, 6, 5, 0) });
        policyPanel.Controls.Add(_duplicatePolicyCombo);

        var bottomPanel = new FlowLayoutPanel { Dock = DockStyle.Bottom, AutoSize = true, FlowDirection = FlowDirection.RightToLeft, Padding = new Padding(10) };
        bottomPanel.Controls.Add(closeButton);
        bottomPanel.Controls.Add(_importButton);

        Controls.Add(_previewGrid);
        Controls.Add(policyPanel);
        Controls.Add(infoPanel);
        Controls.Add(pathPanel);
        Controls.Add(bottomPanel);
        AcceptButton = _importButton;
        CancelButton = closeButton;
    }

    private void ChooseZip()
    {
        using var dialog = new OpenFileDialog { Filter = "SASD-Promptpaket (*.zip)|*.zip|Alle Dateien (*.*)|*.*", CheckFileExists = true, Title = "SASD-Promptpaket auswählen" };
        if (dialog.ShowDialog(this) == DialogResult.OK) _pathTextBox.Text = dialog.FileName;
    }

    private void ChooseFolder()
    {
        using var dialog = new FolderBrowserDialog { Description = "Entpacktes SASD-Promptpaket auswählen", ShowNewFolderButton = false };
        if (dialog.ShowDialog(this) == DialogResult.OK) _pathTextBox.Text = dialog.SelectedPath;
    }

    private void AnalysePackage()
    {
        try
        {
            UseWaitCursor = true;
            _package = _reader.Read(_pathTextBox.Text);
            _packageLabel.Text = $"{_package.Manifest.Name} – {_package.Manifest.PackageId} {_package.Manifest.Version} ({_package.Manifest.Status})";
            RefreshPlan();
            _logger.Info($"SASD prompt package analysed: {_package.Manifest.PackageId}@{_package.Manifest.Version}");
        }
        catch (Exception ex)
        {
            _package = null;
            _plan = null;
            _previewGrid.DataSource = null;
            _importButton.Enabled = false;
            _packageLabel.Text = "Paketprüfung fehlgeschlagen.";
            _summaryLabel.Text = ex.Message;
            _logger.Error("SASD prompt package analysis failed.", ex);
            MessageBox.Show(this, ex.Message, "Promptpaket kann nicht importiert werden", MessageBoxButtons.OK, MessageBoxIcon.Error);
        }
        finally { UseWaitCursor = false; }
    }

    private void RefreshPlan()
    {
        if (_package is null || _duplicatePolicyCombo.SelectedItem is not PolicyItem selected) return;
        _plan = _importService.CreatePlan(_package, selected.Policy);
        _previewGrid.DataSource = _plan.Items.Select(item => new { Action = TranslateAction(item.Action), item.PromptId, item.Title, item.Category, item.Reason }).ToList();
        _summaryLabel.Text = $"{_plan.Items.Count} Prompts: {_plan.CreateCount} neu, {_plan.UpdateCount} aktualisieren, {_plan.SkipCount} überspringen. Vor dem Import wird das JSON-Datenverzeichnis gesichert.";
        _importButton.Enabled = _plan.CreateCount + _plan.UpdateCount > 0;
    }

    private void ImportPackage()
    {
        if (_plan is null) return;
        string warning = $"Der Import legt {_plan.CreateCount} Prompts neu an und aktualisiert {_plan.UpdateCount}.\n\nVorher wird eine Sicherung der JSON-Daten erstellt. Fortfahren?";
        if (MessageBox.Show(this, warning, "SASD-Promptpaket importieren", MessageBoxButtons.YesNo, MessageBoxIcon.Question) != DialogResult.Yes) return;

        UseWaitCursor = true;
        try
        {
            ImportResult = _importService.Execute(_plan, _dataDirectory);
            if (!ImportResult.Succeeded)
            {
                MessageBox.Show(this, string.Join(Environment.NewLine, ImportResult.Messages) + $"\n\nSicherung: {ImportResult.BackupDirectory}", "Import nicht vollständig", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }
            ImportCompleted = true;
            MessageBox.Show(this, string.Join(Environment.NewLine, ImportResult.Messages) + $"\n\nSicherung: {ImportResult.BackupDirectory}", "Import abgeschlossen", MessageBoxButtons.OK, MessageBoxIcon.Information);
            DialogResult = DialogResult.OK;
            Close();
        }
        finally { UseWaitCursor = false; }
    }

    private static string TranslateAction(SasdPromptPackageImportAction action) => action switch
    {
        SasdPromptPackageImportAction.Create => "Neu",
        SasdPromptPackageImportAction.Update => "Aktualisieren",
        _ => "Überspringen"
    };

    private sealed record PolicyItem(string Caption, SasdPromptPackageDuplicatePolicy Policy)
    {
        public override string ToString() => Caption;
    }
}
