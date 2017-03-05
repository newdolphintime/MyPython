import requests
import urllib.request
from bs4 import BeautifulSoup
url = 'http://www.bobx.com/idol/yoshioka-riho'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/51.0.2704.63 Safari/537.36'}
req = requests.get(url=url, headers=headers)

bsObj = BeautifulSoup(req.content, "html.parser")
nameList = bsObj.findAll("a", {"class":"medblack"})
for name in nameList:
    album=name.get_text()
    url = name['href']
    print(album,url)
#print(req.content.decode('utf-8'))
