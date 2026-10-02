param(
    [string]$EngineRoot = "",
    [ValidateSet("DebugGame","Development","Shipping")]
    [string]$Configuration = "Development"
)

$ErrorActionPreference = "Stop"
$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$ProjectFile = Join-Path $ProjectRoot "IlhaTropical.uproject"
$ResolvedEngine = & (Join-Path $PSScriptRoot "Resolve-UE583.ps1") -EngineRoot $EngineRoot

$BuildBat = Join-Path $ResolvedEngine "Engine\Build\BatchFiles\Build.bat"
if (!(Test-Path $BuildBat)) { throw "Build.bat nao encontrado: $BuildBat" }

Write-Host "Compilando IlhaTropicalEditor / Win64 / $Configuration na UE 5.8.3..."
& $BuildBat IlhaTropicalEditor Win64 $Configuration "$ProjectFile" -WaitMutex -NoHotReloadFromIDE

if ($LASTEXITCODE -ne 0) { throw "Build falhou com exit code $LASTEXITCODE." }

Write-Host "BUILD OK - IlhaTropicalEditor $Configuration"