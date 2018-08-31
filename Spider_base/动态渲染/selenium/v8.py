'''
前进和后退
'''
import time
from selenium import webdriver


browser = webdriver .Chrome ()

browser .get('https://www.baidu.com')
browser .get('https://www.taobao.com')
browser .get('https://www.python.org')

browser .back()
print(browser .title )
time.sleep(2)

browser .forward()
print(browser .title )
time.sleep(2)

browser .close()
