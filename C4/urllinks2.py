import urllib.request,urllib.error,urllib.parse
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode=ssl.CERT_NONE

url = input('Enter URL: ')
c = int(input('Enter Count: '))
p = int(input('Enter pos: '))
sum = 0
name = None 
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,'html.parser')
tags = soup('a')
for a in range(c):


    url=tags[p-1].get('href',None)
    print(url)
    name =tags[p-1].contents[0]#tag.get('href',none)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html,'html.parser')
    tags = soup('a')
    
    
    


    
print (name)

