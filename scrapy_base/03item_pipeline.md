# Item Pipeline
- 项目管道，Spider产生的Item会传递给Item Pipeline，组件被顺次调用完成一连串处理过程
- 主要功能
    - 清理HTML数据
    - 验证爬取数据，检查爬取字段
    - 查重并丢弃重复内容
    - 将爬取结果保存到数据库

- **核心方法**
    - 必须实现的
        - **process_item(item,spider)**
            - 被定义的Item Pipeline会默认调用这个方法对Item进行处理
            - 参数
                - item，是Item对象，即被处理的Item
                - spider，是Spider对象，即生成Item的Spider
            - 返回
                - 必须返回Item类型的值或者抛出一个DropItem异常
                - Item/DropItem
    - 比较实用的
        - open_spider(spider)
            - Spider开启时被自动调用的，可以做一些初始化工作，如开启数据库的连接
            - 参数
                - spider，被开启的Spider对象
            - 返回  
                - 一般无返回（None）
        - close_spider(spider)
            - Spider关闭时自动调用，做一些收尾工作，如关闭数据库连接
        - from_crawler(cls,crawler)
            - 类方法，用@classmethod标识，是一种依赖注入的方式
            - 参数
                - crawler，通过crawler对象可以拿到Scrapy的所有核心组件，如全局配置的每个信息
                - 参数cls，就是Class，最后返回一个Class实例
            - 返回
                - 返回一个Class实例

- **Image Pipeline**
    - scrapy提供一个专门处理下载的pipeline，包括文件下载和图片下载（下载到本地）
    - 下载文件和图片的原理与抓取页面的原理一样，因此下载过程支持异步和多线程，下载十分高效
    - 首先定义存储文件的路径，在settings.py中添加`IMAGES_STORE='./images`
    - 内置的ImagePipeline会默认读取Item的image_urls字段，并认为该字段是个列表形式，它会遍历Item的image_urls字段，然后读取每个url进行图片下载
    - 若现在生成Item的图片连接并不是image_urls字段表示，也不是列表形式，只是单个url，要重新定义下载的部分逻辑，即自定义ImagePipeline(继承内置ImagesPipeline)
    - 自定义ImagePipeline，重写方法
        - file_path(request,response=None,info=None)
            - 参数
                - request : 下载对应的Request对象
            - 返回
                - 保存的文件名（每个连接）
        - item_completed(results,item,info)
            - 单个Item完成下载时的处理方法（不是所有的图片都会下载成功）
            - 参数
                - results : Item对应的下载结果，列表形式，列表的每个元素是一个元组，其中包含了下载成功或失败的信息
                    > success 是一个布尔值，当图片成功下载时为 True ，因为某个原因下载失败为``False``
                    > image_info_or_error 是一个包含下列关键字的字典（如果成功为 True ）或者出问题时为 Twisted Failure 。
                        - url - 图片下载的url。这是从 get_media_requests() 方法返回请求的url。
                        - path - 图片存储的路径（类似 IMAGES_STORE）
                        - checksum - 图片内容的 MD5 hash
                        
                        ```
                        [(True,
                        {'checksum': '2b00042f7481c7b056c4b410d28f33cf',
                        'path': 'full/7d97e98f8af710c7e7fe703abc8f639e0ee507c4.jpg',
                        'url': 'http://www.example.com/images/product1.jpg'}),
                        (True,
                        {'checksum': 'b9628c4ab9b595f72f280b90c4fd093d',
                        'path': 'full/1ca5879492b8fd606df1964ea3c1e2f4520f076f.jpg',
                        'url': 'http://www.example.com/images/product2.jpg'}),
                        (False,
                        Failure(...))]
                        ```
            - 返回
                - 返回有效的Item
        - get_media_request(item,info)
            - 参数
                - item : 爬取生成的Item对象
            - 返回
                - 可迭代的Request对象，Request加入调度队列，等待调度执行下载
        
        - 
        ```cython
        import scrapy
        from scrapy.contrib.pipeline.images import ImagesPipeline
        from scrapy.exceptions import DropItem

        class MyImagesPipeline(ImagesPipeline):
  

          def get_media_requests(self, item, info):
              for image_url in item['image_urls']:
                  yield scrapy.Request(image_url)

          def item_completed(self, results, item, info):
              image_paths = [x['path'] for ok, x in results if ok]
              if not image_paths:
                  raise DropItem("Item contains no images")
              item['image_paths'] = image_paths
              return item
        ```
- 常见案例
    - MongoPipeline
    - MysqlPipeline
    - ImagesPipeline
    