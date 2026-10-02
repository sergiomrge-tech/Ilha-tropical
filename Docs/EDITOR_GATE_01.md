# Editor Gate 01 - UE 5.8.3

## Objetivo
Transformar a base textual/versionavel em um projeto real validado no Unreal Editor 5.8.3.

## Entrada
- branch main limpa;
- CI verde;
- UE 5.8.3 confirmada por Engine/Build/Build.version;
- Visual Studio toolchain funcional;
- terrain artifact 4033 da versão v3 ou heightmap gerado localmente.

## Sequencia

### 1. Bootstrap
    .\Tools\Bootstrap-Project.ps1

### 2. Build
    .\Tools\Build-Editor.ps1

Gate: zero erros de compilacao.

### 3. Abrir Editor
    .\Tools\Open-Editor.ps1 -NoCompile

Gate: projeto abre sem missing module/plugin obrigatorio.

### 4. Criar mapa
- criar Open World;
- nome: /Game/IlhaTropical/World/Maps/L_Island_Main;
- World Partition habilitado;
- One File Per Actor habilitado.

### 5. Importar terrain v1
- Heightmap 4033;
- 63 quads/section;
- 2x2 sections/component;
- 32x32 components;
- XY Scale 154.324;
- Z Scale 500.

Gate: tamanho medido proximo a 6.222 km por lado e área emersa aproximada de 20 km².

### 6. Water baseline
- WaterBodyOcean em torno de Z=0;
- nenhuma decisao de shader final nesta etapa;
- verificar intersecao da costa.

### 7. Character baseline
- usar AIslandCharacter como pawn;
- adicionar mesh/animacao temporaria apenas para validar escala se necessario;
- testar WASD, mouse, salto, sprint/stamina, crouch e interact trace.

### 8. Enhanced Input migration
O binding legado atual existe apenas para bootstrap textual.
No primeiro gate do Editor criar assets:
- IMC_Player;
- IA_Move;
- IA_Look;
- IA_Jump;
- IA_Sprint;
- IA_Crouch;
- IA_Interact.

Depois migrar AIslandCharacter para Enhanced Input e remover os mappings legados.

### 9. Setor Sul
- marcar coordenadas VS01-VS08;
- testar escala e desnivel;
- nao adicionar foliage final antes de a rota funcionar.

### 10. Evidencia
Salvar:
- log de build;
- screenshot real do Editor;
- dimensoes do Landscape;
- erros/warnings relevantes;
- FPS apenas depois de haver conteudo representativo.

## Saida
Gate 01 so fica APPROVED quando compilacao e Editor 5.8.3 forem realmente executados. CI textual nao substitui esse gate.