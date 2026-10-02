# Ilha Tropical

Jogo de exploração em terceira pessoa para **PC**, desenvolvido em Unreal Engine 5.8 e versionado pelo GitHub.

## Conceito

Mundo aberto em uma ilha tropical deserta de aproximadamente **20 km²**, extremamente rica em vegetação, relevo e exploração.

Uma grande montanha central domina a paisagem e funciona como referência visual global.

## Direção do mundo

O objetivo não é criar apenas um terreno grande. A ilha será construída com level design detalhado:

- praias irregulares;
- selva densa;
- rios;
- cachoeiras;
- ravinas;
- falésias;
- cavernas;
- vales;
- platôs;
- trilhas naturais;
- passagens escondidas;
- mirantes;
- rotas alternativas;
- pontos de interesse.

PCG será usado para acelerar a vegetação e composição, mas cada região importante receberá passe manual.

## Base técnica

- Unreal Engine 5.8.x
- PC / DirectX 12
- C++
- Landscape + Landmass
- PCG
- Water System
- World Partition
- HLOD
- Lumen
- Nanite
- Virtual Shadow Maps
- Git LFS

## Estado atual — v0.1

Já versionado:
- projeto C++;
- personagem de terceira pessoa;
- câmera e movimentação inicial;
- GameMode;
- configurações base;
- Git LFS;
- regras dos agentes;
- world design;
- level design;
- roadmap;
- referências de skills UE5/MCP;
- validação estática por GitHub Actions.

Ainda não houve validação do projeto novo dentro do Unreal Editor.

## Primeiro grande marco

Criar o **Setor Sul** como vertical slice de qualidade final:

**praia -> mata costeira -> riacho -> floresta densa -> rio -> cachoeira -> subida rochosa -> mirante da montanha**

Esse setor definirá o padrão de densidade e acabamento do restante dos 20 km².
