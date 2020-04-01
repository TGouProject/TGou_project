from django.contrib import admin
from TGous.models import TGou_Order
import time
# 注册模型
@admin.register(TGou_Order)
class AuthorizationUserAdmin(admin.ModelAdmin):
    exclude = ['ordedr_number']  # 屏蔽那些信息
    def save_model(self, request, obj, form, change):
        orderdata = str(obj.order_data)
        res = time.time()
        res =str(res)
        ordedr_number = orderdata+res[:10]
        obj.ordedr_number = ordedr_number
        super().save_model(request,obj,form,change)


