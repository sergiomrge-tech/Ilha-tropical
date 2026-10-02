# Asset Pipeline — Ilha Tropical / UE 5.8.3

## Objetivo
Construir uma ilha tropical densa sem misturar packs, quebrar licenças ou transformar o Content Browser em uma pasta única impossível de manter.

## Fontes preferidas
1. Fab dentro da Unreal Engine para aquisição/importação.
2. Conteúdo gratuito oficial da Epic.
3. Megascans para superfícies, rochas e vegetação quando apropriado.
4. Packs externos somente após verificar licença e compatibilidade.

## Regra importante
Quixel Bridge existe na UE 5.8, mas é um fluxo legado/deprecated. Para novas aquisições, preferir Fab.

## Estrutura
Conteúdo de terceiros:
`Content/ThirdParty/<PackName>/...`

Conteúdo adaptado do projeto:
`Content/IlhaTropical/...`

Nunca editar diretamente um pack externo quando a alteração puder ser feita por Material Instance, Blueprint wrapper ou asset derivado.

## Categorias necessárias

### Tropical Canopy
- palmeiras;
- árvores tropicais altas;
- árvores de copa larga;
- árvores antigas/landmark;
- variações mortas/caídas.

### Understory
- arbustos;
- samambaias;
- plantas largas;
- cipós;
- mudas;
- pequenas palmeiras.

### Ground Cover
- folhas;
- capim;
- plantas baixas;
- galhos;
- detritos orgânicos.

### Geologia
- rochas pequenas;
- boulders;
- paredões;
- blocos de falésia;
- pedras molhadas;
- cavernas/overhangs.

### Superfícies
- areia seca;
- areia molhada;
- solo tropical;
- lama;
- pedra;
- musgo;
- rocha molhada.

### Água
- materiais de rio;
- espuma;
- cachoeira;
- spray/névoa;
- wetness transitions.

## Critérios técnicos de entrada
Antes de aprovar um pack:
- licença registrada;
- escala realista;
- pivôs utilizáveis;
- colisão revisável;
- materiais compatíveis com o pipeline;
- possibilidade de Nanite quando fizer sentido;
- número de materiais por mesh aceitável;
- LOD/Nanite strategy conhecida;
- sem dependência oculta de plugin pago.

## Política Megascans/Fab
Para UE 5.8.3, a janela Fab é o caminho de aquisição recomendado no Editor. Bridge pode ser usado para conteúdo já adquirido, mas não é a base nova do pipeline.

## Não fazer
- jogar todos os assets em `Content/Environment`;
- duplicar textura 4K/8K sem necessidade;
- manter colisão complexa em foliage pequeno;
- importar milhares de assets antes de validar um setor;
- usar material master diferente para cada mesh;
- distribuir foliage como Actors individuais.

## Primeira aquisição
O Setor Sul deve ser suficiente para validar o pipeline com um conjunto pequeno:
- 4-6 árvores/canopy;
- 6-10 understory;
- 6-10 ground cover;
- 8-12 rochas;
- 5-8 superfícies;
- 2-4 troncos/raízes;
- água básica.

Só expandir a biblioteca depois que esse conjunto provar qualidade e performance.
