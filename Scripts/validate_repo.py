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
    "Source/IlhaTropical/Game/IslandGameMode.h",
    "Source/IlhaTropical/Game/IslandGameMode.cpp",
    "Docs/WORLD_DESIGN.md",
    "Docs/ROADMAP.md",
    "Docs/AI_SKILLS.md",
]

FORBIDDEN_TRACKED_DIRS = {
    "Binaries",
    "DerivedDataCache",
    "Intermediate",
    "Saved",
    ".vs",
}

REQUIRED_PLUGINS = {"EnhancedInput", "PCG", "Landmass", "Water"}


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    raise SystemExit(1)


def ok(message: str) -> None:
    print(f"[ OK ] {message}")


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        fail("Arquivos obrigatorios ausentes: " + ", ".join(missing))
    ok(f"{len(REQUIRED_FILES)} arquivos obrigatorios encontrados")

    project_path = ROOT / "IlhaTropical.uproject"
    try:
        project = json.loads(project_path.read_text(encoding="utf-8-sig"))
    except Exception as exc:
        fail(f"IlhaTropical.uproject invalido: {exc}")

    if str(project.get("EngineAssociation", "")).split(".")[:2] != ["5", "8"]:
        fail("EngineAssociation precisa apontar para UE 5.8.x")
    ok("EngineAssociation = UE 5.8")

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
    for marker in ("USpringArmComponent", "UCameraComponent", "BindAxis", "BindAction"):
        if marker not in character_cpp:
            fail(f"Personagem base sem marcador esperado: {marker}")
    ok("Personagem de terceira pessoa possui camera e input basico")

    world_design = (ROOT / "Docs/WORLD_DESIGN.md").read_text(encoding="utf-8-sig")
    for marker in ("20 km", "montanha central", "World Partition", "PCG"):
        if marker.lower() not in world_design.lower():
            fail(f"World design sem requisito: {marker}")
    ok("World design preserva escala e pilares do mapa")

    print("\nVALIDATION OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
