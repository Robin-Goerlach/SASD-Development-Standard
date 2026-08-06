[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$TargetRepositoryRoot,

    [ValidateSet('Debug', 'Release')]
    [string]$Configuration = 'Release',

    [string]$EvidenceRoot
)

$ErrorActionPreference = 'Stop'
$standardRepositoryRoot = Split-Path -Parent $PSScriptRoot
$invocationRoot = (Get-Location).Path

function Resolve-AbsolutePath {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path,
        [Parameter(Mandatory = $true)]
        [string]$BasePath,
        [switch]$MustExist
    )

    $candidate = if ([System.IO.Path]::IsPathRooted($Path)) {
        $Path
    }
    else {
        Join-Path $BasePath $Path
    }

    $fullPath = [System.IO.Path]::GetFullPath($candidate)
    if ($MustExist -and -not (Test-Path -LiteralPath $fullPath)) {
        throw "Required path does not exist: $fullPath"
    }
    return $fullPath
}

$targetRoot = Resolve-AbsolutePath -Path $TargetRepositoryRoot -BasePath $invocationRoot -MustExist
if ([string]::IsNullOrWhiteSpace($EvidenceRoot)) {
    $timestamp = Get-Date -Format 'yyyyMMdd-HHmmss'
    $EvidenceRoot = Join-Path $invocationRoot "evidence/taskhost-local-$timestamp"
}
$evidenceRootAbsolute = Resolve-AbsolutePath -Path $EvidenceRoot -BasePath $invocationRoot
$logsDirectory = Join-Path $evidenceRootAbsolute 'logs'
$publishDirectory = Join-Path $evidenceRootAbsolute 'publish'
$summaryJson = Join-Path $evidenceRootAbsolute 'verification-summary.json'
$summaryMarkdown = Join-Path $evidenceRootAbsolute 'verification-summary.md'

New-Item -ItemType Directory -Path $logsDirectory -Force | Out-Null
New-Item -ItemType Directory -Path $publishDirectory -Force | Out-Null

$solution = Join-Path $targetRoot 'TaskHostLocal.sln'
$productProject = Join-Path $targetRoot 'TaskHostLocal.WinForms/TaskHostLocal.WinForms.csproj'
foreach ($required in @($solution, $productProject)) {
    if (-not (Test-Path -LiteralPath $required -PathType Leaf)) {
        throw "Required TaskHost file is missing: $required"
    }
}

$startedUtc = (Get-Date).ToUniversalTime()
$steps = [System.Collections.Generic.List[object]]::new()
$verificationStatus = 'Failed'
$errorMessage = $null

function Get-GitValue {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Repository,
        [Parameter(Mandatory = $true)]
        [string[]]$Arguments
    )

    $value = & git -C $Repository @Arguments 2>$null
    if ($LASTEXITCODE -ne 0) {
        return $null
    }
    return ($value | Out-String).Trim()
}

function Add-InformationalStep {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Name,
        [Parameter(Mandatory = $true)]
        [string]$Status,
        [Parameter(Mandatory = $true)]
        [string]$Message
    )

    $steps.Add([ordered]@{
        name = $Name
        status = $Status
        exitCode = $null
        durationSeconds = 0
        log = $null
        message = $Message
    })
}

function Invoke-RecordedCommand {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Name,
        [Parameter(Mandatory = $true)]
        [string]$FilePath,
        [Parameter(Mandatory = $true)]
        [string[]]$Arguments
    )

    $logPath = Join-Path $logsDirectory "$Name.log"
    $stepStarted = Get-Date

    Write-Host "== $Name ==" -ForegroundColor Cyan
    Write-Host "$FilePath $($Arguments -join ' ')"

    & $FilePath @Arguments 2>&1 | Tee-Object -FilePath $logPath
    $exitCode = $LASTEXITCODE
    $duration = [math]::Round(((Get-Date) - $stepStarted).TotalSeconds, 3)
    $relativeLog = [System.IO.Path]::GetRelativePath($evidenceRootAbsolute, $logPath)

    $steps.Add([ordered]@{
        name = $Name
        status = if ($exitCode -eq 0) { 'Passed' } else { 'Failed' }
        exitCode = $exitCode
        durationSeconds = $duration
        log = $relativeLog
        message = $null
    })

    if ($exitCode -ne 0) {
        throw "$FilePath $($Arguments -join ' ') failed with exit code $exitCode. See $logPath"
    }
}

$standardCommit = Get-GitValue -Repository $standardRepositoryRoot -Arguments @('rev-parse', 'HEAD')
$targetCommit = Get-GitValue -Repository $targetRoot -Arguments @('rev-parse', 'HEAD')
$targetOrigin = Get-GitValue -Repository $targetRoot -Arguments @('remote', 'get-url', 'origin')
$targetDirtyBeforeBuild = -not [string]::IsNullOrWhiteSpace(
    (Get-GitValue -Repository $targetRoot -Arguments @('status', '--porcelain'))
)

if ($targetCommit -notmatch '^[0-9a-f]{40}$') {
    throw 'The target checkout does not expose a full immutable Git commit.'
}
if ($targetDirtyBeforeBuild) {
    throw 'The target checkout is dirty before verification starts.'
}

