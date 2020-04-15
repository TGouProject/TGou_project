from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, FileResponse, HttpRequest
from TGou import settings
from Login import models
from Login.forms import UserForm, RegisterForm, ModifyForm
from Login.tool_fun import make_confirm_string, send_email
import datetime
from Login.models import User
from django.views import View
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url


# 登录视图
def login(request):
    # 通过session判断用户是否登录
    if request.session.get('is_login'):
        return redirect('/api/v1.0/TGou/index')

    # POST请求
    if request.method == "POST":
        # 接收表单数据生成表单对象
        login_form = UserForm(request.POST)
        # message = '检查填写内容'
        # 使用表单类自带的is_valid()方法一步完成数据验证工作,例如:验证码
        if login_form.is_valid():
            # 验证成功,从表单对象中获取具体的值
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            print('login--------', username, password)
            users = models.User.objects.all()
            try:
                for user in users:
                    # 判断输入的是否存在于name或email中
                    if user.name == username or user.email == username:
                        if not user.has_confirmed:
                            message = "该用户还未通过邮件确认,请先去邮箱确认!"
                            return render(request, 'Login/login.html', locals())
                        if user.password == password:
                            # 在session中添加用户状态或者信息
                            request.session['is_login'] = True
                            # request.session['user_id'] = user.id
                            request.session['user_name'] = user.name
                            return redirect('/api/v1.0/TGou/index')
                else:
                    message = '用户名或密码错误'
            except:
                message = '用户不存在'
        # 验证没通过会返回一个包含先前数据的表单给前端页面，方便用户修改
        # locals() Python内置函数,它返回当前所有的本地变量字典不用去构造字典,例如:{'message':message, 'login_form':login_form},但是同时也可能往模板传入了一些多余的变量数据，造成数据冗余降低效率。
        return render(request, 'Login/login.html', locals())
    # GET请求返回空的表单,用于用户登录
    login_form = UserForm()
    return render(request, 'Login/login.html', locals())


# 注册视图
def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/api/v1.0/TGou/index")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            # 通过验证,获取数据
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
                new_user = models.User.objects.create(name=username, password=password1, email=email, sex=sex)
                # 生成code,用于确认邮件请求
                code = make_confirm_string(new_user)
                # 发送邮件
                send_email(email, code)

                message = '请前往注册邮箱，进行邮件确认！'
                return render(request, 'Login/confirm.html', locals())  # 跳转到等待邮件确认页面。
    register_form = RegisterForm()
    return render(request, 'Login/register.html', locals())


# 退出视图
def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect('/api/v1.0/TGou/index')
    # flush()一次性将session中的所有内容全部清空，确保不留后患
    request.session.flush()
    # 或者使用下面的方法,一条一条删除
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect('/api/v1.0/TGou/index')


# 处理邮箱确认请求
def user_confirm(request):
    # 从GET请求的参数中获取code
    code = request.GET.get('code', None)
    message = ''
    try:
        # 验证是否与ConfirmString表中的一致
        confirm = models.ConfirmString.objects.get(code=code)
    except:
        message = '无效的确认请求!'
        return render(request, 'Login/confirm.html', locals())

    c_time = confirm.c_time
    now = datetime.datetime.now()
    # 判断现在的时间是否超过创建时7天
    if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
        # 删除注册用户与注册码
        confirm.user.delete()
        message = '您的邮件已经过期！请重新注册!'
        return render(request, 'Login/confirm.html', locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        # 只删除注册码
        confirm.delete()
        message = '感谢确认，请使用账户登录！'
        return render(request, 'Login/confirm.html', locals())


# 用户个人信息
class UserInfo(View):
    def get(self, request):
        info = '用户不存在'
        username = request.session.get('user_name')
        if username:
            user = User.objects.get(name=username)
            user_sex = user.sex
            user_email = user.email
            user_name = user.name
            user_address = user.shopping_address
            return render(request, 'TGou_page/user_info.html',
                          {'user_sex': user_sex, 'user_email': user_email, 'user_name': user_name,
                           'user_address': user_address})
        return render(request, 'TGou_page/user_info.html', {'info': info})

    def post(self, request):
        username = request.session.get('user_name')
        if username:
            user = User.objects.get(name=username)
            if user:
                address = request.POST.get('address')
                user.shopping_address = address
                user.save()
                message = '新的地址保存成功'
                return render(request, 'TGou_page/save_success.html', {'message': message})
            return HttpResponse('用户信息不存在')
        return HttpResponse('请先登陆在尝试添加')


# 修改密码,邮件确认
def modify_psd(request):
    if request.method == "POST":
        modify_psd = ModifyForm(request.POST)
        message = "请检查填写的内容！"
        if modify_psd.is_valid():
            # 通过验证,获取数据
            email = modify_psd.cleaned_data['email']
            password1 = modify_psd.cleaned_data['password1']
            password2 = modify_psd.cleaned_data['password2']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'Login/modify_psd.html', locals())
            else:
                user = models.User.objects.get(email=email)
                print('改密码', user)
                if not user:
                    print('改密码1', user)
                    message = "邮箱输入有误!"
                    return render(request, 'Login/modify_psd.html', locals())
                else:
                    print('改密码2', user.email)
                    user.password = password1
                    user.save()
                    # 生成code,用于确认邮件请求
                    code = make_confirm_string(user)
                    # 发送邮件
                    send_email(email, code, type='修改密码')
                    message = '请前往注册邮箱，进行邮件确认！'
                    return render(request, 'Login/confirm.html', locals())
    modify_psd = ModifyForm()
    return render(request, 'Login/modify_psd.html', locals())
