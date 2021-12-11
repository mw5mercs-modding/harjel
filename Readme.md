# Mechwarrior 5 Mod: The Equipment Collection formerly known as HarJel

This mod adds additional equipments to the game which can be installed into individual locations.

- **HarJel I, II, III** - Self-Repair systems. Upon taking damage they will repair armor and structure in their install location for a certain amount of time. Install a total of 7 HarJel systems to make the entire mech self-repair. Different HarJel tiers cannot be combined, also they cannot be installed in the head (lore forbids it!).
- **Modular Armor Mk1 - Mk4** - Armor upgrades which add a fixed amount of armor to their installation location. Variants for rear armor are included. Different tiers for different weight classes.
- **Patchwork T1 - T3** - provide a small amount of weight in exchange for some slots. Because Patchwork is awesome.
- **Black Carapace** - Find it, cower in its presence.
- **Advanced Targetting Computers** - TC upgrades which weigh a ton but add considerable upgrades for different weapon systems.

## Requirements

The HarJel mod depends on YetAnotherMechLab (YAML). It makes use of the extended equipment property system provided by YAML. In fact, the requirements I
had for Harjel let me to develop the equipment properties system in the first place. See below for details.

## Mod Compatibility

HarJel overrides `AbstractMech` in order to trigger the self-repair when taking damage. Thus, it is incompatible with any mod changing it as well.

## Developer Notes

### Equipment Configuration

HarJel makes use of the equipment properties system in YAML. 

YAML supports the configuration of custom equipment via json files called `Equipment_properties.json`. It will load any such files stored
in the main folder of any enabled mod. The files will be loaded in the order of mod priority. That means for example that the values for a specific equipment from a mod with a load order of 7 will overwrite the values for that particular equipment from a mod with load order 6.

These files can contain one entry for each custom equipment (or a type of equipment by using a gameplay tag path which will be mapped non-exact) with a bunch of different properties as described below.

Originally the properties were designed for equipments only. Since then some have been extended to also work with weapons. These are marked in the "W" column as seen below.

YAML by itself already provides the following properties:

