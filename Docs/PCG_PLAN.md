# PCG Production Plan — UE 5.8.3

## Princípio
PCG é usado para construir a primeira camada do ambiente, nunca para substituir o passe de level design.

## Hierarquia de graphs

### PCG_Island_Master
Responsável apenas por coordenar subgraphs por biome/region. Não deve concentrar toda a lógica em um graph monolítico.

Subgraphs previstos:
- PCG_Canopy
- PCG_Understory
- PCG_GroundCover
- PCG_Rocks
- PCG_Deadfall
- PCG_RiverBanks
- PCG_Beach
- PCG_Cliffs
- PCG_Mangrove

## Filtros obrigatórios
Todo graph de scatter deve considerar, quando aplicável:
- altitude;
- slope;
- distância da água;
- distância das trilhas;
- distância de POIs;
- region/biome;
- exclusion volumes;
- seed estável.

## Ordem de composição
1. macroterreno;
2. água;
3. rotas/trilhas;
4. POIs e landmarks;
5. rochas estruturais;
6. canopy;
7. understory;
8. ground cover;
9. deadfall e detalhes;
10. passe manual.

## Regra de trilhas
Manter corredor de exclusão em torno da rota principal. Vegetação pode invadir parcialmente a leitura visual, mas nunca bloquear fisicamente a rota por acaso.

## Regra de rios
Árvores grandes não devem nascer no canal principal. Usar faixa de transição com vegetação ripária, raízes, pedras e cobertura úmida.

## Regra de encostas
- slope baixo: cobertura e vegetação maior;
- slope médio: mistura;
- slope alto: rocha exposta, vegetação esparsa;
- paredões: meshes/rochas estruturais e não apenas Landscape esticado.

## Repetição
Cada camada deve usar:
- variação de escala limitada;
- rotação coerente;
- múltiplas espécies/meshes quando os assets existirem;
- seed por setor;
- clusterização não uniforme.

## Performance
Preferir ISM/HISM/PCG-managed instancing para vegetação repetida. Actors individuais ficam reservados a objetos interativos ou únicos.

## World Partition
Graphs e componentes devem respeitar streaming/células. Conteúdo procedural persistente deve ser gerado de forma compatível com o pipeline escolhido antes do packaging.

## Aprovação
Nenhum graph será marcado como produção antes de:
- gerar sem erros;
- respeitar exclusion zones;
- não bloquear rotas;
- não colocar foliage dentro da água;
- passar inspeção de repetição;
- passar profiling no setor de referência.
