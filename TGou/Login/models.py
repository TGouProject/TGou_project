from django.db import models


class User(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=64, unique=True, primary_key=True)
    password = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)
    # 是否进行了邮件确认
    has_confirmed = models.BooleanField(default=False)
    # 收货地址
    shopping_address = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["c_time"]
        verbose_name = "用户"
        verbose_name_plural = verbose_name


# 用于保存用户的确认码以及注册提交的时间
class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":   " + self.code

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = verbose_name


# 用于保存用户的订单
class AllOrders(models.Model):
    # 订单信息
    order_number = models.CharField(max_length=50,unique=True,default=None)
    # 商品名称
    order_info = models.CharField(max_length=200)
    # 商品数量
    Quantity_of_Goods = models.CharField(max_length=10)
    # 订单金额
    order_money = models.CharField(max_length=100)
    # 订单日期
    order_data = models.DateField(auto_now=True)
    # 交易状态
    order_state = models.CharField(max_length=10)
    # 收货地址
    shipping_address = models.CharField(max_length=150, null=True, blank=True)
    # 外键
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.order_info
