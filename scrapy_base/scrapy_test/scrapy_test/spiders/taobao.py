# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request,FormRequest
from logging import getLogger
from urllib .parse import  quote
import re
from ..items import  ProductItem


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['www.taobao.com']
    # start_urls = ['http://www.taobao.com/']
    login_url = 'https://login.taobao.com/member/login.jhtml'
    base_url = 'https://s.taobao.com/search?q='

    def start_requests(self):
        #post请求，formdata中的参数获得：找到form 中的name属性值
        # yield FormRequest (url= self.login_url,formdata= {'TPL_username':'15927099527','TPL_password':'mlf1456586096'},callback= self.logined_search)
        # yield Request(url='https://s.taobao.com/search?q=ipad' , callback=self.parse, dont_filter=True)#dont_filter=True不去重

    # def logined_search(self,response):
        for keyword in self.settings .get('KEYWORDS'):
            for page in range(1,self.settings .get('MAX_PAGE')+1):
                url = self.base_url + quote(keyword)
                yield Request (url= url,callback= self.parse,meta={'page':page},dont_filter= True )

    def parse(self, response):
       products = response .xpath('//div[@id="mainsrp-itemlist"]//div[@class="items"][1]//div[contains(@class,"item")]')
       for product in products :
           item = ProductItem ()
           item['price'] = ''.join(product .xpath('.//div[contains(@class,"price")]//text()').extract()).strip()
           item['title'] = ''.join(product .xpath('.//div[contains(@class,"title")]//text()').extract()).strip()
           item['shop'] = ''.join(product.xpath('.//div[contains(@class,"shop")]//text()').extract()).strip()
           item['image'] = ''.join(product.xpath('.//div[@class="pic"]//img[contains(@class,"img")]/@data-src').extract()).strip()
           item['deal'] = ''.join(product.xpath('.//div[contains(@class,"deal-cnt")]//text()').extract()).strip()
           item['location'] = ''.join(product.xpath('.//div[@class="location"]//text()').extract()).strip()
           item['url'] = ''.join(product.xpath('.//div[@class="pic"]/a[contains(@class,"pic-link")]/@href').extract()).strip()
           # print(item )
           yield item
