import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url- ')
repeat = input("Repeat how many times? ")
position = input("Which link position do u want to open? ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

for x in range(int(repeat)):
    tags = soup('a')
    print(tags[int(position)-1].get('href', None))
    url = tags[int(position)-1].get('href', None)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')