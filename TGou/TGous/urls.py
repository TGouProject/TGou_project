from django.urls import path
from TGous import views

urlpatterns = [
    path('index', views.index),
    path('message', views.message),
    path('mytgou', views.mytgou),
    path('service_centre', views.service_centre),
    # path('shopp_info/<str:infos>',views.shopping_info),
    path('shopp_info/<infos>', views.ByShopping.as_view()),

]
