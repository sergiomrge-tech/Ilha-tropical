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
    "Source/IlhaTropical/Save/IslandSaveGame.h",
    "Source/IlhaTropical/Save/IslandSaveSubsystem.h",
    "Source/IlhaTropical/Save/IslandSaveSubsystem.cpp",
    "Source/IlhaTropical/World/IslandBiomeDataAsset.h",
    "Source/IlhaTropical/World/IslandRegionVolume.h",
    "Source/IlhaTropical/World/IslandRegionVolume.cpp",
    "Docs/ENGINE_BASELINE.md",
    "Docs/TECHNICAL_ARCHITECTURE.md",
    "Docs/CONTENT_STRUCTURE.md",
    "Docs/WORLD_DESIGN.md",
    "Docs/LEVEL_DESIGN.md",
    "Docs/TERRAIN_PIPELINE.md",
    "Docs/PCG_PLAN.md",
    "Docs/PERFORMANCE_BUDGET.md",
    "Docs/ROADMAP.md",
    "Docs/AI_SKILLS.md",
    "Data/World/island_terrain_v1.json",
    "Data/World/island_sectors_v1.json",
    "Data/World/biome_profiles_v1.json",
    "Data/World/world_partition_v1.json",
    "Docs/WORLD_PARTITION_PLAN.md",
    "Docs/VERTICAL_SLICE_SOUTH.md",
    "Docs/LOCAL_SETUP.md",
    "Docs/EDITOR_GATE_01.md",
    "Docs/SAVE_SYSTEM.md",
    "Tools/Resolve-UE583.ps1",
    "Tools/Bootstrap-Project.ps1",
    "Tools/Build-Editor.ps1",
    "Tools/Open-Editor.ps1",
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

    save_cpp = (ROOT / "Source/IlhaTropical/Save/IslandSaveSubsystem.cpp").read_text(encoding="utf-8-sig")
    for marker in ("SaveGameToSlot", "LoadGameFromSlot", "DoesSaveGameExist", "DeleteGameInSlot"):
        if marker not in save_cpp:
            fail(f"Save subsystem sem operacao esperada: {marker}")
    ok("Save/Load foundation conferida")

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
    if abs(float(terrain["world"].get("target_land_area_km2", 0.0)) - 20.0) > 0.001:
        fail("Terrain spec precisa definir 20 km2 de area emersa")
    if int(terrain.get("generator_algorithm_version", 0)) != 3:
        fail("Terrain spec precisa usar generator_algorithm_version 3")
    ok("Terrain spec validado com 20 km2 de terra emersa")

    sectors = load_json("Data/World/island_sectors_v1.json")
    entries = sectors.get("sectors", [])
    if len(entries) < 10:
        fail("Level design precisa de pelo menos 10 setores macro")
    for sector in entries:
        for key in ("id", "name", "landmark", "primary_route", "secondary_routes", "pois"):
            if not sector.get(key):
                fail(f"Setor {sector.get('id', '?')} sem {key}")
    total_area = sum(float(sector.get("area_km2", 0.0)) for sector in entries)
    if abs(total_area - 20.0) > 0.001:
        fail(f"Areas dos setores precisam somar 20.0 km2, atual={total_area:.3f}")
    ok(f"{len(entries)} setores completos somam {total_area:.1f} km2")

    biomes = load_json("Data/World/biome_profiles_v1.json")
    biome_entries = biomes.get("biomes", [])
    if len(biome_entries) < 6:
        fail("Biomas insuficientes para variedade da ilha")
    biome_ids = [b.get("id") for b in biome_entries]
    if len(biome_ids) != len(set(biome_ids)):
        fail("Biome IDs duplicados")
    ok(f"{len(biome_entries)} perfis de bioma validos")

    partition = load_json("Data/World/world_partition_v1.json")
    landscape = partition.get("landscape", {})
    expected_quads = (
        int(landscape.get("section_size_quads", 0))
        * int(landscape.get("sections_per_component", 0))
        * int(landscape.get("components_x", 0))
    )
    if expected_quads != 4032:
        fail(f"Landscape X precisa fechar 4032 quads, atual={expected_quads}")
    expected_quads_y = (
        int(landscape.get("section_size_quads", 0))
        * int(landscape.get("sections_per_component", 0))
        * int(landscape.get("components_y", 0))
    )
    if expected_quads_y != 4032:
        fail(f"Landscape Y precisa fechar 4032 quads, atual={expected_quads_y}")
    if int(landscape.get("resolution_vertices", 0)) != expected_quads + 1:
        fail("Landscape resolution nao fecha quads + 1")
    if partition.get("engine_target") != "5.8.3":
        fail("World Partition spec precisa usar UE 5.8.3")
    if abs(float(landscape.get("xy_scale_cm", 0.0)) - 154.324) > 0.01:
        fail("XY Scale precisa permanecer 154.324 cm para ~20 km2 emergidos")
    if abs(float(landscape.get("target_emerged_land_area_km2", 0.0)) - 20.0) > 0.001:
        fail("World Partition spec precisa manter alvo de 20 km2 emergidos")
    grid = partition.get("world_partition", {})
    if int(grid.get("cell_size_m", 0)) <= 0 or int(grid.get("loading_range_m", 0)) <= 0:
        fail("World Partition cell/loading range invalidos")
    ok("Landscape 32x32 / 4033 / 154.324 cm e World Partition baseline validados")

    print("\nVALIDATION OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
