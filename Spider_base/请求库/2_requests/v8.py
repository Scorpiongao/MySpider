'''
ssl验证
'''

import requests

import logging

##忽略警告信息
logging  .captureWarnings(True)

# 访问https站点，出现证书验证错误页面
# 设置verify = False可正常访问
rsp = requests .get('https://www.12306.cn',verify =False )


#但会报一个警告
print(rsp.status_code )



