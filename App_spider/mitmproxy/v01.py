

import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 7.1.2; MI 5X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
}

proxies = {
    'https':'http://192.168.23.5:8888',
    'http':'http://192.168.23.5:8888'
}

url ='http://httpbin.org/get'
rsp =requests .get(url,headers=headers ,proxies =proxies )
print(rsp.text)