# -*- coding: utf-8 -*-
import scrapy
from    quotes .  items import QuotesItem


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
       quotes=response.css('div.quote')
       for quote in quotes :
           item=QuotesItem ()#生成数据结构对象
           text=quote .css('.text::text').extract_first()
           author=quote .css('.author::text').extract_first()
           tags=quote .css ('.tags .tag::text').extract()
           item ['text']=text
           item['author'] = author
           item['tags'] = tags
           yield item
        #下一页url
       next=response .css(".pager .next a::attr(href)").extract_first()

       url=response .urljoin(next )
       yield scrapy .Request (url= url ,callback= self.parse)#回调

