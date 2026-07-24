[CmdletBinding()]
param(
    [string]$TargetDirectory = (Join-Path ([Environment]::GetFolderPath('MyDocuments')) 'SASD-TaskHostLocal-Backups')
)

$ErrorActionPreference = 'Stop'
$sourceDatabase = Join-Path $env:APPDATA 'SASD\TaskHostLocal\taskhost.db'

if (-not (Test-Path -LiteralPath $sourceDatabase -PathType Leaf)) {
    Write-Host "No existing TaskHost Local database was found at:`n$sourceDatabase" -ForegroundColor Yellow
    Write-Host 'A backup is not required before the first fresh start.' -ForegroundColor Yellow
    exit 0
}

New-Item -ItemType Directory -Path $TargetDirectory -Force | Out-Null
$timestamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$targetFile = Join-Path $TargetDirectory "taskhost-before-wave01-$timestamp.db"

Copy-Item -LiteralPath $sourceDatabase -Destination $targetFile -ErrorAction Stop
$hash = Get-FileHash -LiteralPath $targetFile -Algorithm SHA256

Write-Host 'Backup created successfully:' -ForegroundColor Green
Write-Host $targetFile
Write-Host "SHA-256: $($hash.Hash)"
