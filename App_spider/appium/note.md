# Appium
- Selenium : 网页端自动化测试工具，抓取JavaScript渲染的网页
- Appium : 跨平台移动端自动化测试工具，为iOS和Android平台创建自动化测试用例，app抓取
- 可以模拟App内部的各种操作 ：点击、滑动、文本输入等，手工操作的Appium都可以完成

## 1. 准备工作
- 环境搭建
    - Java + Appium + Sdk + Android Studio + Appium-Python-Client
- 参考配置环境
    - [用Appium抓取手机app微信的数据](https://blog.csdn.net/fan_shui/article/details/81413595)
    - [Java配置](https://jingyan.baidu.com/article/fd8044fa2c22f15031137a2a.html)
    - [崔大--Appium安装](https://cuiqingcai.com/5407.html)
    - [悠悠博主--Appium + Python环境搭建](https://www.cnblogs.com/yoyoketang/p/6128725.html)
    - [Appium-Python-Client](https://github.com/appium/python-client)
        - `pip install Appium-Python-Client`

## 2. 启动App
- ### Appium内置驱动器打开App
    - 数据线 --> 手机连接到电脑 --> 打开USB调试功能 (打开开发者选项-->USB安全设置，否则会出现Permission错误)
    - Start Server --> Start New Session
    - 配置启动App时的Desired Capabilities参数
        - platformName : 平台名称，Android或iOS
        - deviceName : 设备名称，指手机的具体类型
            - 查看：cmd --> adb devices -l 
        - appPakeage : App程序包名
        - appActivity :　入口Activity名，以.开头
            - [查看appPakeage和appActivity](https://blog.csdn.net/mtbaby/article/details/78676477)
            - 手机上打开该程序
            - cmd --> adb shell --> dumpsys activity | grep mFocusedActivity
    - Start Session 即可
        - Tap : 按钮点击功能
        - Send Keys : 完成文本的输入
        
    - 在Sdk下的tools下打开uiautomatorviewer.bat也可查看
        - 本机 `C:\Users\zs\AppData\Local\Android\Sdk\tools\bin\uiautomatorviewer.bat`

- ### 利用Python程序实现启动操作
    - [appium/python-client](https://github.com/appium/python-client)
    - [appium-python API中文版](https://testerhome.com/topics/3711)
    - 字典类型配置Desired Capabilities参数
        - `server = 'http://localhost:4723/wd/hub'`
        - ```desired_caps = {
                                'platforeName':'Android',
                                'deviceName':'MI_5X',
                                'appPackage':'com.tencent.mm',
                                'appActivity':'.ui.LauncherUI'
                            }
                            ```
        - `driver = webdriver.Remote(server,desired_caps)`
        - 案例v1
    - **初始化**
    ```cython
    from appium import webdriver
    
    server = 'http://localhost:4723/wd/hub'
    desired_caps = {
                    'platforeName':'Android',
                    'deviceName':'MI_5X',
                    'appPackage':'com.tencent.mm',
                    'appActivity':'.ui.LauncherUI'
                }
    driver = webdriver .Remote (server ,desired_caps )
    ```
    - **查找元素**
        - 使用Selenium中的通用查找方法实现元素查找
            - find_element_by_id
            - find_elements_by_name
            - find_elements_by_xpath
            - find_elements_by_link_text
            - find_elements_by_partial_link_text
            - find_elements_by_tag_name
            - find_elements_by_class_name
            - find_elements_by_css_selector
        - Android平台，还可以使用UIAutomator进行元素选择
            - find_element_by_android_uiautomastor('new UiSelector().description("Animation")')
            - find_element_by_android_uiautomastor('new UiSelector().clickable(true)')
        - iOS平台
            - find_element_by_ios_uiautomastor('.elements()[0]')
            - find_elements_by_ios_uiautomastor('.elements())
    - **点击**
        - tap(self,positions,duration=None) 方法模拟手指点击（最多五个手指），可设置按时长短
            - positions : 点击位置组成的列表
            - duration : 点击持续的时间，毫秒
            - driver.tap([(100,10),(200,100),(439,204)],500)
        - click() : 对于某个元素，直接调用click()实现模拟点击
    
    - **屏幕拖动**
        - scroll(self,origin_el,destination_el) : 模拟屏幕滚到
            - origin_el : 被操作的元素
            - destination_el : 目标元素
            - `driver.scroll(el1,el2)`
        - swipe(self,start_x,start_y,end_x,end_y,duration = None) : 模拟从A点滑动到B点
            - start_x : 开始位置横坐标
            - start_y : ....
            - end_x : ...
            - end_y : ...
            - duration : 持续时间
            - `driver.swipe(100,100,200,400,5000)`
        - flick(self,start_x,start_y,end_x,end_y) : 模拟从A点快速滑动到B点
            - `driver.flick(100,100,200,400)`
          
    - **拖拽**
        - drag_and_drop(self,origin_el,destination_el) : 拖动元素到目标元素
            - `driver.drag_and_drop(el1,el2)`
    - **文本输入**
        - set_text() : 实现文本输入
        - `el .set_text('hello world')`
    - **动作链**
        - Selenium : ActionChains
        - Appium : TouchAction
            - tap()
                - 点击
                ```
                el = self.driver.find_element_by_accessibility_id('Animation')
                action = TouchAction(self.driver)
                action.tap(el).perform()
                ```
            - press()
                - 拖动
                ```
                els = self.driver.find_elements_by_id('listView')
                a1 = TouchAction()
                a1.press(els[0]).move_to(x=10,y=0).move_to(x=10,y=-75).move_to(x=10,y=-600).release()
                
                a2 = TouchAction()
                a2.press(els[1]).move_to(x=10,y=10).move_to(x=10,y=-300).move_to(x=10,y=-600).release()
                ```
            - long_press()
            - release()
            - move_to()
            - wait()
            - cancel()
    - 案例weixin_moments
            
        
