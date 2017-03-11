import requests
import urllib.request
from bs4 import BeautifulSoup
baseurl='http://www.bobx.com'
url = 'http://www.bobx.com/idol/riho-yoshioka/photoset/wpb-2016-_48-0-2-8.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/51.0.2704.63 Safari/537.36'}
req = requests.get(url=url, headers=headers)

bsObj = BeautifulSoup(req.content, "html.parser")
nameList = bsObj.findAll("td", {"valign":"TOP"})
for name in nameList:

    print(name.a['href'])
