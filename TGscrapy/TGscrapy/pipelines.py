# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from TGscrapy.items import TgscrapyItem
class TgscrapyPipeline(object):
    def process_item(self, item, spider):
       # 连接数据库
       my_sql = pymysql.connect(host='localhost',port=3306,user='root',password='123456',charset='utf8',db='tgou_sql',use_unicode=True)
       #获取游标
       cur = my_sql.cursor()
       try:
           #插入信息到 tugou_sql
           if isinstance(item,TgscrapyItem):
               cur.execute("insert into tgshoppings(shopping_name,shopping_jiage,shopping_info,shopping_classify,shopping_sv,shopping_photo) VALUE (%s,%s,%s,%s,%s,%s)",(item['shopping_name'],item['shopping_jiage'],item['shopping_info'],item['shopping_classify'],item['shopping_sv'],item['shopping_photo']))
               #提交
               my_sql.commit()
               #关闭游标
               cur.close()
               #关闭数据库连接
               my_sql.close()
       except Exception as e:

           my_sql.commit()
           cur.close()
           my_sql.close()
           print('出现异常',e)
       finally:
           return item
