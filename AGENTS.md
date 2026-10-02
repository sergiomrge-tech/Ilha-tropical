# AGENTS — Ilha Tropical

## Fonte de verdade
O repositório GitHub é a fonte principal do projeto. Evitar lógica crítica que exista apenas em sessão local ou em Blueprint sem documentação.

## Engine
Unreal Engine 5.8.x.

## Direção
Jogo em terceira pessoa em uma ilha tropical deserta de aproximadamente 20 km², com uma grande montanha central como marco visual dominante.

## Regras de desenvolvimento
- Preferir C++ para sistemas centrais.
- Usar Blueprints para composição, tuning, assets e extensões visuais.
- Usar Git LFS para .uasset/.umap e outros binários grandes.
- World Partition para o mundo aberto.
- Landmass + Landscape para macroterreno.
- PCG para vegetação e distribuição procedural.
- Water System para oceano, rios e lagos.
- Não preencher toda a ilha antes de validar o vertical slice inicial.
- Antes de integrar grandes mudanças, validar compilação e referências quebradas.
- Não afirmar que algo foi testado no Editor se o Editor não foi executado.

## Skills recomendadas
Ver Docs/AI_SKILLS.md.
