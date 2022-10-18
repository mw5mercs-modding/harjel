# Mechwarrior 5 Mod: Yet Another Equipment Collection

This mod adds additional equipments to the game which can be installed into individual locations.

Much of this mod is inspired by or based on stuff from Roguetech, arguably my favorite game ever.

- **HarJel I, II, III** - Self-Repair systems. Upon taking damage they will repair armor and structure in their install location for a certain amount of time. Install a total of 7 HarJel systems to make the entire mech self-repair. Different HarJel tiers cannot be combined, also they cannot be installed in the head (lore forbids it!).
- **Modular Armor Mk1 - Mk4** - Armor upgrades which add a fixed amount of armor to their installation location. Variants for rear armor are included. Different tiers for different weight classes.
- **Patchwork T1 - T3** - provide a small amount of weight in exchange for some slots. Because Patchwork is awesome.
- **Black Carapace** - Find it, cower in its presence.
- **Advanced Targetting Computers** - TC upgrades which weigh a ton but add considerable upgrades for different weapon systems.
- **Actuators** - A bunch of actuator equipment which can be installed in arm actuator slots, many being melee-focussed.
- **Gyro upgrades** - Melee focused gyros, defensive gyro (evasion pilot skill improvement), stability gyro (jam chance reduction)
- **Angel ECM**
- **NSS** - The Null Signature System (armor upgrade) is essentially just a stacking ECM. NEEDS TESTING AND FEEDBACK.
- **Battle Computers** - One ton upgrades which can be installed with a "modular TC" and add different bonuses.
- **Laser Insulator** - Essentially an advanced single heatsink which lowers the heat output of lasers installed in the same location.
- **Cockpit Hotseat** - A cockpit upgrade with an integrated TSM that can be triggered via hotkey. The longer the Hotseat is active the more heat it produces.
- **Improved Jump-Jets** - Improved jump jets weight 50% more but burn 15% longer and allow the installation of 1.5 JJs per walk MP. These are RT's I-JJs which I found to be much more reasonable than the TT ones (why would you ever want to use those?).
- **Exchanger and Exchanger Mk2** - very rare and very powerful heatsinks which also lower the heat output of all weapons. Explode!
- **Command Console** - A big cockpit-mounted ECM with sensor and cooldown improvements
- **Advanced Small Cockpit** - Frees up a slot in the head
- **Heat Dissipating Armor** - 50% less heat damage taken from Flamers and inferno missiles for a little bulk.

[Full list of equipments](equipment.md)

## Requirements

The HarJel mod depends on YetAnotherMechLab (YAML). It makes use of the extended equipment property system provided by YAML. In fact, the requirements I
had for Harjel let me to develop the equipment properties system in the first place. See below for details.

## Mod Compatibility

