'''
cookies
'''
import requests

url = 'https://www.baidu.com/s?'

params = {
    'wd': '大熊猫'
}

headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'
}

rsp = requests .get(url,params= params ,headers=headers )

cookiejar = rsp.cookies

#cookieJar类型
print(type(cookiejar ))
print(cookiejar )

for k,v in cookiejar .items() :
    print(k + "=" +v)

#化为字典格式
cookiedict = requests .utils .dict_from_cookiejar(cookiejar)
print(type(cookiedict ))
print(cookiedict )
