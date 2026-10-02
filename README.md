# Ilha Tropical

Projeto Unreal Engine 5.8 em terceira pessoa, desenvolvido com GitHub como fonte de verdade.

## Conceito

Mundo aberto em uma ilha tropical deserta de aproximadamente **20 km²**, com uma grande montanha central visível de boa parte da costa.

## Base técnica

- Unreal Engine 5.8.x
- C++ para sistemas centrais
- Landscape + Landmass
- PCG
- Water System
- World Partition
- Lumen / Nanite / Virtual Shadow Maps
- Git LFS para assets binários

## Estado atual — v0.1

Já versionado:
- projeto C++;
- personagem de terceira pessoa;
- câmera e movimentação inicial;
- GameMode;
- configurações base;
- Git LFS;
- regras para agentes;
- world design;
- roadmap;
- referências de skills UE5/MCP.

Ainda **não** foi validado dentro do Unreal Editor neste repositório novo.

## Próxima etapa

Criar e validar o primeiro mapa World Partition e o vertical slice:

**praia inicial -> floresta -> rio -> cachoeira -> mirante da montanha central**

## Skills de IA

Veja `Docs/AI_SKILLS.md`.

No Windows, o script `Tools/Install-UESkills.ps1` prepara as referências externas e instala o pacote MCP que oferece instalador oficial via `npx skills`.
