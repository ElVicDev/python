import urllib.request as ur
import json

url = input("Enter location: ")
""" Datos de muestra: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
    Datos reales: http://py4e-data.dr-chuck.net/comments_1470272.json (La suma termina en 11)
"""

print("Retrieving ", url)
data = ur.urlopen(url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
data_json = json.loads(data)

sum = 0
num = 0
for comment in data_json["comments"]:
    sum += int(comment["count"])
    num += 1

print('Count:', num)
print('Sum:', sum)
