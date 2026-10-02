# AGENTS — Ilha Tropical

## Fonte de verdade
O repositório GitHub é a fonte principal do projeto. Evitar lógica crítica que exista apenas em sessão local ou em Blueprint sem documentação.

## Engine
Unreal Engine 5.8.x.

## Plataforma
PC.

## Direção oficial
Jogo em terceira pessoa em uma ilha tropical deserta de aproximadamente 20 km².

A ilha deve ser:
- densa;
- exuberante;
- vertical;
- rica em relevo;
- detalhada manualmente;
- reconhecível por regiões;
- construída para exploração.

A grande montanha central é o principal marco visual.

## Level design
Não criar grandes áreas planas ou vazias.

Todo setor importante deve combinar:
- macrorelevo;
- microrelevo;
- rota principal;
- rotas secundárias;
- landmarks;
- pontos de interesse;
- mudanças de visibilidade;
- composição manual após PCG.

PCG é ferramenta de produção, não substituto do level design.

Ver `Docs/LEVEL_DESIGN.md` e `Docs/WORLD_DESIGN.md`.

## Regras de desenvolvimento
- Preferir C++ para sistemas centrais.
- Usar Blueprints para composição, tuning e extensões.
- Git LFS para .uasset/.umap e binários grandes.
- World Partition para o mundo aberto.
- Landmass + Landscape para macroterreno.
- PCG para distribuição procedural em camadas.
- Water System para oceano, rios e lagos.
- Usar HLOD e streaming para preservar densidade no PC.
- Construir e validar primeiro um vertical slice de alta qualidade.
- Não preencher toda a ilha antes de validar escala, navegação e desempenho.
- Antes de integrar grandes mudanças, validar compilação e referências quebradas.
- Não afirmar que algo foi testado no Editor se o Editor não foi executado.

## Skills recomendadas
Ver `Docs/AI_SKILLS.md`.
