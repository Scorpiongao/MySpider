'''
session会话维持
'''

import requests

#设置cookies = {'number':'123456'}
requests .get('http://httpbin.org/cookies/set/number/123456')
#尝试获得cookies
rsp = requests .get('http://httpbin.org/cookies')

#这种方式没成功
print(rsp.text )
#其实是俩次访问服务器，相当于不同的会话，当然获取不到


#session
s = requests .Session ()

#设置cookies = {'number':'123456'}
s .get('http://httpbin.org/cookies/set/number/123456')
#尝试获得cookies
rsp = s .get('http://httpbin.org/cookies')

#这种方式没成功
print(rsp.text )

