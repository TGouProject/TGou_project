from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.http import HttpResponse, JsonResponse, FileResponse, HttpRequest
from TGous import models
from Login.models import User, AllOrders
import time, datetime
from django.db.models import Q
import random


# from TGous.models import TGou_Order, Tgshoppings


# 首页界面控制
def index(request):
    longin_state = '登陆'
    logout = '退出'
    login_url = 'login'
    user_info = 'user_info'
    info = '完善个人信息'
    username = request.session.get('user_name')
    shoppings = models.Tgshoppings.objects.all()[1:9]  # 商品对象
    shoppings2 = models.Tgshoppings.objects.all()[10:18]
    guess_shoppings = models.Tgshoppings.objects.all()[random.randint(19, 30):random.randint(50, 60)]
    if username:
        user = User.objects.get(name=username)

        longin_state = username  # |登陆的用户
        if user.shopping_address is not None:

            # order = TGou_Order.objects.get(user=user)
            return render(request, 'TGou_page/index.html',
                          {'username': username, 'login_state': longin_state, 'logout': logout, 'login_url': user_info,
                           'shoppings': shoppings, 'shoppings2': shoppings2, 'guess_shoppings': guess_shoppings})
        else:
            return render(request, 'TGou_page/index.html',
                          {'login_state': longin_state, 'logout': logout, 'login_url': user_info, 'info': info,
                           'shoppings': shoppings, 'shoppings2': shoppings2, 'guess_shoppings': guess_shoppings})
    return render(request, 'TGou_page/index.html', {'login_state': longin_state, 'login_url': login_url,
                                                    'shoppings': shoppings, 'shoppings2': shoppings2,
                                                    'guess_shoppings': guess_shoppings})


# 消息界面
def message(request):
    return HttpResponse("消息界面")


# 获取登陆状态
def user_longin_state(request):
    username = request.session.get('user_name')
    if username:
        return username


# 我的TGou
def mytgou(request):
    try:
        if user_longin_state(request):
            goods_infos = AllOrders.objects.all()
            print(goods_infos)
            users = request.session.get('user_name')
            user = User.objects.get(name=users)
            infos = []
            for i in goods_infos:
                if i.user == user:
                    infos.append(i)
            print('infos:', infos)
            return render(request, 'TGou_page/mytgou.html', {'infos': infos})
        else:
            return redirect('/api/v1.0/TGou/login')
    except:
        return redirect('/api/v1.0/TGou/404')


# 404界面
def page_not_found(request):
    return render(request, 'TGou_page/not_found.html')


class ByShopping(View):
    def get(self, request, infos):
        # get 返回商品信息
        try:
            shoppings_obj = models.Tgshoppings.objects.get(id=infos)
            return render(request, 'Order_page/shopping_info.html', {'shoppings_obj': shoppings_obj})
        except:
            return redirect('/api/v1.0/TGou/404')

    def post(self, request, infos):
        # post 返回购物车界面
        # username = request.session.get('user_name')  #获取当前登陆用户
        try:
            if user_longin_state(request):
                res = request.POST.get('number')  # 隐藏属性 默认1
                shoppings_obj = models.Tgshoppings.objects.get(id=infos)  # 获取商品对象
                order_info = shoppings_obj.shopping_name
                order_photo = shoppings_obj.shopping_photo
                Quantity_of_Goods = res
                order_money = shoppings_obj.shopping_price
                order_state = '未交易'
                user_order = models.User.objects.get(name=user_longin_state(request))  # 获取用户信息
                shopping_address = user_order.shopping_address
                # 创建订单号
                res = time.time()
                res = str(res)
                ordedr_number = res[:10]
                user = user_order
                models.TGou_Order.objects.create(order_number=ordedr_number,
                                                 order_info=order_info, Quantity_of_Goods=Quantity_of_Goods,
                                                 order_money=order_money, order_state=order_state,
                                                 shopping_address=shopping_address, user=user,
                                                 shopping_photo=order_photo)
                infoss = models.TGou_Order.objects.all()
                infos = []
                for i in infoss:
                    if i.user == user:
                        infos.append(i)
                # print('infos', infos)

                return render(request, 'TGou_page/shopping_car.html',
                              {'infos': infos, 'username': user_longin_state(request)})
            return redirect('/api/v1.0/TGou/login')
        except:
            return redirect('/api/v1.0/TGou/404')


# 服务中心
def service_centre(request):
    return HttpResponse('服务中心界面')


def shopping_car(request):
    try:
        if user_longin_state(request):
            infos = models.TGou_Order.objects.all()
            return render(request, 'TGou_page/shopping_car.html', {'infos': infos})
        return redirect('/api/v1.0/TGou/login')
    except:
        return redirect('/api/v1.0/TGou/404')


# 下单
def buy(request):
    try:
        if request.method == 'POST':
            username = request.session.get('user_name')
            user = User.objects.get(name=username)
            if user:
                order_number = request.POST.get('shoppings_name')
                print(1111111111111111111111111111, order_number)
                if order_number:
                    tg_rouder = models.TGou_Order.objects.get(order_number=order_number)
                    tg_rouder.order_state = '交易完成'
                    tg_rouder.save()

                    AllOrders.objects.create(
                        order_number=tg_rouder.order_number,
                        order_info=tg_rouder.order_info,
                        Quantity_of_Goods=tg_rouder.Quantity_of_Goods,
                        order_money=tg_rouder.order_money,
                        order_data=tg_rouder.order_data,
                        order_state='交易完成',
                        shipping_address=tg_rouder.shopping_address,
                        user=user
                    )
                    goods_infos = AllOrders.objects.all()

                    infos = []
                    for i in goods_infos:
                        if i.user == user:
                            infos.append(i)
                    return render(request, 'TGou_page/mytgou.html', {'infos': infos})
                else:
                    messages.error(request, '请至少购选一种商品!')
                    return redirect('/api/v1.0/TGou/shopping_car')
    except:
        return redirect('/api/v1.0/TGou/404')


class Search(View):
    def get(self, request):

        all_shoppings = models.Tgshoppings.objects.all()
        info = request.GET.get('content')
        if info:
            # 模糊查询
            all_shoppings = all_shoppings.filter(Q(shopping_name__icontains=info) | Q(
                shopping_info__icontains=info) | Q(shopping_price__icontains=info))
            if all_shoppings:
                # print(all_shoppings.count(),1111111111111111111111111111111111111111111)   #获取匹配到的对象的数量
                shoppings = all_shoppings.all()
                return render(request, 'Order_page/search_shoppings.html', {'shoppings_obj': shoppings, 'info': info})
            else:
                return HttpResponse('输入的内容有误或商品不存在')


def delete_order(request, infos):
    if infos != '0':
        # 先把这条数据删除
        models.TGou_Order.objects.get(id=infos).delete()

    # 在查询出登录用户的全部订单,返回前端页面
    username = request.session.get('user_name')
    user_object = models.User.objects.get(name=username)

    infoss = models.TGou_Order.objects.all()
    for db_state in infoss:
        print(db_state.order_state, 1111111222222222222)
        if db_state.order_state == '交易完成':
            db_state.delete()
    infos = []
    for i in infoss:
        if i.user == user_object:
            infos.append(i)
    return render(request, 'TGou_page/shopping_car.html', {'infos': infos})
