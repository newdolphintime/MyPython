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
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/51.0.2704.63 Safari/537.36'}
req = requests.get(url=baseurl+url, headers=headers)

bsObj = BeautifulSoup(req.content, "html.parser")
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
    filepath = branchpath + "\\" + album + ".txt"
    f = open(filepath,'w')
    for jpgadress in photoAdress:
        url=baseurl+jpgadress
        req = requests.get(url=url, headers=headers)
        bsObj = BeautifulSoup(req.content, "html.parser")
        jpgname = bsObj.find("a", {"class":"smallblack"})
        print(baseurl+jpgname['href'])
        str=baseurl+jpgname['href']+"\n"
        f.write(str)
        f.flush()
        print("写入成功")
    f.close()





