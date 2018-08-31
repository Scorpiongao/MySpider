'''
切换Frame
'''

import time
from selenium import webdriver
from selenium .common .exceptions import  NoSuchElementException
from selenium .webdriver import ActionChains

browser = webdriver .Chrome ()

url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
#浏览器屏幕最大化
browser .maximize_window()
browser .get(url)
#切换到子Frame: iframeResult
browser .switch_to.frame('iframeResult')
try:
    logo = browser .find_element_by_css_selector('.logo')
except NoSuchElementException :
    print('NO LOGO')

#切换到父Frame
browser .switch_to.parent_frame()
logo = browser .find_element_by_css_selector('.logo')
print(logo)
print(logo.text )