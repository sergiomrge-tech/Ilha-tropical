# Project Status — Ilha Tropical

## Baseline
- Unreal Engine: **5.8.3**
- Plataforma: Windows PC / DX12
- Perspectiva: terceira pessoa
- Ilha: ~20 km² de área emersa
- Landscape envelope: ~6,222 km x 6,222 km
- Heightmap: 4033 x 4033
- Montanha central: pico base gerado ~1103,5 m
- World Partition baseline: 128 m cells / 800 m loading range

## Concluído fora do Editor

### Repositório
- GitHub como fonte de verdade
- Git LFS configurado
- pastas geradas ignoradas
- CI de validação
- smoke test do gerador

### Terrain v3
- algoritmo determinístico
- costa assimétrica
- maciço central multi-pico
- rios-base curvos
- 20,0006 km² de terra estimada
- R16 oficial verificado por SHA-256
- artifact do GitHub Actions gerado

### World design
- 12 setores somando 20 km²
- 8 perfis de bioma
- Setor Sul VS01-VS08 estruturado
- level design, PCG, World Partition, performance e asset pipeline documentados

### C++
- personagem third-person
- câmera
- walk/jump
- sprint + stamina + exhaustion threshold
- crouch
- interaction trace/interface
- GameMode
- biome DataAsset type
- region volume
- SaveGame + GameInstance Save subsystem

### Ferramentas Windows
- detectar UE 5.8.3
- bootstrap/project files
- build do Editor
- abrir Editor
- gerar terrain v3
- package Win64

## Ainda NÃO validado
Não foi executado neste fluxo:
- UnrealBuildTool real da UE 5.8.3
- compilação C++
- Unreal Editor
- Blueprint compile
- Landscape import
- World Partition runtime
- Water
- PCG Graphs
- Lumen/Nanite/VSM em cena
- PIE
- FPS
- HLOD real
- packaging real

Nenhum desses itens deve ser declarado aprovado antes da execução real.

## Próximo gate
`Docs/EDITOR_GATE_01.md`

Sequência:
1. Bootstrap UE 5.8.3
2. Build IlhaTropicalEditor
3. Abrir Editor
4. Criar L_Island_Main
5. Importar terrain v3
6. WaterBodyOcean
7. validar personagem
8. migrar inputs para Enhanced Input
9. blockout VS01-VS08
10. registrar evidências reais

## Hard blocker atual
A próxima etapa de produção muda assets binários/umap/uasset e exige uma instância real do Unreal Editor 5.8.3 ou MCP conectado a ela.
