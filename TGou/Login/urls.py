from django.urls import path
from Login import views

urlpatterns = [
    path('hello', views.hellodog),
    path('index', views.index),
    path('login', views.login),
    path('register', views.register),
    path('logout', views.logout),
]
