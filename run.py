import args
import maps
params = args.Parse()

latitude = params.latitude
longitude = params.longitude
maps_provider = params.map

url = maps.getUrl(latitude, longitude, maps_provider)

print(url)
