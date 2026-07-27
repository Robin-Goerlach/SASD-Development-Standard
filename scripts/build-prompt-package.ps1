[CmdletBinding()]
param(
    [string]$OutputDirectory = "artifacts/prompt-packages"
)

$ErrorActionPreference = "Stop"
$RepositoryRoot = Split-Path -Parent $PSScriptRoot
Push-Location $RepositoryRoot
try {
    python tooling/validate-prompt-packages.py
    if ($LASTEXITCODE -ne 0) { throw "Prompt-package validation failed." }
    python tooling/build-prompt-package.py --output-dir $OutputDirectory --clean
    if ($LASTEXITCODE -ne 0) { throw "Prompt-package build failed." }
    python tooling/verify-prompt-package.py --directory $OutputDirectory
    if ($LASTEXITCODE -ne 0) { throw "Prompt-package verification failed." }
}
finally {
    Pop-Location
}
