[CmdletBinding()]
param(
    [string]$Configuration = "Release"
)

$ErrorActionPreference = "Stop"
$repositoryRoot = Split-Path -Parent $PSScriptRoot
Push-Location $repositoryRoot
try {
    Write-Host "[1/4] Static overlay validation"
    python .\tooling\validate-prompt-package-import.py

    Write-Host "[2/4] Restore"
    dotnet restore .\Sasd.PromptManager.sln

    Write-Host "[3/4] Build"
    dotnet build .\Sasd.PromptManager.sln --configuration $Configuration --no-restore

    Write-Host "[4/4] Tests"
    dotnet test .\Sasd.PromptManager.sln --configuration $Configuration --no-build
}
finally {
    Pop-Location
}
