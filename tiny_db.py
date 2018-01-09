from metal_archive_api import *
from tinydb import TinyDB
from tinydb import Query

bands = read_json_from_file("cleaned_bands-500.json")
db = TinyDB('bands-db.json')

def insert_bands():
    for band in bands:
        db.insert(band)


# >>> from tinydb import TinyDB, Query
# >>> db = TinyDB('db.json')
# >>> db.insert({'Bird': 'Kiwi', 'Hot': 10})
# >>> db.all()
# [{'Bird': 'Kiwi', 'Hot': 10}]
# >>> db.search(Query().Bird == 'Kiwi')
# [{'Bird': 'Kiwi', 'Hot': 10}]
# >>> db.search(Query().Hot == 10)
# [{'Bird': 'Kiwi', 'Hot': 10}]
# >>> db.update({'Hot': 25},Query().Bird == 'Kiwi')
# >>> db.remove(Query().Bird == 'Kiwi')
# >>> db.purge()
