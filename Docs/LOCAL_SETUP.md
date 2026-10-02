# Local Setup - Windows / Unreal Engine 5.8.3

## Pre-requisitos
- Windows 10/11 64-bit
- Unreal Engine 5.8.3
- Visual Studio com workload C++ exigido pela Unreal
- Git
- Git LFS
- Python 3.11+ para ferramentas offline

## Clone

    git clone https://github.com/sergiomrge-tech/Ilha-tropical.git
    cd Ilha-tropical
    git lfs install
    git lfs pull

## Bootstrap

Instalacao padrao:

    .\Tools\Bootstrap-Project.ps1

Caminho customizado:

    .\Tools\Bootstrap-Project.ps1 -EngineRoot "D:\UE\UE_5.8"

O script le Engine/Build/Build.version e exige exatamente 5.8.3.

## Compilar Editor

    .\Tools\Build-Editor.ps1

## Abrir

    .\Tools\Open-Editor.ps1

Esse comando compila antes de abrir, salvo quando usado com -NoCompile.

## Gerar macroterreno

    python Scripts/terrain/generate_island_heightmap.py

O conteudo gerado fica em Generated/ e nao entra no Git automaticamente.

## Criterio
So registrar "build UE 5.8.3 aprovado" depois de Build-Editor.ps1 concluir com sucesso em uma instalacao real da engine.