# 初识Scrapy
[Scrapy文档](https://docs.scrapy.org/en/latest/topics/commands.html)




## 创建project



- 在命令行切换到存储位置

1.  scrapy startproject <projectname>
2.  cd project
3.  scrapy genspider <spidername>  +start_url(域名，不含http)生成spider类


## selector

-  response.css("path")


1.  css
2. xpath

- 在生成spider类中的parse方法中解析数据
example:
text=response.css(".text::text").extract_first()


1. .text表示class=text
2. ::text 表示提取文本内容
3. extract()返回的是个list,
4.  first则表示列表第一个元素
5.  extract()返回一个list
 **url=response.css(".tags .tag a::attr(href)").extract[0]** 
- 提取a中的href属性值


## 高级提取

###  Xpath 

1. response.xpath("//a[contains(@href,'image')]/@href").extract()
   a:标签    href:属性    image:属性值中包含image的    提取a标签中href属性值包含image的全部href

2. response.xpath("//a[contains(@href,'image')]/img/@src").extract()

3. response.xpath("//a[contains(.,'评论[')]//@href").extract_first()
".":代表文本
提取文本内容中包含"评论"字段的href属性

4. response.xpath("//a[contains(.,'评论[')]//text()").re_first("转发\[(.*?)]\")

### CSS
1. response.css("//a[href*='image']:attr(href)").extract()

2. response.css("//a[href*='image'] img:attr(src)").extract()

### 结合Re

1. response.css("a::text").re("name\:(.*)")
提取a标签中文本信息中name:后面的内容(list)

2. response.css("a::text").re_first("name\:(.*)")
提取a标签中文本信息中name:后面的内容的第一个




**命令行工具**
- **startproject**
> scrapy startproject <project name>
- **runspider**
> scrapy runspider <spider file.py>
- **shell**调试
> scrapy shell <url>
- **view**
> scrapy view <url>


**定义Item**
-  将非结构化的数据结构化
> url=scrapy.Field()
> text=scrapy.Field()
> title=scrapy.Field()
> …
再在spider的parse方法中声明item=Item()对象，item类似dict即可提取,yield生成器

```
for field in item.fields:
         if field in result.get(fields)
             item[field]=result[field]

```


#### eval
```
for field in item.fields:
    item[field]=eval(field)
```


- **翻页功能**
- - 获取下一页next,(response.urljoin(next))然后回调函数自己
>  yield scrapy.Request(url=next,callback=self.parse)

- **数据保存格式**
- scrapy crawl <spider name> -o filename.csv[json…]
-  **Item Pipeline**
-   如果要改变数据格式或存储方式，要激活Item Pipeline
-   定义的每个类方法中必须含process_item(self,item,spider)
-   在settings中配置激活Pipeline类方法


> **MONGODB去重update**
> > 
>     import pymongo
>     client=pymongo.MONGODBClient()
>     db=client[db_name]
>     db.update({'url_token':result["url_token"]},{"$set":result},True)
