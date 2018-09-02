'''
点击验证码测试，登录12306平台
'''
import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chaojiying import Chaojiying
from config import *

USERNAME = USERNAME
PASSWORD = HCP_PASSWORD

CHAOJIYING_USERNAME = CHAOJIYING_USERNAME
CHAOJIYING_PASSWORD = CHAOJIYING_PASSWORD
CHAOJIYING_SOFT_ID = CHAOJIYING_SOFT_ID
CHAOJIYING_KIND = CHAOJIYING_KIND


class CrackTouClick():
    def __init__(self):
        self.url = 'https://kyfw.12306.cn/otn/login/init'
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, 20)
        self.username = USERNAME
        self.password = PASSWORD
        self.chaojiying = Chaojiying(CHAOJIYING_USERNAME, CHAOJIYING_PASSWORD, CHAOJIYING_SOFT_ID)

    def __del__(self):
        self.browser.close()

    def open(self):
        """
        打开网页输入用户名密码
        :return: None
        """
        self.browser.get(self.url)

        username = self.wait.until(EC.presence_of_element_located((By.ID, 'username')))
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'password')))
        username.send_keys(self.username )
        password.send_keys(self.password)


    def get_touclick_button(self):
        """
        获取初始验证按钮
        :return:
        """
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME , 'geetest_radar_tip')))
        return button


    def get_touclick_element(self):
        """
        获取验证图片对象
        :return: 图片对象
        """
        element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'touclick-img-par')))
        return element

    def get_position(self):
        """
        获取验证码位置
        :return: 验证码位置元组
        """
        element = self.get_touclick_element()
        time.sleep(2)
        location = element.location
        size = element.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        return (top, bottom, left, right)

    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图对象
        """
        # self.get_down()

        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        screenshot .save('screenshot.png')
        return screenshot

    def get_touclick_image(self, name='captcha.png'):
        """
        获取验证码图片
        :return: 图片对象
        """
        top, bottom, left, right = self.get_position()
        # top-=550
        # bottom-=500
        print('验证码位置', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save(name)
        return captcha

    def get_points(self, captcha_result):
        """
        解析识别结果
        :param captcha_result: 识别结果
        :return: 转化后的结果
        """
        groups = captcha_result.get('pic_str').split('|')
        locations = [[int(number) for number in group.split(',')] for group in groups]
        return locations

    def touch_click_words(self, locations):
        """
        点击验证图片
        :param locations: 点击位置
        :return: None
        """
        for location in locations:
            print(location)
            ActionChains(self.browser).move_to_element_with_offset(self.get_touclick_element(), location[0],
                                                                   location[1]).click().perform()
            time.sleep(1)

    # def touch_click_verify(self):
    #     """
    #     点击验证按钮
    #     :return: None
    #     """
    #     button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'touclick-pub-submit')))
    #     button.click()

    def login(self):
        """
        登录
        :return: None
        """
        submit = self.wait.until(EC.element_to_be_clickable((By.ID, 'loginSub')))
        submit.click()
        time.sleep(1)
        # print('登录成功')

    def crack(self):
        """
        破解入口
        :return: None
        """
        self.open()

        self.check_verify_again()

    def check_verify_again(self):
        # 获取验证码图片
        image = self.get_touclick_image()
        bytes_array = BytesIO()
        image.save(bytes_array, format='PNG')
        #识别验证码
        result = self.chaojiying.post_pic(bytes_array.getvalue(), CHAOJIYING_KIND)
        print(result)
        locations = self.get_points(result)
        self.touch_click_words(locations)
        # self.touch_click_verify()
        # 判定是否成功
        # success = self.wait.until(
        #     EC.text_to_be_present_in_element((By.CLASS_NAME, 'geetest_success_radar_tip_content'), '验证成功'))
        # print(success)
        time.sleep(1)
        self.login()
        try:
            success = self.wait .until(EC.presence_of_element_located((By .ID ,'my12306page')) )
            print(success )
            print('登录成功！')
            time.sleep(10)
        except Exception as e:
            print(e.args )
            return self.check_verify_again()


        # 失败后重试
        # if not success:
        #     self.crack()
        # else:
        #     self.login()


if __name__ == '__main__':
    crack = CrackTouClick()
    crack.crack()