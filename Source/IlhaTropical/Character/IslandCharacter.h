#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Character.h"
#include "IslandCharacter.generated.h"

class UCameraComponent;
class UIslandInteractionComponent;
class UIslandStaminaComponent;
class USpringArmComponent;

UCLASS()
class ILHATROPICAL_API AIslandCharacter : public ACharacter
{
    GENERATED_BODY()

public:
    AIslandCharacter();

    virtual void Tick(float DeltaSeconds) override;

    UFUNCTION(BlueprintPure, Category="Character|Stamina")
    UIslandStaminaComponent* GetStaminaComponent() const { return StaminaComponent; }

protected:
    virtual void SetupPlayerInputComponent(UInputComponent* PlayerInputComponent) override;

    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category="Character|Movement")
    float WalkSpeed = 500.0f;

    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category="Character|Movement")
    float SprintSpeed = 760.0f;

    UPROPERTY(EditDefaultsOnly, BlueprintReadOnly, Category="Character|Movement")
    float CrouchedSpeed = 250.0f;

private:
    UPROPERTY(VisibleAnywhere, Category="Camera")
    TObjectPtr<USpringArmComponent> CameraBoom;

    UPROPERTY(VisibleAnywhere, Category="Camera")
    TObjectPtr<UCameraComponent> FollowCamera;

    UPROPERTY(VisibleAnywhere, Category="Character|Stamina")
    TObjectPtr<UIslandStaminaComponent> StaminaComponent;

    UPROPERTY(VisibleAnywhere, Category="Character|Interaction")
    TObjectPtr<UIslandInteractionComponent> InteractionComponent;

    bool bWantsToSprint = false;

    void MoveForward(float Value);
    void MoveRight(float Value);
    void Turn(float Value);
    void LookUp(float Value);

    void StartSprint();
    void StopSprint();
    void StartCrouch();
    void StopCrouch();
    void Interact();
    void RefreshMovementSpeed();
};
