param(
    [int]$Seed = 583
)

$ErrorActionPreference = "Stop"
$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path

if (!(Get-Command python -ErrorAction SilentlyContinue)) { throw "Python nao encontrado no PATH." }

python -c "import numpy" 2>$null
if ($LASTEXITCODE -ne 0) {
    python -m pip install numpy
    if ($LASTEXITCODE -ne 0) { throw "Falha ao instalar numpy." }
}

Push-Location $ProjectRoot
try {
    python Scripts/terrain/generate_island_heightmap.py --seed $Seed
    if ($LASTEXITCODE -ne 0) { throw "Geracao do terreno falhou." }
} finally {
    Pop-Location
}

Write-Host "Terrain v3 gerado em Generated\Terrain"