Starting with 0.16 the AbstractMech override was dropped which means it should be compatible with any mod that does not mess up YAML's DerivedMech.

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
|`category`|Allows to set the category of the equipment. One would typically use this on equipments which have the "generic" type `Heatsink.Single`. Can be one of: `equipment.ammo`, `equipment.cooling`, `equipment.mobility`, `equipment.electronics`, `equipment.internal`, `equipment.misc`, `equipment.enginecore`, `equipment.enginetype`. Be aware that setting the category this way means that the equipment will always be shown, independent of the value of the "valid only" checkbox.|`"equipment.internal"`|E|||
|`rarity`|Define the rarity of an equipment between 0 and 1. The rarity directly sets the probability the item will show up in markets and affect the total number of items available. Defaults to `0.3`. See also `marketMaxCnt`.|`0.2`|E|||
|`marketMaxCnt`|Set the maximum number that a market can hold of one equipment. By default this is `3` for everything.|`1`|E|||
|`loreAccurate`|States whether the equipment can be found in the lore. If not and configuration entry `loreAbidingCitizen` is `true` then the equipment will never show up in markets. Defaults to `true`|`false`|E|||
|`relativeWeight`|Sets the equipment weight to a multiple of the mech's max tonnage, rounded to quarter tons (with a minumum weight of 0.25 tons). This should be paired with a 0 weight in the equipment asset. Special case: Gyros, here the multiplicator refers to the weight of a standard Gyro.|`"0.05"`|E|||
|`engineRelativeWeight`|Sets the equipment weight to a multiple of the mech's engine weight, rounded up to the next half-ton.|`0.1`|E|||
|`fillerSlots`|Allows to define the dynamic and fixed fillers an equipment requires. The value is a map which contains any of the following keys: `dynamic` refers to the number of dynamic fillers which can be placed anywhere (a typical example is endo). `Head`, `LeftArm`, `LeftTorso`, `LeftLeg`, etc. refer to the fixed fillers required in specific mech parts. One example is 2 slots in the center torso for an XL Gyro.|`{ "CenterTorso": 2 }`|E|W||
|`fixed`|If `true` the equipment cannot be removed and is considered a fixed equipment. It will not show up in the inventory. This should be combined with autoamtic repair for the equipment asset. The salvage probability can either be set to 0 to prevent salvage completely or the salvaged item can be changed via `salvageInto`. Fixed items can be used to create custom mech variants.|`true`|E|W||
|`introYear`|Override the introduction year of an equipment. This is mostly interesting for mods which support both vanilla and YAML to hide equipment in vanilla.|`3078`|E|||
|`slots`|Override the slot count of an equipment.|`3`|E|||

##### Engine Properties
|Property|Description|Example|E|W|M|
|---|---|---|---|---|---|
|`engineRelativeWeight`|Sets the equipment weight to a multiple of the mech's engine weight, rounded up to the next half-ton. Be aware that this works perfectly for engine upgrades like XL engines by setting it to a negative value like `-0.5`. The rounding up results in the weight reduction matching perfectly.|`0.1`|E|||
|`engineHealthType`|Only relevant for engine upgrades. Set this to one of the following:<ul><li>`xl` - Mech will go down when it loses one side torso (unless `cheatXL` is enabled)</li><li>`light` - Mech can lose one ST before going down.</li><li>`xxl` - Mech will go down when it loses one ST.</li><li>`primitive` - Primitive engine, the rating of the core will be divided by 1.2 before calculating the base speed of the mech.</li></ul>|`xl`|E|||

##### Salvage Properties
|Property|Description|Example|E|W|M|
|---|---|---|---|---|---|
|`salvageInto`|If set this equipment will be replaced in the mission salvage table. The value is a combination of the asset type and the asset name, separated by `:`. This property is very useful for `fixed` equipment which should not show up in the salvage table. An example would be a custom asset representing a fixed XL300 engine which should yield a normal XL300 during salvage.|`MWHeatSinkDataAsset:XL300`|E|||
|`salvageMulti`|Can be used to change the number of salvage items created due to `salvageInto`. One example would be an internal `fixed` self-repair system which yields 7 Harjel II equipments when being salvaged.|`7`|E|||

