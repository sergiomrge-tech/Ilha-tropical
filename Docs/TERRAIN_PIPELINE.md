# Terrain Pipeline

## Objetivo
Gerar uma base determinística para a ilha de aproximadamente 20 km² antes do passe manual na Unreal Engine 5.8.3.

## Resolução
- Heightmap: 4033 x 4033
- Quads: 4032
- Largura nominal: 4472,14 m
- XY Scale sugerido: 110,916 cm
- Z Scale inicial: 500
- Pico alvo: ~1120 m

## Geração

```powershell
python -m pip install numpy
python Scripts/terrain/generate_island_heightmap.py
```

Saídas locais:
- `Generated/Terrain/island_v1.r16`
- `Generated/Terrain/island_v1.meta.json`
- `Generated/Terrain/island_v1_preview.pgm`

`Generated/` permanece fora do Git por padrão.

## Importação no Unreal
1. Criar/Open World com World Partition.
2. Landscape Mode -> Import from File.
3. Selecionar `island_v1.r16`.
4. Usar resolução 4033.
5. XY Scale inicial: 110,916.
6. Z Scale inicial: 500.
7. Posicionar WaterBodyOcean com superfície próxima de Z=0.
8. Validar a escala com o personagem antes de qualquer detalhamento.

## Depois da importação
A base procedural nunca é considerada level design final.

Passe obrigatório:
1. Landmass para corrigir silhueta/macrorrelevo.
2. Landscape Sculpt para rotas e microrelevo.
3. Water splines para rios.
4. PCG por bioma.
5. composição manual do Setor Sul.
6. HLOD/performance.
