'''
cookies操作
'''

from selenium import webdriver

browser = webdriver .Chrome ()
browser .get('https://www.zhihu.com/explore')
print(browser .get_cookies() )

browser .add_cookie({'name':'ming','domain':'www.zhihu.com','value':'fengzi'})
print(browser .get_cookies() )
print(browser .get_cookie('name') )

browser .delete_cookie('name')
print(browser .get_cookies() )

browser .delete_all_cookies()
print(browser .get_cookies() )

browser .close()