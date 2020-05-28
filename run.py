import args

params = args.Parse()

latitude = params.latitude
longitude = params.longitude
maps_provider = params.map

url = ''

if maps_provider == 'google':
    url = 'https://www.google.com/maps/place/%s+%s' % (
        latitude, longitude)
elif maps_provider == 'osm':
    url = 'https://www.openstreetmap.org/#map=14/%s/%s' % (
        latitude, longitude)
elif maps_provider == 'yandex':
    url = 'https://yandex.ru/maps/2/saint-petersburg/?ll=' + \
        longitude + '%2C' + latitude + '&z=13'
elif maps_provider == 'bing':
    url = 'https://www.bing.com/maps?osid=c2e282b4-7d0e-4dd4-a8f8-760191e74204&cp=%s~%s&lvl=13&v=2&sV=2&form=S00027' % (
        latitude, longitude)
    pass
elif maps_provider == 'waze':
    url = 'https://www.waze.com/ul?ll=' + latitude + \
        '%2C' + longitude + '&navigate=yes&zoom=13'

print(url)
