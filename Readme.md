# Mechwarrior 5 Mod: HarJel

This mod adds additional armor upgrades to the game which can be installed into individual locations.

- Modular Armor Mk1 - Mk4: Armor upgrades which add a fixed amount of armor to their installation location. Variants for rear armor are included.
- HarJel I, II, III - Self-Repair systems. Upon taking damage thez will repair armor and structure in their install location for a certain amount of time. Install a total of 7 HarJel systems to make the entire mech self-repair.

## Caveats
- When used without YAML "valid only" has to be unchecked in order to install in the mechlab.
- Thus far there is no restriction on the number of upgrades per location. In the future different versions of HarJel will not be compatible, also only one upgrade will be allowed per location and the head will be excluded.

## YAML Notes
- Equipment colors are controlled via slot colors in "UI/Frontend/Mechlab/Components/Mechlab Inventory EquipmentPanel/Setup Equipment Info"
- Armor upgrade tag must be added to MechlabWidget/SetupEquipmentFilter and the YAML tag list

## YAML Ideas
- Read equipment colors from equipment list file.
- Read equipment filters from equipment list file.
- Support multiple equipment list files from different mods