try {
    Set-Location $targetRoot

    Invoke-RecordedCommand -Name 'dotnet-info' -FilePath 'dotnet' -Arguments @('--info')
    Invoke-RecordedCommand -Name 'restore' -FilePath 'dotnet' -Arguments @('restore', $solution)
    Invoke-RecordedCommand -Name 'build' -FilePath 'dotnet' -Arguments @(
        'build',
        $solution,
        '--configuration', $Configuration,
        '--no-restore'
    )

    $testProjects = @(
        Get-ChildItem -Path $targetRoot -Recurse -Filter '*.csproj' -File |
            Where-Object {
                $_.FullName -notmatch '[\\/](bin|obj)[\\/]' -and
                ($_.BaseName -match 'Tests?$' -or $_.DirectoryName -match '[\\/]tests?[\\/]')
            }
    )

    if ($testProjects.Count -gt 0) {
        Invoke-RecordedCommand -Name 'test' -FilePath 'dotnet' -Arguments @(
            'test',
            $solution,
            '--configuration', $Configuration,
            '--no-build'
        )
    }
    else {
        Add-InformationalStep -Name 'test' -Status 'NotAvailable' -Message `
            'No automated test project is present in the pinned target commit.'
    }

    Invoke-RecordedCommand -Name 'nuget-audit' -FilePath 'dotnet' -Arguments @(
        'list',
        $solution,
        'package',
        '--vulnerable',
        '--include-transitive'
    )

    Invoke-RecordedCommand -Name 'publish' -FilePath 'dotnet' -Arguments @(
        'publish',
        $productProject,
        '--configuration', $Configuration,
        '--no-build',
        '--output', $publishDirectory
    )

    $publishedExecutable = Join-Path $publishDirectory 'TaskHostLocal.WinForms.exe'
    if (-not (Test-Path -LiteralPath $publishedExecutable -PathType Leaf)) {
        throw "Published executable not found: $publishedExecutable"
    }

    $verificationStatus = 'Passed'
}
catch {
    $errorMessage = $_.Exception.Message
    Write-Host $errorMessage -ForegroundColor Red
}
finally {
    Set-Location $invocationRoot
    $completedUtc = (Get-Date).ToUniversalTime()

    $summary = [ordered]@{
        schemaVersion = '1.0'
        evidenceType = 'remote-reference-baseline'
        pilotId = 'SASD-PILOT-001'
        automatedBaselineStatus = $verificationStatus
        fullPilotVerificationStatus = 'Pending'
        manualWindowsSmokeTestStatus = 'Pending'
        standardRepository = 'Robin-Goerlach/SASD-Development-Standard'
        standardCommit = $standardCommit
        targetRepository = $targetOrigin
        targetCommit = $targetCommit
        targetDirtyBeforeBuild = $targetDirtyBeforeBuild
        configuration = $Configuration
        startedUtc = $startedUtc.ToString('O')
        completedUtc = $completedUtc.ToString('O')
        operatingSystem = [System.Runtime.InteropServices.RuntimeInformation]::OSDescription
        processArchitecture = [System.Runtime.InteropServices.RuntimeInformation]::ProcessArchitecture.ToString()
        evidenceRoot = $evidenceRootAbsolute
        steps = $steps
        errorMessage = $errorMessage
        limitations = @(
            'A successful result proves restore, build, available automated tests, NuGet audit execution, and publish for the pinned target commit.',
            'The pinned baseline currently has no required headless runtime self-check.',
            'A manual Windows smoke test remains required.',
            'This baseline result alone does not set pilot verification_state to Passed or close Wave 01.'
        )
    }

    $summary | ConvertTo-Json -Depth 10 | Set-Content -Path $summaryJson -Encoding utf8NoBOM

    $markdown = @(
        '# TaskHost Local – Exact-Commit Remote Baseline',
        '',
        "- Automated baseline: **$verificationStatus**",
        '- Full pilot verification: **Pending**',
        '- Manual Windows smoke test: **Pending**',
        "- Standard commit: ``$standardCommit``",
        "- Target repository: ``$targetOrigin``",
        "- Target commit: ``$targetCommit``",
        "- Target dirty before build: ``$targetDirtyBeforeBuild``",
        "- Configuration: ``$Configuration``",
        "- Started UTC: ``$($startedUtc.ToString('O'))``",
        "- Completed UTC: ``$($completedUtc.ToString('O'))``",
        '',
        '## Automated steps',
        '',
        '| Step | Status | Exit code | Seconds |',
        '|---|---|---:|---:|'
    )

    foreach ($step in $steps) {
        $exitCode = if ($null -eq $step.exitCode) { '—' } else { $step.exitCode }
        $markdown += "| $($step.name) | $($step.status) | $exitCode | $($step.durationSeconds) |"
    }

    $markdown += @(
        '',
        '## Evidence boundary',
        '',
        '- This run uses the public TaskHost repository and an immutable target commit.',
        '- A successful result establishes remote restore/build/audit/publish evidence.',
        '- Missing automated tests are reported as `NotAvailable`, not silently treated as passed.',
        '- Headless runtime verification and the manual Windows smoke test remain open.',
        '- The pilot manifest therefore remains `verification_state: Pending`.',
        ''
    )

    if (-not [string]::IsNullOrWhiteSpace($errorMessage)) {
        $markdown += @(
            '## Failure',
            '',
            '```text',
            $errorMessage,
            '```',
            ''
        )
    }

    $markdown -join [Environment]::NewLine |
        Set-Content -Path $summaryMarkdown -Encoding utf8NoBOM

    Write-Host "Evidence directory: $evidenceRootAbsolute" -ForegroundColor Yellow
    Write-Host "Automated baseline: $verificationStatus" -ForegroundColor $(
        if ($verificationStatus -eq 'Passed') { 'Green' } else { 'Red' }
    )
    Write-Host 'Full pilot verification and manual smoke testing remain pending.' -ForegroundColor Yellow
}

if ($verificationStatus -ne 'Passed') {
    exit 1
}
