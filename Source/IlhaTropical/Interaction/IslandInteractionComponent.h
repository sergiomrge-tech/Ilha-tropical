#pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "IslandInteractionComponent.generated.h"

class UCameraComponent;

UCLASS(ClassGroup=(Island), meta=(BlueprintSpawnableComponent))
class ILHATROPICAL_API UIslandInteractionComponent : public UActorComponent
{
    GENERATED_BODY()

public:
    UIslandInteractionComponent();

    UFUNCTION(BlueprintCallable, Category="Interaction")
    bool TryInteract(UCameraComponent* ViewCamera);

    UFUNCTION(BlueprintCallable, Category="Interaction")
    AActor* FindInteractable(UCameraComponent* ViewCamera) const;

protected:
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category="Interaction", meta=(ClampMin="50.0"))
    float InteractionRange = 350.0f;

    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category="Interaction")
    TEnumAsByte<ECollisionChannel> TraceChannel = ECC_Visibility;
};
