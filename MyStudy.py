import requests
url='http://www.google.com'
headers = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection' : 'Keep-Alive',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
proxies = {
  'https': 'http://127.0.0.1:9000'
}
req = requests.get(url, headers=headers,proxies=proxies)
print(req.status_code)