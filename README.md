# Ilha Tropical

Jogo de exploração em terceira pessoa para **PC**, desenvolvido para **Unreal Engine 5.8.3** e versionado pelo GitHub.

## Conceito

Mundo aberto em uma ilha tropical deserta com aproximadamente **20 km² de área emersa**, extremamente rica em vegetação, relevo e exploração.

Uma grande montanha central domina a paisagem e funciona como referência visual global.

## Direção do mundo

A ilha será construída com level design detalhado:

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

PCG acelera a composição, mas cada região importante recebe passe manual.

## Base técnica

- Unreal Engine 5.8.3
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

## Estado atual

Já versionado:
- projeto C++;
- personagem de terceira pessoa;
- câmera;
- caminhada e salto;
- sprint com stamina;
- agachar;
- interação por trace;
- GameMode;
- gerador determinístico de heightmap 4033;
- especificação do macroterreno;
- 12 setores de level design;
- world design e level design;
- Git LFS;
- skills UE5/MCP documentadas;
- validação estática e smoke test do terreno em GitHub Actions.

Ainda não houve compilação/validação do projeto novo dentro do Unreal Editor 5.8.3.

## Próximo gate real

Abrir e compilar na UE 5.8.3, importar o macroterreno e validar escala do **Setor Sul**:

**praia -> mata costeira -> riacho -> floresta densa -> rio -> cachoeira -> subida rochosa -> mirante da montanha**
