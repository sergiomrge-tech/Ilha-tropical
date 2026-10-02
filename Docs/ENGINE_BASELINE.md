# Engine Baseline — Ilha Tropical

## Versão oficial
**Unreal Engine 5.8.3**

Esta é a versão de referência para desenvolvimento, validação no Editor, geração de projeto, compilação e empacotamento.

## Associação do .uproject
O arquivo `IlhaTropical.uproject` mantém:

```json
"EngineAssociation": "5.8"
```

Isso identifica a família 5.8 instalada. A versão de patch exigida pelo projeto é 5.8.3.

## Plataforma alvo
- Windows PC
- DirectX 12
- Shader Model 6
- Lumen
- Nanite
- Virtual Shadow Maps
- World Partition
- HLOD

## Política de compatibilidade
- Implementações devem ser verificadas prioritariamente contra UE 5.8.3.
- Não usar API marcada como removida/deprecated na 5.8 quando houver substituto documentado.
- Mudanças específicas de outra versão devem ser isoladas e documentadas.
- Não declarar validação na UE 5.8.3 sem executar realmente Editor/Build dessa versão.
