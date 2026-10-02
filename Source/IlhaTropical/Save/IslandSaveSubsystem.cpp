#include "Save/IslandSaveSubsystem.h"

#include "GameFramework/Pawn.h"
#include "Kismet/GameplayStatics.h"
#include "Save/IslandSaveGame.h"

const FString UIslandSaveSubsystem::SlotName(TEXT("IslandMain"));

bool UIslandSaveSubsystem::SavePlayerState(APlayerController* PlayerController, FName CurrentRegionId)
{
    if (!PlayerController)
    {
        return false;
    }

    APawn* Pawn = PlayerController->GetPawn();
    if (!Pawn)
    {
        return false;
    }

    UIslandSaveGame* SaveObject = Cast<UIslandSaveGame>(
        UGameplayStatics::CreateSaveGameObject(UIslandSaveGame::StaticClass()));

    if (!SaveObject)
    {
        return false;
    }

    SaveObject->PlayerTransform = Pawn->GetActorTransform();
    SaveObject->CurrentRegionId = CurrentRegionId;

    if (const UWorld* World = GetWorld())
    {
        SaveObject->TotalPlaySeconds = World->GetTimeSeconds();
    }

    return UGameplayStatics::SaveGameToSlot(SaveObject, SlotName, UserIndex);
}

bool UIslandSaveSubsystem::LoadPlayerState(APlayerController* PlayerController)
{
    if (!PlayerController || !HasSave())
    {
        return false;
    }

    UIslandSaveGame* SaveObject = Cast<UIslandSaveGame>(
        UGameplayStatics::LoadGameFromSlot(SlotName, UserIndex));

    APawn* Pawn = PlayerController->GetPawn();
    if (!SaveObject || !Pawn)
    {
        return false;
    }

    Pawn->SetActorTransform(SaveObject->PlayerTransform, false, nullptr, ETeleportType::TeleportPhysics);
    return true;
}

bool UIslandSaveSubsystem::HasSave() const
{
    return UGameplayStatics::DoesSaveGameExist(SlotName, UserIndex);
}

bool UIslandSaveSubsystem::DeleteSave()
{
    return UGameplayStatics::DeleteGameInSlot(SlotName, UserIndex);
}
