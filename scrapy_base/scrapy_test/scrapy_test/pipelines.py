# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql
import pymongo
from logging import getLogger
from scrapy import Request
from scrapy .exceptions import DropItem
from scrapy .pipelines .images import  ImagesPipeline


class MongoPipeline(object):
    '''储存到mongodb'''
    def __init__(self, mongo_uri, mongo_db):
        # 初始化配置信息
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.logger = getLogger(__name__ )

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        #数据库连接
        self.client = pymongo .MongoClient (self.mongo_uri )
        self.db = self.client [self.mongo_db ]

    def process_item(self,item,spider):
        # self.logger .debug(item)
        self.logger .debug(type(item))#item是ImagesItem对象，要转为字典格式
        if self.db[item .collection] .update({'id':dict(item)['id'],'url':dict(item) ['url']},{'$set':dict(item)},True ) :
            self.logger .debug('save to mongo: ',dict(item)['url'])
            return item

    def close_spider(self,spider):
        self.client .close()


class MysqlPipeline():
    '''储存到Mysql'''
    def __init__(self,host,database,user,password,port):
        '''初始化配置'''
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            host= crawler .settings .get('MYSQL_HOST'),
            database= crawler .settings .get ('MYSQL_DATABASE'),
            user= crawler .settings .get ('MYSQL_USER'),
            password= crawler .settings .get ('MYSQL_PASSWORD'),
            port= crawler .settings .get ('MYSQL_PORT')

        )
    def open_spider(self,spider):
        #数据库连接
        self.db = pymysql .connect (self.host ,self.user ,self.password ,self.database ,charset ='utf8',port=self.port )
        self.cursor = self.db.cursor()

    def process_item(self,item,spider):
        data = dict(item)
        keys = ', '.join(data.keys())
        values = ', '.join(['%s']*len(data))
        #mysql语句
        sql = 'insert into %s (%s) VALUES (%s)'%(item.table,keys,values)
        self.cursor .execute(sql,tuple (data.values() ))
        self.db.commit()
        return item

    def close_spider(self,spider):
        self.db.close()

class ImagePipeline(ImagesPipeline ):
    def file_path(self,request,response=None ,info=None ):
        url = request .url
        file_name = url.split('/')[-1]
        return file_name

    def item_completed(self,results,item,info):
        image_paths = [x['path'] for ok,x in results if ok]#遍历成功的下载列表
        if not image_paths :
            raise DropItem('Images Downloaded Failed.')
        return item

    def get_media_requests(self,item,info):
        yield Request (item ['url'])