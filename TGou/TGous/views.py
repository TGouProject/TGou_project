from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse, FileResponse, HttpRequest
from TGous import models
from Login.models import User, AllOrders
import time


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
        longin_state = username  # |登陆的用户
        if user.shopping_address is not None:

            # order = TGou_Order.objects.get(user=user)
            return render(request, 'TGou_page/index.html',
                          {'username': username, 'login_state': longin_state, 'logout': logout, 'login_url': user_info,
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
    goods_infos = AllOrders.objects.all()
    print(goods_infos)
    user = User.objects.get(name=username)
    infos = []
    for i in goods_infos:
        print(111111111, i)
        if i.user == user:
            print(12312313)
            infos.append(i)
    print('infos:', infos)
    return render(request, 'TGou_page/mytgou.html', {'infos': infos})


class ByShopping(View):
    def get(self, request, infos):
        shoppings_obj = models.Tgshoppings.objects.get(shopping_name=infos)
        return render(request, 'Order_page/shopping_info.html', {'shoppings_obj': shoppings_obj})

    def post(self, request, infos):
        # res = request.POST.get('number')
        shoppings_obj = models.Tgshoppings.objects.get(id=infos)
        print('shoppings_obj', shoppings_obj)
        ordedr_number = time.time()
        order_info = shoppings_obj.shopping_name
        Quantity_of_Goods = 1
        order_money = shoppings_obj.shopping_price
        order_type = '未交易'
        order_data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print('order_info', order_data)
        order_state = '未交易'

        username = request.session.get('user_name')
        user_address = models.User.objects.get(name=username)
        shipping_address = user_address.shopping_address

        user = user_address
        models.TGou_Order.objects.create(
            ordedr_number=ordedr_number, order_info=order_info, Quantity_of_Goods=Quantity_of_Goods,
            order_money=order_money, order_type=order_type, order_data=order_data, order_state=order_state,
            shipping_address=shipping_address, user=user)
        infoss = models.TGou_Order.objects.all()
        infos = []
        for i in infoss:
            if i.user == user:
                infos.append(i)
        print('infos', infos)
        return render(request, 'TGou_page/shopping_car.html', {'infos': infos})


# 服务中心
def service_centre(request):
    return HttpResponse('服务中心界面')

#
# # 商品详情
# def shopping_info(request, infos):
#     shoppings_obj = models.Tgshoppings.objects.get(shopping_name=infos)
#     return render(request, 'Order_page/shopping_info.html', {'shoppings_obj': shoppings_obj})


# 下单
def buy(request):
    if request.method == 'POST':
        order_info = request.POST.get('')