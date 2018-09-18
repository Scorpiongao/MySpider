## pyspider框架
- 由国人binux编写的网络爬虫系统
- [官网](https://docs.pyspider.org/)
- 爬虫框架
    - 关心爬虫的核心逻辑部分（页面信息的提取、下一步请求的生成）
    - 开发效率高

### 基本功能
1. python 脚本控制，可以用任何你喜欢的html解析包（内置 pyquery）
2. WEB 界面（WebUI系统）编写调试脚本，起停脚本，监控执行状态，查看活动历史，获取结果产出
3. 支持 MySQL, MongoDB, SQLite
4. 对接PhantomJS，支持抓取 JavaScript 的页面
5. 组件可替换，支持单机/分布式部署，支持 Docker 部署
6. 提供优先级控制、失败重试、定时抓取等

### pyspider与scrapy的比较
- pyspider 提供了WebUI，爬虫的编写、调试都在WebUI中进行；scrapy则采用代码和命令行操作（需对接Portia实现可视化）
- pyspider 调试非常方便，WebUI操作便捷直观；scrapy 则使用 parse命令调试，没有 pyspider方便
- pyspider 支持PhantomJS来进行JavaScript渲染页面的采集；scrapy 可以对接 scrapy-splash组件（额外配置）
- pyspider 内置pyquery为选择器；scrapy 对接 Re,XPath,CSS选择器
- pyspider 的可扩展性不强，可配置化程度不高；scrapy 对接 Middleware、Pipeline、Extension等组件实现非常强大的功能，模块之间的耦合程度低，可扩展性强

- 使用原则
    - pyspider : 快速抓取一个页面
    - scrapy : 应对反爬程度高、超大规模的抓取

### pyspider 架构
- [架构图](http://s5.sinaimg.cn/mw690/003ubO2Szy7cBYbRHxi84&690)
- Scheduler (调度器) ：发起任务调度
- Fetcher (抓取器) ：负责抓取网页内容
- Processer (处理器) ：负责解析网页内容
- 整个爬取过程受到 Monitor & WebUI(监控器)的监控
- 结果被 Result Worker (结果处理器)处理

- 具体过程
    - 一个项目对应一个脚本，一个Handler类，on_start()生成最初的爬取任务 --> Scheduler
    - Scheduler --> Fetcher 抓取 --> 响应(Response) --> Processer
    - Processer --> 新URL 和 Result --> Scheduler (Result Worker)
    - Scheduler --> 新任务（判断是否为新或重试）--> Fetcher
    - 重复上述工作直至完毕
    - 抓取结束后，回调on_finish(),可以定义后处理过程

### pyspider 用法详解
- 命令行启动
    - `pyspider all`
        - '127.0.0.1:5000'
    - pyspider [OPTIONS] COMMAND [ARGS]
        - pyspider -c pyspider.json webui
    - pyspider scheduler [OPTIONS]
    - pyspider fetcher [OPTIONS] 
    - pyspider processor [OPTIONS]
    - pyspider webui [OPTIONS]
        - pyspider webui --port 5001

- **crawl**(url,callback=self.callback,**kwargs)方法
    - url : 可以为单个url，也可以为url列表
    - callback : 指定该URL对应的响应内容由哪个方法来解析，该方法的第一个参数为response
    - age : 任务的有效时间 age = 10*24*60*60(默认十天)
    - priority : 爬取任务的优先级，默认为0，数值越大，优先级越高
    - exetime : 设置定时任务，其值为时间戳，默认0 exetime = time.time()+30*60
    - retries : 重试次数，默认为3
    - method : 请求方法，默认GET
    - params : GET请求参数
    - data : POST表单数据, method = 'POST',data={k1:v1,k2:v2}
    - headers : 请求头部信息
    - proxy : 代理IP
    - cookies : 爬取使用的Cookies,字典格式
    - connect_timeout : 初始化连接最长等待时间，默认20
    - timeout : 抓取网页时最长等待时间，默认120
    - allow_redirects : 默认True
    - validate_cert : 是否验证HTTPS证书，默认True（Error 599 --> validate_cert = False）
    - fetch_type : 开启PhantomJS渲染 fetch_type = 'js'

- 任务区分
    - pyspider 判断两个任务是否重复使用该任务的URL的MD5值作为唯一ID，如果ID相同，那么两个任务就判定为相同，其中一个就不会爬取
    - 有时请求链接可能为同一个，但是POST的data参数不同，于是重写get_taskid()，改变ID的计算方法
    - 案例v1

- 全局配置
    - crawl_config = {}指定全局变量，配置中的参数与crawl()方法创建任务时的参数合并
    - 案例v1

- 定时爬取
    - every属性来设置爬取的时间间隔 every(minutes=24*60)
    - 在有效时间内爬取不会重复，所以要把有效时间age设置小于定时时间every

- 项目状态
    - TODO
        - 项目刚被创建还未实现时的状态
    - STOP
        - 停止项目抓取
    - CHECKING
        - 正在运行的项目修改时会变成CHECKING状态，出错调整时也会出现这种情况
    - DEBUG
        - 运行项目
    - RUNNING
        - 运行
    - PAUSE
        - 暂停，爬取过程中出现连续多次错误，项目自动设置为PAUSE状态，并等待一定时间后继续爬取

- 爬去进度
    - 5m : 5分钟内的请求情况
    - 1h : 1小时。。。
    - 1d : 1天。。。
    - all : 所有的请求情况
    - 蓝色 : 等待被执行的任务
    - 绿色 : 成功的任务
    - 黄色 : 请求失败后等待重试的任务
    - 红色 : 失败次数过多而被忽略的请求任务

- 删除项目
    - pyspider中没有直接删除项目的选项，如果要删除任务，将状态设置为STOP，分组名设置为delete，24小时后自动删除
- 爬取项目
    - 127.0.0.1:5000