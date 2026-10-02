#include "Interaction/IslandInteractionComponent.h"

#include "Camera/CameraComponent.h"
#include "Interaction/IslandInteractable.h"
#include "Engine/World.h"

UIslandInteractionComponent::UIslandInteractionComponent()
{
    PrimaryComponentTick.bCanEverTick = false;
}

AActor* UIslandInteractionComponent::FindInteractable(UCameraComponent* ViewCamera) const
{
    if (!ViewCamera || !GetWorld())
    {
        return nullptr;
    }

    const FVector Start = ViewCamera->GetComponentLocation();
    const FVector End = Start + ViewCamera->GetForwardVector() * InteractionRange;

    FCollisionQueryParams QueryParams(SCENE_QUERY_STAT(IslandInteraction), false, GetOwner());
    FHitResult Hit;

    if (!GetWorld()->LineTraceSingleByChannel(Hit, Start, End, TraceChannel, QueryParams))
    {
        return nullptr;
    }

    AActor* HitActor = Hit.GetActor();
    if (HitActor && HitActor->GetClass()->ImplementsInterface(UIslandInteractable::StaticClass()))
    {
        return HitActor;
    }

    return nullptr;
}

bool UIslandInteractionComponent::TryInteract(UCameraComponent* ViewCamera)
{
    AActor* Target = FindInteractable(ViewCamera);
    if (!Target)
    {
        return false;
    }

    IIslandInteractable::Execute_Interact(Target, GetOwner());
    return true;
}
