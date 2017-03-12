import requests
import urllib.request
from bs4 import BeautifulSoup
baseurl='http://www.bobx.com'
url = 'http://www.bobx.com/idol/riho-yoshioka/photoset/wpb-net-_183-4-2015-06_07-0-2-8.html'
headers = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection' : 'Keep-Alive',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

photoAdress=set()

while url is not None:
    req = requests.get(url=url, headers=headers)
    bsObj = BeautifulSoup(req.content, "html.parser")
    name = bsObj.find("link", {"rel": "next"})
    photoList = bsObj.findAll("td", {"valign": "TOP"})
    for photo in photoList:
        photoAdress.add(photo.a['href'])
    if name is not None:
        url = name["href"]
        print(url)
    else:
        url=None
print(len(photoAdress))
print(photoAdress)

for jpgadress in photoAdress:
    url=baseurl+jpgadress
    req = requests.get(url=url, headers=headers)
    bsObj = BeautifulSoup(req.content, "html.parser")
    jpgname = bsObj.find("a", {"class":"smallblack"})
    print(jpgname['href'])