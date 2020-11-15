# This API only accepts the university in a list of its accepted ones.
# This API uses the same parameters (sensor and address) as the Google API.
# This API also has no rate limit so you can test as often as you like.
# If you visit the URL with no parameters, you get a list of all of the
# address values which can be used with this API.

import urllib.request as ur
import urllib.parse as up
import json
import ssl

api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
    
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter location: ")

    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key
    url = serviceurl + up.urlencode(parms)

    print('Retrieving', url)
    data = ur.urlopen(url, context=ctx).read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    place_id = js['results'][0]['place_id']
    print('Place id', place_id)
    break
