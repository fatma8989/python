import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.xcite.com/mobile-zone.html")
content = BeautifulSoup(page.content, "html.parser")
x = content.find_all('img')
for i in x:
    try:
        print(i['data-lazy'])
    except:
        pass