##### Financial Properties 
|Property|Description|Example|E|W|M|
|---|---|---|---|---|---|
|`installCost`|Overwrites the install cost defined in the asset.|`20000`|E|W||
|`removeCost`|Overwrites the remove cost defined in the asset.|`20000`|E|W||
|`repairCost`|Overwrites the repair cost defined in the asset.|`20000`|E|W||
|`installCostScaling`|Defines an installation (and removal) cost scaling based on the max mech tonnage. The value defines the multiplier for a 100 ton mech while a 20 ton mech will always set a multiplier of 1.|`10`|E|W||
|`installDays`|Overwrites the install days defined in the asset.|`2`|E|W||
|`removeDays`|Overwrites the remove days defined in the asset.|`2`|E|W||
|`repairDays`|Overwrites the repair days defined in the asset.|`2`|E|W||
|`installDaysScaling`|Defines an installation (and removal) days scaling based on the max mech tonnage. The value defines the multiplier for a 100 ton mech while a 20 ton mech will always set a multiplier of 1.|`10`|E|W||
|`structureRepairCostMulti`|A multiplier on all structure repairs on the mech. This can for example be used on Endosteel to make it more expensive to repair.|`2`|E||M|
|`structureRepairDaysMulti`|A multiplier on all structure repairs on the mech. This can for example be used on Endosteel to make it take longer to repair.|`2`|E||M|
|`armorRepairCostMulti`|A multiplier on all armor repairs on the mech. This can for example be used on Hardened to make it more expensive to repair.|`2`|E||M|
|`armorRepairDaysMulti`|A multiplier on all armor repairs on the mech. This can for example be used on Hardened to make it take longer to repair.|`2`|E||M|
|`upkeepCostMulti`|A multiplier on the recurring upkeep cost for both active 'mechs and those in cold storage.|`0.8`|||M|
|`equipmentRefitCostMulti`|A multiplier for the cost of weapon and equipment refits (install/remove/repair).|`1.2`|E||M|
|`equipmentRefitDaysMulti`|A multiplier for the required time of weapon and equipment refits (install/remove/repair).|`1.2`|E||M|

##### Installation Restriction Properties
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
|`armorComponentFront`|An absolute value that is added to the armor of the mech part the equipment is installed in.|`"35"`|E|W||
|`armorComponentRear`|An absolute value that is added to the rear armor of the mech part the equipment is installed in..|`"35"`|E|W||
|`armorComponentFrontMulti`|A multiplier that is applied to the mech front armor of the mech part the equipment is installed in.|`"1.1"`|E|W||
|`armorComponentRearMulti`|A multiplier that is applied to the rear armor of the mech part the equipment is installed in.|`"1.2"`|E|W||
|`armorMulti`|A multiplier that is applied to the entire mech's armor.|`"2.0"`|E|W|M|
|`armorBonus`|Absolute armor bonus values for each mech surface. The value is a json object which can contain one entry for each surface (`Head`, `CenterTorso`, `RearCenterTorso`, etc).|`{ "RightTorso": 20 }`|||M|
|`structureComponent`|An absolute value that is added to the structure of the mech part the equipment is installed in.|`"35"`|E|W||
|`structureComponentMulti`|A multiplier that is applied to the structure of the mech part the equipment is installed in.|`"1.1"`|E|W||
|`structureMulti`|A multiplier that is applied to the entire mech's structure.|`"2.0"`|E|W|M|
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
|---|---|---|---|---|---|
|`maxJumpJetsMulti`|A multiplicator for the maximum number of jump jets. Only useful on jumpjet equipment. Caution: the first encountered value will be used. Thus, make sure jump jets with different max multis cannot be combined (using `mechConflicts`). An example would be `1.5` for improved jump jets.|`1.5`|E|||
|`jumpJetXyAccelMulti`|Raise (or lower) the horizontal acceleration when jumping.|`1.1`|E||M|
|`jumpJetZAccelMulti`|Raise (or lower) the vertical acceleration when jumping.|`1.1`|E||M|
|`jumpJetInitialZVelocityMulti`|Raise (or lower) the initial vertical velocity when jumping.|`1.1`|E||M|
|`jumpJetFuelBurnTimeMulti`|Raise (or lower) the time jump jet fuel burns. Values above 1 mean that the mech can jump higher.|`1.1`|E||M|
|`jumpJetFuelRegenTimeMulti`|Lower (or raise) the time it takes to regenerate the jump jet fuel. Values below 1 mean faster regen.|`0.9`|E||M|
|`jumpJetHeatMulti`|Lower (or raise) the heat produced by jump jet usage. Values below 1 mean less heat production.|`0.9`|E||M|

