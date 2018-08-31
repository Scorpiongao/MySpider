'''
通过webdriver操作标签进行查找
'''

from selenium import webdriver
import time
import logging
from selenium .webdriver .common .by import  By
from selenium .webdriver .support import  expected_conditions as EC
#等待时间
from selenium .webdriver .support.wait  import WebDriverWait
# 通过Keys模拟键盘
from selenium.webdriver.common.keys import  Keys

# 操作哪个浏览器就对哪个浏览器建一个实例
# 自动按照环境变量查找相应的浏览器
#使用phantomJS()无界面浏览器会有警告信息
#清除警告信息
logging .captureWarnings(True )
driver = webdriver.PhantomJS()


try:
    # 如果浏览器没有在相应环境变量中，需要指定浏览器位置
    driver.get("http://www.baidu.com")

    # 通过函数查找title标签
    print("Title: {0}".format(driver.title))


    input = driver .find_element_by_id('kw')
    # driver .find_elements(By.ID,'kw')
    input .send_keys('python')
    #键盘中的enter键
    input .send_keys(Keys .ENTER )
    #设置最长等待时间
    wait = WebDriverWait (driver ,10)
    #等待条件为页面中出现 id= 'content_left'
    wait .until(EC.presence_of_element_located ((By .ID ,'content_left')))
    #页面截屏
    driver.save_screenshot('python.jpg')

    #当前url
    print(driver .current_url )

    print(driver .get_cookies() )
    print(driver .page_source )
finally:
    driver .close()


