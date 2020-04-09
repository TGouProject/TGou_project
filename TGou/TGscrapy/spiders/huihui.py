# -*- coding: utf-8 -*-
import scrapy
import random
from TGscrapy.items import TgscrapyItem

url = 'http://www.huihui.cn'


class TiangouSpider(scrapy.Spider):
    name = 'tiangou'
    allowed_domains = ['huihui.cn']
    start_urls = ['http://www.huihui.cn']

    def parse(self, response):
        # 商品种类url
        shopping_url = response.xpath("//div[@class='list-inner clearfix']/a/@href").getall()[1:]
        for i in shopping_url:
            yield scrapy.Request(url=url + i, callback=self.two_parse)

    def two_parse(self, response):
        # print('6666666666666666666666666666666666')
        # 单个商品url
        one_shopping_url = response.xpath("//h3/a/@href").getall()
        for a in one_shopping_url:
            print('a------------------------------------------------------------------', a)
            yield scrapy.Request(url=url + a, callback=self.three_parser)

    def three_parser(self, response):
        item = TgscrapyItem()
        print('000000000000000000000000000000000000000000000000000', response.url)
        # 商品的种类
        shopping_classify = response.xpath("//a[@class='hico-doc hico-cagegory js-log']/text()").getall()[1].strip()
        item['shopping_type'] = shopping_classify
        # 商品的名字
        shopping_name = response.xpath('//h1/a/@title').getall()[0]
        item['shopping_name'] = shopping_name
        # 商品的价格
        shopping_jiage = response.xpath('//h4/text()').getall()[0]
        item['shopping_price'] = shopping_jiage
        # 商品的详情
        shopping_info = response.xpath("//p/text()").getall()[0]
        item['shopping_info'] = shopping_info
        # 商品的销量
        shopping_sv = random.randint(0, 99999)
        item['shopping_sv'] = shopping_sv
        # 商品的样式
        shopping_photo = response.xpath('//span/img/@src').getall()[0]
        item['shopping_photo'] = shopping_photo
        print({'shopping_type': shopping_classify,
               'shopping_name': shopping_name,
               'shopping_price': shopping_jiage,
               'shopping_info': shopping_info,
               'shopping_sv': shopping_sv,
               'shopping_photo': shopping_photo})

        yield item
