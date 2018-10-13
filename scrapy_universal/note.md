# Scrapy 通用爬虫
- 多个spider可能包含很多重复代码，将个站点的spider的公共部分保留下来，不同部分提取出来作为单独的配置，比如提取规则、页面解析方式等抽离出来做成一个配置文件，那么在新增一个爬虫的时候，只需要实现这些网站的爬取规则和提取规则即可
- 通用爬虫的实现方法
    - CrawlSpider
    - Item Loader
    
### CrawlSpider
- CrawlSpider是Scrapy提供的一个通用Spider。在Spider里，我们可以指定一些爬取规则来实现页面的提取，这些爬取规则由专门的数据结构Rule表示
- Rulr里包含提取和跟进页面的配置，Spider会根据Rule来确定当前页面中哪些链接需要爬取、哪些结果需要哪个方法解析
- CrawlSpider继承自Spider类，除了Spider类的所有方法和属性，还提供了一个非常重要的属性和方法
    - rules : 爬取规则的属性，包含一个或多个Rule对象的列表，每个Rule对爬取网站的动作做了定义，CrawlSpider会读取读取rules的每个Rule并进行解析
    - parse_start_url() : 可重写的方法，当start_urls里对应的Request得到Response时，该方法被调用，它会分析Response并必须返回Item对象或者Request对象
    
#### 爬取规则Rule的定义
- `class scrapy.contrib.spiders.Rule(link_extractor, callback=None, cb_kwargs=None, follow=None, process_links=None, process_request=None)`
    - link_extractor
        - 是LinkExtractor对象，通过它，spider知道从爬取的页面中提取哪些链接，提取的链接自动生成Request
        - `class scrapy.contrib.linkextractors.lxmlhtml.LxmlLinkExtractor(allow=(), deny=(), allow_domains=(), deny_domains=(), deny_extensions=None, restrict_xpaths=(), tags=('a', 'area'), attrs=('href', ), canonicalize=True, unique=True, process_value=None)`
            - allow : 正则表达式或正则表达式列表，定义了提取的页面中的链接哪些是符合的
            - deny : 与上相反
            - allow_domains : 允许的域名
            - deny_domians : 与上相反
            - restrict_xpaths : 定义了从当前页面中XPath匹配的区域提取链接，其值为XPath表达式
            - restrict_css : 定义了从当前页面中css匹配的区域提取链接，其值为css选择器表达式
    - callback 
        - 回调函数，从link_extractor中每获取到链接时将会调用该函数。该回调函数接受一个response作为其第一个参数， 并返回一个包含 Item 以及(或) Request 对象(或者这两者的子类)的列表(list)。
        - 当编写爬虫规则时，请避免使用 parse 作为回调函数。 由于 CrawlSpider 使用 parse 方法来实现其逻辑，如果 您覆盖了 parse 方法，crawl spider 将会运行失败。
    - cb_kwargs
        - 包含传递给回调函数的参数(keyword argument)的字典
    - follow
        - 是一个布尔(boolean)值，指定了根据该规则从response提取的链接是否需要跟进。 如果 callback 为None， follow 默认设置为 True ，否则默认为 False 。
    - process_links
        - 是一个callable或string(该spider中同名的函数将会被调用)。 从link_extractor中获取到链接列表时将会调用该函数。该方法主要用来过滤。
    - process_request
        - 是一个callable或string(该spider中同名的函数将会被调用)。 该规则提取到每个request时都会调用该函数。该函数必须返回一个request或者None。 (用来过滤request)
        
## Item Loader
- Rule 定义了爬取逻辑，没有对Item的提取方式做规则定义
- 对于Item的提取，借助Item Loader来实现
- Item提供的是保存爬取数据的容器，而Item Loader提供的填充容器的机制
- Item Loader的API : `class scrapy.loader.ItemLoader([item,selector,response,]**kwargs)`
    - item 
        - Item对象，可以调用add_xpath()、add_css()、add_value()等方法填充Item对象
    - selector
        - Selector对象，用于提取填充数据的选择器
    - response
        - Response对象，用于构造选择器的Response
    ```cython
    from scrapy.contrib.loader import ItemLoader
    from myproject.items import Product

    def parse(self, response):
        l = ItemLoader(item=Product(), response=response)#用Product Item和Response对象实例化ItemLoader
        l.add_xpath('name', '//div[@class="product_name"]')
        l.add_xpath('name', '//div[@class="product_title"]')
        l.add_xpath('price', '//p[@id="price"]')
        l.add_css('stock', 'p#stock]')
        l.add_value('last_updated', 'today') # you can also use literal values
        return l.load_item()
    ```
    - 当所有数据被收集起来之后, 调用 ItemLoader.load_item() 方法, 实际上填充并且返回了之前通过调用 add_xpath(), add_css(), and add_value() 所提取和收集到的数据的Item.
    > tem Loader在每个(Item)字段中都包含了一个输入处理器和一个输出处理器｡ 
    > 输入处理器收到数据时立刻提取数据 (通过 add_xpath(), add_css() 或者 add_value() 方法) 之后输入处理器的结果被收集起来并且保存在ItemLoader内. 
    > 收集到所有的数据后, 调用 ItemLoader.load_item() 方法来填充,并得到填充后的 Item 对象. 
    > 这是当输出处理器被和之前收集到的数据(和用输入处理器处理的)被调用.输出处理器的结果是被分配到Item的最终值｡

