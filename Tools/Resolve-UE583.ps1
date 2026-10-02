param(
    [string]$EngineRoot = ""
)

$ErrorActionPreference = "Stop"

function Test-Engine583([string]$Root) {
    if ([string]::IsNullOrWhiteSpace($Root)) { return $false }

    $buildVersion = Join-Path $Root "Engine\Build\Build.version"
    $editor = Join-Path $Root "Engine\Binaries\Win64\UnrealEditor.exe"

    if (!(Test-Path $buildVersion) -or !(Test-Path $editor)) { return $false }

    try {
        $v = Get-Content $buildVersion -Raw | ConvertFrom-Json
        return ($v.MajorVersion -eq 5 -and $v.MinorVersion -eq 8 -and $v.PatchVersion -eq 3)
    } catch {
        return $false
    }
}

$candidates = New-Object System.Collections.Generic.List[string]

if (![string]::IsNullOrWhiteSpace($EngineRoot)) {
    $candidates.Add((Resolve-Path $EngineRoot).Path)
}

if ($env:UE_5_8_3_ROOT) { $candidates.Add($env:UE_5_8_3_ROOT) }

$candidates.Add("C:\Program Files\Epic Games\UE_5.8")
$candidates.Add("D:\Program Files\Epic Games\UE_5.8")
$candidates.Add("D:\Epic Games\UE_5.8")
$candidates.Add("E:\Epic Games\UE_5.8")

foreach ($candidate in ($candidates | Select-Object -Unique)) {
    if (Test-Engine583 $candidate) {
        Write-Output $candidate
        exit 0
    }
}

throw "Unreal Engine 5.8.3 nao encontrada. Passe -EngineRoot ou defina UE_5_8_3_ROOT."