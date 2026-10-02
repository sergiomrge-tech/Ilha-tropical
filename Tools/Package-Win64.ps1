param(
    [string]$EngineRoot = "",
    [ValidateSet("Development","Shipping")]
    [string]$Configuration = "Development",
    [string]$ArchiveDirectory = ""
)

$ErrorActionPreference = "Stop"
$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$ProjectFile = Join-Path $ProjectRoot "IlhaTropical.uproject"
$ResolvedEngine = & (Join-Path $PSScriptRoot "Resolve-UE583.ps1") -EngineRoot $EngineRoot
$RunUAT = Join-Path $ResolvedEngine "Engine\Build\BatchFiles\RunUAT.bat"

if (!(Test-Path $RunUAT)) { throw "RunUAT.bat nao encontrado: $RunUAT" }

if ([string]::IsNullOrWhiteSpace($ArchiveDirectory)) {
    $ArchiveDirectory = Join-Path $ProjectRoot "Builds\Win64\$Configuration"
}

New-Item -ItemType Directory -Force -Path $ArchiveDirectory | Out-Null

Write-Host "Empacotando Ilha Tropical / Win64 / $Configuration / UE 5.8.3..."
& $RunUAT BuildCookRun `
    -project="$ProjectFile" `
    -noP4 `
    -platform=Win64 `
    -clientconfig=$Configuration `
    -build `
    -cook `
    -stage `
    -pak `
    -archive `
    -archivedirectory="$ArchiveDirectory"

if ($LASTEXITCODE -ne 0) { throw "Packaging falhou com exit code $LASTEXITCODE." }

Write-Host "PACKAGE OK - $ArchiveDirectory"