from django.db import models
import hashlib
class TGou_Order(models.Model):
    #订单号
    ordedr_number = models.CharField(max_length=200,default=None,unique=True)
    #订单信息,商品名称
    order_info =models.CharField(max_length=200)
    # 商品数量
    Quantity_of_Goods = models.CharField(max_length=10)
    # 订单金额
    order_money = models.CharField(max_length=100)
    #订单分类,已完成,未完成,退货订单....
    order_type = models.CharField(max_length=15)
    #订单日期
    order_data = models.DateField()
    #交易状态
    order_state = models.CharField(max_length=10)
    #收货地址
    shipping_address = models.CharField(max_length=150,default=None)

    def to_dict(self):
        return {
            'ordedr_number': self.ordedr_number,
            'order_info': self.order_info,
            'Quantity_of_Goods': self.Quantity_of_Goods,
            'order_money': self.order_money,
            'order_type': self.order_type,
            'order_data': self.order_data,
            'order_state': self.order_state
        }

    def __repr__(self):
        return str(self.to_dict())

    def __str__(self):
        order_number = self.ordedr_number
        return self.order_info+'\n'+order_number.replace('-','')

class Tgshoppings(models.Model):
    #商品名
    shopping_name = models.CharField(max_length=100)
    #价格
    shopping_price = models.CharField(max_length=45)
    #信息
    shopping_info = models.CharField(max_length=500)
    #种类
    shopping_type = models.CharField(max_length=45)
    #销量
    shopping_sv = models.CharField(max_length=100)
    #图片url
    shopping_photo = models.CharField(max_length=500)

    def __str__(self):
        return self.shopping_name




