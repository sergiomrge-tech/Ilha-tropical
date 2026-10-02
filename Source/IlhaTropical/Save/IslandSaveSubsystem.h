#pragma once

#include "CoreMinimal.h"
#include "Subsystems/GameInstanceSubsystem.h"
#include "IslandSaveSubsystem.generated.h"

class APlayerController;
class UIslandSaveGame;

UCLASS()
class ILHATROPICAL_API UIslandSaveSubsystem : public UGameInstanceSubsystem
{
    GENERATED_BODY()

public:
    UFUNCTION(BlueprintCallable, Category="Save")
    bool SavePlayerState(APlayerController* PlayerController, FName CurrentRegionId = NAME_None);

    UFUNCTION(BlueprintCallable, Category="Save")
    bool LoadPlayerState(APlayerController* PlayerController);

    UFUNCTION(BlueprintPure, Category="Save")
    bool HasSave() const;

    UFUNCTION(BlueprintCallable, Category="Save")
    bool DeleteSave();

private:
    static constexpr int32 UserIndex = 0;
    static const FString SlotName;
};
