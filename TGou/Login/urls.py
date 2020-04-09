from django.urls import path
from Login import views

urlpatterns = [
    path('login', views.login),
    path('register', views.register),
    path('logout', views.logout),
    path('confirm', views.user_confirm),
    path('user_info', views.UserInfo.as_view()),
    path('modify_psd', views.modify_psd),

]