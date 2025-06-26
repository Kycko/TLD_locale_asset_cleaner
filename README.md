# Description
Use these scripts to get The Long Dark localization files and make `csv` files, ready for editing and then uploading to Steam Workshop.

# Prepare
Install `UnityPy` module only if you need unpack (export Unity asset) function. If you're using another methods of exporting localization files, you can skip "export" step and run `translate.py` without `UnityPy`.

# Export asset
1. Edit `unpack.py` to change the `langs` variable (set the list of needed languages)
2. Find localization file, must be `.../SteamLibrary/steamapps/common/TheLongDark/tld_Data/StreamingAssets/Bundles/Linux/ui/localization` (change `Linux` to `Windows` if you're using it)
3. Run `python unpack.py localization`

# Translate json to csv
- Run `python translate.py English.json` (change to your language file)
