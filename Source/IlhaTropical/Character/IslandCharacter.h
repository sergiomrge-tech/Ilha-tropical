#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Character.h"
#include "IslandCharacter.generated.h"

class UCameraComponent;
class USpringArmComponent;

UCLASS()
class ILHATROPICAL_API AIslandCharacter : public ACharacter
{
    GENERATED_BODY()

public:
    AIslandCharacter();

protected:
    virtual void SetupPlayerInputComponent(UInputComponent* PlayerInputComponent) override;

private:
    UPROPERTY(VisibleAnywhere, Category = "Camera")
    TObjectPtr<USpringArmComponent> CameraBoom;

    UPROPERTY(VisibleAnywhere, Category = "Camera")
    TObjectPtr<UCameraComponent> FollowCamera;

    void MoveForward(float Value);
    void MoveRight(float Value);
    void Turn(float Value);
    void LookUp(float Value);
};
