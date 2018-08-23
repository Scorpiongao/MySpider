'''
代理proxies
'''

import requests

proxies = {
    'http':'123.56.169.22:3128',
    'https':'123.56.169.22:3128'
}

params = {
    'name':'ming',
    'age':18
}

headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'
}
#get方法url中带参数的,拼接成完整URL
rsp = requests .get('http://httpbin.org/get',params= params,headers=headers ,proxies =proxies  )

#返回对象

#json对象数据
print(type(rsp.text))
print(rsp.text )