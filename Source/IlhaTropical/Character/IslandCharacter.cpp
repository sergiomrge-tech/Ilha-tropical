#include "Character/IslandCharacter.h"

#include "Camera/CameraComponent.h"
#include "Character/IslandStaminaComponent.h"
#include "GameFramework/CharacterMovementComponent.h"
#include "GameFramework/Controller.h"
#include "GameFramework/SpringArmComponent.h"
#include "Interaction/IslandInteractionComponent.h"

AIslandCharacter::AIslandCharacter()
{
    PrimaryActorTick.bCanEverTick = true;

    bUseControllerRotationPitch = false;
    bUseControllerRotationYaw = false;
    bUseControllerRotationRoll = false;

    GetCharacterMovement()->bOrientRotationToMovement = true;
    GetCharacterMovement()->RotationRate = FRotator(0.0f, 540.0f, 0.0f);
    GetCharacterMovement()->JumpZVelocity = 700.0f;
    GetCharacterMovement()->AirControl = 0.35f;
    GetCharacterMovement()->MaxWalkSpeed = WalkSpeed;
    GetCharacterMovement()->MaxWalkSpeedCrouched = CrouchedSpeed;
    GetCharacterMovement()->GetNavAgentPropertiesRef().bCanCrouch = true;

    CameraBoom = CreateDefaultSubobject<USpringArmComponent>(TEXT("CameraBoom"));
    CameraBoom->SetupAttachment(RootComponent);
    CameraBoom->TargetArmLength = 420.0f;
    CameraBoom->bUsePawnControlRotation = true;
    CameraBoom->bEnableCameraLag = true;
    CameraBoom->CameraLagSpeed = 12.0f;

    FollowCamera = CreateDefaultSubobject<UCameraComponent>(TEXT("FollowCamera"));
    FollowCamera->SetupAttachment(CameraBoom, USpringArmComponent::SocketName);
    FollowCamera->bUsePawnControlRotation = false;

    StaminaComponent = CreateDefaultSubobject<UIslandStaminaComponent>(TEXT("StaminaComponent"));
    InteractionComponent = CreateDefaultSubobject<UIslandInteractionComponent>(TEXT("InteractionComponent"));
}

void AIslandCharacter::Tick(float DeltaSeconds)
{
    Super::Tick(DeltaSeconds);
    RefreshMovementSpeed();
}

void AIslandCharacter::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{
    Super::SetupPlayerInputComponent(PlayerInputComponent);

    PlayerInputComponent->BindAxis(TEXT("MoveForward"), this, &AIslandCharacter::MoveForward);
    PlayerInputComponent->BindAxis(TEXT("MoveRight"), this, &AIslandCharacter::MoveRight);
    PlayerInputComponent->BindAxis(TEXT("Turn"), this, &AIslandCharacter::Turn);
    PlayerInputComponent->BindAxis(TEXT("LookUp"), this, &AIslandCharacter::LookUp);

    PlayerInputComponent->BindAction(TEXT("Jump"), IE_Pressed, this, &ACharacter::Jump);
    PlayerInputComponent->BindAction(TEXT("Jump"), IE_Released, this, &ACharacter::StopJumping);
    PlayerInputComponent->BindAction(TEXT("Sprint"), IE_Pressed, this, &AIslandCharacter::StartSprint);
    PlayerInputComponent->BindAction(TEXT("Sprint"), IE_Released, this, &AIslandCharacter::StopSprint);
    PlayerInputComponent->BindAction(TEXT("Crouch"), IE_Pressed, this, &AIslandCharacter::StartCrouch);
    PlayerInputComponent->BindAction(TEXT("Crouch"), IE_Released, this, &AIslandCharacter::StopCrouch);
    PlayerInputComponent->BindAction(TEXT("Interact"), IE_Pressed, this, &AIslandCharacter::Interact);
}

void AIslandCharacter::MoveForward(float Value)
{
    if (Controller && !FMath::IsNearlyZero(Value))
    {
        const FRotator Rotation = Controller->GetControlRotation();
        const FRotator YawRotation(0.0f, Rotation.Yaw, 0.0f);
        AddMovementInput(FRotationMatrix(YawRotation).GetUnitAxis(EAxis::X), Value);
    }
}

void AIslandCharacter::MoveRight(float Value)
{
    if (Controller && !FMath::IsNearlyZero(Value))
    {
        const FRotator Rotation = Controller->GetControlRotation();
        const FRotator YawRotation(0.0f, Rotation.Yaw, 0.0f);
        AddMovementInput(FRotationMatrix(YawRotation).GetUnitAxis(EAxis::Y), Value);
    }
}

void AIslandCharacter::Turn(float Value)
{
    AddControllerYawInput(Value);
}

void AIslandCharacter::LookUp(float Value)
{
    AddControllerPitchInput(Value);
}

void AIslandCharacter::StartSprint()
{
    bWantsToSprint = true;
}

void AIslandCharacter::StopSprint()
{
    bWantsToSprint = false;
    if (StaminaComponent)
    {
        StaminaComponent->SetSprinting(false);
    }
}

void AIslandCharacter::StartCrouch()
{
    bWantsToSprint = false;
    Crouch();
}

void AIslandCharacter::StopCrouch()
{
    UnCrouch();
}

void AIslandCharacter::Interact()
{
    if (InteractionComponent)
    {
        InteractionComponent->TryInteract(FollowCamera);
    }
}

void AIslandCharacter::RefreshMovementSpeed()
{
    UCharacterMovementComponent* Movement = GetCharacterMovement();
    if (!Movement || !StaminaComponent)
    {
        return;
    }

    const bool bMoving = GetVelocity().SizeSquared2D() > 25.0f;
    const bool bCanSprintNow = bWantsToSprint && !bIsCrouched && bMoving && StaminaComponent->CanSprint();

    StaminaComponent->SetSprinting(bCanSprintNow);

    if (bIsCrouched)
    {
        Movement->MaxWalkSpeed = CrouchedSpeed;
    }
    else
    {
        Movement->MaxWalkSpeed = bCanSprintNow ? SprintSpeed : WalkSpeed;
    }
}
