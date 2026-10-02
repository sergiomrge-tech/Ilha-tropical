from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "IlhaTropical.uproject",
    "AGENTS.md",
    "Config/DefaultEngine.ini",
    "Config/DefaultGame.ini",
    "Config/DefaultInput.ini",
    "Source/IlhaTropical.Target.cs",
    "Source/IlhaTropicalEditor.Target.cs",
    "Source/IlhaTropical/IlhaTropical.Build.cs",
    "Source/IlhaTropical/IlhaTropical.cpp",
    "Source/IlhaTropical/Character/IslandCharacter.h",
    "Source/IlhaTropical/Character/IslandCharacter.cpp",
    "Source/IlhaTropical/Character/IslandStaminaComponent.h",
    "Source/IlhaTropical/Character/IslandStaminaComponent.cpp",
    "Source/IlhaTropical/Interaction/IslandInteractable.h",
    "Source/IlhaTropical/Interaction/IslandInteractionComponent.h",
    "Source/IlhaTropical/Interaction/IslandInteractionComponent.cpp",
    "Source/IlhaTropical/Game/IslandGameMode.h",
    "Source/IlhaTropical/Game/IslandGameMode.cpp",
    "Docs/ENGINE_BASELINE.md",
    "Docs/WORLD_DESIGN.md",
    "Docs/LEVEL_DESIGN.md",
    "Docs/TERRAIN_PIPELINE.md",
    "Docs/ROADMAP.md",
    "Docs/AI_SKILLS.md",
    "Data/World/island_terrain_v1.json",
    "Data/World/island_sectors_v1.json",
    "Scripts/terrain/generate_island_heightmap.py",
]

FORBIDDEN_TRACKED_DIRS = {
    "Binaries",
    "DerivedDataCache",
    "Intermediate",
    "Saved",
    ".vs",
    "Generated",
}

REQUIRED_PLUGINS = {"EnhancedInput", "PCG", "Landmass", "Water"}


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    raise SystemExit(1)


def ok(message: str) -> None:
    print(f"[ OK ] {message}")


def load_json(relative_path: str):
    try:
        return json.loads((ROOT / relative_path).read_text(encoding="utf-8-sig"))
    except Exception as exc:
        fail(f"{relative_path} invalido: {exc}")


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        fail("Arquivos obrigatorios ausentes: " + ", ".join(missing))
    ok(f"{len(REQUIRED_FILES)} arquivos obrigatorios encontrados")

    project = load_json("IlhaTropical.uproject")
    if str(project.get("EngineAssociation", "")).split(".")[:2] != ["5", "8"]:
        fail("EngineAssociation precisa apontar para a familia UE 5.8")
    ok("EngineAssociation = UE 5.8 family")

    baseline = (ROOT / "Docs/ENGINE_BASELINE.md").read_text(encoding="utf-8-sig")
    if "Unreal Engine 5.8.3" not in baseline:
        fail("Baseline precisa fixar Unreal Engine 5.8.3")
    ok("Engine baseline = UE 5.8.3")

    modules = {m.get("Name") for m in project.get("Modules", [])}
    if "IlhaTropical" not in modules:
        fail("Modulo runtime IlhaTropical ausente do .uproject")
    ok("Modulo IlhaTropical registrado")

    enabled_plugins = {
        p.get("Name")
        for p in project.get("Plugins", [])
        if p.get("Enabled") is True
    }
    missing_plugins = sorted(REQUIRED_PLUGINS - enabled_plugins)
    if missing_plugins:
        fail("Plugins obrigatorios nao habilitados: " + ", ".join(missing_plugins))
    ok("Plugins base habilitados: " + ", ".join(sorted(REQUIRED_PLUGINS)))

    tracked_top_level = {p.name for p in ROOT.iterdir()}
    bad = sorted(FORBIDDEN_TRACKED_DIRS & tracked_top_level)
    if bad:
        fail("Diretorios gerados presentes na raiz: " + ", ".join(bad))
    ok("Nenhum diretorio gerado proibido na raiz")

    build_cs = (ROOT / "Source/IlhaTropical/IlhaTropical.Build.cs").read_text(encoding="utf-8-sig")
    for dep in ("Core", "CoreUObject", "Engine", "InputCore", "EnhancedInput"):
        if f'"{dep}"' not in build_cs:
            fail(f"Dependencia {dep} ausente do Build.cs")
    ok("Dependencias C++ basicas conferidas")

    character_cpp = (ROOT / "Source/IlhaTropical/Character/IslandCharacter.cpp").read_text(encoding="utf-8-sig")
    for marker in (
        "USpringArmComponent",
        "UCameraComponent",
        "Sprint",
        "Crouch",
        "InteractionComponent",
        "StaminaComponent",
    ):
        if marker not in character_cpp:
            fail(f"Personagem base sem marcador esperado: {marker}")
    ok("Exploracao base: camera, sprint, crouch, stamina e interacao")

    world_design = (ROOT / "Docs/WORLD_DESIGN.md").read_text(encoding="utf-8-sig")
    for marker in ("20 km", "montanha central", "World Partition", "PCG", "relevo"):
        if marker.lower() not in world_design.lower():
            fail(f"World design sem requisito: {marker}")
    ok("World design preserva escala, densidade e relevo")

    terrain = load_json("Data/World/island_terrain_v1.json")
    if terrain.get("engine_target") != "5.8.3":
        fail("Terrain spec precisa usar engine_target 5.8.3")
    if terrain["world"].get("heightmap_resolution") != 4033:
        fail("Terrain spec precisa preservar heightmap 4033")
    ok("Terrain spec validado")

    sectors = load_json("Data/World/island_sectors_v1.json")
    entries = sectors.get("sectors", [])
    if len(entries) < 10:
        fail("Level design precisa de pelo menos 10 setores macro")
    for sector in entries:
        for key in ("id", "name", "landmark", "primary_route", "secondary_routes", "pois"):
            if not sector.get(key):
                fail(f"Setor {sector.get('id', '?')} sem {key}")
    ok(f"{len(entries)} setores de level design possuem rotas, landmarks e POIs")

    print("\nVALIDATION OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
