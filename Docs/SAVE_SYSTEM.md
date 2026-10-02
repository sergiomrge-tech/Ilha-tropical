# Save/Load Foundation

## Estado
A fundação de SaveGame é deliberadamente pequena para não congelar decisões de gameplay cedo demais.

## Salvo atualmente
- SaveVersion
- PlayerTransform
- CurrentRegionId
- SessionPlaySecondsAtSave (telemetria local da sessão; não é contador acumulado entre sessões)

## Slot
`IslandMain`, UserIndex 0.

## Uso
O `UIslandSaveSubsystem` é um `UGameInstanceSubsystem` e pode ser acessado por Blueprint/C++.

Operações:
- SavePlayerState
- LoadPlayerState
- HasSave
- DeleteSave

## Evolução futura
Inventário, quests, coleta, fauna persistente e estado do mundo só entram no schema quando esses sistemas existirem.

## Migração
Nunca reutilizar campos com significado diferente.
Quando o formato mudar:
1. incrementar SaveVersion;
2. migrar dados antigos explicitamente;
3. manter teste de carregamento de saves anteriores suportados.
