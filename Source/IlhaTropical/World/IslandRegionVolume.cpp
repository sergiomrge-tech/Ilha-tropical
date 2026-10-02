#include "World/IslandRegionVolume.h"

#include "Components/BrushComponent.h"

AIslandRegionVolume::AIslandRegionVolume()
{
    SetActorEnableCollision(true);

    if (UBrushComponent* BrushComponent = GetBrushComponent())
    {
        BrushComponent->SetCollisionProfileName(TEXT("OverlapAllDynamic"));
    }
}
