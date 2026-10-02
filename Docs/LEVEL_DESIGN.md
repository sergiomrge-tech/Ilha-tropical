# Level Design — Ilha Tropical v0.1

## Objetivo
Criar uma ilha densa e explorável em que caminhar pelo mundo seja interessante mesmo sem combate ou missão ativa.

## Filosofia
O jogador deve encontrar algo visualmente relevante com frequência sem transformar a ilha em um parque temático lotado.

Usar quatro escalas de leitura:

### 1. Landmark global
Elementos vistos de grandes distâncias.
- montanha central;
- grandes falésias;
- cachoeiras principais;
- formações rochosas únicas;
- praias e enseadas marcantes.

### 2. Landmark regional
Ajuda a reconhecer cada área.
- árvore colossal;
- arco natural de pedra;
- lago;
- queda d'água;
- paredão;
- caverna;
- ruína futura;
- praia fechada;
- desfiladeiro.

### 3. Ponto de interesse local
Recompensa exploração de curta distância.
- pequena caverna;
- passagem entre rochas;
- árvore caída formando ponte;
- lagoa escondida;
- mirante;
- trilha secundária;
- pequena gruta;
- naufrágio futuro;
- recurso raro futuro.

### 4. Microcomposição
Mantém cada trecho visualmente rico.
- raízes;
- pedras;
- troncos;
- folhas;
- vegetação baixa;
- mudanças de material;
- pequenas depressões;
- elevações;
- água acumulada;
- recortes do terreno.

## Estrutura de rotas
Cada região importante deve possuir:
- uma rota principal legível;
- uma ou mais rotas secundárias;
- pelo menos um atalho desbloqueável ou descobrível quando fizer sentido;
- rotas altas e baixas quando o relevo permitir;
- locais de observação que ajudem na orientação.

Evitar corredores óbvios desenhados apenas por paredes invisíveis. Preferir bloqueios naturais.

## Ocultação e revelação
O mapa deve alternar momentos de baixa e alta visibilidade.

Exemplos:
- floresta densa bloqueia a visão;
- jogador atravessa um trecho apertado;
- vegetação se abre;
- surge uma cachoeira ou vista da montanha;
- rota volta a se fechar.

Esse ritmo deve ser usado para criar sensação de descoberta.

## Verticalidade
A verticalidade deve ser constante, não limitada à montanha central.

Usar:
- encostas;
- terraços naturais;
- pedras escalonadas;
- pontes naturais;
- raízes;
- vales;
- ravinas;
- falésias;
- caminhos elevados;
- cavernas em diferentes níveis.

## Costa
A costa não será uma faixa plana contínua.

Alternar:
- praias largas;
- praias pequenas entre rochas;
- falésias;
- enseadas;
- recifes;
- pedras gigantes;
- manguezais;
- desembocaduras de rios;
- cavernas costeiras;
- pequenas ilhas próximas.

## Floresta
Evitar floresta procedural homogênea.

Criar bolsões:
- mata muito fechada;
- clareiras;
- bambuzais ou agrupamentos equivalentes;
- áreas com árvores antigas;
- solo encharcado;
- áreas rochosas;
- mata de encosta;
- mata próxima a rios.

## Rios e cachoeiras
Água deve participar da navegação.
- rios cortam rotas;
- pedras criam travessias;
- quedas d'água funcionam como landmarks;
- pequenas piscinas naturais criam pontos de descanso;
- cursos d'água ajudam o jogador a entender a topografia.

## Cavernas
As cavernas devem conectar exploração de superfície e subterrânea.
- entradas visíveis e escondidas;
- atalhos;
- câmaras naturais;
- saídas em outro nível do terreno;
- possibilidade futura de recursos, fauna e narrativa.

## Densidade
A meta não é preencher todo metro quadrado.

A composição deverá alternar:
- densidade alta;
- densidade média;
- zonas de respiro;
- vistas longas;
- espaços comprimidos.

Isso melhora leitura, desempenho e impacto visual.

## Ferramentas
- Landmass: macroformas.
- Landscape Sculpt: refinamento manual.
- PCG: distribuição base.
- Foliage: ajustes artísticos.
- Spline: rios, trilhas e elementos lineares.
- Water: oceano, rios e lagos.
- World Partition + HLOD: streaming e otimização.

## Regra de aprovação
Uma área só é considerada concluída depois de passar por:
1. geração base;
2. composição manual;
3. teste de navegação em terceira pessoa;
4. teste de leitura visual;
5. teste de colisão;
6. teste de desempenho;
7. revisão de repetição visual.

## Primeiro setor de produção
Setor Sul — Praia Inicial.

Subáreas:
1. faixa costeira;
2. dunas e vegetação;
3. entrada da mata;
4. trilha estreita;
5. primeiro riacho;
6. subida rochosa;
7. clareira;
8. visão parcial da montanha.

Este setor será o padrão de qualidade do restante da ilha.
