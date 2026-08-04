using System.Drawing;
using System.Windows.Forms;
using Sasd.PromptManager.App.ViewModels;
using Sasd.PromptManager.Application.Categories;
using Sasd.PromptManager.Application.Logging;
using Sasd.PromptManager.Application.Projects;
using Sasd.PromptManager.Application.ProjectAreas;
using Sasd.PromptManager.Application.ProjectChecklists;
using Sasd.PromptManager.Application.PromptVersions;
using Sasd.PromptManager.Application.Prompts;
using Sasd.PromptManager.Application.PromptPackages;
using Sasd.PromptManager.Application.PromptSets;
using Sasd.PromptManager.Application.Startup;
using Sasd.PromptManager.Application.Tags;
using Sasd.PromptManager.Application.Safety;
using Sasd.PromptManager.Application.Export;
using Sasd.PromptManager.Infrastructure.Export;
using Sasd.PromptManager.Domain.Prompts;
using Sasd.PromptManager.Domain.ProjectAreas;
using Sasd.PromptManager.Domain.Projects;
using Sasd.PromptManager.Infrastructure.Logging;

namespace Sasd.PromptManager.App;

/// <summary>
/// Hauptfenster des SASD Prompt Managers.
/// </summary>
/// <remarks>
/// <para>
/// Phase 25 ergänzt den kontrollierten Import versionierter SASD-Promptpakete.
/// </para>
/// </remarks>
public sealed class MainForm : Form
{
    private readonly StartupDiagnosticReport _startupReport;
    private readonly string _startupLogFilePath;
    private readonly IApplicationLogger _logger;
    private readonly ProjectService? _projectService;
    private readonly PromptService? _promptService;
    private readonly CategoryService? _categoryService;
    private readonly TagService? _tagService;
    private readonly PromptVersionService? _promptVersionService;
    private readonly ProjectPromptChecklistService? _projectPromptChecklistService;
    private readonly PromptSetService? _promptSetService;
    private readonly ProjectAreaService? _projectAreaService;
    private readonly string _currentApplicationLogFilePath;
    private readonly PromptSecretScanner _secretScanner = new();

    private bool _isRefreshingFilters;

    private ListBox? _projectListBox;
    private ListBox? _promptListBox;
    private TextBox? _searchTextBox;
    private PromptFilterPanel? _filterPanel;
    private Label? _promptTitleLabel;
    private Label? _promptMetaLabel;
    private Label? _promptTagsLabel;
    private TextBox? _promptContentTextBox;
    private TextBox? _promptDescriptionTextBox;
    private Label? _detailStatusLabel;
    private Label? _sidebarSummaryLabel;
    private ToolStripStatusLabel? _statusMessageLabel;
    private ToolStripStatusLabel? _statusDataLabel;
    private Button? _copyPromptButton;
    private Button? _usePromptButton;
    private Button? _editPromptButton;
    private Button? _deletePromptButton;
    private Button? _versionsPromptButton;
    private Button? _editProjectButton;
    private Button? _deleteProjectButton;
    private Button? _projectChecklistButton;
    private Button? _projectAreaButton;

    /// <summary>
    /// Fallback-Konstruktor für Zwischenstände, in denen <c>Program.cs</c> direkt ein Formular
    /// mit Logger erzeugt.
    /// </summary>
    public MainForm(IApplicationLogger logger)
        : this(CreateFallbackStartupReport(), string.Empty, logger, null, null, null, null, null)
    {
    }

    /// <summary>
    /// Erstellt das Hauptfenster mit Diagnoseinformationen.
    /// </summary>
    public MainForm(StartupDiagnosticReport startupReport, string startupLogFilePath)
        : this(startupReport, startupLogFilePath, new LocalApplicationLogger(startupReport.LogDirectory), null, null, null, null, null)
    {
    }

    /// <summary>
    /// Erstellt das Hauptfenster mit Diagnoseinformationen und Logger.
    /// </summary>
    public MainForm(
        StartupDiagnosticReport startupReport,
        string startupLogFilePath,
        IApplicationLogger logger)
        : this(startupReport, startupLogFilePath, logger, null, null, null, null, null)
    {
    }

    /// <summary>
    /// Kompatibilitätskonstruktor ohne Kategorie-Service.
    /// </summary>
    public MainForm(
        StartupDiagnosticReport startupReport,
        string startupLogFilePath,
        IApplicationLogger logger,
        ProjectService? projectService,
        PromptService? promptService)
        : this(startupReport, startupLogFilePath, logger, projectService, promptService, null, null, null)
    {
    }

    /// <summary>
    /// Erstellt das Hauptfenster mit Services.
    /// </summary>
    public MainForm(
        StartupDiagnosticReport startupReport,
        string startupLogFilePath,
        IApplicationLogger logger,
        ProjectService? projectService,
        PromptService? promptService,
        CategoryService? categoryService)
        : this(startupReport, startupLogFilePath, logger, projectService, promptService, categoryService, null, null)
    {
    }

    /// <summary>
    /// Erstellt das Hauptfenster mit Services.
    /// </summary>
    public MainForm(
        StartupDiagnosticReport startupReport,
        string startupLogFilePath,
        IApplicationLogger logger,
        ProjectService? projectService,
        PromptService? promptService,
        CategoryService? categoryService,
        TagService? tagService)
        : this(startupReport, startupLogFilePath, logger, projectService, promptService, categoryService, tagService, null)
    {
    }

    /// <summary>
    /// Erstellt das Hauptfenster mit Services einschließlich Versionshistorie.
    /// </summary>
    public MainForm(
        StartupDiagnosticReport startupReport,
        string startupLogFilePath,
        IApplicationLogger logger,
        ProjectService? projectService,
        PromptService? promptService,
        CategoryService? categoryService,
        TagService? tagService,
        PromptVersionService? promptVersionService)
        : this(startupReport, startupLogFilePath, logger, projectService, promptService, categoryService, tagService, promptVersionService, null)
    {
    }

    /// <summary>
    /// Erstellt das Hauptfenster mit Services einschließlich Versionshistorie und Projekt-Checklistenstatus.
    /// </summary>
    public MainForm(
        StartupDiagnosticReport startupReport,
        string startupLogFilePath,
        IApplicationLogger logger,
        ProjectService? projectService,
        PromptService? promptService,
        CategoryService? categoryService,
        TagService? tagService,
        PromptVersionService? promptVersionService,
        ProjectPromptChecklistService? projectPromptChecklistService,
        PromptSetService? promptSetService = null,
        ProjectAreaService? projectAreaService = null)
    {
        _startupReport = startupReport ?? throw new ArgumentNullException(nameof(startupReport));
        _startupLogFilePath = startupLogFilePath ?? string.Empty;
        _logger = logger ?? throw new ArgumentNullException(nameof(logger));
        _projectService = projectService;
        _promptService = promptService;
        _categoryService = categoryService;
        _tagService = tagService;
        _promptVersionService = promptVersionService;
        _projectPromptChecklistService = projectPromptChecklistService;
        _promptSetService = promptSetService;
        _projectAreaService = projectAreaService;
        _currentApplicationLogFilePath = TryGetCurrentLogFilePath(_logger);

        Text = "SASD Prompt Manager - Phase 25";
        Width = 1340;
        Height = 820;
        StartPosition = FormStartPosition.CenterScreen;
        MinimumSize = new Size(1140, 700);

        _logger.Info("MainForm constructor started.");

        BuildUserInterface();
        RefreshFilterCategories();
        RefreshFilterProjectAreas();
        LoadProjects();

        Load += (_, _) => _logger.Info("MainForm loaded.");
        Shown += (_, _) => _logger.Info("MainForm shown.");
        FormClosing += (_, _) => _logger.Info("MainForm closing requested.");
        FormClosed += (_, _) => _logger.Info("MainForm closed.");

        _logger.Info("MainForm constructor finished.");
    }

    /// <summary>
    /// Erstellt eine einfache Fallback-Startdiagnose.
    /// </summary>
    private static StartupDiagnosticReport CreateFallbackStartupReport()
    {
        string localAppData = Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData);
        string rootDirectory = Path.Combine(localAppData, "SASD-GmbH", "PromptManager");
        string dataDirectory = Path.Combine(rootDirectory, "data");
        string logDirectory = Path.Combine(rootDirectory, "logs");
        string exportDirectory = Path.Combine(rootDirectory, "exports");

        Directory.CreateDirectory(dataDirectory);
        Directory.CreateDirectory(logDirectory);
        Directory.CreateDirectory(exportDirectory);

