'''
获取节点信息
'''
from selenium import webdriver


browser = webdriver .Chrome ()

browser .maximize_window()
url = 'https://www.zhihu.com/explore'

browser .get(url)

logo = browser .find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.id )
#获取属性
print(logo.get_attribute('class') )

#获取文本值
print(logo.text )

input = browser .find_element_by_css_selector('.zu-top-search-input')
print(input)
#获取id
print(input .id )
#获取标签名
print(input .tag_name )
#获取位置
print(input .location )
#获取大小：宽高
print(input .size )
