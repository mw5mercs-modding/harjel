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

HarJel makes use of the equipment properties system in YAML.

### Equipment/Weapon Properties and Mech Quirks

YAML supports the configuration of custom equipment and weapons via an ever-growing set of properties. Equipment and weapon properties can be defined via json files called `Equipment_properties.json`. Yaml will will load any such file stored
in the `Resources` folder of any enabled mod. The files will be loaded in the order of mod priority. That means for example that the values for a specific equipment from a mod with a load order of 7 will overwrite the values for that particular equipment from a mod with load order 6.

Mech quirks are defined in a file called `quirks.json` which is loaded the same way as the equipment properties. A third file `mechs.json` contains the mapping from mechs to quirks. See below for more details.

#### Equipment/Weapon Properties

The equipment properties file can contain one entry for each custom equipment (or a type of equipment by using a gameplay tag path which will be mapped exactly, ie. no prefix matching) with a bunch of different properties as described below.

Originally the properties were designed for equipments only. Since then some have been extended to also work with weapons. These are marked in the "W" column as seen below.

YAML by itself already provides the following properties:

##### General Properties
|Property|Description|Example|E|W|M|
|---|---|---|---|---|---|
|`name`|Rename an equipment. Might be useful. Example: the HeatSinkKit mod uses it to rename the "Engine Double Heat Sinks" to "Double Heat Sink Kit".||E|||
|`description`|Because it is annoying to edit the desciption in the asset all the time, and also: newlines!|`"One line\nanother line."`|E|||
|`color`|Set the color of the equipment in the market and mechlab as an RGBA value.|`"(R=0.59,G=0.03,B=0.11,A=1)"`|E|||
|`category`|Allows to set the category of the equipment. One would typically use this on equipments which have the "generic" type `Heatsink.Single`. Can be one of: `equipment.misc`, `equipment.engine`, `equipment.internal` and `equipment.ammo`. Be aware that setting the category this way means that the equipment will always be shown, independent of the value of the "valid only" checkbox.|`"equipment.internal"`|E|||
|`rarity`|Define the rarity of an equipment between 0 and 1. The rarity directly sets the probability the item will show up in markets.|`0.2`|E|||
|`loreAccurate`|States whether the equipment can be found in the lore. If not and configuration entry `loreAbidingCitizen` is `true` then the equipment will never show up in markets. Defaults to `true`|`false`|E|||
|`relativeWeight`|Sets the equipment weight to a multiple of the mech's max tonnage. This should be paired with a 0 weight in the equipment asset. Special case: Gyros, here the multiplicator refers to the weight of a standard Gyro.|`"0.05"`|E|||
|`engineRelativeWeight`|Sets the equipment weight to a multiple of the mech's engine weight, rounded up to the next half-ton.|`0.1`|x|||
|`fillerSlots`|Allows to define the dynamic and fixed fillers an equipment requires. The value is a map which contains any of the following keys: `dynamic` refers to the number of dynamic fillers which can be placed anywhere (a typical example is endo). `Head`, `LeftArm`, `LeftTorso`, `LeftLeg`, etc. refer to the fixed fillers required in specific mech parts. One example is 2 slots in the center torso for an XL Gyro.|`{ "CenterTorso": 2 }`|E|||

##### Refit Cost Properties 
|Property|Description|Example|E|W|M|
|---|---|---|---|---|---|
|`installCost`|Overwrites the install cost defined in the asset.|`20000`|E|||
|`removeCost`|Overwrites the remove cost defined in the asset.|`20000`|E|||
|`repairCost`|Overwrites the repair cost defined in the asset.|`20000`|E|||
|`installCostScaling`|Defines an installation (and removal) cost scaling based on the max mech tonnage. The value defines the multiplier for a 100 ton mech while a 20 ton mech will always set a multiplier of 1.|`10`|E|||
|`installDays`|Overwrites the install days defined in the asset.|`2`|E|||
|`removeDays`|Overwrites the remove days defined in the asset.|`2`|E|||
|`repairDays`|Overwrites the repair days defined in the asset.|`2`|E|||
|`installDaysScaling`|Defines an installation (and removal) days scaling based on the max mech tonnage. The value defines the multiplier for a 100 ton mech while a 20 ton mech will always set a multiplier of 1.|`10`|E|||
|`structureRepairCostMulti`|A multiplier on all structure repairs on the mech. This can for example be used on Endosteel to make it more expensive to repair.|`2`|E||M|
|`structureRepairDaysMulti`|A multiplier on all structure repairs on the mech. This can for example be used on Endosteel to make it take longer to repair.|`2`|E||M|
|`armorRepairCostMulti`|A multiplier on all armor repairs on the mech. This can for example be used on Hardened to make it more expensive to repair.|`2`|E||M|
|`armorRepairDaysMulti`|A multiplier on all armor repairs on the mech. This can for example be used on Hardened to make it take longer to repair.|`2`|E||M|

