# AGENTS — Ilha Tropical

## Fonte de verdade
O repositório GitHub é a fonte principal do projeto. Evitar lógica crítica que exista apenas em sessão local ou em Blueprint sem documentação.

## Engine
Versão oficial de produção e validação: **Unreal Engine 5.8.3**.

O `EngineAssociation` pode permanecer `5.8` para identificar a família instalada; toda validação real deve usar 5.8.3.

## Plataforma
PC / Windows / DirectX 12.

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

Ver `Docs/LEVEL_DESIGN.md`, `Docs/WORLD_DESIGN.md` e `Data/World/island_sectors_v1.json`.

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
- Não afirmar que algo foi testado no Editor se o Editor não foi executado na UE 5.8.3.
- Mudanças geradas automaticamente devem ser verificáveis e determinísticas quando possível.

## Skills recomendadas
Ver `Docs/AI_SKILLS.md`.
