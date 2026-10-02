# Content Structure & Naming — Ilha Tropical

## Objetivo
Manter o projeto legível por humanos e agentes de IA conforme o volume de assets crescer.

## Estrutura de Content

```text
Content/
├── IlhaTropical/
│   ├── Characters/
│   │   ├── Player/
│   │   └── Wildlife/
│   ├── World/
│   │   ├── Maps/
│   │   ├── Landscape/
│   │   ├── Landmass/
│   │   ├── Water/
│   │   ├── PCG/
│   │   ├── Foliage/
│   │   ├── Rocks/
│   │   ├── Caves/
│   │   └── Regions/
│   ├── Environment/
│   ├── Interaction/
│   ├── UI/
│   ├── Audio/
│   ├── VFX/
│   ├── Data/
│   └── Dev/
```

Assets temporários não devem ficar misturados com conteúdo de produção.

## Prefixos
- `L_` — Level/Map
- `BP_` — Blueprint Actor/Object
- `BPC_` — Blueprint Component
- `WBP_` — Widget Blueprint
- `DA_` — Data Asset
- `DT_` — Data Table
- `IA_` — Input Action
- `IMC_` — Input Mapping Context
- `M_` — Material
- `MI_` — Material Instance
- `MF_` — Material Function
- `T_` — Texture
- `SM_` — Static Mesh
- `SK_` — Skeletal Mesh
- `ABP_` — Animation Blueprint
- `A_` — Animation Sequence
- `AM_` — Animation Montage
- `NS_` — Niagara System
- `NE_` — Niagara Emitter
- `PCG_` — PCG Graph
- `SFX_` — Sound Effect
- `MUS_` — Music
- `SC_` — Sound Cue
- `Curve_` — Curve
- `RT_` — Render Target

## Mapas
Mapa principal previsto:
- `L_Island_Main`

Mapas de desenvolvimento:
- `L_Dev_Movement`
- `L_Dev_PCG`
- `L_Dev_Water`
- `L_Dev_Performance`

## Regras
- nomes em inglês para classes/arquivos técnicos;
- nomes legíveis para regiões podem permanecer em português na documentação;
- não usar `NewBlueprint`, `Material1`, `Test2` em conteúdo persistente;
- asset renomeado deve ter redirects corrigidos antes de commit de produção;
- não duplicar assets apenas para variar parâmetros: preferir instâncias/dados;
- conteúdo de terceiros fica isolado sob `Content/ThirdParty/<PackName>`;
- conteúdo próprio nunca deve ser editado diretamente dentro da pasta de um pack externo.

## World Partition
Actors persistentes devem receber nomes descritivos por função/região.
Evitar milhares de Actors individuais onde ISM/HISM/PCG for apropriado.
