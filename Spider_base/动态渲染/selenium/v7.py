'''
延时等待---显示等待
'''

from selenium import webdriver
import time
import logging
from selenium .webdriver .common .by import  By
from selenium .webdriver .support import  expected_conditions as EC
#等待时间
from selenium .webdriver .support.wait  import WebDriverWait
from selenium .common .exceptions import  TimeoutException,NoSuchElementException
# 通过Keys模拟键盘
from selenium.webdriver.common.keys import  Keys


browser = webdriver .Chrome ()

url = 'https://www.taobao.com/'
browser .get(url)
#指定最长等待时间
wait = WebDriverWait (browser ,10)
try:
    #调用方法until(),等待条件为presence_of_element_located(): 代表节点出现，参数为节点的定位元组
    input = wait .until(EC.presence_of_element_located ((By .ID ,'q')))
    #等待条件为element_to_be_clickable(): 表示节点可点击，参数为节点定位元组
    button = wait.until(EC.element_to_be_clickable ((By .CSS_SELECTOR ,'.btn-search')))
    print(input,button)
except TimeoutException :
    print('TIME OUT.')
