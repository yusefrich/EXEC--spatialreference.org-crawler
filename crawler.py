import urllib.request
import re
from bs4 import BeautifulSoup
import json

onloop = True
data = {}
data['spatialref'] = []
pages = 1

while onloop :
    print("crawler na pagiana numero = {}\b".format(pages))
    print("---------------------------------------------------------\b")
    content = urllib.request.urlopen("https://spatialreference.org/ref/epsg/?page={}".format(pages)).read()
    soup = BeautifulSoup(content)

    print("Request da pagina foi okk \b")
    print("---------------------------------------------------------\b")

    alllis = soup.find_all('li')
    
    counter = 0
    for li in alllis:
        counter = counter + 1
        print(li.text)
        print("\b")
        data['spatialref'].append({
            li.a.string: li.text,
        })

    print("---------------------------------------------------------\b")
    print("counter retornou um valor maior que 1 = {}\b".format(counter))

    if counter == 0 :
        onloop = False

    print("onLoop= {}\b".format(onloop))

    pages = pages + 1

print("---------------------------------------------------------\b")
print("Loop terminou, valores serão esquitos em .json\b")

with open('spatialref.json', 'w') as outfile:
    json.dump(data, outfile)