'''
知乎登录
'''
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

PLATFORM='Android'
deviceName='MI_5X'
app_package='com.zhihu.android'
app_activity='.app.ui.activity.MainActivity'
driver_server='http://127.0.0.1:4723/wd/hub'

class Moments():
    def __init__(self):
        self.desired_caps={
        'platformName':PLATFORM,
        'deviceName':deviceName,
        'appPackage':app_package,
        'appActivity':app_activity}
        self.driver=webdriver.Remote(driver_server,self.desired_caps)
        self.wait=WebDriverWait(self.driver,300)

    def login(self):
        print('输入手机号。。。。')
        phone_number = self.wait.until(EC.presence_of_element_located((By.ID,'com.zhihu.android:id/edit_text')))
        phone_number .set_text('15927099527')

        button = self.wait .until(EC .element_to_be_clickable ((By .ID ,'com.zhihu.android:id/btn_progress')))
        button .click()
        print('正在获取验证码。。。')

    def main(self):
        self.login()

if __name__ == '__main__':

    M = Moments()
    M.main()