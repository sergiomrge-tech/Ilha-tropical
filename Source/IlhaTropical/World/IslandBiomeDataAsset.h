#pragma once

#include "CoreMinimal.h"
#include "Engine/DataAsset.h"
#include "IslandBiomeDataAsset.generated.h"

UCLASS(BlueprintType)
class ILHATROPICAL_API UIslandBiomeDataAsset : public UPrimaryDataAsset
{
    GENERATED_BODY()

public:
    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category="Biome")
    FName BiomeId = NAME_None;

    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category="Biome")
    FText DisplayName;

    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category="Biome|Terrain")
    FVector2D ElevationRangeMeters = FVector2D(0.0f, 1200.0f);

    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category="Biome|Terrain")
    FVector2D SlopeRangeDegrees = FVector2D(0.0f, 45.0f);

    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category="Biome|Density", meta=(ClampMin="0.0", ClampMax="2.0"))
    float CanopyDensity = 1.0f;

    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category="Biome|Density", meta=(ClampMin="0.0", ClampMax="2.0"))
    float UnderstoryDensity = 1.0f;

    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category="Biome|Density", meta=(ClampMin="0.0", ClampMax="2.0"))
    float GroundCoverDensity = 1.0f;

    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category="Biome|Density", meta=(ClampMin="0.0", ClampMax="2.0"))
    float RockDensity = 0.5f;

    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category="Biome")
    bool bAllowLargeTrees = true;

    UPROPERTY(EditAnywhere, BlueprintReadOnly, Category="Biome")
    bool bWetBiome = false;
};