### 内置的Processor
- Identity
    - 不进行任何处理，直接返回原来的数据
- TakeFirst
    - 返回列表中第一个非空值，类似extract_first()功能，常用作Output Processor
    ```cython 
    from scrapy.loader.processors import TakeFirst
    processor = TakeFirst()
    print(processor(['',1,2,3]))
    
    out: 1
    ```
- Join
    - 相当于字符串中的join()方法，把列表合并为字符串，默认为空格连接，可以修改连接符
    ```cython
    from scrapy .loader .processors import  Join 
    processor = Join (',')
    print(processor (['hello','world']))
      
    out: 'hello,world' 
    ```
- Compose
    - 给定的多个函数的组合而构造的Processor，每个输入值被传递到第一个函数，其输出再传递到第二个函数，依次类推，直到最后一个函数返回整个处理器的输出
    ```cython
    from scrapy .loader .processors import  Compose 
    processor = Compose (str.upper,lambda s: s.strip())
    print(processor (' hello world'))
  
    out: 'HELLO WORLD' 
    ```
- MapCompose
    - 与Compose类似，MapCompose可以迭代处理一个列表输入值
    ```cython
    from scrapy .loader .processors import  Compose 
    processor = Compose (str.upper,lambda s: s.strip())
    print(processor ([' hello','world ',' python ']))
  
    out: ['HELLO', 'WORLD','PYTHON'] 
    ```

## 案例：中华网科技类新闻 (http://tech.china.com:8000/articles/)
- 新建项目
    - `scrapy startproject scrapy_universal`
- 创建CrawlSpider
    - 制定模板
    - 查看可用模板 ：`scrapy genspider -l`
    - 默认使用basic，这次创建使用CrawlSpider，用crawl
    - `scrapy genspider -t crawl china tech.china.com`
- 定义Rule
    ``
    rules = (
        Rule(LinkExtractor(allow='article\/.*\.html',restrict_xpaths= '//div[@id="left_side"]//div[@class="con_item"]'), callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(.,"下一页")]')),#提取下一页链接
    )
    ``
- 解析页面
    - 定义Item
    - 实现parse_item()方法
        - 原始Item
        - 实现Item Loader
            - 新建loader.py
                ```cython
                  from scrapy .loader import ItemLoader
                  from scrapy .loader .processors import  TakeFirst ,Compose ,Join


                  class NewsLoader(ItemLoader ):
                      default_output_processor = TakeFirst ()

                  class ChinaLoader(NewsLoader ):
                      text_out = Compose (Join (),lambda s:s.strip())
                      source_out = Compose (Join (),lambda s:s.strip ())
                ```
            - parse_item(response)
            ```
            loader = ChinaLoader (item= NewsItem (),response= response )

            loader.add_xpath('title','//h1[@id="chan_newsTitle"]/text()')
            loader .add_value('url',response .url)
            loader .add_xpath('text','//div[@id="chan_newsDetail"]//text()')
            loader .add_xpath('datetime','//div[@id="chan_newsInfo"]/text()',re='(\d+-\d+-\d+\s\d+:\d+:\d+)')
            loader .add_xpath('source','//div[@id="chan_newsInfo"]/text()',re='来源：(.*)')
            loader .add_value('website','中华网')

            yield loader .load_item()
            ```
- 通用配置抽取
    - 新建一个spider来实现此功能：`scrapu genspider -t crawl universal universal`
    - spider内属性抽离: 新建configs文件夹，在其下新建配置文件china.json
        - configs/china.json
            - spider : spider名称
            - 站点描述
                - website : 站点名称
                - type : 类型
                - index : 首页
            - settings : 该spider特有的settings配置
            - spider的属性
                - start_urls
                - allowed_domains
                - rules
    - Rule分离，rules定义为rules.py 
       ```
       from scrapy.linkextractors import LinkExtractor
        from scrapy.spiders import CrawlSpider, Rule

        rules = {

            'china':(
                Rule(LinkExtractor(allow='article\/.*\.html',restrict_xpaths= '//div[@id="left_side"]//div[@class="con_item"]'), callback='parse_item'),
                Rule(LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(.,"下一页")]')),
            )
        }
        ```
    - 新建utils.py，定义读取JSON配置文件的方法
    - 根目录下，定义入口文件run.py，用于启动spider
    - 对universal中，新建__init__()方法，初始化配置
    - 启动爬虫 `python run.py china` 检查是否请求成功
    - 配置解析部分，Item、Item Loader
    - 再次启动spider
    
    - 综上，可配置的内容
        - spider : spider的名称
        - settings : 专门为spider定制的配置信息，覆盖项目级别的配置
        - start_urls :指定爬虫爬取的起始链接
        - allowed_domains : 允许爬取的站点
        - rules : 站点的爬取规则
        - item : 数据的提取规则
        
       