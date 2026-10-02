#pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "IslandStaminaComponent.generated.h"

UCLASS(ClassGroup=(Island), meta=(BlueprintSpawnableComponent))
class ILHATROPICAL_API UIslandStaminaComponent : public UActorComponent
{
    GENERATED_BODY()

public:
    UIslandStaminaComponent();

    virtual void BeginPlay() override;
    virtual void TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction) override;

    UFUNCTION(BlueprintCallable, Category="Stamina")
    void SetSprinting(bool bNewSprinting);

    UFUNCTION(BlueprintPure, Category="Stamina")
    bool CanSprint() const;

    UFUNCTION(BlueprintPure, Category="Stamina")
    float GetStaminaNormalized() const;

    UFUNCTION(BlueprintPure, Category="Stamina")
    float GetCurrentStamina() const { return CurrentStamina; }

protected:
    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category="Stamina", meta=(ClampMin="1.0"))
    float MaxStamina = 100.0f;

    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category="Stamina", meta=(ClampMin="0.0"))
    float DrainPerSecond = 18.0f;

    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category="Stamina", meta=(ClampMin="0.0"))
    float RegenPerSecond = 14.0f;

    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category="Stamina", meta=(ClampMin="0.0"))
    float RegenDelay = 1.15f;

private:
    UPROPERTY(VisibleInstanceOnly, Category="Stamina")
    float CurrentStamina = 100.0f;

    bool bSprinting = false;
    float TimeSinceDrain = 0.0f;
};
