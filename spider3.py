import requests
import urllib.request
from bs4 import BeautifulSoup
baseurl='http://www.bobx.com'
url = 'http://www.bobx.com/idol/riho-yoshioka/riho-yoshioka-4580454.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/51.0.2704.63 Safari/537.36'}
req = requests.get(url=url, headers=headers)

bsObj = BeautifulSoup(req.content, "html.parser")
name = bsObj.find("a", {"class":"smallblack"})
print(name['href'])