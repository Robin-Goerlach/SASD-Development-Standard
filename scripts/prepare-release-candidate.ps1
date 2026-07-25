[CmdletBinding()]
param(
    [ValidateSet("preview", "release")]
    [string]$Mode = "preview",
    [string]$OutputDirectory = "artifacts/release-candidate"
)

$ErrorActionPreference = "Stop"
$RepositoryRoot = Split-Path -Parent $PSScriptRoot
Push-Location $RepositoryRoot
try {
    python tooling/run-quality-gates.py
    if ($LASTEXITCODE -ne 0) { throw "Repository quality gates failed." }

    if ($Mode -eq "release") {
        python tooling/generate-release-candidate-readiness.py --require-ready
        if ($LASTEXITCODE -ne 0) { throw "Release Candidate readiness is not satisfied." }
    }

    python tooling/build-release-candidate.py --mode $Mode --output-dir $OutputDirectory
    if ($LASTEXITCODE -ne 0) { throw "Release Candidate package build failed." }

    python tooling/verify-release-candidate.py --directory $OutputDirectory
    if ($LASTEXITCODE -ne 0) { throw "Release Candidate package verification failed." }
}
finally {
    Pop-Location
}
