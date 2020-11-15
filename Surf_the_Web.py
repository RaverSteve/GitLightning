import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#Extract, count and sum numbers
data = soup.findAll('span', {'class':'comments'})
numbers = [d.text for d in data]
tot = 0
for counts,item in enumerate(numbers):
    print(item)
for number in numbers:
    nums = int(number)
    tot = tot + nums
    
print('Count', counts+1)
print('Sum', tot)
