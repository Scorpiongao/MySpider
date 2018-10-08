# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from urllib.parse import  urlencode
import json
from ..items import  ImagesItem

class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com/']

    def start_requests(self):
        '''构造初始请求'''
        data = {
            'ch': 'photography',#指摄影类别
            'listtype':'new',#排序方式
            'temp':'1',
        }
        base_url = 'http://image.so.com/zj?'
        for page in range(1,self.settings .get('MAX_PAGE')+1):
            data['sn'] = page*30 #偏移量
            params = urlencode(data)#urlencode()将字典格式参数构造成完整GET请求url连接
            url = base_url +params
            yield Request(url,self.parse)

    def parse(self, response):
        #json数据转为python对象
        result = json.loads(response.text)
        if result.get('list'):
            for image in result .get('list'):
                item = ImagesItem ()
                item['id'] = image ['imageid']
                item['url'] = image ['qhimg_url']
                item ['title'] = image ['group_title']
                item ['thumb'] = image ['qhimg_thumb_url']
                item ['tag'] = image['tag']
                yield item