        return new StartupDiagnosticReport(
            ApplicationName: "SASD Prompt Manager",
            Version: "0.25.0-phase25",
            StartedAt: DateTimeOffset.Now,
            WorkspaceRoot: rootDirectory,
            DataDirectory: dataDirectory,
            LogDirectory: logDirectory,
            ExportDirectory: exportDirectory);
    }

    /// <summary>
    /// Versucht, den Pfad der aktuellen Logdatei aus dem konkreten Logger auszulesen.
    /// </summary>
    private static string TryGetCurrentLogFilePath(IApplicationLogger logger)
    {
        if (logger is LocalApplicationLogger localLogger)
        {
            return localLogger.CurrentLogFilePath;
        }

        return string.Empty;
    }

    /// <summary>
    /// Baut die gesamte Benutzeroberfläche auf.
    /// </summary>
    private void BuildUserInterface()
    {
        _logger.Info("Building Phase 25 prompt manager user interface.");

        BackColor = Color.FromArgb(245, 247, 251);

        Controls.Add(CreateMainContentPanel());
        Controls.Add(CreateStatusStrip());
        Controls.Add(CreateAdvancedFilterPanel());
        Controls.Add(CreateHeaderPanel());
        Controls.Add(CreateMenuStrip());

        UpdateStatusMessage("Phase 25 geladen. Versionierte SASD-Promptpakete können geprüft und importiert werden.");
    }

    /// <summary>
    /// Erstellt die Menüleiste.
    /// </summary>
    private MenuStrip CreateMenuStrip()
    {
        var menuStrip = new MenuStrip { Dock = DockStyle.Top };

        var fileMenu = new ToolStripMenuItem("&Datei");
        fileMenu.DropDownItems.Add(new ToolStripMenuItem("&Datenverzeichnis öffnen", null, (_, _) => OpenDataDirectory()));
        fileMenu.DropDownItems.Add(new ToolStripSeparator());

        var exportMenu = new ToolStripMenuItem("&Export");
        exportMenu.DropDownItems.Add(new ToolStripMenuItem("&Vollständiges Backup exportieren...", null, (_, _) => ExportFullBackup()));
        exportMenu.DropDownItems.Add(new ToolStripMenuItem("Ausgewählten Prompt als &Markdown exportieren...", null, (_, _) => ExportSelectedPromptAsMarkdown()));
        exportMenu.DropDownItems.Add(new ToolStripMenuItem("Ausgewähltes Projekt als Markdown exportieren...", null, (_, _) => ExportSelectedProjectAsMarkdown()));
        fileMenu.DropDownItems.Add(exportMenu);

        var importMenu = new ToolStripMenuItem("&Import");
        importMenu.DropDownItems.Add(new ToolStripMenuItem("&Backup importieren...", null, (_, _) => ImportBackup()));
        importMenu.DropDownItems.Add(new ToolStripMenuItem("&SASD-Promptpaket importieren...", null, (_, _) => ImportSasdPromptPackage()));
        fileMenu.DropDownItems.Add(importMenu);

        fileMenu.DropDownItems.Add(new ToolStripSeparator());
        fileMenu.DropDownItems.Add(new ToolStripMenuItem("&Beenden", null, (_, _) =>
        {
            _logger.Info("Exit menu item clicked.");
            Close();
        }));
        menuStrip.Items.Add(fileMenu);

        var projectMenu = new ToolStripMenuItem("&Projekte");
        projectMenu.DropDownItems.Add(new ToolStripMenuItem("&Neues Projekt", null, (_, _) => CreateProject()));
        projectMenu.DropDownItems.Add(new ToolStripMenuItem("Ausgewähltes Projekt &bearbeiten", null, (_, _) => EditSelectedProject()));
        projectMenu.DropDownItems.Add(new ToolStripMenuItem("Projekt-&Checkliste...", null, (_, _) => ShowSelectedProjectChecklist()));
        projectMenu.DropDownItems.Add(new ToolStripMenuItem("Projekt&bereiche verwalten...", null, (_, _) => ManageProjectAreas()));
        projectMenu.DropDownItems.Add(new ToolStripMenuItem("Prompt-Set auf Projekt anwenden...", null, (_, _) => ApplyPromptSetToSelectedProject()));
        projectMenu.DropDownItems.Add(new ToolStripMenuItem("Ausgewähltes Projekt &löschen", null, (_, _) => DeleteSelectedProject()));
        projectMenu.DropDownItems.Add(new ToolStripSeparator());
        projectMenu.DropDownItems.Add(new ToolStripMenuItem("Ausgewähltes Projekt als &Markdown exportieren...", null, (_, _) => ExportSelectedProjectAsMarkdown()));
        menuStrip.Items.Add(projectMenu);

        var categoryMenu = new ToolStripMenuItem("&Kategorien");
        categoryMenu.DropDownItems.Add(new ToolStripMenuItem("&Kategorien verwalten", null, (_, _) => ManageCategories()));
        categoryMenu.DropDownItems.Add(new ToolStripMenuItem("&Neue Kategorie", null, (_, _) => CreateCategoryQuick()));
        menuStrip.Items.Add(categoryMenu);

        var tagMenu = new ToolStripMenuItem("&Tags");
        tagMenu.DropDownItems.Add(new ToolStripMenuItem("&Tags verwalten", null, (_, _) => ManageTags()));
        menuStrip.Items.Add(tagMenu);

        var promptMenu = new ToolStripMenuItem("&Prompts");
        promptMenu.DropDownItems.Add(new ToolStripMenuItem("&Neuer Prompt", null, (_, _) => CreatePrompt()));
        promptMenu.DropDownItems.Add(new ToolStripMenuItem("Prompt-&Sets verwalten...", null, (_, _) => ManagePromptSets()));
        promptMenu.DropDownItems.Add(new ToolStripSeparator());
        promptMenu.DropDownItems.Add(new ToolStripMenuItem("Ausgewählten Prompt &verwenden", null, (_, _) => UseSelectedPrompt()));
        promptMenu.DropDownItems.Add(new ToolStripMenuItem("Ausgewählten Prompt &bearbeiten", null, (_, _) => EditSelectedPrompt()));
        promptMenu.DropDownItems.Add(new ToolStripMenuItem("&Versionshistorie anzeigen...", null, (_, _) => ShowSelectedPromptVersions()));
        promptMenu.DropDownItems.Add(new ToolStripMenuItem("Favorit umschalten", null, (_, _) => ToggleSelectedPromptFavorite()));
        promptMenu.DropDownItems.Add(new ToolStripMenuItem("Ausgewählten Prompt &archivieren", null, (_, _) => DeleteSelectedPrompt()));
        promptMenu.DropDownItems.Add(new ToolStripMenuItem("Ausgewählten Prompt &wiederherstellen", null, (_, _) => RestoreSelectedPrompt()));
        promptMenu.DropDownItems.Add(new ToolStripMenuItem("&Archivierte Prompts anzeigen", null, (_, _) => ShowArchivedPrompts()));
        promptMenu.DropDownItems.Add(new ToolStripSeparator());
        promptMenu.DropDownItems.Add(new ToolStripMenuItem("Ausgewählten Prompt &roh kopieren", null, (_, _) => CopySelectedPromptToClipboard()));
        promptMenu.DropDownItems.Add(new ToolStripMenuItem("Ausgewählten Prompt als &Markdown exportieren...", null, (_, _) => ExportSelectedPromptAsMarkdown()));
        promptMenu.DropDownItems.Add(new ToolStripSeparator());
        promptMenu.DropDownItems.Add(new ToolStripMenuItem("&Tags verwalten", null, (_, _) => ManageTags()));
        promptMenu.DropDownItems.Add(new ToolStripMenuItem("&Filter zurücksetzen", null, (_, _) => ResetFilters()));
        menuStrip.Items.Add(promptMenu);

        var helpMenu = new ToolStripMenuItem("&Hilfe");
        var diagnosticsSubMenu = new ToolStripMenuItem("&Diagnose");
        diagnosticsSubMenu.DropDownItems.Add(new ToolStripMenuItem("&Startup-Diagnose anzeigen", null, (_, _) => ShowStartupDiagnosticsDialog()));
        diagnosticsSubMenu.DropDownItems.Add(new ToolStripSeparator());
        diagnosticsSubMenu.DropDownItems.Add(new ToolStripMenuItem("&Datenverzeichnis öffnen", null, (_, _) => OpenDataDirectory()));
        diagnosticsSubMenu.DropDownItems.Add(new ToolStripMenuItem("Datenpfad &kopieren", null, (_, _) => CopyDataPathToClipboard()));
        diagnosticsSubMenu.DropDownItems.Add(new ToolStripSeparator());
        diagnosticsSubMenu.DropDownItems.Add(new ToolStripMenuItem("&Logverzeichnis öffnen", null, (_, _) => OpenLogDirectory()));
        diagnosticsSubMenu.DropDownItems.Add(new ToolStripMenuItem("Logpfad &kopieren", null, (_, _) => CopyLogPathToClipboard()));

        helpMenu.DropDownItems.Add(diagnosticsSubMenu);
        helpMenu.DropDownItems.Add(new ToolStripSeparator());
        helpMenu.DropDownItems.Add(new ToolStripMenuItem("&Über Phase 25", null, (_, _) => ShowAboutDialog()));

        menuStrip.Items.Add(helpMenu);
        return menuStrip;
    }

    /// <summary>
    /// Erstellt den Header mit Quick Search.
    /// </summary>
    private Control CreateHeaderPanel()
    {
        var headerPanel = new Panel
        {
            Dock = DockStyle.Top,
            Height = 76,
            BackColor = Color.FromArgb(15, 25, 42),
            Padding = new Padding(16, 12, 16, 12)
        };

        var titleLabel = new Label
        {
            Text = "▣  Prompt Manager",
            AutoSize = false,
            Width = 240,
            Dock = DockStyle.Left,
            ForeColor = Color.White,
            Font = new Font("Segoe UI", 14, FontStyle.Bold),
            TextAlign = ContentAlignment.MiddleLeft
        };

        _searchTextBox = new TextBox
        {
            PlaceholderText = "Quick Search: Titel, Inhalt, Beschreibung, Tags, Typ, Status, Projekt, Projektbereich, Kategorie...",
            Width = 600,
            Anchor = AnchorStyles.Left | AnchorStyles.Top,
            Location = new Point(260, 24)
        };
        _searchTextBox.TextChanged += (_, _) =>
        {
            if (_isRefreshingFilters)
            {
                return;
            }

            _logger.Debug($"Quick search text changed: {_searchTextBox.Text}");
            RefreshPromptListForSelectedProject();
        };

        var newPromptButton = new Button
        {
            Text = "+ Neuer Prompt",
            Width = 130,
            Height = 32,
            Anchor = AnchorStyles.Top | AnchorStyles.Right,
            Location = new Point(headerPanel.Width - 150, 22),
            BackColor = Color.FromArgb(116, 86, 242),
            ForeColor = Color.White,
            FlatStyle = FlatStyle.Flat
        };
        newPromptButton.FlatAppearance.BorderSize = 0;
        newPromptButton.Click += (_, _) => CreatePrompt();

        headerPanel.Resize += (_, _) => newPromptButton.Location = new Point(headerPanel.Width - 150, 22);

        headerPanel.Controls.Add(newPromptButton);
        headerPanel.Controls.Add(_searchTextBox);
        headerPanel.Controls.Add(titleLabel);

        return headerPanel;
    }

    /// <summary>
    /// Erstellt das Panel für erweiterte Filter.
    /// </summary>
    private Control CreateAdvancedFilterPanel()
    {
        _filterPanel = new PromptFilterPanel();
        _filterPanel.FilterChanged += (_, _) =>
        {
            if (_isRefreshingFilters)
            {
                return;
            }

            _logger.Debug("Advanced prompt filter changed.");
            RefreshPromptListForSelectedProject();
        };
        _filterPanel.FiltersReset += (_, _) =>
        {
            _logger.Info("Advanced prompt filters reset from filter panel.");
            UpdateStatusMessage("Erweiterte Filter zurückgesetzt.");
        };

        return _filterPanel;
    }

    /// <summary>
    /// Erstellt den Hauptbereich.
    /// </summary>
    private Control CreateMainContentPanel()
    {
        var rootPanel = new TableLayoutPanel
        {
            Dock = DockStyle.Fill,
            ColumnCount = 3,
            RowCount = 1,
            Padding = new Padding(0)
        };

        rootPanel.ColumnStyles.Add(new ColumnStyle(SizeType.Absolute, 190));
        rootPanel.ColumnStyles.Add(new ColumnStyle(SizeType.Absolute, 430));
        rootPanel.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 100));

        rootPanel.Controls.Add(CreateSidebarPanel(), 0, 0);
        rootPanel.Controls.Add(CreateSelectionPanel(), 1, 0);
        rootPanel.Controls.Add(CreatePromptDetailPanel(), 2, 0);

        return rootPanel;
    }

    /// <summary>
    /// Erstellt die linke Navigationsleiste.
    /// </summary>
    private Control CreateSidebarPanel()
    {
        var panel = new Panel
        {
            Dock = DockStyle.Fill,
            BackColor = Color.FromArgb(17, 31, 53),
            Padding = new Padding(12)
        };

        var navigationLabel = new Label
        {
            Text = "NAVIGATION",
            Dock = DockStyle.Top,
            Height = 28,
            ForeColor = Color.FromArgb(170, 185, 205),
            Font = new Font("Segoe UI", 8, FontStyle.Bold)
        };

        var navigationList = new ListBox
        {
            Dock = DockStyle.Top,
            Height = 190,
            BorderStyle = BorderStyle.None,
            BackColor = Color.FromArgb(17, 31, 53),
            ForeColor = Color.White,
            Font = new Font("Segoe UI", 10)
        };

        navigationList.Items.Add("Dashboard");
        navigationList.Items.Add("Prompts");
        navigationList.Items.Add("Alle Prompts");
        navigationList.Items.Add("Archiv");
        navigationList.Items.Add("Projekte");
        navigationList.Items.Add("Projektbereiche");
        navigationList.Items.Add("Kategorien");
        navigationList.Items.Add("Tags");
        navigationList.Items.Add("Checklisten");
        navigationList.Items.Add("Vorlagen");
        navigationList.SelectedIndex = 1;
        navigationList.SelectedIndexChanged += (_, _) =>
        {
            if (navigationList.SelectedItem?.ToString() == "Alle Prompts")
            {
                SelectAllPromptsView();
            }

            if (navigationList.SelectedItem?.ToString() == "Archiv")
            {
                ShowArchivedPrompts();
            }

            if (navigationList.SelectedItem?.ToString() == "Projektbereiche")
            {
                ManageProjectAreas();
            }

            if (navigationList.SelectedItem?.ToString() == "Kategorien")
            {
                ManageCategories();
            }

            if (navigationList.SelectedItem?.ToString() == "Tags")
            {
                ManageTags();
            }

            if (navigationList.SelectedItem?.ToString() == "Checklisten")
            {
                ShowSelectedProjectChecklist();
            }
        };

        var toolsLabel = new Label
        {
            Text = "WERKZEUGE",
            Dock = DockStyle.Top,
            Height = 28,
            ForeColor = Color.FromArgb(170, 185, 205),
            Font = new Font("Segoe UI", 8, FontStyle.Bold)
        };

        var toolsList = new ListBox
        {
            Dock = DockStyle.Top,
            Height = 120,
            BorderStyle = BorderStyle.None,
            BackColor = Color.FromArgb(17, 31, 53),
            ForeColor = Color.White,
            Font = new Font("Segoe UI", 10)
        };

        toolsList.Items.Add("Quick Search");
        toolsList.Items.Add("Erweiterte Filter");
        toolsList.Items.Add("Prompt verwenden");
        toolsList.Items.Add("Kategorien");
        toolsList.Items.Add("Projektbereiche");
        toolsList.Items.Add("Tag-Verwaltung");

        _sidebarSummaryLabel = new Label
        {
            Dock = DockStyle.Bottom,
            Height = 150,
            ForeColor = Color.FromArgb(210, 220, 235),
            Font = new Font("Segoe UI", 9),
            Text = BuildSidebarSummaryText()
        };

        panel.Controls.Add(_sidebarSummaryLabel);
        panel.Controls.Add(toolsList);
        panel.Controls.Add(toolsLabel);
        panel.Controls.Add(navigationList);
        panel.Controls.Add(navigationLabel);

        return panel;
    }

    /// <summary>
    /// Erstellt Projektliste und Promptliste.
    /// </summary>
    private Control CreateSelectionPanel()
    {
        var panel = new TableLayoutPanel
        {
            Dock = DockStyle.Fill,
            RowCount = 5,
            ColumnCount = 1,
            Padding = new Padding(14),
            BackColor = Color.White
        };

        panel.RowStyles.Add(new RowStyle(SizeType.Absolute, 34));
        panel.RowStyles.Add(new RowStyle(SizeType.Absolute, 40));
        panel.RowStyles.Add(new RowStyle(SizeType.Percent, 34));
        panel.RowStyles.Add(new RowStyle(SizeType.Absolute, 44));
        panel.RowStyles.Add(new RowStyle(SizeType.Percent, 66));

        var projectHeader = new Label
        {
            Text = "Projekte",
            Dock = DockStyle.Fill,
            Font = new Font("Segoe UI", 12, FontStyle.Bold)
        };

        var projectButtonPanel = new FlowLayoutPanel { Dock = DockStyle.Fill, FlowDirection = FlowDirection.LeftToRight };

        var createProjectButton = new Button { Text = "Neu", Width = 72, Height = 28 };
        createProjectButton.Click += (_, _) => CreateProject();

        _editProjectButton = new Button { Text = "Bearbeiten", Width = 92, Height = 28, Enabled = false };
        _editProjectButton.Click += (_, _) => EditSelectedProject();

        _deleteProjectButton = new Button { Text = "Löschen", Width = 82, Height = 28, Enabled = false };
        _deleteProjectButton.Click += (_, _) => DeleteSelectedProject();

        _projectChecklistButton = new Button { Text = "Checkliste", Width = 88, Height = 28, Enabled = false };
        _projectChecklistButton.Click += (_, _) => ShowSelectedProjectChecklist();

        _projectAreaButton = new Button { Text = "Bereiche", Width = 82, Height = 28, Enabled = false };
        _projectAreaButton.Click += (_, _) => ManageProjectAreas();

        projectButtonPanel.Controls.Add(createProjectButton);
        projectButtonPanel.Controls.Add(_editProjectButton);
        projectButtonPanel.Controls.Add(_deleteProjectButton);
        projectButtonPanel.Controls.Add(_projectChecklistButton);
        projectButtonPanel.Controls.Add(_projectAreaButton);

        _projectListBox = new ListBox { Dock = DockStyle.Fill, Font = new Font("Segoe UI", 10) };
        _projectListBox.SelectedIndexChanged += (_, _) => ProjectSelectionChanged();

        /*
         * Desktop-Nutzer erwarten, dass Rechtsklick und Doppelklick etwas Sinnvolles tun.
         * Deshalb selektieren wir beim Rechtsklick zuerst das Element unter der Maus und
         * öffnen dann ein Kontextmenü mit den wichtigsten Projektaktionen.
         */
        _projectListBox.MouseDown += (_, eventArgs) => SelectListBoxItemUnderMouse(_projectListBox, eventArgs, clearSelectionWhenNoItemWasHit: true);
        _projectListBox.DoubleClick += (_, _) => OpenSelectedProjectByDoubleClick();
        _projectListBox.ContextMenuStrip = CreateProjectListContextMenu();

        var promptHeader = new Label
        {
            Text = "Prompts",
            Dock = DockStyle.Fill,
            Font = new Font("Segoe UI", 12, FontStyle.Bold),
            Padding = new Padding(0, 10, 0, 0)
        };

        _promptListBox = new ListBox { Dock = DockStyle.Fill, Font = new Font("Segoe UI", 10) };
        _promptListBox.SelectedIndexChanged += (_, _) => PromptSelectionChanged();

        /*
         * Der wichtigste Zweck eines Prompts ist seine Verwendung. Darum öffnet der
         * Doppelklick direkt den Verwenden-Dialog. Bearbeiten bleibt über Button, Menü
         * und Kontextmenü erreichbar.
         */
        _promptListBox.MouseDown += (_, eventArgs) => SelectListBoxItemUnderMouse(_promptListBox, eventArgs, clearSelectionWhenNoItemWasHit: true);
        _promptListBox.DoubleClick += (_, _) => UseSelectedPrompt();
        _promptListBox.ContextMenuStrip = CreatePromptListContextMenu();

        panel.Controls.Add(projectHeader, 0, 0);
        panel.Controls.Add(projectButtonPanel, 0, 1);
        panel.Controls.Add(_projectListBox, 0, 2);
        panel.Controls.Add(promptHeader, 0, 3);
        panel.Controls.Add(_promptListBox, 0, 4);

        return panel;
    }

    /// <summary>
    /// Erstellt die rechte Prompt-Detailansicht.
    /// </summary>
    private Control CreatePromptDetailPanel()
    {
        var panel = new TableLayoutPanel
        {
            Dock = DockStyle.Fill,
            RowCount = 7,
            ColumnCount = 1,
            Padding = new Padding(22),
            BackColor = Color.FromArgb(248, 250, 253)
        };

        panel.RowStyles.Add(new RowStyle(SizeType.Absolute, 42));
        panel.RowStyles.Add(new RowStyle(SizeType.Absolute, 28));
        panel.RowStyles.Add(new RowStyle(SizeType.Absolute, 28));
        panel.RowStyles.Add(new RowStyle(SizeType.Percent, 65));
        panel.RowStyles.Add(new RowStyle(SizeType.Absolute, 46));
        panel.RowStyles.Add(new RowStyle(SizeType.Percent, 35));
        panel.RowStyles.Add(new RowStyle(SizeType.Absolute, 28));

        _promptTitleLabel = new Label { Text = "Kein Prompt ausgewählt", Dock = DockStyle.Fill, Font = new Font("Segoe UI", 15, FontStyle.Bold) };
        _promptMetaLabel = new Label { Text = "Wähle links ein Projekt oder 'Alle Prompts' und anschließend einen Prompt aus.", Dock = DockStyle.Fill, ForeColor = Color.FromArgb(80, 95, 115) };
        _promptTagsLabel = new Label { Text = "Tags: -", Dock = DockStyle.Fill, ForeColor = Color.FromArgb(80, 95, 115) };

        _promptContentTextBox = new TextBox
        {
            Dock = DockStyle.Fill,
            Multiline = true,
            ReadOnly = true,
            ScrollBars = ScrollBars.Both,
            Font = new Font("Consolas", 10),
            Text = "Prompt-Inhalt erscheint hier."
        };
        _promptContentTextBox.ContextMenuStrip = CreatePromptDetailContextMenu();

        var buttonPanel = new FlowLayoutPanel { Dock = DockStyle.Fill, FlowDirection = FlowDirection.LeftToRight };

        _copyPromptButton = new Button { Text = "Roh kopieren", Width = 110, Height = 32, Enabled = false };
        _copyPromptButton.Click += (_, _) => CopySelectedPromptToClipboard();

        _usePromptButton = new Button { Text = "Verwenden...", Width = 110, Height = 32, Enabled = false };
        _usePromptButton.Click += (_, _) => UseSelectedPrompt();

        _editPromptButton = new Button { Text = "Bearbeiten", Width = 100, Height = 32, Enabled = false };
        _editPromptButton.Click += (_, _) => EditSelectedPrompt();

        _versionsPromptButton = new Button { Text = "Versionen...", Width = 110, Height = 32, Enabled = false };
        _versionsPromptButton.Click += (_, _) => ShowSelectedPromptVersions();

        _deletePromptButton = new Button { Text = "Archivieren", Width = 110, Height = 32, Enabled = false };
        _deletePromptButton.Click += (_, _) => ArchiveOrRestoreSelectedPrompt();

        buttonPanel.Controls.Add(_copyPromptButton);
        buttonPanel.Controls.Add(_usePromptButton);
        buttonPanel.Controls.Add(_editPromptButton);
        buttonPanel.Controls.Add(_versionsPromptButton);
        buttonPanel.Controls.Add(_deletePromptButton);

        _promptDescriptionTextBox = new TextBox { Dock = DockStyle.Fill, Multiline = true, ReadOnly = true, ScrollBars = ScrollBars.Vertical, Font = new Font("Segoe UI", 10), Text = "Beschreibung erscheint hier." };
        _promptDescriptionTextBox.ContextMenuStrip = CreatePromptDetailContextMenu();
        _detailStatusLabel = new Label { Text = "Bereit.", Dock = DockStyle.Fill, ForeColor = Color.FromArgb(80, 95, 115) };

        panel.Controls.Add(_promptTitleLabel, 0, 0);
        panel.Controls.Add(_promptMetaLabel, 0, 1);
        panel.Controls.Add(_promptTagsLabel, 0, 2);
        panel.Controls.Add(_promptContentTextBox, 0, 3);
        panel.Controls.Add(buttonPanel, 0, 4);
        panel.Controls.Add(_promptDescriptionTextBox, 0, 5);
        panel.Controls.Add(_detailStatusLabel, 0, 6);

        return panel;
    }

    /// <summary>
    /// Erstellt die Statusleiste.
    /// </summary>
    private StatusStrip CreateStatusStrip()
    {
        var statusStrip = new StatusStrip();

        _statusMessageLabel = new ToolStripStatusLabel("Bereit.");
        _statusDataLabel = new ToolStripStatusLabel
        {
            Spring = true,
            TextAlign = ContentAlignment.MiddleRight,
            Text = BuildStatusDataText()
        };

        statusStrip.Items.Add(_statusMessageLabel);
        statusStrip.Items.Add(_statusDataLabel);

        return statusStrip;
    }


    /// <summary>
    /// Erstellt das Kontextmenü für die Projektliste.
    /// </summary>
    private ContextMenuStrip CreateProjectListContextMenu()
    {
        var menu = new ContextMenuStrip();

        ToolStripMenuItem newProjectItem = new("Neues Projekt...", null, (_, _) => CreateProject());
        ToolStripMenuItem newPromptItem = new("Neuer Prompt in diesem Projekt...", null, (_, _) => CreatePrompt());
        ToolStripMenuItem editProjectItem = new("Projekt bearbeiten...", null, (_, _) => EditSelectedProject());
        ToolStripMenuItem checklistProjectItem = new("Projekt-Checkliste...", null, (_, _) => ShowSelectedProjectChecklist());
        ToolStripMenuItem manageProjectAreasItem = new("Projektbereiche verwalten...", null, (_, _) => ManageProjectAreas());
        ToolStripMenuItem exportProjectItem = new("Projekt als Markdown exportieren...", null, (_, _) => ExportSelectedProjectAsMarkdown());
        ToolStripMenuItem deleteProjectItem = new("Projekt löschen", null, (_, _) => DeleteSelectedProject());
        ToolStripMenuItem showAllPromptsItem = new("Alle Prompts anzeigen", null, (_, _) => SelectAllPromptsView());
        ToolStripMenuItem openDataDirectoryItem = new("Datenverzeichnis öffnen", null, (_, _) => OpenDataDirectory());

        menu.Items.Add(newPromptItem);
        menu.Items.Add(newProjectItem);
        menu.Items.Add(new ToolStripSeparator());
        menu.Items.Add(editProjectItem);
        menu.Items.Add(checklistProjectItem);
        menu.Items.Add(manageProjectAreasItem);
        menu.Items.Add(exportProjectItem);
        menu.Items.Add(deleteProjectItem);
        menu.Items.Add(new ToolStripSeparator());
        menu.Items.Add(showAllPromptsItem);
        menu.Items.Add(openDataDirectoryItem);

        menu.Opening += (_, _) =>
        {
            bool hasRealProject = GetSelectedProject() is not null;
            newPromptItem.Enabled = _projectService is not null && _promptService is not null;
            editProjectItem.Enabled = hasRealProject;
            checklistProjectItem.Enabled = hasRealProject;
            manageProjectAreasItem.Enabled = _projectAreaService is not null && _projectService is not null && _promptService is not null;
            exportProjectItem.Enabled = hasRealProject;
            deleteProjectItem.Enabled = hasRealProject;
        };

        return menu;
    }

    /// <summary>
    /// Erstellt das Kontextmenü für die Promptliste.
    /// </summary>
    private ContextMenuStrip CreatePromptListContextMenu()
    {
        var menu = new ContextMenuStrip();

        ToolStripMenuItem usePromptItem = new("Verwenden...", null, (_, _) => UseSelectedPrompt());
        ToolStripMenuItem editPromptItem = new("Bearbeiten...", null, (_, _) => EditSelectedPrompt());
        ToolStripMenuItem copyRawPromptItem = new("Roh kopieren", null, (_, _) => CopySelectedPromptToClipboard());
        ToolStripMenuItem exportPromptItem = new("Als Markdown exportieren...", null, (_, _) => ExportSelectedPromptAsMarkdown());
        ToolStripMenuItem toggleFavoriteItem = new("Favorit umschalten", null, (_, _) => ToggleSelectedPromptFavorite());
        ToolStripMenuItem versionsItem = new("Versionshistorie...", null, (_, _) => ShowSelectedPromptVersions());
        ToolStripMenuItem archivePromptItem = new("Archivieren", null, (_, _) => DeleteSelectedPrompt());
        ToolStripMenuItem restorePromptItem = new("Wiederherstellen", null, (_, _) => RestoreSelectedPrompt());
        ToolStripMenuItem showArchivedItem = new("Archivierte Prompts anzeigen", null, (_, _) => ShowArchivedPrompts());
        ToolStripMenuItem newPromptItem = new("Neuen Prompt anlegen...", null, (_, _) => CreatePrompt());
        ToolStripMenuItem resetFiltersItem = new("Filter zurücksetzen", null, (_, _) => ResetFilters());
        ToolStripMenuItem manageTagsItem = new("Tags verwalten...", null, (_, _) => ManageTags());

        menu.Items.Add(usePromptItem);
        menu.Items.Add(editPromptItem);
        menu.Items.Add(copyRawPromptItem);
        menu.Items.Add(exportPromptItem);
        menu.Items.Add(toggleFavoriteItem);
        menu.Items.Add(versionsItem);
        menu.Items.Add(new ToolStripSeparator());
        menu.Items.Add(archivePromptItem);
        menu.Items.Add(restorePromptItem);
        menu.Items.Add(showArchivedItem);
        menu.Items.Add(new ToolStripSeparator());
        menu.Items.Add(newPromptItem);
        menu.Items.Add(resetFiltersItem);
        menu.Items.Add(manageTagsItem);

        menu.Opening += (_, _) =>
        {
            Prompt? selectedPrompt = GetSelectedPrompt();
            bool hasPrompt = selectedPrompt is not null;
            bool isArchived = selectedPrompt?.IsArchived ?? false;

            /*
             * Archivierte Prompts sollen sichtbar und wiederherstellbar sein, aber nicht aus
             * Versehen verwendet, bearbeitet oder erneut gezählt werden. Deshalb sind aktive
             * Arbeitsaktionen nur für nicht archivierte Prompts verfügbar.
             */
            usePromptItem.Enabled = hasPrompt && !isArchived;
            editPromptItem.Enabled = hasPrompt && !isArchived;
            copyRawPromptItem.Enabled = hasPrompt && !isArchived;
            toggleFavoriteItem.Enabled = hasPrompt && !isArchived;

            exportPromptItem.Enabled = hasPrompt;
            versionsItem.Enabled = hasPrompt && _promptVersionService is not null;
            archivePromptItem.Enabled = hasPrompt && !isArchived;
            restorePromptItem.Enabled = hasPrompt && isArchived;
        };

        return menu;
    }

    /// <summary>
    /// Erstellt das Kontextmenü für die Prompt-Detailansicht.
    /// </summary>
    private ContextMenuStrip CreatePromptDetailContextMenu()
    {
        var menu = new ContextMenuStrip();

        ToolStripMenuItem usePromptItem = new("Prompt verwenden...", null, (_, _) => UseSelectedPrompt());
        ToolStripMenuItem copyRawPromptItem = new("Rohprompt kopieren", null, (_, _) => CopySelectedPromptToClipboard());
        ToolStripMenuItem exportPromptItem = new("Als Markdown exportieren...", null, (_, _) => ExportSelectedPromptAsMarkdown());
        ToolStripMenuItem toggleFavoriteItem = new("Favorit umschalten", null, (_, _) => ToggleSelectedPromptFavorite());
        ToolStripMenuItem versionsItem = new("Versionshistorie...", null, (_, _) => ShowSelectedPromptVersions());
        ToolStripMenuItem editPromptItem = new("Prompt bearbeiten...", null, (_, _) => EditSelectedPrompt());
        ToolStripMenuItem archivePromptItem = new("Prompt archivieren", null, (_, _) => DeleteSelectedPrompt());
        ToolStripMenuItem restorePromptItem = new("Prompt wiederherstellen", null, (_, _) => RestoreSelectedPrompt());
        ToolStripMenuItem showArchivedItem = new("Archivierte Prompts anzeigen", null, (_, _) => ShowArchivedPrompts());

        menu.Items.Add(usePromptItem);
        menu.Items.Add(copyRawPromptItem);
        menu.Items.Add(exportPromptItem);
        menu.Items.Add(toggleFavoriteItem);
        menu.Items.Add(versionsItem);
        menu.Items.Add(new ToolStripSeparator());
        menu.Items.Add(editPromptItem);
        menu.Items.Add(archivePromptItem);
        menu.Items.Add(restorePromptItem);
        menu.Items.Add(showArchivedItem);

        menu.Opening += (_, _) =>
        {
            Prompt? selectedPrompt = GetSelectedPrompt();
            bool hasPrompt = selectedPrompt is not null;
            bool isArchived = selectedPrompt?.IsArchived ?? false;

            usePromptItem.Enabled = hasPrompt && !isArchived;
            copyRawPromptItem.Enabled = hasPrompt && !isArchived;
            toggleFavoriteItem.Enabled = hasPrompt && !isArchived;
            editPromptItem.Enabled = hasPrompt && !isArchived;

            exportPromptItem.Enabled = hasPrompt;
            versionsItem.Enabled = hasPrompt && _promptVersionService is not null;
            archivePromptItem.Enabled = hasPrompt && !isArchived;
            restorePromptItem.Enabled = hasPrompt && isArchived;
        };

        return menu;
    }

    /// <summary>
    /// Selektiert bei Rechtsklick das ListBox-Element unter der Maus.
    /// </summary>
    /// <remarks>
    /// Ohne diese Hilfsmethode würde das Kontextmenü häufig auf dem alten, noch selektierten
    /// Element arbeiten. Das fühlt sich für Anwender falsch an und kann zu Fehlbedienung führen.
    /// </remarks>
    private static void SelectListBoxItemUnderMouse(ListBox? listBox, MouseEventArgs eventArgs, bool clearSelectionWhenNoItemWasHit)
    {
        if (listBox is null || eventArgs.Button != MouseButtons.Right)
        {
            return;
        }

        int index = listBox.IndexFromPoint(eventArgs.Location);

        if (index >= 0 && index < listBox.Items.Count)
        {
            listBox.SelectedIndex = index;
        }
        else if (clearSelectionWhenNoItemWasHit)
        {
            listBox.ClearSelected();
        }
    }

    /// <summary>
    /// Führt die Doppelklick-Aktion für die Projektliste aus.
    /// </summary>
    private void OpenSelectedProjectByDoubleClick()
    {
        if (_projectListBox?.SelectedItem is not ProjectListItem selectedProject)
        {
            UpdateStatusMessage("Kein Projekt ausgewählt.");
            return;
        }

        if (selectedProject.ShowsAllPrompts)
        {
            _logger.Info("All prompts double-clicked.");
            RefreshPromptListForSelectedProject();
            UpdateStatusMessage("Alle Prompts werden angezeigt.");
            return;
        }

        _logger.Info($"Project double-clicked: {selectedProject.Project?.Id}");
        RefreshPromptListForSelectedProject();
        UpdateStatusMessage($"Projekt geöffnet: {selectedProject.Project?.Name}");
    }

    /// <summary>
    /// Lädt Kategorien in das Filterpanel.
    /// </summary>
    private void RefreshFilterCategories()
    {
        if (_filterPanel is null || _categoryService is null)
        {
            return;
        }

        _filterPanel.SetCategories(_categoryService.GetAllCategories());
    }

    /// <summary>
    /// Lädt Projektbereiche in das Filterpanel.
    /// </summary>
    /// <remarks>
    /// <para>
    /// Die Liste hängt von der aktuellen Projektauswahl ab. In der Ansicht "Alle Prompts"
    /// werden Projektbereichsnamen mit Projektnamen ergänzt, damit gleichnamige Bereiche
    /// nicht verwechselt werden.
    /// </para>
    /// </remarks>
    private void RefreshFilterProjectAreas()
    {
        if (_filterPanel is null || _projectAreaService is null)
        {
            return;
        }

        _filterPanel.SetProjectAreas(BuildProjectAreaFilterOptions());
    }

    /// <summary>
    /// Baut die Projektbereichsoptionen für den Filter.
    /// </summary>
    private IReadOnlyList<ProjectAreaFilterOption> BuildProjectAreaFilterOptions()
    {
        if (_projectAreaService is null)
        {
            return Array.Empty<ProjectAreaFilterOption>();
        }

        PromptProject? selectedProject = GetSelectedProject();

        if (selectedProject is not null)
        {
            return _projectAreaService.GetAreasByProject(selectedProject.Id)
                .Select(area => new ProjectAreaFilterOption(area.Id, area.Name))
                .ToList();
        }

        return _projectAreaService.GetAllAreas()
            .Select(area => new ProjectAreaFilterOption(area.Id, $"{GetProjectName(area.ProjectId)} · {area.Name}"))
            .ToList();
    }

    /// <summary>
    /// Lädt die Projektliste.
    /// </summary>
    private void LoadProjects(Guid? projectIdToSelect = null)
    {
        _logger.Info("Loading project list.");

        if (_projectListBox is null)
        {
            return;
        }

        _projectListBox.Items.Clear();

        if (_projectService is null || _promptService is null)
        {
            _projectListBox.Items.Add("Keine Services verfügbar");
            UpdateStatusMessage("Keine Services verfügbar.");
            return;
        }

        IReadOnlyList<PromptProject> projects = _projectService.GetAllProjects();
        int totalPromptCount = _promptService.GetAllPrompts().Count;

        _projectListBox.Items.Add(ProjectListItem.CreateAllPrompts(totalPromptCount));

        foreach (PromptProject project in projects)
        {
            int promptCount = _promptService.GetPromptsByProject(project.Id).Count;
            _projectListBox.Items.Add(new ProjectListItem(project, promptCount));
        }

        UpdateProjectButtons();
        UpdateSummaryAndStatusData();

        UpdateStatusMessage($"{projects.Count} Projekte und {totalPromptCount} Prompts geladen.");
        _logger.Info($"Project list loaded: {projects.Count} projects, {totalPromptCount} prompts.");

        if (projectIdToSelect is not null && SelectProjectById(projectIdToSelect.Value))
        {
            return;
        }

        if (_projectListBox.Items.Count > 0)
        {
            _projectListBox.SelectedIndex = 0;
        }
        else
        {
            RefreshPromptListForSelectedProject();
        }
    }

    /// <summary>
    /// Wählt die Ansicht "Alle Prompts" aus.
    /// </summary>
    private void SelectAllPromptsView()
    {
        if (_projectListBox is null)
        {
            return;
        }

        for (int index = 0; index < _projectListBox.Items.Count; index++)
        {
            if (_projectListBox.Items[index] is ProjectListItem item && item.ShowsAllPrompts)
            {
                _projectListBox.SelectedIndex = index;
                return;
            }
        }
    }

    /// <summary>
    /// Wählt ein Projekt anhand seiner ID aus.
    /// </summary>
    private bool SelectProjectById(Guid projectId)
    {
        if (_projectListBox is null)
        {
            return false;
        }

        for (int index = 0; index < _projectListBox.Items.Count; index++)
        {
            if (_projectListBox.Items[index] is ProjectListItem item &&
                item.Project is not null &&
                item.Project.Id == projectId)
            {
                _projectListBox.SelectedIndex = index;
                return true;
            }
        }

        return false;
    }

    /// <summary>
    /// Wählt einen Prompt anhand seiner ID aus.
    /// </summary>
    private bool SelectPromptById(Guid promptId)
    {
        if (_promptListBox is null)
        {
            return false;
        }

        for (int index = 0; index < _promptListBox.Items.Count; index++)
        {
            if (_promptListBox.Items[index] is PromptListItem item && item.Prompt.Id == promptId)
            {
                _promptListBox.SelectedIndex = index;
                return true;
            }
        }

        return false;
    }

    /// <summary>
    /// Reagiert auf Projektauswahl.
    /// </summary>
    private void ProjectSelectionChanged()
    {
        UpdateProjectButtons();

        if (_projectListBox?.SelectedItem is not ProjectListItem selectedProject)
        {
            return;
        }

        if (selectedProject.ShowsAllPrompts)
        {
            _logger.Info("All prompts view selected.");
        }
        else
        {
            _logger.Info($"Project selected: {selectedProject.Project?.Name} ({selectedProject.Project?.Id})");
        }

        RefreshFilterProjectAreas();
        RefreshPromptListForSelectedProject();
    }

    /// <summary>
    /// Aktiviert/deaktiviert Projektbuttons.
    /// </summary>
    private void UpdateProjectButtons()
    {
        bool hasRealProjectSelection =
            _projectListBox?.SelectedItem is ProjectListItem selectedProject &&
            !selectedProject.ShowsAllPrompts;

        if (_editProjectButton is not null)
        {
            _editProjectButton.Enabled = hasRealProjectSelection;
        }

        if (_deleteProjectButton is not null)
        {
            _deleteProjectButton.Enabled = hasRealProjectSelection;
        }

        if (_projectChecklistButton is not null)
        {
            _projectChecklistButton.Enabled = hasRealProjectSelection;
        }

        if (_projectAreaButton is not null)
        {
            _projectAreaButton.Enabled = hasRealProjectSelection && _projectAreaService is not null;
        }
    }

    /// <summary>
    /// Setzt Quick Search und erweiterte Filter zurück.
    /// </summary>
    private void ResetFilters()
    {
        _logger.Info("Prompt filters reset.");

        _isRefreshingFilters = true;

        if (_searchTextBox is not null)
        {
            _searchTextBox.Text = string.Empty;
        }

        _filterPanel?.ResetFilters();

        _isRefreshingFilters = false;

        RefreshPromptListForSelectedProject();
        UpdateStatusMessage("Suche und Filter zurückgesetzt.");
    }

    /// <summary>
    /// Aktiviert eine Ansicht für archivierte Prompts.
    /// </summary>
    private void ShowArchivedPrompts()
    {
        _logger.Info("Archived prompt view requested.");

        if (_filterPanel is null)
        {
            UpdateStatusMessage("Archivansicht kann nicht aktiviert werden: Filterpanel fehlt.");
            return;
        }

        /*
         * Die Archivansicht ist keine neue Datenstruktur, sondern eine klare Filterkombination:
         * - Archivdaten einbeziehen
         * - Status auf Archived setzen
         * - über alle Projekte anzeigen, sofern möglich
         */
        _filterPanel.ShowArchivedPromptsOnly();
        SelectAllPromptsView();
        RefreshPromptListForSelectedProject();
        UpdateStatusMessage("Archivierte Prompts werden angezeigt.");
    }

    /// <summary>
    /// Aktualisiert die Promptliste.
    /// </summary>
    private void RefreshPromptListForSelectedProject(Guid? promptIdToSelect = null)
    {
        if (_promptListBox is null)
        {
            return;
        }

        _promptListBox.Items.Clear();
        ClearPromptDetails();

        if (_promptService is null)
        {
            UpdateStatusMessage("PromptService nicht verfügbar.");
            return;
        }

        PromptSearchCriteria criteria = BuildPromptSearchCriteria();

        IReadOnlyList<Prompt> promptList = _promptService.SearchPrompts(criteria);

        bool showProjectName =
            _projectListBox?.SelectedItem is ProjectListItem selectedProject &&
            selectedProject.ShowsAllPrompts;

        foreach (Prompt prompt in promptList)
        {
            string projectName = showProjectName ? GetProjectName(prompt.ProjectId) : string.Empty;
            string projectAreaName = GetPromptListProjectAreaDisplayName(prompt.ProjectAreaId);
            _promptListBox.Items.Add(new PromptListItem(prompt, projectName, projectAreaName));
        }

        UpdateStatusMessage(BuildPromptResultMessage(promptList.Count, criteria));
        _logger.Info($"Prompt list refreshed using search criteria: {promptList.Count} prompts.");

        if (promptIdToSelect is not null && SelectPromptById(promptIdToSelect.Value))
        {
            return;
        }

        if (_promptListBox.Items.Count > 0)
        {
            _promptListBox.SelectedIndex = 0;
        }
        else
        {
            _logger.Info("No prompt matched current filters.");
            ShowPromptListEmptyState(criteria);
        }
    }

    /// <summary>
    /// Zeigt einen hilfreichen Leerzustand an, wenn keine Prompts gefunden wurden.
    /// </summary>
    private void ShowPromptListEmptyState(PromptSearchCriteria criteria)
    {
        if (_promptTitleLabel is null ||
            _promptMetaLabel is null ||
            _promptTagsLabel is null ||
            _promptContentTextBox is null ||
            _promptDescriptionTextBox is null ||
            _detailStatusLabel is null)
        {
            return;
        }

        bool hasSearchOrFilter =
            !string.IsNullOrWhiteSpace(criteria.SearchText) ||
            criteria.ProjectAreaId is not null ||
            criteria.WithoutProjectAreaOnly ||
            criteria.CategoryId is not null ||
            criteria.Type is not null ||
            criteria.Status is not null ||
            criteria.FavoritesOnly ||
            criteria.IncludeArchived ||
            !string.IsNullOrWhiteSpace(criteria.TagText);

        if (hasSearchOrFilter)
        {
            _promptTitleLabel.Text = criteria.Status == PromptStatus.Archived
                ? "Keine archivierten Prompts gefunden"
                : "Keine Prompts gefunden";

            _promptMetaLabel.Text = "Die aktuelle Suche oder Filterkombination liefert keine Treffer.";
            _promptContentTextBox.Text = "Tipp: Setze die Filter über das Kontextmenü der Promptliste oder den Button im Filterbereich zurück.";
            _promptDescriptionTextBox.Text = criteria.IncludeArchived
                ? "Archivierte Prompts erscheinen nur bei aktivierter Archivansicht oder Statusfilter 'Archived'."
                : "Du kannst auch mit Rechtsklick in die Promptliste einen neuen Prompt anlegen.";
            _detailStatusLabel.Text = "Keine Treffer.";
        }
        else
        {
            _promptTitleLabel.Text = "Noch keine Prompts vorhanden";
            _promptMetaLabel.Text = "Lege einen neuen Prompt an, um mit der Sammlung zu beginnen.";
            _promptContentTextBox.Text = "Rechtsklick in die Promptliste oder Button '+ Neuer Prompt'.";
            _promptDescriptionTextBox.Text = "Prompts können später Projekten, Kategorien und Tags zugeordnet werden.";
            _detailStatusLabel.Text = "Leerer Zustand.";
        }

        _promptTagsLabel.Text = "Tags: -";
    }

    /// <summary>
    /// Baut Suchkriterien aus der UI.
    /// </summary>
    private PromptSearchCriteria BuildPromptSearchCriteria()
    {
        Guid? selectedProjectId = GetSelectedProjectId();

        return new PromptSearchCriteria
        {
            SearchText = _searchTextBox?.Text.Trim() ?? string.Empty,
            ProjectId = selectedProjectId,
            ProjectAreaId = _filterPanel?.SelectedProjectAreaId,
            WithoutProjectAreaOnly = _filterPanel?.WithoutProjectAreaOnly ?? false,
            CategoryId = _filterPanel?.SelectedCategoryId,
            Type = _filterPanel?.SelectedPromptType,
            Status = _filterPanel?.SelectedPromptStatus,
            TagText = _filterPanel?.TagText ?? string.Empty,
            FavoritesOnly = _filterPanel?.FavoritesOnly ?? false,
            IncludeArchived = _filterPanel?.IncludeArchived ?? false,
            SortMode = _filterPanel?.SortMode ?? PromptSortMode.TitleAscending
        };
    }

    /// <summary>
    /// Baut eine Statusmeldung zur Suche.
    /// </summary>
    private string BuildPromptResultMessage(int resultCount, PromptSearchCriteria criteria)
    {
        string scope = criteria.ProjectId is null
            ? "alle Projekte"
            : $"Projekt '{GetProjectName(criteria.ProjectId)}'";

        bool hasOnlyProjectScope =
            criteria.ProjectId is not null &&
            criteria.ProjectAreaId is null &&
            !criteria.WithoutProjectAreaOnly &&
            criteria.CategoryId is null &&
            string.IsNullOrWhiteSpace(criteria.SearchText) &&
            criteria.Type is null &&
            criteria.Status is null &&
            !criteria.FavoritesOnly &&
            !criteria.IncludeArchived &&
            string.IsNullOrWhiteSpace(criteria.TagText);

        string archiveText = criteria.IncludeArchived ? ", inkl. Archiv" : string.Empty;
        string projectAreaText = BuildProjectAreaScopeText(criteria);

        if (!criteria.HasActiveFilters || hasOnlyProjectScope)
        {
            return $"{resultCount} Prompts angezeigt ({scope}{projectAreaText}{archiveText}).";
        }

        return $"{resultCount} Prompts gefunden ({scope}{projectAreaText}, Filter aktiv{archiveText}).";
    }

    /// <summary>
    /// Baut einen kurzen Text für den Projektbereichsfilter in der Statuszeile.
    /// </summary>
    private string BuildProjectAreaScopeText(PromptSearchCriteria criteria)
    {
        if (criteria.WithoutProjectAreaOnly)
        {
            return ", ohne Projektbereich";
        }

        if (criteria.ProjectAreaId is Guid projectAreaId)
        {
            return $", Projektbereich '{GetProjectAreaName(projectAreaId)}'";
        }

        return string.Empty;
    }

    /// <summary>
    /// Baut den Projektbereichsnamen für die Promptliste.
    /// </summary>
    private string GetPromptListProjectAreaDisplayName(Guid? projectAreaId)
    {
        if (projectAreaId is null)
        {
            return string.Empty;
        }

        return GetProjectAreaName(projectAreaId);
    }

    /// <summary>
    /// Reagiert auf Promptauswahl.
    /// </summary>
    private void PromptSelectionChanged()
    {
        if (_promptListBox?.SelectedItem is not PromptListItem selectedPrompt)
        {
            ClearPromptDetails();
            return;
        }

        _logger.Info($"Prompt selected: {selectedPrompt.Prompt.Title} ({selectedPrompt.Prompt.Id})");
        ShowPromptDetails(selectedPrompt.Prompt);
    }

    /// <summary>
    /// Öffnet die Projektbereichsverwaltung.
    /// </summary>
    private void ManageProjectAreas()
    {
        _logger.Info("Project area management requested.");

        if (_projectAreaService is null || _promptService is null || _projectService is null)
        {
            UpdateStatusMessage("Projektbereichsverwaltung ist nicht verfügbar.");
            MessageBox.Show(this, "Die Projektbereichsverwaltung ist in diesem Startmodus nicht verfügbar.", "Projektbereiche", MessageBoxButtons.OK, MessageBoxIcon.Information);
            return;
        }

        PromptProject? selectedProject = GetSelectedProject();
        using var dialog = new ProjectAreaManagementDialog(_projectAreaService, _promptService, _projectService, selectedProject, _logger);
        dialog.ShowDialog(this);

        if (!dialog.HasDataChanged)
        {
            return;
        }

        RefreshFilterProjectAreas();
        LoadProjects(selectedProject?.Id);
        RefreshPromptListForSelectedProject();
        UpdateStatusMessage("Projektbereiche aktualisiert.");
    }

    /// <summary>
    /// Öffnet die Prompt-Set-Verwaltung.
    /// </summary>
    private void ManagePromptSets()
    {
        _logger.Info("Prompt set management requested.");

        if (_promptSetService is null || _promptService is null)
        {
            UpdateStatusMessage("Prompt-Set-Verwaltung ist nicht verfügbar.");
            return;
        }

        using var dialog = new PromptSetManagementDialog(_promptSetService, _promptService, GetSelectedProject(), _logger);
        dialog.ShowDialog(this);

        if (dialog.HasDataChanged)
        {
            RefreshPromptListForSelectedProject();
            UpdateStatusMessage("Prompt-Sets aktualisiert.");
        }
    }

    /// <summary>
    /// Wendet ein Prompt-Set auf das aktuell ausgewählte Projekt an.
    /// </summary>
    private void ApplyPromptSetToSelectedProject()
    {
        _logger.Info("Prompt set apply to selected project requested.");

        if (_promptSetService is null)
        {
            UpdateStatusMessage("Prompt-Sets sind nicht verfügbar.");
            return;
        }

        if (GetSelectedProject() is not PromptProject selectedProject)
        {
            MessageBox.Show(this, "Bitte zuerst ein konkretes Projekt auswählen.", "Prompt-Set anwenden", MessageBoxButtons.OK, MessageBoxIcon.Information);
            return;
        }

        using var dialog = new PromptSetApplyDialog(selectedProject, _promptSetService, _logger);

        if (dialog.ShowDialog(this) != DialogResult.OK || !dialog.HasAppliedSet)
        {
            return;
        }

        LoadProjects(selectedProject.Id);
        RefreshPromptListForSelectedProject();
        UpdateStatusMessage("Prompt-Set wurde auf das Projekt angewendet: " + selectedProject.Name);
    }

    /// <summary>
    /// Öffnet die Projekt-Checkliste für das aktuell ausgewählte Projekt.
    /// </summary>
    /// <remarks>
    /// Die Checkliste ist bewusst ein eigener Dialog. Dadurch muss die Hauptoberfläche in
    /// Phase 21 nicht komplett umgebaut werden, und der Nutzer erhält trotzdem einen schnellen
    /// projektbezogenen Arbeitszugriff auf seine Prompts.
    /// </remarks>
    private void ShowSelectedProjectChecklist()
    {
        _logger.Info("Project prompt checklist requested.");

        if (_promptService is null)
        {
            UpdateStatusMessage("PromptService nicht verfügbar.");
            return;
        }

        if (GetSelectedProject() is not PromptProject selectedProject)
        {
            UpdateStatusMessage("Bitte zuerst ein konkretes Projekt auswählen.");
            MessageBox.Show(
                this,
                "Bitte wähle links zuerst ein konkretes Projekt aus.\n\nDie Ansicht 'Alle Prompts' hat keine eigene Projekt-Checkliste.",
                "Projekt-Checkliste",
                MessageBoxButtons.OK,
                MessageBoxIcon.Information);
            return;
        }

        using var dialog = new ProjectPromptChecklistDialog(
            selectedProject,
            _promptService,
            _promptVersionService,
            _projectPromptChecklistService,
            _promptSetService,
            _logger);

        dialog.ShowDialog(this);

        /*
         * Die Checkliste kann Nutzung zählen oder aus dem Dialog heraus eine Bearbeitung
         * anfordern. Deshalb wird die Hauptliste nach dem Schließen gezielt aktualisiert.
         */
        Guid? promptIdToSelect = dialog.RequestedEditPromptId ?? dialog.SelectedPromptId;

        if (dialog.HasDataChanged || promptIdToSelect is not null)
        {
            LoadProjects(selectedProject.Id);
            RefreshPromptListForSelectedProject(promptIdToSelect);
        }

        if (dialog.RequestedEditPromptId is Guid promptId && SelectPromptById(promptId))
        {
            EditSelectedPrompt();
        }

        UpdateStatusMessage("Projekt-Checkliste geschlossen: " + selectedProject.Name);
    }

    private void ManageCategories()
    {
        _logger.Info("Category management dialog requested.");

        if (_categoryService is null || _promptService is null)
        {
            UpdateStatusMessage("Kategorieverwaltung ist nicht verfügbar.");
            return;
        }

        using var dialog = new CategoryManagementDialog(_categoryService, _promptService, _logger);
        dialog.ShowDialog(this);

        RefreshFilterCategories();
        UpdateSummaryAndStatusData();
        RefreshPromptListForSelectedProject();
    }

    /// <summary>
    /// Öffnet den Tag-Verwaltungsdialog.
    /// </summary>
    private void ManageTags()
    {
        _logger.Info("Tag management dialog requested.");

        if (_tagService is null)
        {
            UpdateStatusMessage("Tag-Verwaltung ist nicht verfügbar.");
            MessageBox.Show(this, "Die Tag-Verwaltung ist derzeit nicht verfügbar.", "Tags", MessageBoxButtons.OK, MessageBoxIcon.Information);
            return;
        }

        using var dialog = new TagManagementDialog(_tagService, _logger);
        dialog.ShowDialog(this);

        /*
         * Tags hängen direkt an Prompts. Nach Umbenennen oder Entfernen müssen daher Promptliste,
         * Detailansicht, Filterergebnisse und Sidebar-Zähler aktualisiert werden.
         */
        UpdateSummaryAndStatusData();
        RefreshPromptListForSelectedProject();
        UpdateStatusMessage("Tags aktualisiert.");
    }

    /// <summary>
    /// Legt schnell eine Kategorie über den normalen Kategoriedialog an.
    /// </summary>
    private void CreateCategoryQuick()
    {
        _logger.Info("Quick category create requested.");

        if (_categoryService is null)
        {
            UpdateStatusMessage("Kategorie kann nicht angelegt werden: CategoryService fehlt.");
            return;
        }

        using var dialog = new CategoryEditorDialog();

        if (dialog.ShowDialog(this) != DialogResult.OK)
        {
            _logger.Info("Quick category create cancelled.");
            return;
        }

        try
        {
            PromptCategory category = _categoryService.CreateCategory(dialog.CategoryName, dialog.CategoryDescription);
            _logger.Info($"Category created from UI: {category.Name} ({category.Id})");

            RefreshFilterCategories();
            UpdateSummaryAndStatusData();
            UpdateStatusMessage($"Kategorie angelegt: {category.Name}");
        }
        catch (Exception exception)
        {
            _logger.Error("Quick category creation failed.", exception);
            MessageBox.Show(this, exception.Message, "Kategorie konnte nicht angelegt werden", MessageBoxButtons.OK, MessageBoxIcon.Warning);
        }
    }

    /// <summary>
    /// Öffnet den Dialog zum Erstellen eines Projekts.
    /// </summary>
    private void CreateProject()
    {
        _logger.Info("Project create workflow started.");

        if (_projectService is null)
        {
            UpdateStatusMessage("Projekt kann nicht angelegt werden: ProjectService fehlt.");
            return;
        }

        using var dialog = new ProjectEditorDialog();

        if (dialog.ShowDialog(this) != DialogResult.OK)
        {
            _logger.Info("Project create workflow cancelled.");
            UpdateStatusMessage("Projekt-Anlage abgebrochen.");
            return;
        }

        try
        {
            PromptProject project = _projectService.CreateProject(dialog.ProjectName, dialog.ProjectDescription);
            _logger.Info($"Project created from UI: {project.Name} ({project.Id})");
            UpdateStatusMessage($"Projekt angelegt: {project.Name}");
            LoadProjects(project.Id);
        }
        catch (Exception exception)
        {
            _logger.Error("Project creation failed.", exception);
            MessageBox.Show(this, exception.Message, "Projekt konnte nicht angelegt werden", MessageBoxButtons.OK, MessageBoxIcon.Warning);
        }
    }

    /// <summary>
    /// Bearbeitet das ausgewählte Projekt.
    /// </summary>
    private void EditSelectedProject()
    {
        _logger.Info("Project edit workflow requested.");

        if (_projectService is null)
        {
            UpdateStatusMessage("Projekt kann nicht bearbeitet werden: ProjectService fehlt.");
            return;
        }

        if (GetSelectedProject() is not PromptProject selectedProject)
        {
            _logger.Warning("Project edit requested but no project is selected.");
            UpdateStatusMessage("Kein Projekt zum Bearbeiten ausgewählt.");
            return;
        }

        using var dialog = new ProjectEditorDialog(selectedProject);

        if (dialog.ShowDialog(this) != DialogResult.OK)
        {
            _logger.Info($"Project edit workflow cancelled: {selectedProject.Id}");
            UpdateStatusMessage("Projekt-Bearbeitung abgebrochen.");
            return;
        }

        try
        {
            _projectService.RenameProject(selectedProject.Id, dialog.ProjectName);
            _projectService.ChangeProjectDescription(selectedProject.Id, dialog.ProjectDescription);

            _logger.Info($"Project updated from UI: {selectedProject.Id}");
            UpdateStatusMessage($"Projekt aktualisiert: {dialog.ProjectName}");

            LoadProjects(selectedProject.Id);
        }
        catch (Exception exception)
        {
            _logger.Error("Project update failed.", exception);
            MessageBox.Show(this, exception.Message, "Projekt konnte nicht gespeichert werden", MessageBoxButtons.OK, MessageBoxIcon.Warning);
        }
    }

    /// <summary>
    /// Löscht das ausgewählte Projekt, wenn keine Prompts zugeordnet sind.
    /// </summary>
    private void DeleteSelectedProject()
    {
        _logger.Info("Project delete workflow requested.");

        if (_projectService is null || _promptService is null)
        {
            UpdateStatusMessage("Projekt kann nicht gelöscht werden: Services fehlen.");
            return;
        }

        if (GetSelectedProject() is not PromptProject selectedProject)
        {
            _logger.Warning("Project delete requested but no project is selected.");
            UpdateStatusMessage("Kein Projekt zum Löschen ausgewählt.");
            return;
        }

        IReadOnlyList<Prompt> promptsInProject = _promptService.GetPromptsByProject(selectedProject.Id);

        if (promptsInProject.Count > 0)
        {
            _logger.Warning($"Project delete blocked because prompts exist: {selectedProject.Id}, prompts={promptsInProject.Count}");
            MessageBox.Show(this, $"Das Projekt '{selectedProject.Name}' enthält noch {promptsInProject.Count} Prompt(s) und kann deshalb nicht gelöscht werden.", "Projekt kann nicht gelöscht werden", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            UpdateStatusMessage("Projekt wurde nicht gelöscht, weil noch Prompts zugeordnet sind.");
            return;
        }

        DialogResult result = MessageBox.Show(this, $"Möchtest du das Projekt '{selectedProject.Name}' wirklich löschen?", "Projekt löschen", MessageBoxButtons.YesNo, MessageBoxIcon.Question, MessageBoxDefaultButton.Button2);

        if (result != DialogResult.Yes)
        {
            _logger.Info($"Project delete workflow cancelled: {selectedProject.Id}");
            UpdateStatusMessage("Projekt-Löschung abgebrochen.");
            return;
        }

        try
        {
            string projectName = selectedProject.Name;
            _projectService.DeleteProject(selectedProject.Id);
            _logger.Info($"Project deleted from UI: {selectedProject.Id}");
            UpdateStatusMessage($"Projekt gelöscht: {projectName}");
            LoadProjects();
        }
        catch (Exception exception)
        {
            _logger.Error("Project deletion failed.", exception);
            MessageBox.Show(this, exception.Message, "Projekt konnte nicht gelöscht werden", MessageBoxButtons.OK, MessageBoxIcon.Warning);
        }
    }

    /// <summary>
    /// Gibt die bekannten Tagnamen für den Prompt-Editor zurück.
    /// </summary>
    private IReadOnlyList<string> GetKnownTagNames()
    {
        if (_tagService is not null)
        {
            return _tagService.GetAllTagNames();
        }

        if (_promptService is not null)
        {
            return _promptService.GetAllTagNames();
        }

        return Array.Empty<string>();
    }

    /// <summary>
    /// Prüft den Prompt-Dialog auf mögliche Secrets und fragt bei Warnungen nach.
    /// </summary>
    /// <remarks>
    /// Die Prüfung ist bewusst eine einfache Heuristik. Sie soll den Nutzer warnen, aber nicht
    /// hart blockieren, weil auch Beispieltexte legitime Treffer auslösen können.
    /// </remarks>
    private bool ConfirmPromptSafety(PromptEditorDialog dialog)
    {
        PromptSafetyScanResult scanResult = _secretScanner.ScanPrompt(
            dialog.PromptTitle,
            dialog.PromptContent,
            dialog.PromptDescription,
            dialog.ExpectedResult,
            dialog.Source,
            dialog.Notes);

        if (!scanResult.HasWarnings)
        {
            return true;
        }

        string issueText = string.Join(
            Environment.NewLine,
            scanResult.Issues
                .Take(6)
                .Select(issue => $"- {issue.FieldName}: {issue.Message}"));

        if (scanResult.Issues.Count > 6)
        {
            issueText += Environment.NewLine + $"- weitere {scanResult.Issues.Count - 6} Warnung(en)";
        }

        DialogResult result = MessageBox.Show(
            this,
            "Der Prompt enthält möglicherweise sensible Daten." + Environment.NewLine + Environment.NewLine +
            issueText + Environment.NewLine + Environment.NewLine +
            "Bitte speichere keine Passwörter, API-Keys, Tokens oder privaten Schlüssel in Prompts." + Environment.NewLine + Environment.NewLine +
            "Trotzdem speichern?",
            "Sicherheitswarnung",
            MessageBoxButtons.YesNo,
            MessageBoxIcon.Warning,
            MessageBoxDefaultButton.Button2);

        return result == DialogResult.Yes;
    }

    /// <summary>
    /// Erstellt einen Prompt.
    /// </summary>
    private void CreatePrompt()
    {
        _logger.Info("New prompt workflow started.");

        if (_projectService is null || _promptService is null)
        {
            UpdateStatusMessage("Prompt kann nicht angelegt werden: Services fehlen.");
            return;
        }

        Guid? defaultProjectId = GetSelectedProjectId();
        IReadOnlyList<PromptCategory> categories = _categoryService?.GetAllCategories() ?? Array.Empty<PromptCategory>();
        IReadOnlyList<ProjectArea> projectAreas = _projectAreaService?.GetAllAreas() ?? Array.Empty<ProjectArea>();

        using var dialog = new PromptEditorDialog(
            _projectService.GetAllProjects(),
            categories,
            projectAreas,
            prompt: null,
            defaultProjectId: defaultProjectId,
            existingTagNames: GetKnownTagNames());

        if (dialog.ShowDialog(this) != DialogResult.OK)
        {
            _logger.Info("New prompt workflow cancelled.");
            UpdateStatusMessage("Prompt-Anlage abgebrochen.");
            return;
        }

        try
        {
            if (!ConfirmPromptSafety(dialog))
            {
                UpdateStatusMessage("Prompt-Anlage wegen Sicherheitswarnung abgebrochen.");
                return;
            }

            Prompt newPrompt = _promptService.CreatePromptWithTags(
                dialog.PromptTitle,
                dialog.PromptContent,
                dialog.PromptDescription,
                dialog.SelectedProjectId,
                dialog.SelectedCategoryId,
                dialog.SelectedPromptType,
                dialog.SelectedPromptStatus,
                dialog.SelectedConfidentiality,
                dialog.ExpectedResult,
                dialog.Language,
                dialog.StyleProfile,
                dialog.Source,
                dialog.Notes,
                dialog.TagNames,
                changeNote: dialog.ChangeNote,
                projectAreaId: dialog.SelectedProjectAreaId);

            _logger.Info($"Prompt created from UI: {newPrompt.Title} ({newPrompt.Id})");
            UpdateStatusMessage($"Prompt angelegt: {newPrompt.Title}");

            ResetFiltersWithoutRefreshing();

            LoadProjects(newPrompt.ProjectId);
            RefreshPromptListForSelectedProject(newPrompt.Id);
        }
        catch (Exception exception)
        {
            _logger.Error("Prompt creation failed.", exception);
            MessageBox.Show(this, exception.Message, "Prompt konnte nicht angelegt werden", MessageBoxButtons.OK, MessageBoxIcon.Warning);
        }
    }

    /// <summary>
    /// Bearbeitet den ausgewählten Prompt.
    /// </summary>
    private void EditSelectedPrompt()
    {
        _logger.Info("Edit prompt workflow requested.");

        if (_projectService is null || _promptService is null)
        {
            UpdateStatusMessage("Prompt kann nicht bearbeitet werden: Services fehlen.");
            return;
        }

        if (GetSelectedPrompt() is not Prompt selectedPrompt)
        {
            _logger.Warning("Edit prompt requested but no prompt is selected.");
            UpdateStatusMessage("Kein Prompt zum Bearbeiten ausgewählt.");
            return;
        }

        if (selectedPrompt.IsArchived)
        {
            UpdateStatusMessage("Archivierte Prompts bitte zuerst wiederherstellen.");
            MessageBox.Show(this, "Archivierte Prompts können nicht direkt bearbeitet werden. Bitte stelle den Prompt zuerst wieder her.", "Prompt ist archiviert", MessageBoxButtons.OK, MessageBoxIcon.Information);
            return;
        }

        IReadOnlyList<PromptCategory> categories = _categoryService?.GetAllCategories() ?? Array.Empty<PromptCategory>();
        IReadOnlyList<ProjectArea> projectAreas = _projectAreaService?.GetAllAreas() ?? Array.Empty<ProjectArea>();

        using var dialog = new PromptEditorDialog(
            _projectService.GetAllProjects(),
            categories,
            projectAreas,
            selectedPrompt,
            defaultProjectId: selectedPrompt.ProjectId,
            existingTagNames: GetKnownTagNames());

        if (dialog.ShowDialog(this) != DialogResult.OK)
        {
            _logger.Info($"Edit prompt workflow cancelled: {selectedPrompt.Id}");
            UpdateStatusMessage("Prompt-Bearbeitung abgebrochen.");
            return;
        }

        try
        {
            if (!ConfirmPromptSafety(dialog))
            {
                UpdateStatusMessage("Prompt-Bearbeitung wegen Sicherheitswarnung abgebrochen.");
                return;
            }

            _promptService.UpdatePromptFromEditor(
                selectedPrompt.Id,
                dialog.PromptTitle,
                dialog.PromptContent,
                dialog.PromptDescription,
                dialog.SelectedProjectId,
                dialog.SelectedCategoryId,
                dialog.SelectedPromptType,
                dialog.SelectedPromptStatus,
                dialog.SelectedConfidentiality,
                dialog.ExpectedResult,
                dialog.Language,
                dialog.StyleProfile,
                dialog.Source,
                dialog.Notes,
                dialog.TagNames,
                changeNote: dialog.ChangeNote,
                projectAreaId: dialog.SelectedProjectAreaId);

            Prompt? updatedPrompt = _promptService.FindPrompt(selectedPrompt.Id);

            _logger.Info($"Prompt updated from UI: {selectedPrompt.Id}");
            UpdateStatusMessage($"Prompt aktualisiert: {dialog.PromptTitle}");

            ResetFiltersWithoutRefreshing();

            LoadProjects(updatedPrompt?.ProjectId ?? dialog.SelectedProjectId);
            RefreshPromptListForSelectedProject(selectedPrompt.Id);
        }
        catch (Exception exception)
        {
            _logger.Error("Prompt update failed.", exception);
            MessageBox.Show(this, exception.Message, "Prompt konnte nicht gespeichert werden", MessageBoxButtons.OK, MessageBoxIcon.Warning);
        }
    }

    /// <summary>
    /// Führt abhängig vom Archivstatus die passende Aktion aus.
    /// </summary>
    private void ArchiveOrRestoreSelectedPrompt()
    {
        Prompt? selectedPrompt = GetSelectedPrompt();

        if (selectedPrompt is null)
        {
            UpdateStatusMessage("Kein Prompt ausgewählt.");
            return;
        }

        if (selectedPrompt.IsArchived)
        {
            RestoreSelectedPrompt();
        }
        else
        {
            DeleteSelectedPrompt();
        }
    }

    /// <summary>
    /// Archiviert den ausgewählten Prompt.
    /// </summary>
    private void DeleteSelectedPrompt()
    {
        _logger.Info("Archive prompt workflow requested.");

        if (_promptService is null)
        {
            UpdateStatusMessage("Prompt kann nicht archiviert werden: Service fehlt.");
            return;
        }

        if (GetSelectedPrompt() is not Prompt selectedPrompt)
        {
            _logger.Warning("Archive prompt requested but no prompt is selected.");
            UpdateStatusMessage("Kein Prompt zum Archivieren ausgewählt.");
            return;
        }

        if (selectedPrompt.IsArchived)
        {
            UpdateStatusMessage("Prompt ist bereits archiviert.");
            MessageBox.Show(this, "Dieser Prompt ist bereits archiviert. Du kannst ihn über 'Wiederherstellen' zurückholen.", "Prompt ist bereits archiviert", MessageBoxButtons.OK, MessageBoxIcon.Information);
            return;
        }

        DialogResult result = MessageBox.Show(this, $"Möchtest du den Prompt '{selectedPrompt.Title}' archivieren?\n\nEr bleibt im JSON-Datenbestand erhalten, wird aber in normalen Listen ausgeblendet.", "Prompt archivieren", MessageBoxButtons.YesNo, MessageBoxIcon.Question, MessageBoxDefaultButton.Button2);

        if (result != DialogResult.Yes)
        {
            _logger.Info($"Archive prompt workflow cancelled: {selectedPrompt.Id}");
            UpdateStatusMessage("Archivieren abgebrochen.");
            return;
        }

        try
        {
            Guid? projectId = selectedPrompt.ProjectId;
            string title = selectedPrompt.Title;

            _promptService.DeletePrompt(selectedPrompt.Id);

            _logger.Info($"Prompt archived from UI: {selectedPrompt.Id}");
            UpdateStatusMessage($"Prompt archiviert: {title}");

            LoadProjects(projectId);
            RefreshPromptListForSelectedProject();
        }
        catch (Exception exception)
        {
            _logger.Error("Prompt archive failed.", exception);
            MessageBox.Show(this, exception.Message, "Prompt konnte nicht archiviert werden", MessageBoxButtons.OK, MessageBoxIcon.Warning);
        }
    }

    /// <summary>
    /// Stellt einen archivierten Prompt wieder her.
    /// </summary>
    private void RestoreSelectedPrompt()
    {
        _logger.Info("Restore archived prompt workflow requested.");

        if (_promptService is null)
        {
            UpdateStatusMessage("Prompt kann nicht wiederhergestellt werden: Service fehlt.");
            return;
        }

        if (GetSelectedPrompt() is not Prompt selectedPrompt)
        {
            _logger.Warning("Restore prompt requested but no prompt is selected.");
            UpdateStatusMessage("Kein Prompt zum Wiederherstellen ausgewählt.");
            return;
        }

        if (!selectedPrompt.IsArchived)
        {
            UpdateStatusMessage("Prompt ist nicht archiviert.");
            MessageBox.Show(this, "Dieser Prompt ist nicht archiviert.", "Wiederherstellen nicht erforderlich", MessageBoxButtons.OK, MessageBoxIcon.Information);
            return;
        }

        DialogResult result = MessageBox.Show(
            this,
            $"Möchtest du den archivierten Prompt '{selectedPrompt.Title}' wiederherstellen?\n\n" +
            "Der Prompt erscheint danach wieder in den normalen Listen.",
            "Prompt wiederherstellen",
            MessageBoxButtons.YesNo,
            MessageBoxIcon.Question,
            MessageBoxDefaultButton.Button1);

        if (result != DialogResult.Yes)
        {
            _logger.Info($"Restore prompt workflow cancelled: {selectedPrompt.Id}");
            UpdateStatusMessage("Wiederherstellen abgebrochen.");
            return;
        }

        try
        {
            Guid promptId = selectedPrompt.Id;
            Guid? projectId = selectedPrompt.ProjectId;
            string title = selectedPrompt.Title;

            _promptService.RestorePrompt(promptId);

            _logger.Info($"Prompt restored from UI: {promptId}");
            UpdateStatusMessage($"Prompt wiederhergestellt: {title}");

            LoadProjects(projectId);
            RefreshPromptListForSelectedProject(promptId);
        }
        catch (Exception exception)
        {
            _logger.Error("Prompt restore failed.", exception);
            MessageBox.Show(this, exception.Message, "Prompt konnte nicht wiederhergestellt werden", MessageBoxButtons.OK, MessageBoxIcon.Warning);
        }
    }

    /// <summary>
    /// Öffnet die Versionshistorie des ausgewählten Prompts.
    /// </summary>
    private void ShowSelectedPromptVersions()
    {
        _logger.Info("Prompt version history requested.");

        if (_promptVersionService is null || _promptService is null)
        {
            UpdateStatusMessage("Versionshistorie ist nicht verfügbar.");
            MessageBox.Show(this, "Die Versionshistorie ist derzeit nicht verfügbar.", "Versionshistorie", MessageBoxButtons.OK, MessageBoxIcon.Information);
            return;
        }

        if (GetSelectedPrompt() is not Prompt selectedPrompt)
        {
            UpdateStatusMessage("Kein Prompt für die Versionshistorie ausgewählt.");
            MessageBox.Show(this, "Bitte wähle zuerst einen Prompt aus.", "Versionshistorie", MessageBoxButtons.OK, MessageBoxIcon.Information);
            return;
        }

        using var dialog = new PromptVersionHistoryDialog(selectedPrompt, _promptVersionService, _promptService, _logger);
        dialog.ShowDialog(this);

        if (dialog.HasDataChanged)
        {
            LoadProjects(selectedPrompt.ProjectId);
            RefreshPromptListForSelectedProject(selectedPrompt.Id);
        }

        UpdateStatusMessage("Versionshistorie geschlossen: " + selectedPrompt.Title);
    }

    /// <summary>
    /// Schaltet den Favoritenstatus des ausgewählten Prompts um.
    /// </summary>
    private void ToggleSelectedPromptFavorite()
    {
        if (_promptService is null)
        {
            UpdateStatusMessage("PromptService nicht verfügbar.");
            return;
        }

        if (GetSelectedPrompt() is not Prompt selectedPrompt)
        {
            _logger.Warning("Favorite toggle requested but no prompt is selected.");
            UpdateStatusMessage("Kein Prompt ausgewählt.");
            return;
        }

        if (selectedPrompt.IsArchived)
        {
            UpdateStatusMessage("Archivierte Prompts bitte zuerst wiederherstellen.");
            MessageBox.Show(this, "Archivierte Prompts können nicht als Favorit umgeschaltet werden. Bitte stelle den Prompt zuerst wieder her.", "Prompt ist archiviert", MessageBoxButtons.OK, MessageBoxIcon.Information);
            return;
        }

        bool isFavorite = _promptService.TogglePromptFavorite(selectedPrompt.Id);
        _logger.Info($"Prompt favorite toggled from UI: {selectedPrompt.Id}, isFavorite={isFavorite}");
        UpdateStatusMessage(isFavorite ? "Prompt als Favorit markiert." : "Prompt ist kein Favorit mehr.");
        RefreshPromptListForSelectedProject(selectedPrompt.Id);
    }

    /// <summary>
    /// Registriert eine fachliche Verwendung und aktualisiert die Anzeige.
    /// </summary>
    private void RegisterPromptUsageFromUi(Prompt prompt)
    {
        if (_promptService is null)
        {
            return;
        }

        _promptService.RegisterPromptUsage(prompt.Id);
        RefreshPromptListForSelectedProject(prompt.Id);
    }

    /// <summary>
    /// Öffnet den Verwendungsdialog für den ausgewählten Prompt.
    /// </summary>
    private void UseSelectedPrompt()
    {
        _logger.Info("Use prompt workflow requested.");

        if (GetSelectedPrompt() is not Prompt selectedPrompt)
        {
            _logger.Warning("Use prompt requested but no prompt is selected.");
            UpdateStatusMessage("Kein Prompt zum Verwenden ausgewählt.");
            return;
        }

        if (selectedPrompt.IsArchived)
        {
            _logger.Warning($"Use requested for archived prompt: {selectedPrompt.Id}");
            UpdateStatusMessage("Archivierte Prompts bitte zuerst wiederherstellen.");
            MessageBox.Show(this, "Archivierte Prompts können nicht direkt verwendet werden. Bitte stelle den Prompt zuerst wieder her.", "Prompt ist archiviert", MessageBoxButtons.OK, MessageBoxIcon.Information);
            return;
        }

        using var dialog = new PromptUseDialog(selectedPrompt, _logger);
        dialog.ShowDialog(this);

        if (dialog.WasPromptCopied)
        {
            RegisterPromptUsageFromUi(selectedPrompt);
            UpdateStatusMessage($"Prompt verwendet: {selectedPrompt.Title}");
        }
        else
        {
            UpdateStatusMessage($"Prompt-Verwendung geschlossen: {selectedPrompt.Title}");
        }
    }

    /// <summary>
    /// Setzt Suche und Filter ohne direkte Suche zurück.
    /// </summary>
    private void ResetFiltersWithoutRefreshing()
    {
        _isRefreshingFilters = true;

        if (_searchTextBox is not null)
        {
            _searchTextBox.Text = string.Empty;
        }

        _filterPanel?.ResetFilters();

        _isRefreshingFilters = false;
    }

    /// <summary>
    /// Gibt das ausgewählte Projekt zurück.
    /// </summary>
    private PromptProject? GetSelectedProject()
    {
        if (_projectListBox?.SelectedItem is ProjectListItem selectedProject && !selectedProject.ShowsAllPrompts)
        {
            return selectedProject.Project;
        }

        return null;
    }

    /// <summary>
    /// Gibt den ausgewählten Prompt zurück.
    /// </summary>
    private Prompt? GetSelectedPrompt()
    {
        return _promptListBox?.SelectedItem is PromptListItem selectedPrompt
            ? selectedPrompt.Prompt
            : null;
    }

    /// <summary>
    /// Gibt die ausgewählte Projekt-ID zurück.
    /// </summary>
    private Guid? GetSelectedProjectId()
    {
        return GetSelectedProject()?.Id;
    }

    /// <summary>
    /// Zeigt einen Prompt in der Detailansicht.
    /// </summary>
    private void ShowPromptDetails(Prompt prompt)
    {
        if (_promptTitleLabel is null ||
            _promptMetaLabel is null ||
            _promptTagsLabel is null ||
            _promptContentTextBox is null ||
            _promptDescriptionTextBox is null ||
            _copyPromptButton is null ||
            _usePromptButton is null ||
            _editPromptButton is null ||
            _versionsPromptButton is null ||
            _deletePromptButton is null ||
            _detailStatusLabel is null)
        {
            return;
        }

        string projectText = GetProjectName(prompt.ProjectId);
        string categoryText = GetCategoryName(prompt.CategoryId);
        string projectAreaText = GetProjectAreaName(prompt.ProjectAreaId);
        string tagText = prompt.Tags.Count == 0
            ? "-"
            : string.Join(", ", prompt.Tags.Select(tag => tag.Name));

        string favoriteText = prompt.IsFavorite ? "★ Favorit" : "Kein Favorit";
        string archiveText = prompt.IsArchived ? "ARCHIVIERT" : "Aktiv";
        string lastUsedText = prompt.LastUsedAt is null ? "noch nie verwendet" : prompt.LastUsedAt.Value.ToString("dd.MM.yyyy HH:mm");
        int versionCount = _promptVersionService?.GetVersionsForPrompt(prompt.Id).Count ?? 0;

        string titlePrefix = prompt.IsArchived ? "🗄 " : prompt.IsFavorite ? "★ " : string.Empty;
        _promptTitleLabel.Text = titlePrefix + prompt.Title;
        _promptMetaLabel.Text = $"{archiveText}    {favoriteText}    Nutzung: {prompt.UsageCount}x    Versionen: {versionCount}    Zuletzt verwendet: {lastUsedText}    Projektbereich: {projectAreaText}    Kategorie: {categoryText}    Typ: {prompt.Type}    Status: {prompt.Status}    Projekt: {projectText}";
        _promptTagsLabel.Text = $"Tags: {tagText}";
        _promptContentTextBox.Text = prompt.Content;
        _promptDescriptionTextBox.Text = BuildPromptDescriptionAndMetadataText(prompt);
        _copyPromptButton.Enabled = !prompt.IsArchived;
        _usePromptButton.Enabled = !prompt.IsArchived;
        _editPromptButton.Enabled = !prompt.IsArchived;
        _versionsPromptButton.Enabled = _promptVersionService is not null;
        _deletePromptButton.Text = prompt.IsArchived ? "Wiederherstellen" : "Archivieren";
        _deletePromptButton.Enabled = true;
        _detailStatusLabel.Text = $"Erstellt am {prompt.CreatedAt:dd.MM.yyyy HH:mm} · ID: {prompt.Id}";

        UpdateStatusMessage($"Prompt ausgewählt: {prompt.Title}");
    }

    /// <summary>
    /// Baut den Detailtext aus Beschreibung und V1-Metadaten.
    /// </summary>
    private static string BuildPromptDescriptionAndMetadataText(Prompt prompt)
    {
        static string ValueOrDash(string? value) => string.IsNullOrWhiteSpace(value) ? "-" : value.Trim();

        /*
         * WinForms-TextBoxen sind bei Zeilenumbrüchen auf Windows am zuverlässigsten,
         * wenn wir explizit Environment.NewLine verwenden. Dadurch wird die Detailbox
         * nicht mehr als schwer lesbare Ein-Zeilen-Kette angezeigt.
         */
        return string.Join(Environment.NewLine, new[]
        {
            "Beschreibung:",
            ValueOrDash(prompt.Description),
            string.Empty,
            "Erwartetes Ergebnis:",
            ValueOrDash(prompt.ExpectedResult),
            string.Empty,
            $"Sprache: {ValueOrDash(prompt.Language)}",
            $"Stilprofil: {ValueOrDash(prompt.StyleProfile)}",
            $"Quelle: {ValueOrDash(prompt.Source)}",
            string.Empty,
            "Archiv:",
            $"Archiviert: {(prompt.IsArchived ? "Ja" : "Nein")}",
            $"Archiviert am: {(prompt.ArchivedAt is null ? "-" : prompt.ArchivedAt.Value.ToString("dd.MM.yyyy HH:mm"))}",
            string.Empty,
            "Nutzung:",
            $"Favorit: {(prompt.IsFavorite ? "Ja" : "Nein")}",
            $"Verwendet: {prompt.UsageCount}x",
            $"Zuletzt verwendet: {(prompt.LastUsedAt is null ? "Noch nie" : prompt.LastUsedAt.Value.ToString("dd.MM.yyyy HH:mm"))}",
            string.Empty,
            "Notizen:",
            ValueOrDash(prompt.Notes)
        });
    }

    /// <summary>
    /// Leert die Detailansicht.
    /// </summary>
    private void ClearPromptDetails()
    {
        if (_promptTitleLabel is not null) _promptTitleLabel.Text = "Kein Prompt ausgewählt";
        if (_promptMetaLabel is not null) _promptMetaLabel.Text = "Wähle einen Prompt aus der Liste.";
        if (_promptTagsLabel is not null) _promptTagsLabel.Text = "Tags: -";
        if (_promptContentTextBox is not null) _promptContentTextBox.Text = string.Empty;
        if (_promptDescriptionTextBox is not null) _promptDescriptionTextBox.Text = string.Empty;
        if (_copyPromptButton is not null) _copyPromptButton.Enabled = false;
        if (_usePromptButton is not null) _usePromptButton.Enabled = false;
        if (_editPromptButton is not null) _editPromptButton.Enabled = false;
        if (_versionsPromptButton is not null) _versionsPromptButton.Enabled = false;
        if (_deletePromptButton is not null) { _deletePromptButton.Text = "Archivieren"; _deletePromptButton.Enabled = false; }
        if (_detailStatusLabel is not null) _detailStatusLabel.Text = "Kein Prompt ausgewählt.";
    }

    /// <summary>
    /// Kopiert den Rohprompt in die Zwischenablage.
    /// </summary>
    private void CopySelectedPromptToClipboard()
    {
        if (GetSelectedPrompt() is not Prompt selectedPrompt)
        {
            _logger.Warning("Copy prompt requested but no prompt is selected.");
            UpdateStatusMessage("Kein Prompt ausgewählt.");
            return;
        }

        if (selectedPrompt.IsArchived)
        {
            _logger.Warning($"Raw copy requested for archived prompt: {selectedPrompt.Id}");
            UpdateStatusMessage("Archivierte Prompts bitte zuerst wiederherstellen.");
            MessageBox.Show(this, "Archivierte Prompts werden nicht als aktive Arbeitsfassung kopiert. Bitte stelle den Prompt zuerst wieder her.", "Prompt ist archiviert", MessageBoxButtons.OK, MessageBoxIcon.Information);
            return;
        }

        Clipboard.SetText(selectedPrompt.Content);
        RegisterPromptUsageFromUi(selectedPrompt);

        _logger.Info($"Raw prompt copied to clipboard: {selectedPrompt.Id}");
        UpdateStatusMessage($"Rohprompt in Zwischenablage kopiert: {selectedPrompt.Title}");

        if (_detailStatusLabel is not null)
        {
            _detailStatusLabel.Text = $"Rohprompt kopiert: {DateTime.Now:HH:mm:ss}";
        }
    }

    /// <summary>
    /// Ermittelt einen Projektnamen.
    /// </summary>
    private string GetProjectName(Guid? projectId)
    {
        if (projectId is null || _projectService is null)
        {
            return "-";
        }

        PromptProject? project = _projectService.FindProject(projectId.Value);
        return project?.Name ?? "(unbekannt)";
    }

    /// <summary>
    /// Ermittelt den Namen eines Projektbereichs.
    /// </summary>
    private string GetProjectAreaName(Guid? projectAreaId)
    {
        if (projectAreaId is null || _projectAreaService is null)
        {
            return "-";
        }

        ProjectArea? area = _projectAreaService.FindArea(projectAreaId.Value);
        return area?.Name ?? "(unbekannt)";
    }

    /// <summary>
    /// Ermittelt einen Kategorienamen.
    /// </summary>
    private string GetCategoryName(Guid? categoryId)
    {
        if (categoryId is null || _categoryService is null)
        {
            return "-";
        }

        PromptCategory? category = _categoryService.FindCategory(categoryId.Value);
        return category?.Name ?? "(unbekannt)";
    }

    /// <summary>
    /// Baut den Sidebar-Überblick.
    /// </summary>
    private string BuildSidebarSummaryText()
    {
        if (_projectService is null || _promptService is null)
        {
            return """
            KURZÜBERSICHT

            Services nicht verfügbar
            """;
        }

        int projectCount = _projectService.GetAllProjects().Count;
        int promptCount = _promptService.GetAllPrompts().Count;
        int archivedPromptCount = _promptService.GetAllPrompts(includeArchived: true).Count(prompt => prompt.IsArchived);
        int tagCount = _tagService?.GetTagUsages().Count ?? _promptService.GetAllTagNames().Count;
        int categoryCount = _categoryService?.GetAllCategories().Count ?? 0;
        int versionCount = _promptVersionService?.GetAllVersions().Count ?? 0;
        int projectAreaCount = _projectAreaService?.GetAllAreas().Count ?? 0;

        return $"""
        KURZÜBERSICHT

        Prompts       {promptCount}
        Archiviert    {archivedPromptCount}
        Projekte      {projectCount}
        Kategorien    {categoryCount}
        Tags          {tagCount}
        Versionen     {versionCount}
        Bereiche      {projectAreaCount}
        Speicherung   JSON lokal
        """;
    }

    /// <summary>
    /// Baut Statuspfade.
    /// </summary>
    private string BuildStatusDataText()
    {
        return $"Daten: {_startupReport.DataDirectory}    Log: {_currentApplicationLogFilePath}";
    }

    /// <summary>
    /// Aktualisiert Sidebar und Statuspfad.
    /// </summary>
    private void UpdateSummaryAndStatusData()
    {
        if (_sidebarSummaryLabel is not null)
        {
            _sidebarSummaryLabel.Text = BuildSidebarSummaryText();
        }

        if (_statusDataLabel is not null)
        {
            _statusDataLabel.Text = BuildStatusDataText();
        }
    }

    /// <summary>
    /// Aktualisiert die Statusmeldung.
    /// </summary>
    private void UpdateStatusMessage(string message)
    {
        if (_statusMessageLabel is not null)
        {
            _statusMessageLabel.Text = message;
        }
    }

    /// <summary>
    /// Exportiert den vollständigen lokalen JSON-Datenbestand als ZIP.
    /// </summary>
    private void ExportFullBackup()
    {
        _logger.Info("Full backup export requested.");

        if (_projectService is null || _promptService is null || _categoryService is null)
        {
            UpdateStatusMessage("Backup-Export nicht möglich: Services fehlen.");
            return;
        }

        using var dialog = new SaveFileDialog
        {
            Title = "Vollständiges Prompt-Manager-Backup exportieren",
            Filter = "ZIP Backup (*.zip)|*.zip",
            FileName = PromptExportFileNameBuilder.BuildBackupFileName(DateTimeOffset.Now),
            InitialDirectory = _startupReport.ExportDirectory
        };

        if (dialog.ShowDialog(this) != DialogResult.OK)
        {
            _logger.Info("Full backup export cancelled.");
            UpdateStatusMessage("Backup-Export abgebrochen.");
            return;
        }

        try
        {
            var manifest = new PromptBackupManifest
            {
                ExportedAt = DateTimeOffset.Now,
                ProjectCount = _projectService.GetAllProjects().Count,
                PromptCount = _promptService.GetAllPrompts(includeArchived: true).Count,
                CategoryCount = _categoryService.GetAllCategories().Count,
                VersionCount = _promptVersionService?.GetAllVersions().Count ?? 0,
                ProjectChecklistItemCount = _projectPromptChecklistService?.GetAllItems().Count ?? 0,
                PromptSetCount = _promptSetService?.GetAllSets(includeArchived: true).Count ?? 0,
                ProjectAreaCount = _projectAreaService?.GetAllAreas(includeArchived: true).Count ?? 0
            };

            var backupService = new PromptBackupService(_logger);
            backupService.CreateBackup(_startupReport.DataDirectory, dialog.FileName, manifest);

            UpdateStatusMessage("Backup exportiert: " + dialog.FileName);
            MessageBox.Show(this, "Das Backup wurde erfolgreich exportiert.", "Backup exportiert", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }
        catch (Exception exception)
        {
            _logger.Error("Full backup export failed.", exception);
            MessageBox.Show(this, exception.Message, "Backup konnte nicht exportiert werden", MessageBoxButtons.OK, MessageBoxIcon.Warning);
        }
    }

    /// <summary>
    /// Analysiert und importiert ein versioniertes SASD-Promptpaket.
    /// </summary>
    private void ImportSasdPromptPackage()
    {
        if (_promptService is null || _categoryService is null)
        {
            UpdateStatusMessage("Promptpaket-Import ist nicht verfügbar: erforderliche Services fehlen.");
            return;
        }

        using var dialog = new SasdPromptPackageImportDialog(
            _promptService,
            _categoryService,
            _logger,
            _startupReport.DataDirectory);

        if (dialog.ShowDialog(this) != DialogResult.OK || !dialog.ImportCompleted)
        {
            UpdateStatusMessage("SASD-Promptpaket-Import geschlossen.");
            return;
        }

        RefreshFilterCategories();
        ResetFiltersWithoutRefreshing();
        RefreshPromptListForSelectedProject();
        SasdPromptPackageImportResult? result = dialog.ImportResult;
        UpdateStatusMessage(result is null
            ? "SASD-Promptpaket importiert."
            : $"SASD-Promptpaket importiert: {result.Created} neu, {result.Updated} aktualisiert, {result.Skipped} übersprungen.");
    }

    /// <summary>
    /// Importiert ein vollständiges Backup-ZIP.
    /// </summary>
    /// <remarks>
    /// Der Import ersetzt die lokalen JSON-Dateien. Vorher wird durch den BackupService
    /// automatisch ein Sicherheitsbackup des aktuellen Datenstands erzeugt.
    /// </remarks>
    private void ImportBackup()
    {
        _logger.Info("Backup import requested.");

        using var dialog = new OpenFileDialog
        {
            Title = "Prompt-Manager-Backup importieren",
            Filter = "ZIP Backup (*.zip)|*.zip"
        };

        if (dialog.ShowDialog(this) != DialogResult.OK)
        {
            _logger.Info("Backup import cancelled.");
            UpdateStatusMessage("Backup-Import abgebrochen.");
            return;
        }

        DialogResult confirmation = MessageBox.Show(
            this,
            "Der Import ersetzt die aktuellen lokalen Daten.\n\nVorher wird automatisch ein Sicherheitsbackup erstellt.\n\nFortfahren?",
            "Backup importieren",
            MessageBoxButtons.YesNo,
            MessageBoxIcon.Warning,
            MessageBoxDefaultButton.Button2);

        if (confirmation != DialogResult.Yes)
        {
            _logger.Info("Backup import rejected by user.");
            UpdateStatusMessage("Backup-Import abgebrochen.");
            return;
        }

        try
        {
            var backupService = new PromptBackupService(_logger);
            BackupImportResult result = backupService.ImportBackup(dialog.FileName, _startupReport.DataDirectory);

            UpdateStatusMessage("Backup importiert. Neustart erforderlich.");

            DialogResult restartResult = MessageBox.Show(
                this,
                "Das Backup wurde importiert.\n\n" +
                "Ein Sicherheitsbackup wurde erstellt:\n" +
                result.SafetyBackupPath + "\n\n" +
                "Die Anwendung muss neu gestartet werden, damit alle Daten sauber neu geladen werden.\n\n" +
                "Möchtest du die Anwendung jetzt schließen?",
                "Backup importiert - Neustart erforderlich",
                MessageBoxButtons.YesNo,
                MessageBoxIcon.Information,
                MessageBoxDefaultButton.Button1);

            if (restartResult == DialogResult.Yes)
            {
                _logger.Info("Application close requested after successful backup import.");
                Close();
            }
        }
        catch (Exception exception)
        {
            _logger.Error("Backup import failed.", exception);
            MessageBox.Show(this, exception.Message, "Backup konnte nicht importiert werden", MessageBoxButtons.OK, MessageBoxIcon.Warning);
        }
    }

    /// <summary>
    /// Exportiert den ausgewählten Prompt als Markdown-Datei.
    /// </summary>
    private void ExportSelectedPromptAsMarkdown()
    {
        _logger.Info("Prompt markdown export requested.");

        if (GetSelectedPrompt() is not Prompt selectedPrompt)
        {
            UpdateStatusMessage("Kein Prompt für den Markdown-Export ausgewählt.");
            MessageBox.Show(this, "Bitte wähle zuerst einen Prompt aus.", "Markdown-Export", MessageBoxButtons.OK, MessageBoxIcon.Information);
            return;
        }

        using var dialog = new SaveFileDialog
        {
            Title = "Prompt als Markdown exportieren",
            Filter = "Markdown (*.md)|*.md",
            FileName = PromptExportFileNameBuilder.BuildPromptMarkdownFileName(selectedPrompt.Title),
            InitialDirectory = _startupReport.ExportDirectory
        };

        if (dialog.ShowDialog(this) != DialogResult.OK)
        {
            _logger.Info("Prompt markdown export cancelled.");
            UpdateStatusMessage("Markdown-Export abgebrochen.");
            return;
        }

        try
        {
            var exporter = new PromptMarkdownExporter();
            string markdown = exporter.ExportPrompt(
                selectedPrompt,
                GetProjectName(selectedPrompt.ProjectId),
                GetCategoryName(selectedPrompt.CategoryId));

            File.WriteAllText(dialog.FileName, markdown);

            _logger.Info($"Prompt exported as markdown: {selectedPrompt.Id} -> {dialog.FileName}");
            UpdateStatusMessage("Prompt als Markdown exportiert: " + dialog.FileName);
        }
        catch (Exception exception)
        {
            _logger.Error("Prompt markdown export failed.", exception);
            MessageBox.Show(this, exception.Message, "Prompt konnte nicht exportiert werden", MessageBoxButtons.OK, MessageBoxIcon.Warning);
        }
    }

    /// <summary>
    /// Exportiert alle Prompts des ausgewählten Projekts als Markdown-Datei.
    /// </summary>
    private void ExportSelectedProjectAsMarkdown()
    {
        _logger.Info("Project markdown export requested.");

        if (_promptService is null)
        {
            UpdateStatusMessage("Projekt-Export nicht möglich: PromptService fehlt.");
            return;
        }

        PromptProject? selectedProject = GetSelectedProject();

        if (selectedProject is null)
        {
            UpdateStatusMessage("Kein Projekt für den Markdown-Export ausgewählt.");
            MessageBox.Show(this, "Bitte wähle zuerst ein konkretes Projekt aus. Die Ansicht 'Alle Prompts' ist kein einzelnes Projekt.", "Markdown-Export", MessageBoxButtons.OK, MessageBoxIcon.Information);
            return;
        }

        IReadOnlyList<Prompt> prompts = _promptService.GetPromptsByProject(selectedProject.Id);

        using var dialog = new SaveFileDialog
        {
            Title = "Projekt-Prompts als Markdown exportieren",
            Filter = "Markdown (*.md)|*.md",
            FileName = PromptExportFileNameBuilder.BuildProjectMarkdownFileName(selectedProject.Name),
            InitialDirectory = _startupReport.ExportDirectory
        };

        if (dialog.ShowDialog(this) != DialogResult.OK)
        {
            _logger.Info("Project markdown export cancelled.");
            UpdateStatusMessage("Projekt-Markdown-Export abgebrochen.");
            return;
        }

        try
        {
            var exporter = new PromptMarkdownExporter();
            string markdown = exporter.ExportPromptCollection(
                selectedProject.Name,
                prompts,
                GetProjectName,
                GetCategoryName);

            File.WriteAllText(dialog.FileName, markdown);

            _logger.Info($"Project exported as markdown: {selectedProject.Id} -> {dialog.FileName}");
            UpdateStatusMessage("Projekt als Markdown exportiert: " + dialog.FileName);
        }
        catch (Exception exception)
        {
            _logger.Error("Project markdown export failed.", exception);
            MessageBox.Show(this, exception.Message, "Projekt konnte nicht exportiert werden", MessageBoxButtons.OK, MessageBoxIcon.Warning);
        }
    }

    /// <summary>
    /// Baut den Diagnosetext.
    /// </summary>
    private string BuildStartupText()
    {
        string applicationLogText = string.IsNullOrWhiteSpace(_currentApplicationLogFilePath)
            ? "(nicht verfügbar)"
            : _currentApplicationLogFilePath;

        return $"""
        Application : {_startupReport.ApplicationName}
        Version     : {_startupReport.Version}
        Started at  : {_startupReport.StartedAt:yyyy-MM-dd HH:mm:ss zzz}

        Workspace root:
        {_startupReport.WorkspaceRoot}

        Data directory:
        {_startupReport.DataDirectory}

        Log directory:
        {_startupReport.LogDirectory}

        Export directory:
        {_startupReport.ExportDirectory}

        Startup log file:
        {_startupLogFilePath}

        Current application log file:
        {applicationLogText}
        """;
    }

    /// <summary>
    /// Zeigt Startup-Diagnose.
    /// </summary>
    private void ShowStartupDiagnosticsDialog()
    {
        _logger.Info("Startup diagnostics dialog opened.");

        MessageBox.Show(this, BuildStartupText(), "SASD Prompt Manager - Startup-Diagnose", MessageBoxButtons.OK, MessageBoxIcon.Information);
    }

    /// <summary>
    /// Öffnet das Datenverzeichnis.
    /// </summary>
    private void OpenDataDirectory()
    {
        _logger.Info("Open data directory requested.");

        try
        {
            Directory.CreateDirectory(_startupReport.DataDirectory);

            System.Diagnostics.Process.Start(new System.Diagnostics.ProcessStartInfo
            {
                FileName = _startupReport.DataDirectory,
                UseShellExecute = true
            });

            UpdateStatusMessage("Datenverzeichnis geöffnet.");
        }
        catch (Exception exception)
        {
            _logger.Error("Could not open data directory.", exception);
            MessageBox.Show(this, "Das Datenverzeichnis konnte nicht geöffnet werden. Details stehen im Log.", "SASD Prompt Manager - Diagnose", MessageBoxButtons.OK, MessageBoxIcon.Warning);
        }
    }

    /// <summary>
    /// Kopiert den Datenpfad.
    /// </summary>
    private void CopyDataPathToClipboard()
    {
        _logger.Info("Copy data path requested.");
        Clipboard.SetText(_startupReport.DataDirectory);
        _logger.Info($"Data path copied to clipboard: {_startupReport.DataDirectory}");
        UpdateStatusMessage("Datenpfad in Zwischenablage kopiert.");
    }

    /// <summary>
    /// Öffnet das Logverzeichnis.
    /// </summary>
    private void OpenLogDirectory()
    {
        _logger.Info("Open log directory requested.");

        try
        {
            string logDirectory = _startupReport.LogDirectory;

            if (!Directory.Exists(logDirectory))
            {
                Directory.CreateDirectory(logDirectory);
                _logger.Warning($"Log directory did not exist and was created: {logDirectory}");
            }

            System.Diagnostics.Process.Start(new System.Diagnostics.ProcessStartInfo
            {
                FileName = logDirectory,
                UseShellExecute = true
            });

            UpdateStatusMessage("Logverzeichnis geöffnet.");
        }
        catch (Exception exception)
        {
            _logger.Error("Could not open log directory.", exception);
            MessageBox.Show(this, "Das Logverzeichnis konnte nicht geöffnet werden. Details stehen im Log.", "SASD Prompt Manager - Diagnose", MessageBoxButtons.OK, MessageBoxIcon.Warning);
        }
    }

    /// <summary>
    /// Kopiert den Logpfad.
    /// </summary>
    private void CopyLogPathToClipboard()
    {
        _logger.Info("Copy log path requested.");

        string pathToCopy = string.IsNullOrWhiteSpace(_currentApplicationLogFilePath)
            ? _startupReport.LogDirectory
            : _currentApplicationLogFilePath;

        Clipboard.SetText(pathToCopy);

        _logger.Info($"Log path copied to clipboard: {pathToCopy}");
        UpdateStatusMessage("Logpfad in Zwischenablage kopiert.");
    }

    /// <summary>
    /// Zeigt Info-Dialog.
    /// </summary>
    private void ShowAboutDialog()
    {
        _logger.Info("About dialog opened.");

        MessageBox.Show(
            this,
            "SASD Prompt Manager\n\nPhase 25 ergänzt den kontrollierten Import versionierter SASD-Promptpakete.",
            "Über SASD Prompt Manager",
            MessageBoxButtons.OK,
            MessageBoxIcon.Information);
    }
}
