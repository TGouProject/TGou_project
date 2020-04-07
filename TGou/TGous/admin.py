from django.contrib import admin
from TGous.models import TGou_Order,Tgshoppings
import time
# 注册模型
admin.site.register(Tgshoppings)  #商品模型
@admin.register(TGou_Order)  #订单模型
class AuthorizationUserAdmin(admin.ModelAdmin):
    exclude = ['ordedr_number']  # 屏蔽那些信息
    def save_model(self, request, obj, form, change):
        res = time.time()
        res =str(res)
        ordedr_number =res[:10]
        obj.ordedr_number = ordedr_number
        super().save_model(request,obj,form,change)



