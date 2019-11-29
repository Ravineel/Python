import urllib.request,urllib.error,urllib.parse
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode=ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,'html.parser')
tags = soup('span')
sum = 0 
for tag in tags:
    sum = sum + int(tag.contents[0])
print (sum)

