[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$VerificationSummary,

    [Parameter(Mandatory = $true)]
    [string]$ManualTestRecord,

    [Parameter(Mandatory = $true)]
    [ValidateSet('Passed', 'Failed')]
    [string]$CiResult,

    [Parameter(Mandatory = $true)]
    [ValidatePattern('^https://github\.com/.+/actions/runs/\d+.*$')]
    [string]$CiRunUrl,

    [string]$Tester = $env:USERNAME,

    [string]$Notes = ''
)

$ErrorActionPreference = 'Stop'
$repositoryRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repositoryRoot

$summaryPath = [System.IO.Path]::GetFullPath($VerificationSummary)
if (-not (Test-Path $summaryPath)) {
    throw "Verification summary not found: $summaryPath"
}

$summary = Get-Content $summaryPath -Raw | ConvertFrom-Json
if ($summary.automatedVerificationStatus -ne 'Passed') {
    throw 'Wave 01 cannot be finalized because automated verification did not pass.'
}

if ($summary.repositoryDirty -eq $true) {
    throw 'Wave 01 cannot be finalized from a dirty repository. Run verification again after committing all intended changes.'
}

if ([string]::IsNullOrWhiteSpace($summary.commitSha)) {
    throw 'Wave 01 cannot be finalized without a recorded commit SHA.'
}

$manualRecordPath = [System.IO.Path]::GetFullPath($ManualTestRecord)
if (-not (Test-Path $manualRecordPath)) {
    throw "Manual test record not found: $manualRecordPath"
}

$manualRecord = Get-Content $manualRecordPath -Raw
if ($manualRecord -notmatch '\*\*Overall result:\*\*\s+Passed') {
    throw 'Wave 01 cannot be finalized because the manual test record is not marked Passed.'
}

$escapedCommit = [regex]::Escape([string]$summary.commitSha)
if ($manualRecord -notmatch $escapedCommit) {
    throw 'The manual test record does not reference the same commit as the automated verification.'
}

if ($CiResult -ne 'Passed') {
    throw 'Wave 01 cannot be finalized because the GitHub Actions run did not pass.'
}

$recordPath = Join-Path $repositoryRoot 'docs\evidence\WAVE-01-VERIFICATION-RECORD.md'
New-Item -ItemType Directory -Path (Split-Path -Parent $recordPath) -Force | Out-Null

$generatedUtc = (Get-Date).ToUniversalTime().ToString('O')
$manualRecordRelative = [System.IO.Path]::GetRelativePath((Split-Path -Parent $recordPath), $manualRecordPath).Replace('\\', '/')
$content = @"
# TaskHost Local – Wave 01 Verification Record

**Status:** Passed  
**Generated UTC:** $generatedUtc  
**Verified commit:** ``$($summary.commitSha)``  
**Tester:** $Tester

## Evidence

| Evidence | Result |
|---|---|
| Automated restore, build, tests, audit, publish and headless self-check | Passed |
| Manual Windows smoke test | [Passed record]($manualRecordRelative) |
| GitHub Actions run | [Passed run]($CiRunUrl) |
| Repository clean during automated verification | Yes |

## Automated run

- Started UTC: ``$($summary.startedUtc)``
- Completed UTC: ``$($summary.completedUtc)``
- Configuration: ``$($summary.configuration)``
- Operating system: ``$($summary.operatingSystem)``
- Process architecture: ``$($summary.processArchitecture)``

## Notes

$Notes

## Closeout statement

Wave 01 is verified for the commit named above. This statement applies only to that immutable source state and the linked CI run. Later changes require their own verification.
"@

Set-Content -Path $recordPath -Value $content -Encoding utf8
Write-Host "Created verified evidence record: $recordPath" -ForegroundColor Green
Write-Host 'Review the generated record before committing it.' -ForegroundColor Yellow
