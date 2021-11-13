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

HarJel makes use of the equipment properties system in YAML. YAML will look for a file called `Equipment_properties.json` in each enabled mod's
root folder and read its contents. YAML will then enforce a variety of properties defined in the json file which are keyed to equipment names. This
allows adding new equipments which are simply typed as `Heatsink.Single` (remember to set the cooling to 0) and control a variety of properties via
the json file.

YAML by itself already provides the following properties:

|Property|Description|Example|
|---|---|---|
|`description`|Because it is annoying to edit the desciption in the asset all the time, and also: newlines!|`"One line\nanother line."`|
|`loreAccurate`|States whether the equipment can be found in the lore. If not and configuration entry `loreAbidingCitizen` is `true` then the equipment will never show up in markets. Defaults to `true`|`false`|
|`maxTonnage`|This equipment can only be equipped to a mech whose tonnage does not exceed this value.|`"35"`|
|`minTonnage`|This equipment can only be equipped to a mech whose tonnage matches at least this value.|`"80"`|
|`color`|Set the color of the equipment in the market and mechlab as an RGBA value.|`"(R=0.59,G=0.03,B=0.11,A=1)"`|
|`category`|Allows to set the category of the equipment. One would typically use this on equipments which have the "generic" type `Heatsink.Single`. Can be one of: `equipment.misc`, `equipment.engine`, `equipment.internal` and `equipment.ammo`. Be aware that setting the category this way means that the equipment will always be shown, independent of the value of the "valid only" checkbox.|`"equipment.internal"`|
|`invalidMechParts`|A list of mech parts the equipment can not be installed in. Possible values are: `Head`, `LeftArm`, `LeftTorso`, `LeftLeg`, etc..|`[ "CenterTorso" ]`|
|`mechPartConflicts`|A list of equipments which cannot be installed in the same location as this equipment.|`["HARJEL_II", "HARHEL_III"]`|
|`mechConflicts`|A list of equipments which cannot be installed in the mech in combination with this equipment.|`["HARJEL_II", "HARHEL_III"]`|
|`mechPartRequirements`|A list of equipments which need to be installed in the same location as this equipment.||
|`mechRequirements`|A list of equipments which need to be installed in the mech in combination with this equipment.||
|`armorComponentFront`|An absolute value that is added to the armor of the mech part the equipment is installed in.|`"35"`|
|`armorComponentRear`|An absolute value that is added to the rear armor of the mech part the equipment is installed in..|`"35"`|
|`armorComponentFrontMulti`|A multiplier that is applied to the mech front armor of the mech part the equipment is installed in.|`"1.1"`|
|`armorComponentRearMulti`|A multiplier that is applied to the rear armor of the mech part the equipment is installed in.|`"1.2"`|
|`armorMulti`|A multiplier that is applied to the entire mech's armor.|`"2.0"`|
|`structureComponent`|An absolute value that is added to the structure of the mech part the equipment is installed in.|`"35"`|
|`structureComponentMulti`|A multiplier that is applied to the structure of the mech part the equipment is installed in. Values below 1.0 are ignored. Use `structureDamageMulti` instead.|`"1.1"`|
|`structureDamageMulti`|A multiplier for the damage internal structure receives. Any damage caused to internal structure is scaled with this value. This is typically only used for structure upgrades like Composite. **CAUTION: this is broken and does nothing currently.**|`2`|
|`structureMulti`|A multiplier that is applied to the entire mech's structure. Values below 1.0 are ignored.|`"2.0"`|
|`relativeWeight`|Sets the equipment weight to a multiple of the mech's max tonnage. This should be paired with a 0 weight in the equipment asset. Special case: Gyros, here the multiplicator refers to the weight of a standard Gyro.|`"0.05"`|
|`armorWeightMulti`|A multiplicator for an armor upgrade. Does only make sense for armor equipments (type tags starting with `Internal.Armor`) and is typically combined with `armorMulti`. An example would be Hardened armor which uses a multi of `2.0` in combination with ab `armorMulti` of `2.0`.|`"2.0"`|
|`structureWeightMulti`|A multiplicator for a structure upgrade. Does only make sense for structure equipments (type tags starting with `Internal.Structure`) and is typically combined with `structureMulti`. An example would be Endosteel which uses a multi of `0.5` to reduce the weight of the structure by 50%.|`"0.5"`|
|`fillerSlots`|Allows to define the dynamic and fixed fillers an equipment requires. The value is a map which contains any of the following keys: `dynamic` refers to the number of dynamic fillers which can be placed anywhere (a typical example is endo). `Head`, `LeftArm`, `LeftTorso`, `LeftLeg`, etc. refer to the fixed fillers required in specific mech parts. One example is 2 slots in the center torso for an XL Gyro.|`{ "CenterTorso": 2 }`|
|`torsoTwistAngleMulti`|Changes the torso twist angle (how far can the torso turn) via a multiplier. This is typically used on Gyros.|`1.10`|
|`torsoTwistRateMulti`|Changes the torso twist rate (how fast can the torso turn) via a multiplier. This is typically used on Gyros.|`1.10`|
|`topSpeedMulti`|Change the top speed of the mech by this multiplier.|`1.1`|
|`topSpeedReverseMulti`|Change the top reverse speed of the mech by this multiplier (or slower).|`1.1`|
|`accelerationMulti`|Change the acceleration for the mech by this multiplier. Get fast faster (or slower).|`1.1`|
|`decelerationMulti`|Change the deceleration for the mech by this multiplier. Get slow faster (or slower).|`1.1`|
|`turnSpeedMulti`|Change the turn speed of the mech by this multiplier. Turn corners faster (or slower).|`1.1`|
|`sensorRangeBonus`|A fixed bonus to the sensor range in meters.|`2000`|
|`sensorRangeMulti`|A multiplier for the sensor range.|`1.5`|
|`sensorFov`|The value of the sensor's field of view in degrees. Use `360` for the ultimate sensor upgrade.|`360`|
|`weapons`|A json object containing weapon bonus properties as described below.||

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

If you read until here, congrats, you can now go ahead and make your own self-repair equipment which can only be installed in the left leg, adds a total armor of 400, repairs 42 points of armor every 10 seconds for 2 hours, and is presented in a bright unicorn pink in the mechlab.

## TODO
- Harjel equipment destruction should set self-repair values to 0. Probably not that important since a damaged harjel will blow up, most likely taking the component with it. But still...
  - EquipmentData has HealthState - maybe check that whenever taking damage
- Use categories and colors in market window.
  - NewMarketItemWidget/SetEquipmentDetails to set equipment color
- keep armor traits in mind when changing armor in mechlab, see MechComponentHeader/IncreaseArmor
- additional properties
  - armorWeightMulti (for ferro or hardened)
  - structureWeightMulti (for endo etc)

## YAML notes
- armor cleanup:
  - DLC Get Installed Internals - special handling of techlevel for hardended, etc. NEVER USER FOR ARMOR!
  - MechlabWidget/UpdateArmorButtons might need changes if we consider armor upgrades in the mechlab
  - fcnt79/Get Current Mech Tonnage calculates ENDO etc
  - mech without anything, ie. structure only is always tonnage/10
  - why use armor traits when calculating weight for mechlab? That seems incorrect.
  - armor traits are actually applied in the mechlab!
- Format Text can be used to replace things like {string}. Maybe interesting for equip prop labels
- DerivedMech Setup inventory and stuff sets health trait multi to -0.5 for endo. Does that mean endo makes it so we have less structure??
