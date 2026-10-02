#pragma once

#include "CoreMinimal.h"
#include "GameFramework/SaveGame.h"
#include "IslandSaveGame.generated.h"

UCLASS()
class ILHATROPICAL_API UIslandSaveGame : public USaveGame
{
    GENERATED_BODY()

public:
    UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category="Save")
    int32 SaveVersion = 1;

    UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category="Save")
    FTransform PlayerTransform = FTransform::Identity;

    UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category="Save")
    FName CurrentRegionId = NAME_None;

    UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category="Save")
    float TotalPlaySeconds = 0.0f;
};
