# Skills e referências de IA para Unreal Engine 5.8

Estas referências foram validadas em 2026-10-02 e fazem parte do fluxo recomendado do projeto.

## 1. unreal-mcp-skills
Repositorio: https://github.com/soatori/unreal-mcp-skills

Uso principal: automação do Unreal Editor usando o ModelContextProtocol oficial da Epic. O projeto declara suporte a UE 5.8+ e inclui descoberta/configuração/verificação do MCP.

Instalação sugerida pelo próprio projeto:

    npx skills add soatori/unreal-mcp-skills

## 2. ue5-mcp
Repositorio: https://github.com/ibrews/ue5-mcp

Uso principal: manual de campo para agentes trabalhando na Unreal via MCP, cobrindo comportamento de reflexão, Blueprint, Materials, Niagara, MetaSounds, assets, widgets, levels e Python Editor Scripting. O conteúdo cobre especificamente UE 5.7 e UE 5.8.

## 3. UnrealEngine5-Skills
Repositorio: https://github.com/UnrealXu/UnrealEngine5-Skills

Uso principal: pacote de skills para UE 5.6-5.8, incluindo arquitetura, Blueprint, C++ gameplay, PCG, save/load, UI, interação, debug, performance e packaging.

Skills relevantes para Ilha Tropical:
- ue5-auto-assistant
- ue5-module-router
- ue5-architecture
- ue5-pcg-building
- ue5-blueprint-workflow
- ue5-cpp-gameplay
- ue5-save-load-replication
- ue5-world-interaction
- ue5-ui-umg-slate
- ue5-performance-packaging
- ue5-debug-validation

## Regra do projeto

O GitHub e o código-fonte são a fonte de verdade. Blueprints e assets binários devem ser usados quando agregarem valor visual/editorial, mas a lógica central deve permanecer o máximo possível em C++ e dados versionáveis.
