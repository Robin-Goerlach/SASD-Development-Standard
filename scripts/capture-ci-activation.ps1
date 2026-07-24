[CmdletBinding()]
param(
    [switch]$RequireActiveRuleset
)

$ErrorActionPreference = "Stop"
$RepositoryRoot = Split-Path -Parent $PSScriptRoot
Push-Location $RepositoryRoot
try {
    $Arguments = @("tooling/capture-ci-activation.py", "--write")
    if ($RequireActiveRuleset) {
        $Arguments += "--require-active-ruleset"
    }
    & python @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "CI activation evidence capture failed with exit code $LASTEXITCODE."
    }
}
finally {
    Pop-Location
}
