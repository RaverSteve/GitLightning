import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
loc = urllib.request.urlopen(url)
print('Retrieving', url)
data = loc.read()
print('Retrieved', len(data), 'characters')


stuff = ET.fromstring(data)
lst = stuff.findall('comments/comment')
counts = 0
tot = 0
for item in lst:
    counts = counts + 1
    tot = tot + int(item.find('count').text)

print('Count:', counts)
print('Sum:', tot)
