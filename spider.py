#经过分析得出结果 还是日文界面的东西好提取！
import requests
import urllib.request
from bs4 import BeautifulSoup
baseurl='http://www.bobx.com'
url = '/av-idol/mikami-yua/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/51.0.2704.63 Safari/537.36'}
req = requests.get(url=baseurl+url, headers=headers)

bsObj = BeautifulSoup(req.content, "html.parser")
nojpUrl = bsObj.find("img", {"name":"gsplitjp"})
nameList = bsObj.findAll("a", {"class":"medblack"})
if nojpUrl is not None:
    print("请切换日链")
    exit()
for name in nameList:
    album=name.get_text()
    url = name['href']
    print('-------------------------------------------------------------------------------------------')
    print(album)
    print('-------------------------------------------------------------------------------------------')
    print(baseurl+url)
    url=baseurl+url
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
        print(baseurl+jpgname['href'])