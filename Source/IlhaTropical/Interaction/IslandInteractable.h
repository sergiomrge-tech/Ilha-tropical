#pragma once

#include "CoreMinimal.h"
#include "UObject/Interface.h"
#include "IslandInteractable.generated.h"

UINTERFACE(BlueprintType)
class ILHATROPICAL_API UIslandInteractable : public UInterface
{
    GENERATED_BODY()
};

class ILHATROPICAL_API IIslandInteractable
{
    GENERATED_BODY()

public:
    UFUNCTION(BlueprintNativeEvent, BlueprintCallable, Category="Interaction")
    void Interact(AActor* Interactor);

    UFUNCTION(BlueprintNativeEvent, BlueprintCallable, Category="Interaction")
    FText GetInteractionText() const;
};