#### Pilot Skill Properties
|Property|Description|Example|E|W|M|
|---|---|---|---|---|---|
|`gunnerySkillBonus`|A bonus/modifier for a pilot skill, can be positive or negative.|`2`|E||M|
|`ballisticSkillBonus`|A bonus/modifier for a pilot skill, can be positive or negative.|`2`|E||M|
|`missileSkillBonus`|A bonus/modifier for a pilot skill, can be positive or negative.|`2`|E||M|
|`energySkillBonus`|A bonus/modifier for a pilot skill, can be positive or negative.|`2`|E||M|
|`pilotingSkillBonus`|A bonus/modifier for a pilot skill, can be positive or negative.|`2`|E||M|
|`evasionSkillBonus`|A bonus/modifier for a pilot skill, can be positive or negative.|`2`|E||M|
|`shieldingSkillBonus`|A bonus/modifier for a pilot skill, can be positive or negative.|`2`|E||M|
|`heatManagementSkillBonus`|A bonus/modifier for a pilot skill, can be positive or negative.|`2`|E||M|

#### Misc Properties
|Property|Description|Example|E|W|M|
|---|---|---|---|---|---|
|`engineHeatsinkMulti`|Normally any engine above a 250 comes with external engine heatsinks (one per every 25 engine rating - 275 has one, 300 two, etc). This multiplier can be used to modify that number.|`0`|E||M|
|`internalHeatsinkBonus`|Adds (or removes) internal engine heatsinks. This is typically used to strip heatsinks from the engine to save weight.|`-1`|E||M|
|`heatCapacityBonus`|A bonus to the mech's total heat capacity.|`0.3`|E||M|
|`coolingMulti`|A multiplier for the heat dissipation of the equipments (heat sinks) in the component or the entire mech (see also `coolingMultiScope`).|`1.1`|E|W|M|
|`coolingMultiScope`|Defines to which mech parts the heat dissipation multi applies.  Can be either `component` or `mech`. Defaults to `mech`.|`1.1`|E|W||
|`dmgEvasionChance`|A chance to avoid any incoming fire. At 1.0 this is quite similar to god-mode.|`0.05`|E||M|
|`caseLevel`|The level of C.A.S.E. protection provided. Can be either `1` (ammo explosion damage does not spread to other components) or `2` (ammo explosion damage is reduced to `2` points of damage).|`1`|E||M|
|`caseScope`|States which parts of the mech are protected by the `caseLevel`. Can be either `component` or `mech`.|`component`|E|||
|`case2MaxDmg`|Sets the maximum damage an ammo explosion can cause if `caseLevel` is 2. Defaults to `2.0` .|`5.0`|E||M|

