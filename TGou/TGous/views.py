from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse, FileResponse, HttpRequest
from TGous import models
from Login.models import User


# from TGous.models import TGou_Order, Tgshoppings


# 首页界面控制
def index(request):
    longin_state = '登陆'
    logout = '退出'
    login_url = 'login'
    user_info = 'user_info'
    info = '完善个人信息'
    username = request.session.get('user_name')
    if username:
        user = User.objects.get(name=username)
        shoppings = models.Tgshoppings.objects.all()[1:9]  # 商品对象
        shoppings2 = models.Tgshoppings.objects.all()[10:18]
        guess_shoppings = models.Tgshoppings.objects.all()[43:63]

        if user.shopping_address != None:
            longin_state = username  # |登陆的用户
            # order = TGou_Order.objects.get(user=user)
            return render(request, 'TGou_page/index.html',
                          {'login_state': longin_state, 'logout': logout, 'login_url': user_info,
                           'shoppings': shoppings, 'shoppings2': shoppings2, 'guess_shoppings': guess_shoppings})
        else:
            return render(request, 'TGou_page/index.html',
                          {'login_state': longin_state, 'logout': logout, 'login_url': user_info, 'info': info})
    return render(request, 'TGou_page/index.html', {'login_state': longin_state, 'login_url': login_url})


# 消息界面
def message(request):
    return HttpResponse("消息界面")


# 我的TGou
def mytgou(request):
    username = request.session.get('user_name')
    order_number = models.TGou_Order.objects.get(ordedr_number='ss')
    shopping_info = models.Tgshoppings.objects.get(shopping_price='$1209.99')
    overmonney = int(order_number.Quantity_of_Goods[0]) * shopping_info.shopping_price[2]
    return render(request, "Order_page/orderpage.html",
                  {'order_number': order_number.ordedr_number, 'shopinfo': shopping_info.shopping_info,
                   'monney': shopping_info.shopping_price, 'shopnum': order_number.Quantity_of_Goods,
                   'shopname': shopping_info.shopping_name, 'overmonney': overmonney})





class ByShopping(View):
    def get(self,request,infos):
        shoppings_obj = models.Tgshoppings.objects.get(shopping_name=infos)
        return render(request, 'Order_page/shopping_info.html', {'shoppings_obj': shoppings_obj})
    def post(self,request,infos):
        print(infos,11111111111111111111)
        res = request.POST.get('number')
        print(res)
        shoppings_obj = models.Tgshoppings.objects.get(shopping_name=infos)
        return HttpRequest(shoppings_obj)






# 服务中心
def service_centre(request):
    return HttpResponse('服务中心界面')

#
# # 商品详情
# def shopping_info(request, infos):
#     shoppings_obj = models.Tgshoppings.objects.get(shopping_name=infos)
#     return render(request, 'Order_page/shopping_info.html', {'shoppings_obj': shoppings_obj})
