# Mechwarrior 5 Mod: HarJel

This mod adds additional armor upgrades to the game which can be installed into individual locations.

- Modular Armor Mk1 - Mk4: Armor upgrades which add a fixed amount of armor to their installation location. Variants for rear armor are included.
- HarJel I, II, III - Self-Repair systems. Upon taking damage they will repair armor and structure in their install location for a certain amount of time. Install a total of 7 HarJel systems to make the entire mech self-repair.

## TODO
- Harjel equipment destruction should set self-repair values to 0. Probably not that important since a damaged harjel will blow up, most likely taking the component with it. But still...

## Developer Notes

### Equipment Configuration

In addition to the equipment properties provided by YAML the HarJel mod adds the following:

|Property|Description|Default|Example|
|---|---|---|---|
|`armorComponentFront`|An absolute value that is added to the mech part's front armor.|`"0"`|`"35"`|
|`armorComponentRear`|An absolute value that is added to the mech part's rear armor.|`"0"`|`"35"`|
|`armorComponentMultiFront`|A multiplier that is applied to the mech part's front armor.|`"0"`|`"1.1"`|
|`armorComponentMultiRear`|A multiplier that is applied to the mech part's rear armor.|`"0"`|`"1.2"`|
|`armorMulti`|A multiplier that is applied to the entire mech's armor.|`"0"`|`"2.0"`|
|`selfRepairArmor`|The amount of armor the equipment repairs at each interval.|`"0"`|`"2"`|
|`selfRepairStructure`|The amount of structure the equipment repairs at each interval.|`"0"`|`"0.5"`|
|`selfRepairDuration`|The duration of self-repair after taking damage on the self-repair enabled mech part (in seconds).|`"0"`|`"5"`|
|`selfRepairInterval`|The interval at which self-repair will be performed (in seconds).|`"1"`|`"0.5"`|
|`selfRepairScope`|The scope of the self-repair equipment. Can be either `component` to only repair the install location or `mech` to repair the entire mech (excluding the head).|`"component"`|`"mech"`|