|Property|Description|Example|E|W|
|---|---|---|---|---|
|`description`|Because it is annoying to edit the desciption in the asset all the time, and also: newlines!|`"One line\nanother line."`|x|o|
|`rarity`|Define the rarity of an equipment between 0 and 1. The rarity directly sets the probability the item will show up in markets.|`0.2`|x|o|
|`loreAccurate`|States whether the equipment can be found in the lore. If not and configuration entry `loreAbidingCitizen` is `true` then the equipment will never show up in markets. Defaults to `true`|`false`|x|o|
|`maxTonnage`|This equipment can only be equipped to a mech whose tonnage does not exceed this value.|`"35"`|x|o|
|`minTonnage`|This equipment can only be equipped to a mech whose tonnage matches at least this value.|`"80"`|x|o|
|`color`|Set the color of the equipment in the market and mechlab as an RGBA value.|`"(R=0.59,G=0.03,B=0.11,A=1)"`|x|o|
|`category`|Allows to set the category of the equipment. One would typically use this on equipments which have the "generic" type `Heatsink.Single`. Can be one of: `equipment.misc`, `equipment.engine`, `equipment.internal` and `equipment.ammo`. Be aware that setting the category this way means that the equipment will always be shown, independent of the value of the "valid only" checkbox.|`"equipment.internal"`|x|o|
|`invalidMechParts`|A list of mech parts the equipment can not be installed in. Possible values are: `Head`, `LeftArm`, `LeftTorso`, `LeftLeg`, etc..|`[ "CenterTorso" ]`|x|x|
|`mechPartConflicts`|A list of equipments which cannot be installed in the same location as this equipment.|`["HARJEL_II", "HARHEL_III"]`|x|x|
|`mechConflicts`|A list of equipments which cannot be installed in the mech in combination with this equipment.|`["HARJEL_II", "HARHEL_III"]`|x|x|
|`mechPartRequirements`|A list of equipments which need to be installed in the same location as this equipment. This can be either equipment names or tag names.|`GuardianECM` or `Equipment.ECM`|x|x|
|`mechRequirements`|A list of equipments which need to be installed in the mech in combination with this equipment. This can be either equipment names or tag names.|`GuardianECM` or `Equipment.ECM`|x|x|
|`armorComponentFront`|An absolute value that is added to the armor of the mech part the equipment is installed in.|`"35"`|x|o|
|`armorComponentRear`|An absolute value that is added to the rear armor of the mech part the equipment is installed in..|`"35"`|x|o|
|`armorComponentFrontMulti`|A multiplier that is applied to the mech front armor of the mech part the equipment is installed in.|`"1.1"`|x|o|
|`armorComponentRearMulti`|A multiplier that is applied to the rear armor of the mech part the equipment is installed in.|`"1.2"`|x|o|
|`armorMulti`|A multiplier that is applied to the entire mech's armor.|`"2.0"`|x|o|
|`structureComponent`|An absolute value that is added to the structure of the mech part the equipment is installed in.|`"35"`|x|o|
|`structureComponentMulti`|A multiplier that is applied to the structure of the mech part the equipment is installed in.|`"1.1"`|x|o|
|`structureMulti`|A multiplier that is applied to the entire mech's structure.|`"2.0"`|x|o|
|`relativeWeight`|Sets the equipment weight to a multiple of the mech's max tonnage. This should be paired with a 0 weight in the equipment asset. Special case: Gyros, here the multiplicator refers to the weight of a standard Gyro.|`"0.05"`|x|o|
|`engineRelativeWeight`|Sets the equipment weight to a multiple of the mech's engine weight, rounded up to the next half-ton.|`0.1`|x|o|
|`armorWeightMulti`|A multiplicator for an armor upgrade. Does only make sense for armor equipments (type tags starting with `Internal.Armor`) and is typically combined with `armorMulti`. An example would be Hardened armor which uses a multi of `2.0` in combination with ab `armorMulti` of `2.0`. Alternatively `armorPerTon` can be used.|`2.0`|x|o|
|`armorPerTon`|The amount of armor points one ton yields. Does only make sense for armor equipments (type tags starting with `Internal.Armor`). An example would be Hardened armor which uses a value of `64` in combination with ab `armorMulti` of `2.0`. An alternative to `armorWeightMulti` with a higher priority.|`64`|x|o|
|`structureWeightMulti`|A multiplicator for a structure upgrade. Does only make sense for structure equipments (type tags starting with `Internal.Structure`) and is typically combined with `structureMulti`. An example would be Endosteel which uses a multi of `0.5` to reduce the weight of the structure by 50%.|`"0.5"`|x|o|
|`fillerSlots`|Allows to define the dynamic and fixed fillers an equipment requires. The value is a map which contains any of the following keys: `dynamic` refers to the number of dynamic fillers which can be placed anywhere (a typical example is endo). `Head`, `LeftArm`, `LeftTorso`, `LeftLeg`, etc. refer to the fixed fillers required in specific mech parts. One example is 2 slots in the center torso for an XL Gyro.|`{ "CenterTorso": 2 }`|x|o|
|`torsoTwistAngleMulti`|Changes the torso twist angle (how far can the torso turn) via a multiplier. This is typically used on Gyros.|`1.10`|x|o|
|`torsoTwistRateMulti`|Changes the torso twist rate (how fast can the torso turn) via a multiplier. This is typically used on Gyros.|`1.10`|x|o|
|`topSpeedMulti`|Change the top speed of the mech by this multiplier.|`1.1`|x|o|
|`topSpeedReverseMulti`|Change the top reverse speed of the mech by this multiplier (or slower).|`1.1`|x|o|
|`accelerationMulti`|Change the acceleration for the mech by this multiplier. Get fast faster (or slower).|`1.1`|x|o|
|`decelerationMulti`|Change the deceleration for the mech by this multiplier. Get slow faster (or slower).|`1.1`|x|o|
|`turnSpeedMulti`|Change the turn speed of the mech by this multiplier. Turn corners faster (or slower).|`1.1`|x|o|
|`sensorRangeBonus`|A fixed bonus to the sensor range in meters.|`2000`|x|o|
|`sensorRangeMulti`|A multiplier for the sensor range.|`1.5`|x|o|
|`sensorFov`|The value of the sensor's field of view in degrees. Use `360` for the ultimate sensor upgrade.|`360`|x|o|
|`maxJumpJetsMulti`|A multiplicator for the maximum number of jump jets. Only useful on jumpjet equipment. Caution: the first encountered value will be used. Thus, make sure jump jets with different max multis cannot be combined (using `mechConflicts`). An example would be `1.5` for improved jump jets.|`1.5`|x|o|
|`installCost`|Overwrites the install cost defined in the asset.|`20000`|x|o|
|`removeCost`|Overwrites the remove cost defined in the asset.|`20000`|x|o|
|`installCostScaling`|Defines an installation (and removal) cost scaling based on the max mech tonnage. The value defines the multiplier for a 100 ton mech while a 20 ton mech will always set a multiplier of 1.|`10`|x|o|
|`weapons`|A json object containing weapon bonus properties as described below.||x|o|

