'''
执行JavaScript---下拉进度条
'''

from selenium import webdriver


browser = webdriver .Chrome ()

browser .maximize_window()
url = 'https://www.zhihu.com/explore'

browser .get(url)
#执行javascript,window.scrollTo()进度条下拉从哪到哪
browser .execute_script('window.scrollTo(0,document.body.scrollHeight)')
#弹出alert提示框
browser .execute_script('alert("To Bottom")')