from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse, FileResponse, HttpRequest
from TGou import settings
from Login import models
from Login.forms import UserForm, RegisterForm


def hellodog(request):
    return HttpResponse('Hello TGou')


def index(request):
    pass
    return render(request, 'Login/index.html')


def login(request):
    # 通过session判断用户是否登录
    if request.session.get('is_login'):
        return redirect('/api/v1.0/TGou/index')
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = '检查填写内容'
        # 使用表单类自带的is_valid()方法一步完成数据验证工作
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            print('login--------', username, password)
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/api/v1.0/TGou/index')
                else:
                    message = '昵称或密码错误'
            except:
                message = '用户不存在'
        # locals() Python内置函数,它返回当前所有的本地变量字典不用去构造字典,但是同时也可能往模板传入了一些多余的变量数据，造成数据冗余降低效率。
        return render(request, 'Login/login.html', locals())
    login_form = UserForm()
    return render(request, 'Login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/api/v1.0/TGou/index")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'Login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'Login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'Login/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                print(123132132)
                return redirect('/api/v1.0/TGou/login')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'Login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect('/api/v1.0/TGou/index')
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect('/api/v1.0/TGou/index')
