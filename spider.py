#经过分析得出结果 还是日文界面的东西好提取！
import requests
import urllib.request
from bs4 import BeautifulSoup
import os
def mkdir(path):
    # 引入模块
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print(path + ' 创建成功')
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False
#############################################
#################开始采集数据##################
#############################################
baseurl='http://www.bobx.com'
url = '/idol/yoshioka-riho/'
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
# 定义要创建的目录
mainpath = "d:\\"+path[2]
# 调用函数
mkdir(mainpath)
for name in nameList:
    album=name.get_text()
    url = name['href']
    print('-------------------------------------------------------------------------------------------')
    print(album)
    print('-------------------------------------------------------------------------------------------')
    print(baseurl+url)
    branchpath=mainpath+"\\"+album
    mkdir(branchpath)
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
    filepath = branchpath + "\\" + album + ".txt"
    jpgAdressSet=set()
    for jpgadress in photoAdress:
        url=baseurl+jpgadress
        req = requests.get(url=url, headers=headers)
        bsObj = BeautifulSoup(req.content, 'html5lib')
        jpgname = bsObj.find("a", {"class":"smallblack"})
        print(baseurl+jpgname['href'])
        str=baseurl+jpgname['href']+"\n"
        jpgAdressSet.add(str)

    f = open(filepath, 'w')
    f.writelines(jpgAdressSet)
    f.flush()
    print("写入成功")
    f.close()





