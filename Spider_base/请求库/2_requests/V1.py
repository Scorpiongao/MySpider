import requests


url = "http://www.baidu.com"
# 两种请求方式
# 使用get请求
rsp = requests.get(url)

#响应
print(rsp.text)
print(type(rsp))
print(rsp.status_code )
print(rsp.cookies )
for k,v in rsp.cookies .items() :
    print(k + "=" +v)
print(rsp.headers )
print(rsp.request .headers)

# 使用request请求
rsp = requests.request("get", url)
print(rsp.text)