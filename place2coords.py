import requests

API_KEY = '7e399ab0a4184390ba2b430e9dd8ac75'


def find(string):
    url = "https://api.opencagedata.com/geocode/v1/json?q=%s&key=%s" % (
        string, API_KEY)

    resonse = requests.get(url)

    response = resonse.json()

    response = response['results']

    if len(response) == 0:
        return None

    response = response[0]

    geometry = response['geometry']

    lat = geometry['lat']
    lng = geometry['lng']

    return {"latitude": lat, "longitude": lng}
