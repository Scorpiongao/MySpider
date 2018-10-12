'''
taobao - selenium测试
'''

from selenium import webdriver
from selenium .common .exceptions import  TimeoutException
from selenium .webdriver .common .by import  By
from selenium .webdriver .support .ui import WebDriverWait
from selenium .webdriver .support import expected_conditions as EC
from urllib .parse import quote
import time

base_url = 'https://s.taobao.com/search?q='
keyword = '算法'

search_url = base_url + quote(keyword )

browser = webdriver .Chrome ()
browser .maximize_window()

browser .get(search_url )
#手机扫码登录
time.sleep(20)

print(browser .page_source)


