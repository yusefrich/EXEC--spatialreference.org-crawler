import urllib.request
import re
from bs4 import BeautifulSoup
import json

onloop = True
data = {}
data['spatialref'] = []
pages = 1

while onloop :
    print("crawler in page number = {}\b".format(pages))
    print("---------------------------------------------------------\b")
    content = urllib.request.urlopen("https://spatialreference.org/ref/epsg/?page={}".format(pages)).read()
    soup = BeautifulSoup(content)

    print("Page request successful \b")
    print("---------------------------------------------------------\b")

    alllis = soup.find_all('li')
    
    counter = 0
    for li in alllis:
        counter = counter + 1
        print(li.text)
        print("\b")
        data['spatialref'].append({
            "full": li.text,
            "number": li.a.string,
        })

    print("---------------------------------------------------------\b")
    print("counter of li tags retuned a value of = {}\b".format(counter))

    if counter == 0 :
        onloop = False

    print("onLoop= {}\b".format(onloop))

    pages = pages + 1

print("---------------------------------------------------------\b")
print("Loop finished, the values will be written on the .json file\b")

with open('spatialref.json', 'w') as outfile:
    json.dump(data, outfile)