##### Installation Restrition Properties
|Property|Description|Example|E|W|M|
|---|---|---|---|---|---|
|`maxTonnage`|This equipment can only be equipped to a mech whose tonnage does not exceed this value.|`"35"`|E|||
|`minTonnage`|This equipment can only be equipped to a mech whose tonnage matches at least this value.|`"80"`|E|||
|`invalidMechParts`|A list of mech parts the equipment can not be installed in. Possible values are: `Head`, `LeftArm`, `LeftTorso`, `LeftLeg`, etc..|`[ "CenterTorso" ]`|E|W||
|`mechPartConflicts`|A list of equipments which cannot be installed in the same location as this equipment.|`["HARJEL_II", "HARHEL_III"]`|E|W||
|`mechConflicts`|A list of equipments which cannot be installed in the mech in combination with this equipment.|`["HARJEL_II", "HARHEL_III"]`|E|W||
|`mechPartRequirements`|A list of equipments which need to be installed in the same location as this equipment. This can be either equipment names or tag names.|`GuardianECM` or `Equipment.ECM`|E|W||
|`mechRequirements`|A list of equipments which need to be installed in the mech in combination with this equipment. This can be either equipment names or tag names.|`GuardianECM` or `Equipment.ECM`|E|W||

##### Armor and Structure Properties
|Property|Description|Example|E|W|M|
|---|---|---|---|---|---|
|`armorComponentFront`|An absolute value that is added to the armor of the mech part the equipment is installed in.|`"35"`|E|||
|`armorComponentRear`|An absolute value that is added to the rear armor of the mech part the equipment is installed in..|`"35"`|E|||
|`armorComponentFrontMulti`|A multiplier that is applied to the mech front armor of the mech part the equipment is installed in.|`"1.1"`|E|||
|`armorComponentRearMulti`|A multiplier that is applied to the rear armor of the mech part the equipment is installed in.|`"1.2"`|E|||
|`armorMulti`|A multiplier that is applied to the entire mech's armor.|`"2.0"`|E||M|
|`armorBonus`|Absolute armor bonus values for each mech surface. The value is a json object which can contain one entry for each surface (`Head`, `CenterTorso`, `RearCenterTorso`, etc).|`{ "RightTorso": 20 }`|||M|
|`structureComponent`|An absolute value that is added to the structure of the mech part the equipment is installed in.|`"35"`|E|||
|`structureComponentMulti`|A multiplier that is applied to the structure of the mech part the equipment is installed in.|`"1.1"`|E|||
|`structureMulti`|A multiplier that is applied to the entire mech's structure.|`"2.0"`|E||M|
|`structureBonus`|Absolute structure bonus values for each mech surface. The value is a json object which can contain one entry for each surface (`Head`, `CenterTorso`, `RearCenterTorso`, etc).|`{ "RightTorso": 20 }`|||M|
|`armorWeightMulti`|A multiplicator for an armor upgrade. Does only make sense for armor equipments (type tags starting with `Internal.Armor`) and is typically combined with `armorMulti`. An example would be Hardened armor which uses a multi of `2.0` in combination with ab `armorMulti` of `2.0`. Alternatively `armorPerTon` can be used.|`2.0`|E|||
|`armorPerTon`|The amount of armor points one ton yields. Does only make sense for armor equipments (type tags starting with `Internal.Armor`). An example would be Hardened armor which uses a value of `64` in combination with ab `armorMulti` of `2.0`. An alternative to `armorWeightMulti` with a higher priority.|`64`|E|||
|`structureWeightMulti`|A multiplicator for a structure upgrade. Does only make sense for structure equipments (type tags starting with `Internal.Structure`) and is typically combined with `structureMulti`. An example would be Endosteel which uses a multi of `0.5` to reduce the weight of the structure by 50%.|`"0.5"`|E|||

##### Movement and Mobility Properties
|Property|Description|Example|E|W|M|
|---|---|---|---|---|---|
|`torsoTwistAngleMulti`|Changes the torso twist angle (how far can the torso turn) via a multiplier. This is typically used on Gyros.|`1.10`|E||M|
|`torsoTwistRateMulti`|Changes the torso twist rate (how fast can the torso turn) via a multiplier. This is typically used on Gyros.|`1.10`|E||M|
|`armTwistAngleMulti`|Changes the arm twist angle (how far can the arms turn) via a multiplier. This is typically used on Gyros.|`1.10`|E||M|
|`armTwistRateMulti`|Changes the arm twist rate (how fast can the arms turn) via a multiplier. This is typically used on Gyros.|`1.10`|E||M|
|`topSpeedMulti`|Change the top speed of the mech by this multiplier.|`1.1`|E||M|
|`topSpeedReverseMulti`|Change the top reverse speed of the mech by this multiplier (or slower).|`1.1`|E||M|
|`accelerationMulti`|Change the acceleration for the mech by this multiplier. Get fast faster (or slower).|`1.1`|E||M|
|`decelerationMulti`|Change the deceleration for the mech by this multiplier. Get slow faster (or slower).|`1.1`|E||M|
|`turnSpeedMulti`|Change the turn speed of the mech by this multiplier. Turn corners faster (or slower).|`1.1`|E||M|

