from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse, FileResponse, HttpRequest
from TGou import settings
from TGous.models import TGou_Order, Tgshoppings
from Login.models import User


def home_page(request):
    return render(request, 'TGou_page/index.html')


# 消息界面
def message(request):
    return HttpResponse("消息界面")


# 我的TGou
def mytgou(request):
    # username = request.session.get('user_name')
    sss = '2020-03-311585625311'
    order_number = TGou_Order.objects.get(ordedr_number=sss)
    shopping_info = Tgshoppings.objects.get(shopping_price='$1209.99')
    overmonney = int(order_number.Quantity_of_Goods[0])* shopping_info.shopping_price[2]
    return render(request, "Order_page/orderpage.html",
                  {'order_number': order_number.ordedr_number, 'shopinfo': shopping_info.shopping_info,
                   'monney':shopping_info.shopping_price,'shopnum':order_number.Quantity_of_Goods,'shopname':shopping_info.shopping_name,'overmonney':overmonney})


# 购物车
def shopping_car(request):
    return render(request, "TGou_page/shopping_car.html")


# 收藏夹
def favorite(request):
    return HttpResponse('收藏夹界面')


# 商品分类
def shopping_type(requset):
    return HttpResponse('商品分类界面')


# 服务中心
def service_centre(request):
    return HttpResponse('服务中心界面')
