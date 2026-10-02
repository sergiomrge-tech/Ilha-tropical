# Vertical Slice — Setor Sul v0.1

## Função
O Setor Sul é o benchmark visual, de navegação e performance da ilha inteira.

Ele deve provar:
- escala;
- densidade tropical;
- relevo;
- rios/água;
- PCG em camadas;
- composição manual;
- streaming;
- HLOD;
- traversal de terceira pessoa.

## Coordenadas de referência
Origem da ilha: centro do Landscape.

As coordenadas abaixo foram recalibradas para o Landscape de ~6,22 km por lado e continuam sendo metas aproximadas em metros; devem ser refinadas após importar o heightmap.

### VS01 — Spawn / Praia
- centro aproximado: X=-167, Y=-2811
- altitude: 3-8 m
- largura útil de praia: 80-160 m
- visão parcial da montanha, nunca visão totalmente aberta do cume
- rota principal legível pela quebra da vegetação

### VS02 — Dunas / Transição
- X=-111, Y=-2532
- altitude: 10-30 m
- areia -> solo úmido -> vegetação
- pequenas elevações bloqueiam linha reta entre praia e mata

### VS03 — Mata Costeira
- X=-167, Y=-2157
- altitude: 30-85 m
- primeiro trecho realmente denso
- rota principal sinuosa
- pelo menos duas derivações curtas
- árvore/rocha de escala regional para orientação

### VS04 — Riacho
- X=-56, Y=-1837
- altitude: 65-105 m
- água cruza a rota
- travessia principal natural
- travessia alternativa por pedras/tronco

### VS05 — Floresta Fechada
- X=56, Y=-1572
- altitude: 90-145 m
- visibilidade curta
- relevo lateral impede sensação de corredor artificial
- micro-POI fora da rota principal

### VS06 — Base da Cachoeira
- X=111, Y=-1252
- altitude: 120-170 m
- landmark principal do setor
- piscina natural
- rocha estrutural substitui Landscape esticado nas paredes importantes

### VS07 — Subida Rochosa
- X=264, Y=-1057
- altitude: 170-285 m
- zigue-zague
- rota baixa e rota alta se reencontram
- exposição progressiva da paisagem

### VS08 — Mirante
- X=362, Y=-863
- altitude: 285-340 m
- primeira revelação ampla da montanha central
- enquadramento deve comunicar que ainda existe grande distância/altitude a explorar

## Ritmo visual
Sequência intencional:
aberto -> comprimido -> semiaberto -> comprimido -> landmark -> subida -> grande revelação.

## Regras
- nenhuma reta longa atravessa toda a selva;
- evitar paredes invisíveis;
- bloquear com relevo, água, rochas e vegetação;
- manter rotas secundárias descobríveis;
- POIs não podem parecer distribuídos em grade;
- PCG nunca deve fechar a rota principal;
- cada trecho precisa continuar interessante sem missão ativa.

## Gate
Somente após VS01-VS08 funcionarem em PIE e atingirem performance aceitável o padrão será replicado para os setores de prioridade 2+.
