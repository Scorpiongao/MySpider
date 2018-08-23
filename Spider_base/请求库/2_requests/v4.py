'''
requests.post
'''

import requests

data = {
    'username':'ming',
    'password':123456
}

headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'
}

#post方法,data=data提交表单数据
rsp = requests .post('http://httpbin.org/post',data= data,headers=headers  )

#返回对象

#json对象数据
print(type(rsp.text))
print(rsp.text )

#json数据格式转化为字典，方便提取
print(rsp.json() )
print(type(rsp.json() ))
