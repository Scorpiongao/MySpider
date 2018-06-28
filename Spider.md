# 抓取
### 请求与解析
参考

- [抓包分析](https://zhuanlan.zhihu.com/p/23088379)

- [宁哥的小站](http://www.lining0806.com)


## 1. 最基本的抓取

- Requests:
```
import requests
resq=requests.get(url)
content=resq.text
print(content)
print(resq.headers)
```

- Urllib
```
import urllib
resq=urllib.urlopen(url)
content=resq.read()
print(content)
print(resq.headers)
```

- Httplib
```
import httplib
http=httplib.Http()
resq_headers,content=http.request(url,"GET")
print(content)
print(resq.headers)
```

## 2.带有查询字段的url,以？或&分割

data={"data1":"？？","data2":"？？？"}

- Requests
```
import requests
resq=requests.get(url=url,params=data)
或者
data=urllib.urlencode(data)
url=base_url+data
resq=requests.get(url=url)
```

实例
```

from urllib.parse import urlencode 

base_url="http://www.baidu.com/" 

data={ "pn":2, "type":"明星" } 

url=base_url+urlencode(data)
```


- Urllib
```
import urllib,urllib2
data=urllib.urlencode(data)
url=base_url+data
resq=urllib2.urlopen(url)
```

## 3.表单登录post
data={"data1":"？？","data2":"？？？"}

- Requests
```
import requests
resq=requests.post(url=url,data=data)
```

- Uillib2

```
import urllib,urllib2
data=urllib.urlencode(data)
resq=urllib2.Request(url,data)
request=urllib2.urlopen(resq)
```

-  使用cookie

```
import request
session=requests.session()
resq=session.post(url=login_url,data=data)


```
- 有验证码的

```
resq=session.get(url=login_url,cookies=cookies)
resq1=requests.get(url_login)#未登录
resq2=session.get(url_login)#登录，之前拿到了response.Cookies
resq3=session.get(url_results)#可以访问

```
# 反反爬虫

## 1.伪装headers
headers={"User-agent":"？？"}

headers={"User-agent":"？？","Referer":"?？？"}
```
from fake_useragent import UserAgent
ua=UserAgent()
headers={"User-agent":ua.random}
```

- Requests
```
import requests
resq=requests.get(url=url,headers=headers)
```

- Urllib2
```
resq=urllib.Request(url=url,headers=headers)
response=urllib2.urlopen(resq)
```

## 2.时间设置
```
import time
time.sleep(1)

```

## 3.代理IP
proxies={"http":"http://"+"ip"+":"+"port"}

- Requests

```
response=requests.get(url=url,proxies=proxies)
```

- Urllib

```
proxy_support=urllib.ProxyHandler(proxies)
opener=urllib.build_opener(proxy_support,urllib.HTTPHandler)
urllib.install_opener(opener)
resq=urllib.urlopen(url)
```
## cookie处理
```
r=requests.get(url,headers=headers)
for cookie in r.cookies.keys():
cookie_list.append(cookie+"="+r.cookies.get(cookie))
```

# 解析

-[Re](https://zhuanlan.zhihu.com/p/26019553)

-[Beautifulsoup](https://zhuanlan.zhihu.com/p/28759710)

-[Xpath](https://zhuanlan.zhihu.com/p/29436838)

-[PyQuery](https://zhuanlan.zhihu.com/p/25164773)

- 相对网址变为绝对网址
```
import urlparse
full_url=urlpase.urljoin(base_url,new_url)
```


# 存储

## 去重处理

1. 集合Set
2. 数据库MongoDB
```
import pymongo
client=pymongo.Client()
db=client["datadbname"]
db["tablename"].update({"url":result["url"]},{"$set":result},True)
```



