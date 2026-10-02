#include "World/IslandRegionVolume.h"

AIslandRegionVolume::AIslandRegionVolume()
{
    SetActorEnableCollision(true);
    GetBrushComponent()->SetCollisionProfileName(TEXT("OverlapAllDynamic"));
}
