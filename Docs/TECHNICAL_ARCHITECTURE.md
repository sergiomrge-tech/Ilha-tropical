# Technical Architecture — UE 5.8.3

## Estratégia
Começar com um único módulo de gameplay (`IlhaTropical`) organizado por domínio. Separar módulos adicionais apenas quando houver benefício real de build, dependência ou ownership.

## Domínios atuais

```text
Source/IlhaTropical/
├── Character/
│   ├── IslandCharacter
│   └── IslandStaminaComponent
├── Interaction/
│   ├── IslandInteractable
│   └── IslandInteractionComponent
├── Game/
│   └── IslandGameMode
├── Save/
│   ├── IslandSaveGame
│   └── IslandSaveSubsystem
└── World/
    ├── IslandBiomeDataAsset
    └── IslandRegionVolume
```

## Regras de dependência
- Character pode depender de componentes de Interaction.
- Interaction não depende de Character concreto.
- World não depende do Player.
- Dados de bioma não devem conhecer UI ou gameplay do jogador.
- Sistemas futuros devem preferir interfaces/componentes a casts para classes concretas.

## C++
Usar C++ para:
- movement base;
- interação;
- sistemas persistentes;
- regras de gameplay;
- save/load;
- streaming helpers;
- lógica que precisa de testes/revisão em diff.

## Blueprint
Usar Blueprint para:
- composição de Actors;
- conexão com assets;
- tuning;
- prototipagem visual;
- extensão de interfaces;
- triggers e sequências locais simples.

Blueprint não deve virar repositório de regras críticas impossíveis de revisar fora do Editor.

## Dados
Preferir:
- Data Assets;
- Data Tables;
- JSON versionável apenas para ferramentas/source-of-truth externos ao runtime quando fizer sentido.

## World
- World Partition: streaming.
- Data Layers: estados editoriais/temáticos quando necessário.
- HLOD: redução de custo de conteúdo distante.
- PCG: distribuição procedural, sempre com seed e regras reproduzíveis.
- Landmass/Landscape: macro e microterreno.
- Water: oceano e rios.

## Testes
Camadas:
1. validação estática em GitHub Actions;
2. testes de ferramentas Python;
3. compilação C++ UE 5.8.3;
4. Automation Tests quando o Editor estiver integrado;
5. PIE traversal;
6. profiling;
7. package smoke test.

## Política de mudanças
Cada mudança deve preservar:
- build;
- leitura do projeto;
- determinismo de geração quando aplicável;
- rollback por Git;
- separação entre conteúdo gerado e fonte de geração.
