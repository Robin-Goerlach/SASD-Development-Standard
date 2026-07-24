[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [switch]$SkipValidation
)

$ErrorActionPreference = 'Stop'
$repositoryRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repositoryRoot

$requiredMarkers = @(
    'README.md',
    'docs\00-foundation\PROJECT-CHARTER.md',
    'docs\40-governance\NORMATIVE-LANGUAGE.md',
    'tooling\run-quality-gates.py'
)
foreach ($marker in $requiredMarkers) {
    if (-not (Test-Path (Join-Path $repositoryRoot $marker))) {
        throw "This does not look like the SASD Development Standard repository. Missing: $marker"
    }
}

$remote = (& git config --get remote.origin.url 2>$null)
if ($LASTEXITCODE -eq 0 -and -not [string]::IsNullOrWhiteSpace($remote)) {
    if ($remote -notmatch '(?i)Robin-Goerlach[/:]SASD-Development-Standard(?:\.git)?$') {
        throw "Unexpected origin remote: $remote"
    }
}

$foreignPaths = @(
    'SASD-Development-Standard',
    'TaskHostLocal.Tests',
    'TaskHostLocal.WinForms',
    'TaskHostLocal.sln',
    'WAVE-01-UPDATE-MANIFEST.md',
    'WAVE-01-VERIFICATION-UPDATE-MANIFEST.md',
    'Directory.Build.props',
    'Directory.Packages.props',
    'global.json',
    '.github\workflows\ci.yml',
    'docs\080_Known_Issues.md',
    'docs\100_Manual_Test_Plan.md',
    'docs\110_SASD_Alignment.md',
    'docs\120_Wave_01_Review.md',
    'docs\130_Build_and_Test.md',
    'docs\140_Migration_Notes.md',
    'docs\150_Wave_01_Verification.md',
    'docs\160_Wave_01_Closeout.md',
    'docs\170_CI_Evidence_Guide.md',
    'docs\adr',
    'docs\evidence',
    'scripts\backup-taskhost-data.ps1',
    'scripts\finalize-wave-01.ps1',
    'scripts\verify-wave-01.ps1',
    'tooling\validate-wave-01.py'
)

$removed = @()
foreach ($relativePath in $foreignPaths) {
    $fullPath = Join-Path $repositoryRoot $relativePath
    if (Test-Path $fullPath) {
        if ($PSCmdlet.ShouldProcess($relativePath, 'Remove misplaced TaskHost or nested-repository content')) {
            Remove-Item -LiteralPath $fullPath -Recurse -Force
            $removed += $relativePath
        }
    }
}

Write-Host "Removed $($removed.Count) misplaced paths." -ForegroundColor Green
foreach ($item in $removed) {
    Write-Host "  - $item"
}

& python tooling/generate-repository-manifest.py --write
if ($LASTEXITCODE -ne 0) {
    throw 'Repository manifest generation failed.'
}

if (-not $SkipValidation) {
    & python tooling/run-quality-gates.py --output-dir artifacts/quality-gates/boundary-repair
    if ($LASTEXITCODE -ne 0) {
        throw 'Repository quality gates still fail after the boundary repair.'
    }
}

Write-Host ''
Write-Host 'Repository boundary repair completed.' -ForegroundColor Green
Write-Host 'Review the deletions with: git status --short'
Write-Host 'Commit deletions and additions with: git add -A'
