import requests
import urllib.request
from bs4 import BeautifulSoup
baseurl='http://www.bobx.com'
url = '/av-idol/mikami-yua/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/51.0.2704.63 Safari/537.36'}
req = requests.get(url=baseurl+url, headers=headers)

bsObj = BeautifulSoup(req.content, "html.parser")
nameList = bsObj.findAll("a", {"class":"medblack"})
othername = bsObj.findAll("a",{"rel":"nofollow"})
for name in othername:
    print(name)
for name in nameList:
    album=name.get_text()
    url = name['href']
    print('-------------------------------------------------------------------------------------------')
    print(album)
    print('-------------------------------------------------------------------------------------------')
    print(baseurl+url)
    url=baseurl+url
