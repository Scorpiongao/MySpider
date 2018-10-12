# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field ,Item


class ImagesItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #images的Item
    # collection，table分别为MongoDB、MySQL的集合与表
    collection = table = "images"
    id = Field ()
    url = Field ()
    title = Field ()
    tag = Field ()
    thumb = Field ()

class ProductItem(Item ):
    #taobao的Item
    collection = 'products'
    image = Field ()
    price = Field ()
    deal = Field ()
    title = Field ()
    url = Field ()
    shop = Field ()
    location = Field ()