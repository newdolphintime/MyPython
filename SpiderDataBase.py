import requests
import mysql.connector
from bs4 import BeautifulSoup
conn = mysql.connector.connect(user='photo', password='photo', database='photo')
cursor = conn.cursor()
#############################################
#################开始采集数据##################
#############################################
baseurl='http://www.bobx.com'
url = '/idol/takeda-rena/'
headers = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection' : 'Keep-Alive',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
req = requests.get(url=baseurl+url, headers=headers)

bsObj = BeautifulSoup(req.content, 'html5lib')
nojpUrl = bsObj.find("img", {"name":"gsplitjp"})
nameList = bsObj.findAll("a", {"class":"medblack"})
if nojpUrl is not None:
    print("请切换日链")
    exit()
path=url.split("/")

idol=path[2]

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
        bsObj = BeautifulSoup(req.content, 'html5lib')
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
        bsObj = BeautifulSoup(req.content, 'html5lib')
        jpgname = bsObj.find("a", {"class":"smallblack"})
        print(baseurl+jpgname['href'])
        donwloadadress=baseurl+jpgname['href']
        cursor.execute('insert into idol (idol, album,photolink) select %s,%s,%s from dual where  not exists (SELECT *FROM idol WHERE photolink = %s)', [idol, album , donwloadadress, donwloadadress])

    conn.commit()
    print("写入成功")
cursor.close()
conn.close()