##### Sensor Properties
|Property|Description|Example|E|W|M|
|---|---|---|---|---|---|
|`sensorRangeBonus`|A fixed bonus to the sensor range in meters.|`2000`|E||M|
|`sensorRangeMulti`|A multiplier for the sensor range.|`1.5`|E||M|
|`sensorFov`|The value of the sensor's field of view in degrees. Use `360` for the ultimate sensor upgrade.|`360`|E||M|

##### Jump-Jet related Properties
|Property|Description|Example|E|W|M|
|---|---|---|-----|-----|---|
|`maxJumpJetsMulti`|A multiplicator for the maximum number of jump jets. Only useful on jumpjet equipment. Caution: the first encountered value will be used. Thus, make sure jump jets with different max multis cannot be combined (using `mechConflicts`). An example would be `1.5` for improved jump jets.|`1.5`|E|||
|`jumpJetXyAccelMulti`|Raise (or lower) the horizontal acceleration when jumping.|`1.1`|E||M|
|`jumpJetZAccelMulti`|Raise (or lower) the vertical acceleration when jumping.|`1.1`|E||M|
|`jumpJetInitialZVelocityMulti`|Raise (or lower) the initial vertical velocity when jumping.|`1.1`|E||M|
|`jumpJetFuelBurnTimeMulti`|Raise (or lower) the time jump jet fuel burns. Values above 1 mean that the mech can jump higher.|`1.1`|E||M|
|`jumpJetFuelRegenTimeMulti`|Lower (or raise) the time it takes to regenerate the jump jet fuel. Values below 1 mean faster regen.|`0.9`|E||M|
|`jumpJetHeatMulti`|Lower (or raise) the heat produced by jump jet usage. Values below 1 mean less heat production.|`0.9`|E||M|

##### Weapon Modifier Properties
The special property `weapons` allows to define a multitude of weapon modifiers ranging from a simple PPC range upgrade to cooldown modifiers for SRM6 launchers.

|Property|Description| Example |E|W|M|
|---|---|---------|-----|---|---|
|`weapons`|A json object containing weapon bonus properties as described below.||E||M|

The following bonus properties can be specified in the `weapons` section of an equipment.

|Property|Description|
|---|---|
|`groups`|Contains an array of weapon group objects as decribed below.|
|`lockonTimeMulti`||
|`traceDurationMulti`||
|`traceDamageMulti`||
|`traceCooldownMulti`||
|`traceHeatMulti`||
|`traceOptimalRangeMulti`||
|`traceMaxRangeMulti`||
|`ballisticSpreadRadiusMulti`||
|`ballisticSpreadDistanceMulti`||
|`ballisticSpeedMulti`||
|`ballisticDamageMulti`||
|`ballisticCooldownMulti`||
|`ballisticHeatMulti`||
|`ballisticNullRangeMulti`||
|`ballisticMinRangeMulti`||
|`ballisticOptimalRangeMulti`||
|`ballisticMaxRangeMulti`||
|`ppcSpreadRadiusMulti`||
|`ppcSpreadDistanceMulti`||
|`ppcSpeedMulti`||
|`ppcDamageMulti`||
|`ppcCooldownMulti`||
|`ppcHeatMulti`||
|`ppcNullRangeMulti`||
|`ppcMinRangeMulti`||
|`ppcOptimalRangeMulti`||
|`ppcMaxRangeMulti`||
|`missleSpreadRadiusMulti`||
|`missleSpreadDistanceMulti`||
|`missleSpeedMulti`||
|`missleDamageMulti`||
|`missleCooldownMulti`||
|`missleHeatMulti`||
|`missileNullRangeMulti`||
|`missileMinRangeMulti`||
|`missileOptimalRangeMulti`||
|`missileMaxRangeMulti`||
|`meleeDamageMulti`||
|`meleeCooldownMulti`||
|`meleeHeatMulti`||
|`meleeOptimalRangeMulti`||
|`meleeMaxRangeMulti`||
|`amsMissilesDestroyedMulti`||
|`amsRofMulti`||
|`amsOptimalRangeMulti`||
|`amsMaxRangeMulti`||

##### Weapon Groups

