import requests

params = {
    'name':'ming',
    'age':18
}

headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'
}
#get方法url中带参数的,拼接成完整URL
rsp = requests .get('http://httpbin.org/get',params= params,headers=headers  )

#返回对象

#json对象数据
print(type(rsp.text))
print(rsp.text )

#响应
print(rsp.status_code )
print(rsp.cookies )
print("response headers: ",rsp.headers )
print("request headers: ",rsp.request .headers)



#json数据格式转化为字典，方便提取
print(rsp.json() )
print(type(rsp.json() ))

