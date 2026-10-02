# World Partition & Landscape Plan — UE 5.8.3

## Landscape principal

A configuração fecha exatamente a resolução 4033:

- Section Size: **63 x 63 quads**
- Sections per Component: **2 x 2**
- Component Size: **126 x 126 quads**
- Components: **32 x 32**
- Total: **4032 x 4032 quads**
- Vertices: **4033 x 4033**
- XY Scale inicial: **110,916 cm**
- dimensão nominal: **4472,14 m**
- Z Scale inicial: **500**

Com Z Scale 500, existe margem vertical suficiente para a montanha central alvo (~1120 m) sem comprimir demais o height range.

## World Partition

Baseline inicial:
- Runtime Grid: `MainGrid`
- Cell Size: **128 m**
- Loading Range: **800 m**
- Streaming: habilitado
- One File Per Actor: habilitado

Esses valores são baseline, não dogma. O primeiro profiling real no Setor Sul pode alterar loading range/cell strategy.

## Por que 128 m
A ilha é densa e possui muita oclusão natural. Células menores permitem granularidade melhor de streaming que uma malha de células muito grandes, sem ir imediatamente para uma fragmentação extrema.

## Data Layers previstas

Somente criar quando houver conteúdo real:
- DL_Gameplay
- DL_Water
- DL_POI
- DL_ManualFoliage
- DL_Debug

Não usar Data Layer para substituir organização normal de pastas.

## HLOD
HLOD será orientado por conteúdo real.

Prioridades:
1. conjuntos rochosos;
2. grupos de cenário;
3. elementos arquitetônicos futuros;
4. vegetação estrutural quando fizer sentido.

Ground cover e foliage pequeno devem resolver custo principalmente por instancing/cull, não por gerar HLOD pesado indiscriminadamente.

## Validação obrigatória no Editor
- Landscape importa como 32x32 components.
- tamanho medido confere com ~4,47 km.
- personagem tem escala natural na praia.
- streaming carrega/descarrega células sem buracos visíveis.
- montanha permanece landmark sem obrigar conteúdo completo a ficar carregado.