Weapon groups are the most flexible way of defining weapon modifiers. Each group has a set of gameplay `tags` which define the weapons the properties apply to (with prefix matching), a `weaponGroupName` which is used to identify the list of tags in the UI, and a set of properties. Possible properties are listed below.

| Property                 | Description                   |
|--------------------------|-------------------------------|
| `durationMulti`          | Only applies to trace weapons |
| `spreadRadiusMulti`      ||
| `spreadDistanceMulti`    ||
| `speedMulti`             ||
| `damageMulti`            ||
| `cooldownMulti`          ||
| `heatMulti`              ||
| `nullRangeMulti`         ||
| `minRangeMulti`          ||
| `optimalRangeMulti`      ||
| `maxRangeMulti`          ||
| `missilesDestroyedMulti` | Only applies to AMS           |
| `rofMulti`               | Only applies to AMS           |

The following example applies heat and damage multipliers to all MRM weapons.
```json
{
    "weaponGroupName": "MRM",
    "tags": [
        "Weapon.Missile.LRM.LRM10.MRM20",
        "Weapon.Missile.LRM.LRM15.MRM30",
        "Weapon.Missile.LRM.LRM20.MRM40",
        "Weapon.Missile.LRM.LRM10.MRM10",
        "Weapon.Missile.LRM.LRM20.MRM20",
        "Weapon.Missile.LRM.LRM20.MRM30",
        "Weapon.Missile.LRM.LRM20.MRM40"
    ],
    "heatMulti": 0.9,
    "damageMulti": 1.2
}
```

The following example applies a cooldown multi only to medium standard lasers.
```json
{
    "weaponGroupName": "Medium Laser",
    "tags": [
        "Weapon.Energy.Laser.Standard.Medium"
    ],
    "cooldownMulti": 0.95
}
```

The following example applies a heat multi to all weapons.
```json
{
    "weaponGroupName": "Weapon",
    "tags": [
        "Weapon"
    ],
    "heatMulti": 0.9
}
```

##### Harjel Properties
In addition to the equipment properties provided by YAML the HarJel mod adds the following:

|Property|Description|Default|Example|
|---|---|---|---|
|`selfRepairArmor`|The amount of armor the equipment repairs at each interval.|`"0"`|`"2"`|
|`selfRepairStructure`|The amount of structure the equipment repairs at each interval.|`"0"`|`"0.5"`|
|`selfRepairDuration`|The duration of self-repair after taking damage on the self-repair enabled mech part (in seconds).|`"0"`|`"5"`|
|`selfRepairInterval`|The interval at which self-repair will be performed (in seconds).|`"1"`|`"0.5"`|
|`selfRepairScope`|The scope of the self-repair equipment. Can be either `component` to only repair the install location or `mech` to repair the entire mech (excluding the head).|`"component"`|`"mech"`|

##### Example

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

#### Mech Quirks

Mech quirks can be defined in a file called `quirks.json` in the `Resources` directory. The file contains a map of quirks where each quirk has a `name`, a `description`, an optional `color` and a set of `properties`. The supported properties are listed above and are marked in the `M` column as being compatible with mech quirks.

The key of the quirk object can be arbitrary as it is only used to reference the quirk in the mech definitions.

The following example defines the quirks for the Atlas Boar's Head Hero mech.

```json
{
  "AS7-BH": {
    "name": "The Boar's Head",
    "description": "Unique set of quirks for the Atlas The Boar's Head Hero 'Mech",
    "color": "(R=1,G=0.4,B=0,A=1)",
    "properties": {
      "weapons": {
        "groups": [
          {
            "weaponGroupName": "Weapon",
            "tags": [
              "Weapon"
            ],
            "heatMulti": 0.9
          },
          {
            "weaponGroupName": "Energy",
            "tags": [
              "Weapon.Energy"
            ],
            "heatMulti": 0.9,
            "optimalRangeMulti": 1.1,
            "maxRangeMulti": 1.1
          },
          {
            "weaponGroupName": "Ballistic",
            "tags": [
              "Weapon.Ballistic"
            ],
            "cooldownMulti": 0.9,
            "speedMulti": 1.1
          }
        ]
      }
    }
  }
}
```

#### Mech Properties
Once quirks have been defined they also need to be applied to mechs. This is done in a file called `mechs.json`. It contains a map of mech definitions where the key can be either the variant name or the MDL name. Each mech is then an object which can have any of the following properties.

|Property|Description|
|---|---|
|`quirks`|An array of quirk ids which have been defined as detailed above.|
|`scale`|A scaling vector for the mech which is applied in DerivedMech. Example: `X=1.1 Y=1.1 Z=1.1`|


If you read until here, congrats, you can now go ahead and make your own self-repair equipment which can only be installed in the left leg, adds a total armor of 400, repairs 42 points of armor every 10 seconds for 2 hours, and is presented in a bright unicorn pink in the mechlab.
