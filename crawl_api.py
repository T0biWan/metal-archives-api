from metal_archive_api import *

bands = []

for i in range(1, 527):
    print("Band id: ", i)
    bands.append(process_band_from_id(i))

write_json_to_file("cleaned_bands.json", remove_invalid_ids(bands))
