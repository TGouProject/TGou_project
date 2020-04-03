# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TgscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    shopping_type = scrapy.Field()#商品的种类
    shopping_name = scrapy.Field()#商品的名字
    shopping_price = scrapy.Field()#商品的价格
    shopping_info = scrapy.Field()#商品的详情
    shopping_sv = scrapy.Field()#商品的销量
    shopping_photo = scrapy.Field()#商品的样式
