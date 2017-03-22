#<img name="gsplitjp" src="http://img.bobx.com/images/gsplitjp0.gif" border="0" ALT="japanese picture gallery of Yua Mikami" WIDTH="23" HEIGHT="23">
import requests
import urllib.request
from bs4 import BeautifulSoup
baseurl='http://www.bobx.com'
url = '/av-idol/mikami-yua/'
url='/av-idol/yua-mikami/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/51.0.2704.63 Safari/537.36'}
req = requests.get(url=baseurl+url, headers=headers)

bsObj = BeautifulSoup(req.content, "html.parser")
nameList = bsObj.findAll("a", {"class":"medblack"})
jp = bsObj.find("img",{"name":"gsplitjp"})
print(jp)
if jp is not None:
    print("该链接是美链，请更换")
    exit()
    for name in nameList:
        album=name.get_text()
        url = name['href']
        print('-------------------------------------------------------------------------------------------')
        print(album)
        print('-------------------------------------------------------------------------------------------')
        print(baseurl+url)