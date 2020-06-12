import requests

API_KEY = '7e399ab0a4184390ba2b430e9dd8ac75'


def find(latitude, longitude):
    url = "https://api.opencagedata.com/geocode/v1/json?q=%s+%s&key=%s" % (
        latitude, longitude, API_KEY)

    resonse = requests.get(url)

    response = resonse.json()

    response = response['results']

    if len(response) == 0:
        return None

    response = response[0]

    addressString = response['formatted']

    return addressString
