from metal_archive_api import *

bands = []

for i in range(51, 52):
    print("Band id: ", i)
    bands.append(process_band_from_id(i))

write_json_to_file("bands.json", bands)
