#include "World/IslandRegionVolume.h"

#include "Components/BrushComponent.h"

AIslandRegionVolume::AIslandRegionVolume()
{
    SetActorEnableCollision(true);

    if (UBrushComponent* Brush = GetBrushComponent())
    {
        Brush->SetCollisionProfileName(TEXT("OverlapAllDynamic"));
    }
}
