# Scrapy对接Selenium
- scrapy抓取页面的方式和request库类似，都是直接模拟HTTP请求，而scrapy也不能抓取JavaScript动态渲染的页面
- 抓取动态页面的两种方式
    - 分析Ajax请求，找到其对应的接口抓取
    - 直接用selenium/splash模拟浏览器进行抓取
    
## selenium抓取淘宝商品
- 新建项目
    - `scrapy startproject <project name>`
    - cd <project name>
    - `scrapy genspider taobao www.taobao.com`
    - 修改`ROBOTSTXT_OBEY = False`
- 定义Item
    
        class ProductItem(Item ):
        #taobao的Item
        collection = 'products'
        image = Field ()
        price = Field ()
        deal = Field ()
        title = Field ()
        url = Field ()
        shop = Field ()
        location = Field ()
- spider
    - 实现start_requests()方法
        - 关键字quote(key)拼接Url
        - 构造生成Request
        - 每次搜索的url相同，分页码数用meta = {'page':page}传递
            - 获得meta参数 `page = request.meta.get('page')`
        - 设置dont_filter = True(不去重)
- 对接selenium
    - 在Downloader Middleware中实现process_request(request,spider)方法对每个请求进行处理
    - __init__(): 初始化对象
    - 启动浏览器进行页面的渲染，结果返回给HtmlRequest(url=request.url,body=html,request=request,encoding="utf-8",status=200)对象，其为Response类的子类
    - 其返回的Response对象直接传给Spider进行解析    
- 解析页面
    - spider中解析response
- 存储结果
    - 存储到mongodb数据库，编写MongoPipeline
- 运行
    - 激活SeleniumMiddleware、MongoPipeline