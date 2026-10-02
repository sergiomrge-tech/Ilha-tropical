using UnrealBuildTool;
using System.Collections.Generic;

public class IlhaTropicalEditorTarget : TargetRules
{
    public IlhaTropicalEditorTarget(TargetInfo Target) : base(Target)
    {
        Type = TargetType.Editor;
        DefaultBuildSettings = BuildSettingsVersion.Latest;
        IncludeOrderVersion = EngineIncludeOrderVersion.Latest;
        ExtraModuleNames.Add("IlhaTropical");
    }
}
