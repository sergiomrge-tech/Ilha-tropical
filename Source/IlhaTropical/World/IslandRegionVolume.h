#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Volume.h"
#include "IslandRegionVolume.generated.h"

UCLASS(Blueprintable)
class ILHATROPICAL_API AIslandRegionVolume : public AVolume
{
    GENERATED_BODY()

public:
    AIslandRegionVolume();

    UFUNCTION(BlueprintPure, Category="Island|Region")
    FName GetRegionId() const { return RegionId; }

    UFUNCTION(BlueprintPure, Category="Island|Region")
    FName GetBiomeId() const { return BiomeId; }

protected:
    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category="Island|Region")
    FName RegionId = NAME_None;

    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category="Island|Region")
    FName BiomeId = NAME_None;

    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category="Island|Region")
    int32 RegionPriority = 0;

    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category="Island|Region")
    bool bVerticalSliceRegion = false;
};
