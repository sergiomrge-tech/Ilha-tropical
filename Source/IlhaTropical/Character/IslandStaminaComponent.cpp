#include "Character/IslandStaminaComponent.h"

UIslandStaminaComponent::UIslandStaminaComponent()
{
    PrimaryComponentTick.bCanEverTick = true;
}

void UIslandStaminaComponent::BeginPlay()
{
    Super::BeginPlay();
    CurrentStamina = MaxStamina;
}

void UIslandStaminaComponent::TickComponent(
    float DeltaTime,
    ELevelTick TickType,
    FActorComponentTickFunction* ThisTickFunction)
{
    Super::TickComponent(DeltaTime, TickType, ThisTickFunction);

    if (bSprinting && CurrentStamina > 0.0f)
    {
        CurrentStamina = FMath::Max(0.0f, CurrentStamina - DrainPerSecond * DeltaTime);
        TimeSinceDrain = 0.0f;

        if (CurrentStamina <= KINDA_SMALL_NUMBER)
        {
            CurrentStamina = 0.0f;
            bSprinting = false;
            bExhausted = true;
        }
        return;
    }

    TimeSinceDrain += DeltaTime;
    if (TimeSinceDrain >= RegenDelay && CurrentStamina < MaxStamina)
    {
        CurrentStamina = FMath::Min(MaxStamina, CurrentStamina + RegenPerSecond * DeltaTime);

        if (bExhausted && CurrentStamina >= FMath::Min(SprintRestartThreshold, MaxStamina))
        {
            bExhausted = false;
        }
    }
}

void UIslandStaminaComponent::SetSprinting(bool bNewSprinting)
{
    bSprinting = bNewSprinting && CanSprint();
    if (bSprinting)
    {
        TimeSinceDrain = 0.0f;
    }
}

bool UIslandStaminaComponent::CanSprint() const
{
    return !bExhausted && CurrentStamina > 1.0f;
}

float UIslandStaminaComponent::GetStaminaNormalized() const
{
    return MaxStamina > 0.0f ? CurrentStamina / MaxStamina : 0.0f;
}
