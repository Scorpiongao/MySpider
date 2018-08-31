'''
选项卡管理
'''
import time
from selenium import webdriver

browser = webdriver .Chrome ()
browser .get('https://www.baidu.com')
#执行javascript语句window.open()开启一个选项卡
browser .execute_script('window.open()')
#获取选项卡列表
print(browser .window_handles )
#切换选项卡，新开的那个去
browser .switch_to_window(browser .window_handles [1])
browser .get('https://www.taobao.com')

time.sleep(2)
#切换选项卡
browser .switch_to_window(browser .window_handles [0])
browser .get('https://python.org')

time .sleep(2)
browser .close()