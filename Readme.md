# Mechwarrior 5 Mod: HarJel

This mod adds additional armor upgrades to the game which can be installed into individual locations.

- Modular Armor Mk1 - Mk4: Armor upgrades which add a fixed amount of armor to their installation location. Variants for rear armor are included.
- HarJel I, II, III - Self-Repair systems. Upon taking damage they will repair armor and structure in their install location for a certain amount of time. Install a total of 7 HarJel systems to make the entire mech self-repair.
- Patchwork T1 to T3 which provide a small amount of weight in exchange for some slots.

## Requirements

The HarJel mod depends on YetAnotherMechLab (YAML). It makes use of the extended equipment property system provided by YAML. In fact, the requirements I
had for Harjel let me to develop the equipment properties system in the first place. See below for details.

## Developer Notes

### Equipment Configuration

HarJel makes use of the equipment properties system in YAML. YAML will look for a file called `Equipment_properties.json` in each enabled mod's
root folder and read its contents. YAML will then enforce a variety of properties defined in the json file which are keyed to equipment names. This
allows adding new equipments which are simply typed as `Heatsink.Single` (remember to set the cooling to 0) and control a variety of properties via
the json file.

YAML by itself already provides the following properties:

|Property|Description|Example|
|---|---|---|
|`maxTonnage`|This equipment can only be equipped to a mech whose tonnage does not exceed this value.|`"35"`|
|`minTonnage`|This equipment can only be equipped to a mech whose tonnage matches at least this value.|`"80"`|
|`color`|Set the color of the equipment in the market and mechlab as an RGBA value.|`"(R=0.59,G=0.03,B=0.11,A=1)"`|
|`category`|Allows to set the category of the equipment. One would typically use this on equipments which have the "generic" type `Heatsink.Single`. Can be one of: `equipment.misc`, `equipment.engine`, `equipment.internal` and `equipment.ammo`. Be aware that setting the category this way means that the equipment will always be shown, independent of the value of the "valid only" checkbox.|`"equipment.internal"`|
|`invalidMechParts`|A list of mech parts the equipment can not be installed in. Possible values are: `Head`, `LeftArm`, `LeftTorso`, `LeftLeg`, etc..|`[ "CenterTorso" ]`|
|`mechPartConflicts`|A list of equipments which cannot be installed in the same location as this equipment.|`["HARJEL_II", "HARHEL_III"]`|
|`mechConflicts`|A list of equipments which cannot be installed in the mech in combination with this equipment.|`["HARJEL_II", "HARHEL_III"]`|
|`armorComponentFront`|An absolute value that is added to the mech part's front armor.|`"35"`|
|`armorComponentRear`|An absolute value that is added to the mech part's rear armor.|`"35"`|
|`armorComponentMultiFront`|A multiplier that is applied to the mech part's front armor.|`"1.1"`|
|`armorComponentMultiRear`|A multiplier that is applied to the mech part's rear armor.|`"1.2"`|
|`armorMulti`|A multiplier that is applied to the entire mech's armor.|`"2.0"`|


In addition to the equipment properties provided by YAML the HarJel mod adds the following:

|Property|Description|Default|Example|
|---|---|---|---|
|`selfRepairArmor`|The amount of armor the equipment repairs at each interval.|`"0"`|`"2"`|
|`selfRepairStructure`|The amount of structure the equipment repairs at each interval.|`"0"`|`"0.5"`|
|`selfRepairDuration`|The duration of self-repair after taking damage on the self-repair enabled mech part (in seconds).|`"0"`|`"5"`|
|`selfRepairInterval`|The interval at which self-repair will be performed (in seconds).|`"1"`|`"0.5"`|
|`selfRepairScope`|The scope of the self-repair equipment. Can be either `component` to only repair the install location or `mech` to repair the entire mech (excluding the head).|`"component"`|`"mech"`|

### Example

```json
{
	"HARJEL_I": {
		"armorComponentFrontMulti": "1.1",
		"armorComponentRearMulti": "1.1",
		"selfRepairComponentArmor": "1",
		"selfRepairComponentStructure": "0.5",
		"selfRepairComponentDuration": "5",
		"mechPartConflicts": [
			"HARJEL_I"
		],
		"mechConflicts": [
			"HARJEL_II",
			"HARJEL_III"
		],
		"invalidMechParts": [
			"Head"
		],
		"color": "(R=0.11,G=0.19,B=0.77,A=0.5)",
		"category": "equipment.internal"
	}
}
```

## TODO
- Harjel equipment destruction should set self-repair values to 0. Probably not that important since a damaged harjel will blow up, most likely taking the component with it. But still...
