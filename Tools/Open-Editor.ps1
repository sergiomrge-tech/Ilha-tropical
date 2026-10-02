param(
    [string]$EngineRoot = "",
    [switch]$NoCompile
)

$ErrorActionPreference = "Stop"
$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$ProjectFile = Join-Path $ProjectRoot "IlhaTropical.uproject"
$ResolvedEngine = & (Join-Path $PSScriptRoot "Resolve-UE583.ps1") -EngineRoot $EngineRoot
$Editor = Join-Path $ResolvedEngine "Engine\Binaries\Win64\UnrealEditor.exe"

if (!$NoCompile) {
    & (Join-Path $PSScriptRoot "Build-Editor.ps1") -EngineRoot $ResolvedEngine
    if ($LASTEXITCODE -ne 0) { throw "Build falhou; Editor nao sera aberto." }
}

Write-Host "Abrindo UE 5.8.3..."
Start-Process -FilePath $Editor -ArgumentList @("`"$ProjectFile`"", "-log")