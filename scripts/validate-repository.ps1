[CmdletBinding()]
param(
    [string]$OutputDirectory = "artifacts/quality-gates/local"
)

$ErrorActionPreference = "Stop"
$RepositoryRoot = Split-Path -Parent $PSScriptRoot
Push-Location $RepositoryRoot
try {
    $env:PYTHONUTF8 = "1"
    python tooling/run-quality-gates.py --output-dir $OutputDirectory
    if ($LASTEXITCODE -ne 0) {
        throw "SASD repository quality gates failed with exit code $LASTEXITCODE."
    }
}
finally {
    Pop-Location
}
