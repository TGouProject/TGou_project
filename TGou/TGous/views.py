from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,JsonResponse,FileResponse,HttpRequest
from TGou import settings
def home_page(request):
    return render(request,'TGou_page/index.html')


def hellodog(request):
    return HttpResponse('Hello TGou')


#消息界面
def message(request):
    return HttpResponse("消息界面")

#我的TGou
def mytgou(requset):
    return render(requset,"Order_page/orderpage.html")

#购物车
def shopping_car(request):
    return HttpResponse('购物车界面')

#收藏夹
def favorite(request):
    return HttpResponse('收藏夹界面')

#商品分类
def shopping_type(requset):
    return HttpResponse('商品分类界面')

#服务中心
def service_centre(request):
    return HttpResponse('服务中心界面')