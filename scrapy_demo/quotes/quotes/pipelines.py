# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy .exceptions import  DropItem
import pymongo

class  TextPipeline(object):    #item 处理
    def __init__(self):
        self.limit=50

    def process_item(self, item, spider):
        if item ['text']:
            if len(item['text'])>self.limit :
                item ['text']=item ['text'][0:self.limit].rstrip()+'...'
                return item
        else:
            return DropItem ('Missing Text!')

class MongoPipeline():       #item存储处理，保存到数据库
    def __init__(self,mongo_uri,mongo_db):    #全局变量
        self.mongo_uri=mongo_uri
        self.mongo_db = mongo_db

    @classmethod#类方法
    def from_crawler(cls,crawler):#从settinngs中获取配置信息
        return cls(
            mongo_uri= crawler .settings.get('MONGO_URI'),
            mongo_db=crawler .settings.get ('MONGO_DB')
        )

    # 启动mongodb
    def open_spider(self,spider):
        self.client=pymongo .MongoClient (self.mongo_uri )
        self.db=self.client [self.mongo_db ]
    #保存到mongodb
    def process_item(self,item,spider):
        name=item.__class__.__name__#与item类的名相同
        self.db [name].insert(dict(item))
        return item

    def close_spider(self,spider):
        self.client .close()

