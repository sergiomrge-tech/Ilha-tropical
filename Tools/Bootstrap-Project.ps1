param(
    [string]$EngineRoot = ""
)

$ErrorActionPreference = "Stop"
$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$ProjectFile = Join-Path $ProjectRoot "IlhaTropical.uproject"

Write-Host "== Ilha Tropical / Bootstrap UE 5.8.3 =="

if (!(Get-Command git -ErrorAction SilentlyContinue)) { throw "Git nao encontrado no PATH." }

if (Get-Command git-lfs -ErrorAction SilentlyContinue) {
    git lfs install
    git lfs pull
} else {
    Write-Warning "Git LFS nao encontrado. Instale Git LFS antes de baixar assets binarios."
}

if (!(Get-Command python -ErrorAction SilentlyContinue)) { throw "Python nao encontrado no PATH." }

Write-Host "[1/4] Validacao estatica..."
python (Join-Path $ProjectRoot "Scripts\validate_repo.py")
if ($LASTEXITCODE -ne 0) { throw "Validacao estatica falhou." }

Write-Host "[2/4] Dependencia do gerador..."
python -c "import numpy" 2>$null
if ($LASTEXITCODE -ne 0) {
    python -m pip install numpy
    if ($LASTEXITCODE -ne 0) { throw "Falha ao instalar numpy." }
}

Write-Host "[3/4] Smoke test do terreno..."
python (Join-Path $ProjectRoot "Scripts\test_terrain_generator.py")
if ($LASTEXITCODE -ne 0) { throw "Smoke test do terreno falhou." }

Write-Host "[4/4] Localizando UE 5.8.3..."
$ResolvedEngine = & (Join-Path $PSScriptRoot "Resolve-UE583.ps1") -EngineRoot $EngineRoot
if ($LASTEXITCODE -ne 0) { throw "UE 5.8.3 nao localizada." }

$UBT = Join-Path $ResolvedEngine "Engine\Binaries\DotNET\UnrealBuildTool\UnrealBuildTool.exe"
if (!(Test-Path $UBT)) { throw "UnrealBuildTool nao encontrado: $UBT" }

Write-Host "Gerando arquivos de projeto..."
& $UBT -projectfiles -project="$ProjectFile" -game -rocket -progress
if ($LASTEXITCODE -ne 0) { throw "Geracao dos arquivos de projeto falhou." }

Write-Host ""
Write-Host "Bootstrap concluido."
Write-Host "Engine: $ResolvedEngine"
Write-Host "Projeto: $ProjectFile"
Write-Host "Proximo passo: .\Tools\Build-Editor.ps1"