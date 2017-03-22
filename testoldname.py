#经过分析得出结果 还是日文界面的东西好提取！
import requests
import urllib.request
import re
from bs4 import BeautifulSoup
baseurl='http://www.bobx.com'
url = '/av-idol/mikami-yua/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/51.0.2704.63 Safari/537.36'}
req = requests.get(url=baseurl+url, headers=headers)

bsObj = BeautifulSoup(req.content, "html.parser")
nameList = bsObj.findAll("a",{"href":re.compile("\/[idol|av_idol]\/jp_index.html")})
for name in nameList:
    print(name)