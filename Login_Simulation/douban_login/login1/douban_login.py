'''
利用selenium模拟登录豆瓣
需要输入验证码
思路：
1. 保存页面成快照
2. 等待用户手动输入验证码
3. 继续自动执行提交等动作

'''

from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import time
from io import BytesIO
from PIL import Image


url = 'https://accounts.douban.com/login?alias=&redir=https%3A%2F%2Fwww.douban.com%2F&source=index_nav&error=1001'
driver = webdriver.Chrome()
driver.get(url)

time.sleep(4)

# 生成快照，用来查看验证码
screen_shot = driver.get_screenshot_as_png()
screen_shot = Image .open(BytesIO (screen_shot))
img = driver.find_element_by_css_selector('.item-captcha img')
#图片位置
location = img.location
#图片宽高
size = img.size

top,bottom,left,right = location ['y'],location ['y'] + size['height'],location ['x'],location ['x']+size ['width']
print(top,bottom ,left ,right )
#截取图片
code_png = screen_shot .crop((left,top ,right ,bottom ))
code_png .save('captcha.png')

captcha = input("plz input youre code:")

# 利用账户信息和验证码登录
driver.find_element_by_id("email").send_keys("1456586096@qq.com")
driver.find_element_by_id("password").send_keys("mlf123456")
driver.find_element_by_id("captcha_field").send_keys(captcha)


driver.find_element_by_xpath("//input[@class='btn-submit']").click()

time.sleep(3)

driver.save_screenshot("logined.png")

with open("douban_home.html", 'w', encoding='utf-8') as file:
    file.write(driver.page_source)

driver.quit()
