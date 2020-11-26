import urllib.parse,urllib.request,urllib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode=ssl.CERT_NONE


while True:
    sum = 0    
    url = input('Enter url: ')
    
    if len(url) < 1:
        break
    html = urllib.request.urlopen(url).read()
    data = html.decode()

    x = json.loads(data)

    print(x)
    print(len(x['comments']))
    for i in x['comments']:
        
        sum = sum+ int (i['count'])
    print(sum)
