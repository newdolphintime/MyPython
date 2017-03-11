import requests
import urllib.request
from bs4 import BeautifulSoup
baseurl='http://www.bobx.com'
url = 'http://www.bobx.com/idol/riho-yoshioka/photoset/wpb-net-_183-4-2015-06_07-0-2-8.html'
headers = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection' : 'Keep-Alive',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
req = requests.get(url=url, headers=headers)
print(req.content)
bsObj = BeautifulSoup(req.content, "html.parser")

nameList = bsObj.findAll("link", {"rel":"next"})
for name in nameList:
    print(name["href"])