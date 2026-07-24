[CmdletBinding()]
param(
    [ValidateSet('Debug', 'Release')]
    [string]$Configuration = 'Release'
)

$ErrorActionPreference = 'Stop'
$repositoryRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repositoryRoot

function Invoke-DotNet {
    param(
        [Parameter(Mandatory = $true)]
        [string[]]$Arguments
    )

    & dotnet @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "dotnet $($Arguments -join ' ') failed with exit code $LASTEXITCODE."
    }
}

Write-Host '== .NET information ==' -ForegroundColor Cyan
Invoke-DotNet -Arguments @('--info')

Write-Host '== Restore ==' -ForegroundColor Cyan
Invoke-DotNet -Arguments @('restore', '.\TaskHostLocal.sln')

Write-Host '== Build ==' -ForegroundColor Cyan
Invoke-DotNet -Arguments @(
    'build',
    '.\TaskHostLocal.sln',
    '--configuration',
    $Configuration,
    '--no-restore'
)

Write-Host '== Tests ==' -ForegroundColor Cyan
Invoke-DotNet -Arguments @(
    'test',
    '.\TaskHostLocal.sln',
    '--configuration',
    $Configuration,
    '--no-build',
    '--logger',
    'console;verbosity=normal',
    '--collect',
    'XPlat Code Coverage',
    '--results-directory',
    '.\TestResults'
)

Write-Host '== NuGet vulnerability audit ==' -ForegroundColor Cyan
Invoke-DotNet -Arguments @(
    'list',
    '.\TaskHostLocal.sln',
    'package',
    '--vulnerable',
    '--include-transitive'
)

Write-Host 'Wave 01 automated verification completed successfully.' -ForegroundColor Green
Write-Host 'Next: execute docs/100_Manual_Test_Plan.md on Windows.' -ForegroundColor Yellow