In addition to the equipment properties provided by YAML the HarJel mod adds the following:

|Property|Description|Default|Example|
|---|---|---|---|
|`selfRepairArmor`|The amount of armor the equipment repairs at each interval.|`"0"`|`"2"`|
|`selfRepairStructure`|The amount of structure the equipment repairs at each interval.|`"0"`|`"0.5"`|
|`selfRepairDuration`|The duration of self-repair after taking damage on the self-repair enabled mech part (in seconds).|`"0"`|`"5"`|
|`selfRepairInterval`|The interval at which self-repair will be performed (in seconds).|`"1"`|`"0.5"`|
|`selfRepairScope`|The scope of the self-repair equipment. Can be either `component` to only repair the install location or `mech` to repair the entire mech (excluding the head).|`"component"`|`"mech"`|

### Equipment weapon Modifier Properties

The following bonus properties can be specified in the `weapons` section of an equipment.

|Property|Description|Example|
|---|---|---|
|`traceDurationMulti`||``|
|`traceDamageMulti`||``|
|`traceCooldownMulti`||``|
|`traceHeatMulti`||``|
|`traceOptimalRangeMulti`||``|
|`traceMaxRangeMulti`||``|
|`ballisticSpreadRadiusMulti`||``|
|`ballisticSpreadDistanceMulti`||``|
|`ballisticSpeedMulti`||``|
|`ballisticDamageMulti`||``|
|`ballisticCooldownMulti`||``|
|`ballisticHeatMulti`||``|
|`ballisticNullRangeMulti`||``|
|`ballisticMinRangeMulti`||``|
|`ballisticOptimalRangeMulti`||``|
|`ballisticMaxRangeMulti`||``|
|`ppcSpreadRadiusMulti`||``|
|`ppcSpreadDistanceMulti`||``|
|`ppcSpeedMulti`||``|
|`ppcDamageMulti`||``|
|`ppcCooldownMulti`||``|
|`ppcHeatMulti`||``|
|`ppcNullRangeMulti`||``|
|`ppcMinRangeMulti`||``|
|`ppcOptimalRangeMulti`||``|
|`ppcMaxRangeMulti`||``|
|`missleSpreadRadiusMulti`||``|
|`missleSpreadDistanceMulti`||``|
|`missleSpeedMulti`||``|
|`missleDamageMulti`||``|
|`missleCooldownMulti`||``|
|`missleHeatMulti`||``|
|`missileNullRangeMulti`||``|
|`missileMinRangeMulti`||``|
|`missileOptimalRangeMulti`||``|
|`missileMaxRangeMulti`||``|
|`lockonTimeMulti`||``|

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

If you read until here, congrats, you can now go ahead and make your own self-repair equipment which can only be installed in the left leg, adds a total armor of 400, repairs 42 points of armor every 10 seconds for 2 hours, and is presented in a bright unicorn pink in the mechlab.
