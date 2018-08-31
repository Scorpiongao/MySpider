# 动态HTML介绍
- JavaScrapt
- jQuery
- Ajax
- DHTML
- Python采集动态数据
    - 从Javascript代码入手采集
    - Python第三方库运行JavaScript，直接采集你在浏览器看到的页面

## Selenium
### 1. 准备工作
- Selenium: web自动化测试工具
    - 自动加载页面
    - 获取数据
    - 截屏
    - 安装： pip install selenium==2.48.0
    - 官网： http://selenium-python.readthedocs.io/index.html
- PhantomJS(幽灵)
    - 基于Webkit 的无界面的浏览器 
    - 官网： http://phantomjs.org/download.html

- chrome + chromedriver
    - 下载安装chrome： 下载+安装
    - [下载安装chromedriver](https://chromedriver.storage.googleapis.com/index.html)
    - 注意：chromedriver与chrome版本号对应
    - 环境变量配置
        - (Windows)直接将chromedriver.exe文件拖到Python的Scripts目录下
- firefox + geckodriver
    - 类似chrome
    - [geckodriver下载地址](https://github.com/mozilla/geckodriver/releases)

- Selenium 库有有一个WebDriver的API
- WebDriver可以跟页面上的元素进行各种交互，用它可以来进行爬取
- Selenium操作主要分两大类：
    - 得到UI元素
        - find_element_by_id
        - find_elements_by_name
        - find_elements_by_xpath
        - find_elements_by_link_text
        - find_elements_by_partial_link_text
        - find_elements_by_tag_name
        - find_elements_by_class_name
        - find_elements_by_css_selector
    - 基于UI元素操作的模拟
        - 单击
        - 右键
        - 拖拽
        - 输入
        - 可以通过导入ActionsChains类来做到
 
### 2. 基本使用
- 案例v1
- 声明浏览器对象
    - browser = webdriver.PhantomJS()
    - browser = webdriver.Chrome()
    - browser = webdriver.Firefox()
- 访问页面
    - browser.get(url)
    - browser.page_source
    - browser.get_cookies()
    - browser.current_url
- 查找结点
    - 单个节点
        - 方式一
            - find_element_by_id
            - find_elements_by_name
            - find_elements_by_xpath
            - find_elements_by_link_text
            - find_elements_by_partial_link_text
            - find_elements_by_tag_name
            - find_elements_by_class_name
            - find_elements_by_css_selector
        - 方式二
            - find_element(by=By.ID,value)
            - 俩个参数：查找方式和值
            - find_element_by_id(id) 等价于 find_element(By.ID,id)
    - 多个节点
        - 类似单个节点，只是为elements
        - 返回列表类型
        - ru: find_elements(By.CSS_SELECTOR,'#id li')
- 节点交互
    - 输入文字
        - send_keys()
    - 清空文字
        - clear()
    - 点击按钮
        - click()
    - [更多动作介绍](https://selenium-python.readthedocs.io/navigating.html#module-selenium.webdriver.remote.webelement)
    - 案例v2
    
- 动作链
    - 动作执行对象
    - 鼠标拖拽、键盘按键 
    - [动作链](https://selenium-python.readthedocs.io/navigating.html#drag-and-drop)
    - 案例v3

- 执行JavaScript
    - 某些操作，selenium API没有提供，如：下拉进度条
    - 直接模拟运行JavaScript
    - execute_script()实现
    - 案例v4

### 3. 获取节点信息
- 获取属性
    - get_attribute(name)
- 获取文本值
    - 属性 : text()
- 获取id、位置、标签名、大小
    - 属性：id,location,size,tag_name
- 案例v5

### 4. 切换Frame
- selenium默认在父级Frame里面操作的，不能直接获取子Frame的节点
- switch_to.frame(name)方法来切换到子Frame
- switch_to.parent_frame() : 切换到父Frame
- 案例v6

### 5. 延时等待
- 隐式等待
    - 指定节点，规定一个固定时间，超时抛出异常，页面加载时间会受到网络条件的影响
    - `browser.implicitly_wait(10)`
- 显示等待
    - 指定节点，指定一个最长等待时间，如在指定的时间内加载出节点则返回查找节点，反之，抛出异常
    - 案例v7
    - 常见等待条件如下：[更多等待条件(官网)](https://selenium-python.readthedocs.io/waits.html#)
    ```
    等待条件                                   含义
    title_is                               标题内容是
    title_contains                         标题包含某内容
    presence_of_element_located            节点加载出来，传入定位元组
    visibility_of_element_located          节点可见，传入定位元组
    visibility_of                          可见，传入节点对象
    presence_of_all_elements_located       所有节点加载出来
    text_to_be_present_in_element          某个节点文本包含某文字
    text_to_be_present_in_element_value    某个节点值包含某文字
    frame_to_be_available_and_switch_to_it  加载并切换
    invisibility_of_element_located         节点不可见
    element_to_be_clickable                 节点可点击
    staleness_of                          判断一个节点是否仍在DOM，可判断页面是否刷新
    element_to_be_selected                 节点可选择，传入节点对象
    element_located_to_selected            节点可选择，传入定位元组
    element_selection_state_to_be           传入节点对象及状态，相等返回True，反之False
    alert_is_present                         是否出现警告
    ```
    
### 6. 前进和后退
- forward() : 前进
- back() : 后退
- 案例v8

### 7. Cookies
- 对cookies进行操作，获取、添加、删除等
- 获取
    - get_cookies()
- 添加
    - add_cookie({k1:v1,k2:v2..})
- 删除
    - delete_all_cookies()
- 案例v9

### 8. 选项卡管理
- 访问页面是会开启选项卡
- 开启 `browser.execute_script('window.open()')`
- 获取选项卡列表 `browser .window_handles `
- 切换 `browser.switch_to_window(browser.window_handles[1])`
- 案例v10

### 9. 异常处理
- 超时(TimeoutException)
- 节点未找到(NoSuchElementException)
- 解决：try ... except...[else....finally...]
`from selenium .common .exceptions import  TimeoutException,NoSuchElemetException`