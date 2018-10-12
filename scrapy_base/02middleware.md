# Middleware
- Downloader Middleware
- Spider Middleware

## 1. Downloader Middleware的用法
- 下载器中间件是介于Scrapy的request/response处理的钩子框架。 是用于全局修改Scrapy request和response的一个轻量、底层的系统。
- 作用的位置
    - 在scheduler调度出队列的Request发送给Downloader下载之前，在Request执行下载之前对其进行修改
        - 修改Request的User-Agent、处理重定向、设置代理、失败重试、设置Cookies...
    - 在下载后生成的Request发送给Spider之前，生成的Request被Spider解析之前对其进行修改
        - 修改Response的状态码。。。
- 激活下载中间件
    - 要激活下载器中间件组件，将其加入到 DOWNLOADER_MIDDLEWARES 设置中。 该设置是一个字典(dict)，键为中间件类的路径，值为其中间件的顺序(order)
    - DOWNLOADER_MIDDLEWARES设置会与Scrapy定义的 DOWNLOADER_MIDDLEWARES_BASE 设置合并(但不是覆盖)， 而后根据顺序(order)进行排序，最后得到启用中间件的有序列表: 第一个中间件是最靠近引擎的，最后一个中间件是最靠近下载器的。
    - 如果您想禁止内置的(在 DOWNLOADER_MIDDLEWARES_BASE 中设置并默认启用的)中间件， 您必须在项目的 DOWNLOADER_MIDDLEWARES 设置中定义该中间件，并将其值赋为 None 
    ```
    DOWNLOADER_MIDDLEWARES = {
    'myproject.middlewares.CustomDownloaderMiddleware': 543,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    }
    ```
    
- **编写自己的下载中间件**
    - 每个Downloader Middleware都定义一个或多个方法的类，核心方法三个
        - process_request(request,spider)
            - 参数	
                - request (Request 对象) – 处理的request
                - spider (Spider 对象) – 该request对应的spider
            - 返回
                - process_request() 必须返回其中之一: 返回 None 、返回一个 Response 对象、返回一个 Request 对象或raise IgnoreRequest 。
        - process_response(request,response,spider)
            - 参数	
                - request (Request 对象) – response所对应的request
                - response (Response 对象) – 被处理的response
                - spider (Spider 对象) – response所对应的spider
            - 返回
                - process_request() 必须返回以下之一: 返回一个 Response 对象、 返回一个 Request 对象或raise一个 IgnoreRequest 异常。
        - process_exception(request,exception,spider)
            - 参数	
                - request (是 Request 对象) – 产生异常的request
                - exception (Exception 对象) – 抛出的异常
                - spider (Spider 对象) – request对应的spider
            - 返回
                - process_exception() 应该返回以下之一: 返回 None 、 一个 Response 对象、或者一个 Request 对象。
    - 项目实战httpbin.py
        - **修改Request请求的User-Agent**
            - 修改settings.py中USER_AGENT变量
            - 定义Downloader Middleware的process_request()来修改 
                - 在middlewares.py文件中添加一个RandomUserAgentMiddleware的类
            - 修改cookies类似，request.headers['cookies']=''
        - **使用代理**
            - 使用request.meta['proxy']
            ```
                class RandomProxy(object):
                    def process_request(self, request, spider):
                        proxy = random.choice(PROXIES)
                        if proxy['user_passwd'] is None:
                            #  没有代理账户验证的代理使用方式
                            request.meta['proxy'] = "http://" + proxy['ip_port']
                        else:
                            #  对账户密码进行 base64 编码转换
                            base64_userpasswd = base64.b64encode(proxy['user_passwd'])
                            #  对应到代理服务器的信令格式里
                            request.headers['Proxy-Authorization'] = 'Basic ' + base64_userpasswd
                            request.meta['proxy'] = "http://" + proxy['ip_port']     
            ```
            - setting中的相关配置
                    
                    
                    PROXIES = [
                        {'ip_port': '111.8.60.9:8123', 'user_passwd': 'user1:pass1'},
                        {'ip_port': '101.71.27.120:80', 'user_passwd': 'user2:pass2'},
                        {'ip_port': '122.96.59.104:80', 'user_passwd': 'user3:pass3'},
                        {'ip_port': '122.224.249.122:8088', 'user_passwd': 'user4:pass4'},
                        ]



## 2. Spider Middleware
- 介于Engine和Spider的钩子框架
    - 当Downloader生成Response之后，Response会经过Spider Middleware被发送给Spider
    - 当Spider生成Item和Request之后，Item、Request会经Spider Middleware处理发送给Item Pipeline或Scheduler
- 三个作用
    - 当Downloader生成Response之后，发送给Spider之前对Response处理
    - 当Spider生成Item和Request之后，Request在发送给Scheduler之前，对Request处理
    - 当Spider生成Item和Request之后，Item发送给Item Pipeline之前对Item处理
- 定义/激活Spider Middleware
    - 与Downloader Middleware类似
    - 核心方法
        - process_spider_input(response,spider)
            - 参数
                - response (Response 对象) – 被处理的response
                - spider (Spider 对象) – response所对应的spider
            - 返回
                - 返回None或抛出一个异常
        - process_spider_output(response,result,spider)
            - 参数
                - response (Response 对象) – 被处理的response
                - result (包含Request或Item对象的可迭代对象) - Spider的返回结果
                - spider (Spider 对象) – response所对应的spider
            - 返回
                - 包含Request或Item对象的可迭代对象
        - process_spider_exception(response,exception,spider)
            - 参数
                - response (Response 对象) – 被处理的response
                - exception (Exception对象) - 抛出的异常
                - spider (Spider 对象) – response所对应的spider
            - 返回
                - None或包含Request或Item对象的可迭代对象
        - process_start_requests(start_requests,spider)
            - 参数
                - start_requests (包含Request的可迭代对象) - Start Requests
                - spider (Spider对象) - Start Requests所属Spider
            - 返回
                - 包含Request对象的可迭代对象
            
    