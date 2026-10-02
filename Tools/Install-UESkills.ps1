param(
    [string]$Root = "$PSScriptRoot\..\External\AgentSkills"
)

$ErrorActionPreference = "Stop"
New-Item -ItemType Directory -Force -Path $Root | Out-Null

Write-Host "== Ilha Tropical: preparando skills UE 5.8 =="

if (Get-Command npx -ErrorAction SilentlyContinue) {
    Write-Host "[1/3] Instalando unreal-mcp-skills via skills CLI..."
    npx --yes skills add soatori/unreal-mcp-skills
} else {
    Write-Warning "npx nao encontrado. Instale Node.js para usar o instalador oficial do unreal-mcp-skills."
}

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "git nao encontrado no PATH."
}

$repos = @(
    @{ Name = "ue5-mcp"; Url = "https://github.com/ibrews/ue5-mcp.git" },
    @{ Name = "UnrealEngine5-Skills"; Url = "https://github.com/UnrealXu/UnrealEngine5-Skills.git" }
)

foreach ($repo in $repos) {
    $dest = Join-Path $Root $repo.Name
    if (Test-Path (Join-Path $dest ".git")) {
        Write-Host "Atualizando $($repo.Name)..."
        git -C $dest pull --ff-only
    } else {
        Write-Host "Clonando $($repo.Name)..."
        git clone --depth 1 $repo.Url $dest
    }
}

Write-Host ""
Write-Host "Skills/fontes preparadas em: $Root"
Write-Host "Leia Docs\AI_SKILLS.md para o papel de cada pacote."
