'''selenium 扫码登录知乎'''

from selenium import webdriver
import requests
from selenium .webdriver .common.by   import By
from selenium .webdriver .support .ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium .common .exceptions import  TimeoutException
import time

browser = webdriver .Chrome ()
browser .maximize_window()
wait = WebDriverWait (browser ,10)


def login(url):
    '''登录'''
    browser.get(url)
    button = browser .find_element_by_css_selector('.Login-qrcode .Button--plain')
    print(button .text )
    button .click()
    #等待验证码出现
    wait .until(EC.presence_of_element_located ((By .CSS_SELECTOR ,'.Qrcode-img')))
    time.sleep(3)

if __name__ == '__main__':
    url = 'https://www.zhihu.com/signin'
    login(url)

    wait .until(EC.text_to_be_present_in_element ((By .CSS_SELECTOR ,'.Card .GlobalSideBar-navNumber'),str(16)))
    print('登录成功！')
    html = browser.page_source
    print(html)