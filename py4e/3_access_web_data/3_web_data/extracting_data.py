import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
sum = 0

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
# Datos de muestra: http://py4e-data.dr-chuck.net/comments_42.xml
# Datos reales: http://py4e-data.dr-chuck.net/comments_1470271.xml

print("Retrieving", url)

#serviceurl = urllib.request.Request(url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
name = tree.findall('.//comment')
print('Users:', len(name))
for item in name:
    sum = sum + int(item.find('count').text)
print("Sum:",sum)
