'''
微信朋友圈抓取
'''
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import re
import time
import pymongo


PLATFORM='Android'
deviceName='MI_5X'
app_package='com.tencent.mm'
app_activity='.ui.LauncherUI'

driver_server='http://127.0.0.1:4723/wd/hub'
TIMEOUT = 300

#MONGODB配置
MONGO_URL = 'localhost'
MONGO_DB = 'weixin'
MONGO_COLLECTION = 'moments'

#登录信息
USERNAME = '15927099527'
PASSWORD = 'mlf1456586096'

#滑动点
FLICK_START_X = 300
FLICK_START_Y = 300
FLICK_DISTANCE = 700

class Moments():
    def __init__(self):
        '''
        初始化
        '''
        #驱动配置
        self.desired_caps={
        'platformName':PLATFORM,
        'deviceName':deviceName,
        'appPackage':app_package,
        'appActivity':app_activity}
        self.driver=webdriver.Remote(driver_server,self.desired_caps)
        self.wait=WebDriverWait(self.driver,300)

        #mongodb配置
        self.client = pymongo .MongoClient (MONGO_URL )
        self.db = self .client [MONGO_DB ]
        self.collection = self.db[MONGO_COLLECTION ]

    def login(self):
        '''登录'''
        #登录按钮
        print('等待登录。。。')
        login = self.wait.until(EC.presence_of_element_located((By.ID,'com.tencent.mm:id/dbe')))
        login  .click()

        #手机号输入
        print('输入手机号。。。')
        phone = self.wait .until(EC.presence_of_element_located ((By .ID ,'com.tencent.mm:id/jd')))
        phone .set_text(USERNAME )

        #下一步
        next = self.wait .until(EC.presence_of_element_located ((By .ID ,'com.tencent.mm:id/ao8')))
        next .click()

        #输入密码
        # password = self.wait .until(EC .presence_of_element_located ((By .XPATH ,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText')))
        print('输入密码。。。')
        password = self.wait .until(EC.presence_of_element_located ((By .ID,'com.tencent.mm:id/jd')))
        password .set_text(PASSWORD)

        #提交登录
        submit = self.wait .until(EC.presence_of_element_located ((By .ID ,'com.tencent.mm:id/ao8')))
        submit.click()
        print('登录中。。。')

        # 提示信息
        tip = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/apj')))
        tip.click()


        print('登录成功！')

    def enter(self):
        '''选项卡，选择朋友圈'''
        #选择发现
        time.sleep(5)
        print('点击发现按钮。。。')
        # tab = self.wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.RelativeLayout[@resoure-id="com.tencent.mm:id/bg"]/android.widget.LinearLayout/android.widget.RelativeLayout[3]')))
        tab = self.wait .until(EC.presence_of_element_located ((By .XPATH ,'//android.widget.FrameLayout[@content-desc="当前所在页面,与的聊天"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView')))
        tab.click()

        #朋友圈
        print('查看朋友圈。。。')
        moments = self.wait .until(EC.presence_of_element_located ((By .XPATH ,'//android.widget.FrameLayout[@content-desc="当前所在页面,与的聊天"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.mm.ui.mogic.WxViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]')))
        # moments = self.wait .until(EC.presence_of_element_located ((By .XPATH ,'//*[@resource-id="com.tencent.mm:id/acu"]/android.widget.LinearLayout[1]')))
        print(moments )
        moments .click()
        print('进入朋友圈。。。')
        time.sleep(3)
        print('开始爬取。。。')

    def crawl(self):
        '''抓取'''
        try:
            time.sleep(3)
            while True :
                #上滑
                self.driver .swipe(FLICK_START_X ,FLICK_START_Y +FLICK_DISTANCE ,FLICK_START_Y ,FLICK_START_Y )

                #当前页面显示的所有状态
                # items = self.wait .until(EC. presence_of_all_elements_located  ((By .XPATH,'//*[@resource-id="com.tencent.mm:id/doq"]//android.widget.FrameLayout')))
                items = self.wait.until(
                    EC.presence_of_all_elements_located((By.XPATH, '//*[@resource-id="com.tencent.mm:id/dq2"]')))
                # print(items )
                # print(type(items ))
                #遍历每条状态
                for item in items :
                    try:
                        #昵称
                        nickname = item.find_element_by_id('com.tencent.mm:id/aul').get_attribute('text')
                        #内容
                        content = item.find_element_by_id ('com.tencent.mm:id/dq6').get_attribute('text')
                        #日期
                        date = item .find_element_by_id ('com.tencent.mm:id/dq9').get_attribute('text')
                        #处理日期
                        # print(date)
                        # date = self.handler_date(date)
                        print(nickname ,content ,date)
                        data = {
                            'nickname':nickname ,
                            'content' : content ,
                            # 'date' : date
                        }
                        self.save_to_mongo(data)
                    except NoSuchElementException:
                        pass
        except TimeoutException:
            self.crawl()

    def save_to_mongo(self,data):
        if data and self.collection .update({'nickname':data['nickname'],'content':data['content']},{'$set':data},True ) :
            print('Saved to mongo...',data)
        else :
            print('Failed to mongo...')

    def handler_date(self,date):
        '''处理时间'''
        if re.match('\d+分钟前',date):
            minute = re.match('(\d+)',date).group(1)
            date = time.strftime('%Y-%m-%d',time.localtime(time.time() - float (minute )*60))
        if re.match('\d+小时前',date):
            hour = re.match('(\d+)',date).group(1)
            date = time.strftime('%Y-%m-%d',time.localtime(time.time() - float(hour)*60*60) )
        if re.match('昨天',date):
            date = time.strftime('%Y-%m-%d',time.localtime(time.time() - 24*60*60) )
        if re.match('\d+天前',date):
            day = re.match('(\d+)',date).group(1)
            date = time.strftime('%Y-%m-%d',time.time() - float(day) *24*60*60)
        return date

    def main(self):
        #登录
        self.login()
        #进入朋友圈
        self.enter()
        #爬取
        self.crawl()

if __name__ == '__main__':

    M = Moments()
    M.main()