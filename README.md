# 爬虫基础

## HTTP基本原理
- 详情见http.md
- http与https
    - http: Hyper Text Transfer Protocol
    - https: Hyter Text Transfer Protocol over Secure Socket Layer
    - https: 以安全为目的的HTTP通道，即http的安全版，在HTTP下加了SSL层，简称HTTPS
    - HTTPS的安全基础是SSL，因此通过它传输的内容都是经过SSL加密的，主要作用：
        - 建立一个信息安全通道来保证数据传输的安全
        - 确认网站的真实性，凡是使用了HTTPS的网站，都可以通过点击浏览器地址栏的锁头标志来查看网站认证之后的真实信息，也可以通过CA机构颁发的安全签章来查询
    
- http请求过程
    - ![模型图](https://images2017.cnblogs.com/blog/1122865/201711/1122865-20171109162243872-1491006257.png)

### 请求
1. 请求方法·Request Method
    - GET
    - POST
    - 区别
        - GET请求中的参数包含在URL里面，数据可以在URL中看到，而POST请求的URL不会包含这些数据，数据通过表单形式传输，会包含在请求体中
        - GET请求提交的数据最多只有1024字节，而POST没有限制
        - 一般来说，登录时需要提交用户名和密码，其中包含敏感的信息，用POST表单传输

2. 请求网址·Request URL
    - URL：统一资源定位符

3. 请求头·Request Headers
    - 常用头信息
    - Accept：请求报头域，用于指定客户端可接受哪些类型的信息
    - Accept-Language：指定客户端可接受语言类型
    - Host：用于指定请求资源的主机IP和端口号，其内容为请求的URL的原始服务器或网关的位置
    - Cookie(Cookies)：网站为了辨别用户进行会话跟踪而存储在用户本地的数据。主要功能是维持当前访问会话
    - Referer：表示请求是从哪个页面发过来的
    - User-Agent(UA)：是服务器识别客户使用的操作系统及版本，浏览器及版本信息（爬虫时可以伪装为浏览器）
    - Content-Type：互联网媒体类型（Internet Media Type）或MIME类型，用来表示具体请求中的媒体类型信息
        - text/html：HTML格式
        - image/gif：GIF图片
        - application/json：JSON类型
        - 对照表参考：http://tool.oschina.net/commons
        - 登录时，填写了用户名和密码信息，提交时这些内容会以表单的形式提交给服务器，此时需要注意Request Headers中指定Content-Type为application/x-www-form-urlencode
        - Content-Type和POST提交数据方式的关系  
            ```
            Content-Type                          提交数据的方式
            application/x-www-form-urlencode      表单数据
            multipart/form-data                   表单文件上传
            application/json                      序列化JSON数据
            text/xml                              XML数据  
            ```    
4. 请求体·Request Body
    - 请求体一般承载的内容是POST请求中的表单数据，对于GET请求，可能为空
    
    
### 响应
1. 相应状态码
    - http.md中有状态码说明
2. 响应头
    - 类似请求头
    - Set-Cookie：设置Cookies，下次请求带上Cookies请求
    - Content-Type
    - Server
    - Content-Encoding
3. 响应体
    - 网页的源代码或JSON数据

## 网页基础
- 网页组成
    - HTML：定义了网页的内容和结构
    - CSS：描述了网页的布局
    - JavaScript：定义网页的行为

-网页结构
    - 标签 + 内容

- 节点树
    - 节点
        - 父（parent）
        - 子（child）
        - 兄弟（sibling）

- 选择器
    - id：`#`
    - class：`.`
    - 标签选择器
    - 各选择器之间加空格分隔开来表示嵌套关系，不加空格表示并列关系
    
## 爬虫基本原理
> 我们可以把互联网比作一张大网，而爬虫便是网上爬行的蜘蛛
>
> 爬虫就是获取页面并提取和保存信息的自动化程序

- 参考资料
    - python3网络爬虫开发实战，崔庆才，人民邮电出版社
    - [Python3网络爬虫](http://blog.csdn.net/c406495762/article/details/72858983)
    - [Scrapy官方教程](http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html)

- 前提知识
    - url
    - http协议
    - web前端，html, css, js
    - ajax
    - re, xpath
    - xml

- 两大特征
    - 能按作者要求下载数据或者内容
    - 能自动在网络上流窜

- **三大步骤（ 请求 ---> 解析 ---> 存储 ）**
    1. **获取网页**
        - urllib
            - cookies
            - youdao
            - renren
        - request
            - session(v7)
    2. **提取正确的信息（解析）**
        - re
            - maoyan-top100
        - xpath
            - lianjia
        - Beautiful Soup
            - douban-top250
        - pyquery
            - zhihu-explore
    3. **保存数据**
        - 静态文件
            - txt
            - json
            - csv
        - 数据库
            - 关系型
                - MySQL
            - 非关系型
                - MongoDB
                - Redis
    
- **JavaScript渲染页面**
    - 使用基本的http请求得到的源代码可能跟浏览器中的页面源代码不太一样
    - 分析后台的Ajax接口，也可以使用Selenium、Splash来实现模拟JavaScript渲染
    - 抓包分析
        - ajax：XHR (x-requested-with: XMLHttpRequest)
        - 静态：DOC
    - Ajax
        - toutiao-jiepai
        - douyu
    - Selenium
        - taobao-meishi
        - douban-tushu

- 会话session和Cookies
    - 背景
        - 只有登录之后方可访问的页面
        - HTTP请求的无状态性
    - 保持HTTP连接状态
        - 会话(session)
            - 服务端，用来保存用户的会话信息
        - Cookie
            - 客户端（浏览器端）
            - 有了Cookies，浏览器在下次访问页面时自动附带上它发送给服务器，服务器通过识别Cookies并鉴定出哪个用户，判断出是否为登录状态，作出响应
            - key = value 键值对，value为Unicode字符，则为字符编码，若为二进制数据，需要使用BASE64编码
                - Domain : 可以访问该Cookie的域名
                - Max Age : 该Cookie失效的时间（秒）
                - Path : 该Cookie使用路径
                - Size : 此Cookie的大小
                - HTTP字段 : Cookie的httponly属性
                - Secure : 是否仅被使用安全协议传输，默认False
        - 会话维持
            - 当客户端第一次请求服务器时，服务器会返回一个请求头中带有Set-Cookies字段的响应给客户端，用来标记是哪个用户，客户端浏览器会把Cookies保存起来。
            下次请求时，浏览器会把此Cookies放在请求头一起提交给服务器，Cookies携带了会话ID信息，服务器检查Cookies即可找到对应的会话是什么，然后再判断会话来辨别用户状态
            - 有过期时间（Expires）
    - 应用
        - 模拟登陆时，session保持登录状态
        - **Login_Simulation** 
            - douban
            - zhihu   
### 代理(proxy server)
- 代理服务器
    - 网络信息的中转站，可以隐藏真实IP，防止被封号
    - ![代理服务图](https://images2015.cnblogs.com/blog/820365/201610/820365-20161013111614531-49092943.png)
    - ![代理服务流程图](https://images2015.cnblogs.com/blog/820365/201610/820365-20161013111623375-1106775830.png)

- 优点
    - 突破自身IP访问限制，访问国外站点。教育网、过去的169网等
    - 网络用户可以通过代理访问国外网站
    - 访问一些单位或团体内部资源，如某大学FTP（前提是该代理地址在该资源 的允许访问范围之内），使用教育网内地址段免费代理服务器，就可以用于对教育网开放的各类FTP下载上传，以及各类资料查询共享等服务
    - 突破中国电信的IP封锁：中国电信用户有很多网站是被限制访问的，这种限制是人为的，不同Serve对地址的封锁是不同的。所以不能访问时可以换一个国外的代理服务器试试
    - 提高访问速度：通常代理服务器都设置一个较大的硬盘缓冲区，当有外界的信息通过时，同时也将其保存到缓冲区中，当其他用户再访问相同的信息时， 则直接由缓冲区中取出信息，传给用户，以提高访问速度
    - 隐藏真实IP：上网者也可以通过这种方法隐藏自己的IP，免受攻击

- 代理池
    - proxypool

### 爬虫框架
- Pyspider
    - 可以快速编写爬虫，但可配置化程度不高，异常处理能力有限
    - 详见pyspider
- Scrapy
    - 基于Twisted的异步处理框架，功能强大，爬取效率高，相关扩展件多，可配置和可扩展程度非常高，几乎可以应对所有的反爬虫网站
    - 各大组件
        - Scrapy Engine
        - Scheduler
        - Downloader
        - Spider
        - Item Pipeline
            - **process_item(item,spider)**
            - open_spider(spider)
            - close_spider(spider)
            - from_crawler(cls,crawler)
        - Middleware
            - Downloader Middleware
                - process_request(request,spider)
                - process_response(request,response,spider)
                - process_exception(request,exception,spider)
            - Spider Middleware
    - 详见scrapy_base

### 反爬虫与反反爬虫之战
- 应对网络的反爬虫措施，一般做以下反反爬虫策略
    - 降低爬取速度 
        - time.sleep(3)
    - 伪装请求头
        - headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
    - session会话维持
        - 使用cookies
    - 更换代理
        - 使用代理IP (proxy pool)
    - 模拟登录
        - 读懂Js加密，模拟构造出请求的参数
    - 使用selenium
        - 模拟人的操作去访问服务器
    - 转为app端抓取
        - charles + mitmproxy + appium
