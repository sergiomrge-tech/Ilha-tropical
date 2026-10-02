# QA Matrix — Ilha Tropical

## Gate A — Repositório
Status esperado antes de qualquer teste no Editor:
- validação estática verde;
- terrain smoke test verde;
- nenhum Binaries/Intermediate/Saved versionado;
- dados de setores somam 20 km²;
- terrain v3 registrado.

## Gate B — Build UE 5.8.3
- UnrealBuildTool gera project files;
- IlhaTropicalEditor Development compila;
- zero erro C++;
- warnings relevantes documentados;
- plugins obrigatórios carregam.

## Gate C — Editor
- L_Island_Main abre;
- World Partition ativo;
- Landscape 4033 correto;
- XY 154.324;
- Z 500;
- WaterBodyOcean coerente com Z=0;
- sem referências quebradas.

## Gate D — Movimento
- WASD;
- mouse;
- jump;
- sprint;
- stamina drena/regenera;
- crouch;
- interaction trace;
- câmera sem clipping grave.

## Gate E — Streaming
Testar:
- caminhada;
- sprint contínuo;
- deslocamento por várias células;
- teleporte de desenvolvimento entre extremos.

Verificar:
- hitch;
- célula não descarregada;
- pop excessivo;
- buraco no Landscape;
- actor persistindo fora da região.

## Gate F — Setor Sul Blockout
VS01-VS08:
- percurso completo;
- sem parede invisível;
- sem salto impossível;
- sem inclinação absurda;
- rota principal legível;
- rota secundária reconhecível;
- cachoeira/mirante enquadrados.

## Gate G — PCG
- foliage não nasce dentro da água;
- rota principal preservada;
- exclusion volumes respeitados;
- seed reproduzível;
- nenhum Actor spam;
- distribuição não uniforme;
- transição entre biomas legível.

## Gate H — Performance
No setor representativo:
- alvo 60 FPS;
- Game Thread investigado;
- Render Thread investigado;
- GPU investigada;
- memória observada;
- World Partition observado;
- VSM/Lumen/foliage analisados.

Não aprovar performance em cena vazia.

## Gate I — Save/Load
- salvar posição;
- fechar/abrir;
- carregar posição;
- slot inexistente tratado;
- delete funciona;
- SaveVersion preservado.

## Evidências
Cada gate aprovado deve deixar pelo menos uma evidência:
- log;
- captura real;
- resultado de teste;
- métricas;
- commit.
