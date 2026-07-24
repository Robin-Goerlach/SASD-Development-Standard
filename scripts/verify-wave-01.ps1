[CmdletBinding()]
param(
    [ValidateSet('Debug', 'Release')]
    [string]$Configuration = 'Release',

    [string]$EvidenceRoot,

    [switch]$KeepSelfCheckDatabase
)

$ErrorActionPreference = 'Stop'
$repositoryRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repositoryRoot

if ([string]::IsNullOrWhiteSpace($EvidenceRoot)) {
    $timestamp = Get-Date -Format 'yyyyMMdd-HHmmss'
    $EvidenceRoot = Join-Path $repositoryRoot "verification-results\wave-01-$timestamp"
}

$EvidenceRoot = [System.IO.Path]::GetFullPath($EvidenceRoot)
$logsDirectory = Join-Path $EvidenceRoot 'logs'
$testResultsDirectory = Join-Path $EvidenceRoot 'test-results'
$publishDirectory = Join-Path $EvidenceRoot 'publish'
$selfCheckReport = Join-Path $EvidenceRoot 'self-check-report.json'
$summaryJson = Join-Path $EvidenceRoot 'verification-summary.json'
$summaryMarkdown = Join-Path $EvidenceRoot 'verification-summary.md'

New-Item -ItemType Directory -Path $logsDirectory -Force | Out-Null
New-Item -ItemType Directory -Path $testResultsDirectory -Force | Out-Null
New-Item -ItemType Directory -Path $publishDirectory -Force | Out-Null

$startedUtc = (Get-Date).ToUniversalTime()
$steps = [System.Collections.Generic.List[object]]::new()

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

    $steps.Add([ordered]@{
        name = $Name
        status = if ($exitCode -eq 0) { 'Passed' } else { 'Failed' }
        exitCode = $exitCode
        durationSeconds = $duration
        log = [System.IO.Path]::GetRelativePath($EvidenceRoot, $logPath)
    })

    if ($exitCode -ne 0) {
        throw "$FilePath $($Arguments -join ' ') failed with exit code $exitCode. See $logPath"
    }
}

$verificationStatus = 'Failed'
$errorMessage = $null

try {
    Invoke-RecordedCommand -Name 'dotnet-info' -FilePath 'dotnet' -Arguments @('--info')
    Invoke-RecordedCommand -Name 'restore' -FilePath 'dotnet' -Arguments @('restore', '.\TaskHostLocal.sln')
    Invoke-RecordedCommand -Name 'build' -FilePath 'dotnet' -Arguments @(
        'build',
        '.\TaskHostLocal.sln',
        '--configuration', $Configuration,
        '--no-restore'
    )
    Invoke-RecordedCommand -Name 'test' -FilePath 'dotnet' -Arguments @(
        'test',
        '.\TaskHostLocal.sln',
        '--configuration', $Configuration,
        '--no-build',
        '--logger', 'trx;LogFileName=taskhost-local-tests.trx',
        '--collect', 'XPlat Code Coverage',
        '--results-directory', $testResultsDirectory
    )
    Invoke-RecordedCommand -Name 'nuget-audit' -FilePath 'dotnet' -Arguments @(
        'list',
        '.\TaskHostLocal.sln',
        'package',
        '--vulnerable',
        '--include-transitive'
    )
    Invoke-RecordedCommand -Name 'publish' -FilePath 'dotnet' -Arguments @(
        'publish',
        '.\TaskHostLocal.WinForms\TaskHostLocal.WinForms.csproj',
        '--configuration', $Configuration,
        '--no-build',
        '--output', $publishDirectory
    )

    $executable = Join-Path $publishDirectory 'TaskHostLocal.WinForms.exe'
    if (-not (Test-Path $executable)) {
        throw "Published executable not found: $executable"
    }

    $selfCheckArguments = @('--self-check', '--report', $selfCheckReport)
    if ($KeepSelfCheckDatabase) {
        $selfCheckArguments += '--keep-database'
    }

    Invoke-RecordedCommand -Name 'headless-self-check' -FilePath $executable -Arguments $selfCheckArguments

    $selfCheck = Get-Content $selfCheckReport -Raw | ConvertFrom-Json
    if (-not $selfCheck.success) {
        throw 'The headless TaskHost Local self-check reported failure.'
    }

    $verificationStatus = 'Passed'
}
catch {
    $errorMessage = $_.Exception.Message
    Write-Host $errorMessage -ForegroundColor Red
}
finally {
    $completedUtc = (Get-Date).ToUniversalTime()
    $commitSha = $null
    $repositoryDirty = $null

    if (Get-Command git -ErrorAction SilentlyContinue) {
        $commitSha = (& git rev-parse HEAD 2>$null)
        $repositoryDirty = -not [string]::IsNullOrWhiteSpace((& git status --porcelain 2>$null))
    }

    $summary = [ordered]@{
        schemaVersion = '1.0'
        wave = 'Wave 01'
        automatedVerificationStatus = $verificationStatus
        manualSmokeTestStatus = 'Pending'
        overallCloseoutStatus = 'Pending'
        startedUtc = $startedUtc.ToString('O')
        completedUtc = $completedUtc.ToString('O')
        configuration = $Configuration
        commitSha = $commitSha
        repositoryDirty = $repositoryDirty
        operatingSystem = [System.Runtime.InteropServices.RuntimeInformation]::OSDescription
        processArchitecture = [System.Runtime.InteropServices.RuntimeInformation]::ProcessArchitecture.ToString()
        evidenceRoot = $EvidenceRoot
        steps = $steps
        errorMessage = $errorMessage
    }

    $summary | ConvertTo-Json -Depth 8 | Set-Content -Path $summaryJson -Encoding utf8

    $markdown = @(
        '# TaskHost Local – Wave 01 Verification Summary',
        '',
        "- Automated verification: **$verificationStatus**",
        '- Manual Windows smoke test: **Pending**',
        '- Overall closeout: **Pending**',
        "- Commit: ``$commitSha``",
        "- Repository dirty during run: ``$repositoryDirty``",
        "- Started UTC: ``$($startedUtc.ToString('O'))``",
        "- Completed UTC: ``$($completedUtc.ToString('O'))``",
        '',
        '## Automated steps',
        '',
        '| Step | Status | Exit code | Seconds |',
        '|---|---|---:|---:|'
    )

    foreach ($step in $steps) {
        $markdown += "| $($step.name) | $($step.status) | $($step.exitCode) | $($step.durationSeconds) |"
    }

    $markdown += @(
        '',
        '## Remaining evidence',
        '',
        '- Execute `docs/100_Manual_Test_Plan.md` on Windows.',
        '- Confirm the GitHub Actions run for the same commit.',
        '- Finalize the wave only with `scripts/finalize-wave-01.ps1`.',
        '',
        '> This report deliberately does not mark Wave 01 complete.'
    )

    $markdown -join [Environment]::NewLine | Set-Content -Path $summaryMarkdown -Encoding utf8

    Write-Host "Evidence directory: $EvidenceRoot" -ForegroundColor Yellow
    Write-Host "Automated verification: $verificationStatus" -ForegroundColor $(if ($verificationStatus -eq 'Passed') { 'Green' } else { 'Red' })
    Write-Host 'Manual smoke test and CI confirmation are still required.' -ForegroundColor Yellow
}

if ($verificationStatus -ne 'Passed') {
    exit 1
}
