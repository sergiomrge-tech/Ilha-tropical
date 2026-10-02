#include "Game/IslandGameMode.h"
#include "Character/IslandCharacter.h"

AIslandGameMode::AIslandGameMode()
{
    DefaultPawnClass = AIslandCharacter::StaticClass();
}
