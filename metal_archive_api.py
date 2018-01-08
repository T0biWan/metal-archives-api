import json
import requests



api_url_base = 'http://em.wemakesites.net/'
api_token = open("api_token.txt", "r").read()
header = {'Content-Type': 'application/json'}


def get_band_by_id(id):
    request =  api_url_base + "band/" + str(id) + "?api_key=" + api_token
    response = requests.get(request, headers = header)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))


def process_band_from_id(id):
    band = get_band_by_id(id)
    data = band["data"]
    processed_band = {}

    if "band_name" in data: processed_band["name"] = data["band_name"]
    if "genre" in data["details"]: processed_band["genre"] = data["details"]["genre"]
    if "logo" in data: processed_band["logo"] = data["logo"]
    if "lyrical themes" in data["details"]: processed_band["lyrical_themes"] = data["details"]["lyrical themes"]
    if "status" in data["details"]: processed_band["status"] = data["details"]["status"]
    if "formed in" in data["details"]: processed_band["formed_in"] = data["details"]["formed in"]
    if "years active" in data["details"]: processed_band["years_active"] = data["details"]["years active"]
    if "country of origin" in data["details"]: processed_band["country_of_origin"] = data["details"]["country of origin"]
    if "location" in data["details"]: processed_band["location"] = data["details"]["location"]
    if "bio" in data: processed_band["bio"] = data["bio"]
    if "discography" in data: processed_band["discography"] = data["discography"]

    return processed_band


def write_json_to_file(path, data):
    with open(path, 'w') as file:
         json.dump(data, file)
