# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field ,Item


class ImagesItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #collection，table分别为MongoDB、MySQL的集合与表
    collection = table = "images"
    id = Field ()
    url = Field ()
    title = Field ()
    tag = Field ()
    thumb = Field ()