from django.urls import path,include
from Login import views
from captcha.views import captcha_refresh

urlpatterns = [
    path('login', views.login),
    path('register', views.register),
    path('logout', views.logout),
    path('confirm', views.user_confirm),
    # path('user_info', views.UserInfo.as_view()),
    path('user_info', views.UserInfo),
    path('modify_psd', views.modify_psd)
]