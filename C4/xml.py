import urllib.request,urllib.error,urllib.parse
import ssl
import xml.etree.ElementTree as et

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode=ssl.CERT_NONE

url = input('Enter URL: ')
print('Retrieving ', url)
html = urllib.request.urlopen(url, context=ctx).read()

#print(html.decode())
print('Retrieved ',len(html),' characters')
tree = et.fromstring(html)
count = tree.findall('.//count')
print('Counts: ',len(count))
sum =0
for c in count:
    sum = sum + int(c.text)
print(sum)