##### Special Properties
|Property|Description|Example|E|W|M|
|---|---|---|---|---|---|
|`predictiveTargeting`|A boolean property which can be used to enable predictive targeting, ie. a target recticle which points to where one has to shoot, accouting for things like drop-off and target speed.|`true`|E||M|
|`antiAirTargeting`|Same as above, but only applies to VTOLs (other units won't have the reticle unless a Predictive TC or quirk is installed).|`true`|E||M|
|`hasBasicUAV`|Integer number to add to Ammo.Consumable.UAV to any 'Mech. They will have this many norma UAVs plus whatever is equipped. Advanced UAV upgrades all to the increased stats.|`4`|M|

##### Weapon Modifier Properties
|Property|Description| Example |E|W|M|
|---|---|---|---|---|---|
|`weapons`|A json object containing weapon bonus properties as described below.||E||M|
|`armorDamageMulti`|A multiplier for the damage dealt to armor. This allows to create weapons that do more or less damage to armor.||W||
|`structureDamageMulti`|A multiplier for the damage dealt to structure. This allows to create weapons that do more or less damage to structure.||W||

The special property `weapons` allows to define a multitude of weapon modifiers ranging from a simple PPC range upgrade to cooldown modifiers for SRM6 launchers.


The following bonus properties can be specified in the `weapons` section of an equipment.

|Property|Description|
|---|---|
|`scope`|Can be either `mech` (default) or `component`. In the latter case the bonuses only apply to weapons installed in the same location. This property is ignored for mech quirks.|
|`groups`|Contains an array of weapon group objects as decribed below.|
|`lockonTimeMulti`|Modifies the time it takes for weapons like LRMs to get a lock. Caution: this property is not subject to the `scope` since lock-on times are not weapon-specific.|
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
|`ballisticJamChanceMulti`||
|`ballisticAmmoMulti`||
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
|`missileJamChanceMulti`||
|`missileAmmoMulti`||
|`meleeDamageMulti`||
|`meleeCooldownMulti`||
|`meleeHeatMulti`||
|`meleeOptimalRangeMulti`||
|`meleeMaxRangeMulti`||
|`amsMissilesDestroyedMulti`||
|`amsRofMulti`||
|`amsOptimalRangeMulti`||
|`amsMaxRangeMulti`||
|`amsAmmoMulti`||

##### Weapon Groups

Weapon groups are the most flexible way of defining weapon modifiers. Each group has a set of gameplay `tags` which define the weapons the properties apply to (with prefix matching), a `weaponGroupName` which is used to identify the list of tags in the UI, and a set of properties. Possible properties are listed below.

|Property|Description|
|---|---|
|`weaponGroupName`|The human-readable name of the weapon group which is also used for labelling the bonuses in the UI. Typically this would be something like "Laser" or "MRM" or even "Arm-mounted weapons".|
|`tags`|An array of weapon tags and/or weapon asset ids which the bonuses apply for. The simplest value would be `["Weapon"]` which would cause the bonus to be applied to all weapons. See the examples below for more.|
|`excludeTags`|An optional array of weapon tags and/or weapon asset ids which the bonuses do not apply for.|
|`mechParts`|An optional array of mech parts the bonuses apply for. This is only really useful for 'mech quirks and allows to restrict the bonuses to specific parts. A typical example would be arm-mounted weapons. In that case the value would be `["LeftArm", "RightArm"]`.|
| `durationMulti`          | Only applies to trace weapons |
| `spreadRadiusMulti`      ||
| `spreadDistanceMulti`    ||
| `speedMulti`             ||
| `damageMulti`            ||
| `heatDamageMulti`        | Only applies to trace and melee weapons for now. |
| `cooldownMulti`          ||
| `heatMulti`              ||
| `nullRangeMulti`         ||
| `minRangeMulti`          ||
| `optimalRangeMulti`      ||
| `maxRangeMulti`          ||
| `jamChanceMulti`         |Weapons can have a jam chance between 0 and 1 with 1 refering to a 100% jam chance. This multi will be applied to the weapon's jam chance. In most cases `jamChanceBonus` makes more sense.|
| `jamChanceBonus`      |Weapons can have a jam chance between 0 and 1 with 1 refering to a 100% jam chance. This modifier will directly be added on top of the weapon's jam chance. Example: given a weapon jam chance of `0.3` (30%) and a modifier of `-0.1` the final jam chance of the weapon will be `0.2` (20%&).|
| `ammoMulti`              |A multiplier for ammo bins. Caution: since ammo multis are defined for weapons rather than their ammo type more than one multi can apply to one ammo type. In this case the highest multi is used.|
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


##### Incoming Damage Properties
The special property `incomingDamage` allows to define modifiers for incoming damage based on the weapon type. These can be used in 'mech quirks as well as equipment properties.

The `incomingDamage` object has the following properties:

|Property|Description| Example |
|---|---|---|
|`groups`|A json array which contains weapon group objects as decribed below.||E||M|
|`heatMulti`|A multiplier for incoming heat damage from flamers, etc..|`0.5`|E||M|

Like with the weapon modifiers `groups` define incoming damage modifiers for a group of weapons based on weapon tags. Other than for weapon groups, though, the `scope` can be defined individually for each group.

Groups have the following properties:

|Property|Description|
|---|---|
|`weaponGroupName`|The human-readable name of the weapon group which is also used for labelling the bonuses in the UI. Typically this would be something like "Laser" or "MRM".|
|`tags`|An array of weapon tags which the modifiers apply for. The simplest value would be `["Weapon"]` which would cause the modifiers to be applied to all incoming weapons. See the examples below for more.|
|`scope`|Can be either `mech` (default) or `component`. In the latter case the modifiers only apply to incoming damage in the same location. This property is ignored for mech quirks.|
|`armorDamageMulti`|A multiplier for the damage caused to armor.|
|`structureDamageMulti`|A multiplier for the damage caused to structure.|

###### Examples

```json
"ARMOR_GLAZED": {
	"incomingDamage": {
		"groups": [{
			"weaponGroupName": "Energy",
			"tags": ["Weapon.Energy"],
			"armorDamageMulti": 0.5,
			"scope": "mech"
		}]
	}
}
```
```json
"UPPER_SPIKED": {
	"incomingDamage": {
		"groups": [{
			"weaponGroupName": "Melee",
			"tags": ["Weapon.Melee"],
			"armorDamageMulti": 0.85,
			"strutureDamageMulti": 0.85,
			"scope": "component"
		}]
	}
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
|`useSkinsFrom`|An optional gameplay tag indicating the mech variant from which this mech use the skins. This is useful for introducing new mech types without the need to manually update all skins.|
|`aiMechRole`|Set the default AI mech role from the TTRulez_AI mod. This will only take effect if that mod is active. For possible values see below.|
|`mechType`|The type of mech which can be `bipedal` (default) or `quad` for now. Only has an impact on quad mechs which will then have their arm slots replaced with leg slots.|
|`autoconv`|An object defining details for YAML's automatic vanilla mech conversion (see below).|

##### TTRulez_AI Mech Roles

YAML has built-in support for TTRulez_AI mech roles. These can be chosen in the mech lab, allowing the player to give roles to their custom builds. A default role can be set in `mechs.json` via the `aiMechRole` property (there is no real advantage over setting these in the UnitCard, when implementing this feature I was under the impression that TTRulez_AI introduced additional roles which can not be set in the UnitCard). The following values are supported:

|Value|Description|
|---|---|
|`AntiAir`|Antiaircraft: These are usually sniper type units with ballistic weapons designed for antiaircraft and antitank targets<ul><li>Same function as Snipers but Target preference is VTOL and TANK</li><li>RECOMMEND USE IN FOCUSED FIRE and mainly to provide air and antitank support</li></ul>|
|`Ambusher`|Ambusher: Slow heavily armed city fighters that use cover to engage enemies<ul><li>Target preference: Heavy units</li><li>If more than 300m from the enemy and has JJ, the AI will jump towards the target to close quickly skimming the ground, if no JJ the AI will rush towards the target.</li><li>If less than 300m from the enemy, and the enemy has sight will move behind cover (building), if it has LOS and JJ it will use them to get cover quickly.  Once out of sight the AI will work to regain LOS to fire on the enemy. Then in a few seconds of firing try to move back to cover again.</li></ul>|
|`Brawler`|Brawler: Heavily armored and slower mechs with mix of ranged weapons. <ul><li>Target preference: Heavy units</li><li>Focus fire: Will use vanilla logic of closing and circling the enemy</li><li>Engage at will: Will use ranged tactics based on their weapon range compared to the enemies range to maximize damage.  May occasionally use cover logic to engage.</li></ul>|
|`Juggernaut`|Juggernaut: Heavily armed and armored mechs with close range weapons designed to push an advance.<ul><li>Target preference: Assault units</li><li>The AI will move aggressively towards the enemy using JJ if possible and engage at more than 200m</li><li>Juggernauts do not break off if damaged so provide support with other units</li></ul>|
|`MissleBoat`|Sniper/Firesupport/Missileboat: These often slow mech types are used to fire on enemy mechs at a range to minimize damage to themselves and support a more aggressive unit. <ul><li>Target preference: Slow heavy and assault units</li><li>Focused fire: These mechs deploy on the battlefield near the player on the high ground</li><li>Engage at will: These mechs engaged in ranged combat maximizing distance from the enemy</li><li>RECOMMEND USE IN FOCUSED FIRE</li></ul>|
|`Scout`|Scout: Light recon units mainly used to fight vehicles, turrets, and light mechs<ul><li>Target preference: Light fast units</li><li>If a VTOL, Tank, or Turret is targeted will aggressively engage at close range</li><li>If a fast mech is targeted they will engage in a circle fight trying to gain advantage with spins and occasionally hit and run</li><li>If a slow mech is targeted they will engage in hit and run tactics with occasional circling</li><li>RECOMMEND IN ENGAGE AT WILL</li></ul>|
|`Skirmisher`|Skirmisher: Fast, lightly armored, units with long range weapons, they use cover or hit and run tactics and have two main roles to kill fast light units and keep them off heavier units or to distract heavier units<ul><li>Target preference: Fast units</li><li>If a fast mech is targeted (>90kph is targeted) they will use JJ to close and attack circling</li><li>Engage at will: If a slower heavier mech is targeted they will use hit and run or ranged tactics</li><li>Focused fire: If ordered to attack the players target they will jump/rush in to engage the target then break off and return to the player. Once back to the player will rush to the enemy again. This is skirmishing and distracts he enemy</li></ul>|
|`Sniper`|Sniper/Firesupport/Missileboat: These often slow mech types are used to fire on enemy mechs at a range to minimize damage to themselves and support a more aggressive unit. <ul><li>Target preference: Slow heavy and assault units</li><li>Focused fire: These mechs deploy on the battlefield near the player on the high ground</li><li>Engage at will: These mechs engaged in ranged combat maximizing distance from the enemy</li><li>RECOMMEND USE IN FOCUSED FIRE</li></ul>|
|`Striker`|Striker: Fast lightly armored units with close range heavy damage weapons such as SRMs. Ideally they flank the target to maximize damage. They stay on a target until it is dead or forced to retreat.<ul><li>Target Preference: Slow heavy and assault units</li><li>If fighting fast enemies, they engage in circle fights or hit and run.</li><li>If the target is any mech with speed less than 80kph, the AI will run the flanking logic.  This selects a point to the side of the enemy at least 100m away.  Rushes/jumps to this point and once it detects the enemies rear arc the AI rushes to engage their rear armor.  If the player uses FocusFire they will use the player as a reference for their flank so the enemy will have to focus  on either the player or striker.</li><li>RECOMMEND USE IN FOCUSED FIRE</li></ul>|

#### Automatic Mech Conversion
YAML can automatically convert vanilla mechs. This is done by injecting required slots types and equipment.

In order for the final weight of the 'mech to be perfect vanilla mechs should be designed taking TT rules into account, both with regards to base weight (account for engine rating and engine type) and used slots. Example: if the 'mech is supposed to run an XL engine make sure to not give the vanilla MDA more than 8 slots in the side torsos.

However, MW5 does not account for XXL or light engines or gyro upgrades. This is why YAML allows to give hints for the conversion
mechanism via `mechs.json` like so:

```
{
	"AWII_11A": {
		"autoconv": {
			"engine": "xxl"
		}
	},
	"AGS-4D": {
		"autoconv": {
			"engine": "xl",
			"gyro": "xl"
		}
	}
}
```

|Property|Description|
|---|---|
|`engine`|Gives a hint regarding the engine type to inject, overriding the XL flag in the MDA. Can be one of `xl`, `xxl`, `light`, `compact`.|
|`gyro`|Gives a hint regarding the gyro to inject. Can be `xl` or `compact`.|
|`coreCnt`|By default all 'mechs have one engine core slot (unless the MDA already contains more). This property can be used to raise the number of core slots. Typically this would be set to `2` for superheavy mechs|
