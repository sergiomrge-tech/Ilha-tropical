# Performance Budget — PC / UE 5.8.3

## Meta técnica inicial
Alvo de desenvolvimento: **60 FPS**, ou **16,67 ms por frame**.

Não representa requisito mínimo de hardware final; é um orçamento de engenharia para impedir que a densidade visual cresça sem controle.

## Budgets de frame
- Game Thread: ideal <= 8 ms
- Render Thread: ideal <= 8 ms
- GPU: ideal <= 14,5 ms em cenário de referência
- margem restante: streaming, picos e variabilidade

Não somar esses valores como se todos fossem seriais; são limites de diagnóstico por pipeline.

## Mundo aberto
- World Partition obrigatório.
- HLOD obrigatório para conjuntos relevantes.
- Não manter a ilha inteira carregada.
- Testar traversal rápido entre células.
- Evitar Actor por planta/pedra repetida.

## Vegetação
- usar instancing;
- colisão apenas onde necessária;
- canopy distante deve reduzir custo de material/sombra;
- ground cover deve ter cull agressivo;
- densidade PCG controlada por biome e distância;
- evitar overdraw extremo em camadas transparentes.

## Nanite
Usar quando o asset e material se beneficiarem, principalmente:
- grandes rochas;
- falésias;
- formações estruturais;
- meshes ambientais de alta complexidade.

Não assumir que Nanite elimina custo de material, translucência, WPO ou sombra.

## Lumen
- controlar quantidade de luzes locais móveis;
- evitar materiais emissivos usados como iluminação principal em larga escala;
- validar interiores/cavernas separadamente;
- manter fallback de escalabilidade planejado.

## Virtual Shadow Maps
- limitar objetos pequenos que projetam sombra a longa distância;
- foliage deve usar distâncias e estratégias de sombra coerentes;
- perfilar páginas VSM no setor de selva densa.

## Water
- oceano é dominante, mas rios/cachoeiras não devem acumular efeitos caros sem profiling;
- controlar translucência, foam e refraction;
- cachoeiras complexas serão validadas isoladamente.

## Métricas de aprovação de setor
Um setor não é aprovado para replicação pelo mapa inteiro sem:
1. traversal sem hitch grave;
2. memória estabilizada;
3. nenhuma célula retendo conteúdo indevido;
4. GPU dentro do orçamento no cenário de referência;
5. Game/Render threads sem gargalo persistente;
6. densidade visual mantida após otimização.

## Vertical slice
O Setor Sul será o benchmark principal. A floresta densa e a cachoeira devem representar um caso pesado, não uma cena vazia usada apenas para obter FPS.
