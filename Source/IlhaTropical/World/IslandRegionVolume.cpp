#include "World/IslandRegionVolume.h"

#include "Components/BrushComponent.h"

AIslandRegionVolume::AIslandRegionVolume()
{
    SetActorEnableCollision(true);

    if (UBrushComponent* LocalBrushComponent = GetBrushComponent())
    {
        LocalBrushComponent->SetCollisionProfileName(TEXT("OverlapAllDynamic"));
    }
}
