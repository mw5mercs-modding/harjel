import unreal

def get_asset(path):
	ad = unreal.EditorAssetLibrary.find_asset_data(path)
	o = unreal.AssetRegistryHelpers.get_asset(ad)
	return o
	
def get_primary_asset_id(path):
	return unreal.SystemLibrary.get_primary_asset_id_from_object(unreal.AssetRegistryHelpers.get_asset(unreal.EditorAssetLibrary.find_asset_data(path)))

asset_location = "/harjel/Objects/Mechs/_common/"
csv = "E:/Games/MechWarrior5Editor/MW5Mercs/Plugins/harjel/equipment.md"

with unreal.ScopedEditorTransaction("CollectEquipmentMetadata Script") as trans:
	assets = unreal.EditorAssetLibrary.list_assets(asset_location, True)
	with open(csv, "w") as f:
		f.write("# Yet Another Equipment Collection\n\n")
		f.write("Name|Year|Weight|Size|Description|Base Price\n")
		f.write("---|---|---|---|---|---\n")
		lines = []
		for asset_path in assets:
			asset = get_asset(asset_path)
			if hasattr(asset, "name"):
				#unreal.log(dir(asset))
				unreal.log(asset.name)
				unreal.log("Intro year: {}".format(asset.intro_date.to_tuple()[0]))
				unreal.log("Tons: {}".format(asset.tons))
				unreal.log("Slots: {}".format(asset.slots))
				unreal.log("Description: {}".format(asset.description))
				unreal.log("Base Price: {}".format(asset.c_bill_base_value))
				lines.append("{}|{}|{:.1f}|{}|{}|{}".format(asset.name, asset.intro_date.to_tuple()[0], asset.tons, asset.slots, asset.description, asset.c_bill_base_value))
		for l in sorted(lines):
			f.write(l + "\n") 
