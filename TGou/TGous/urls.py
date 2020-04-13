from django.urls import path
from TGous import views

urlpatterns = [
    path('index', views.index),
    path('message', views.message),
    path('mytgou', views.mytgou),
    path('service_centre', views.service_centre),
    path('shopp_info/<infos>', views.ByShopping.as_view()),
    path('buy', views.buy),
    path('shopping_car', views.shopping_car),
    path('Search', views.Search.as_view()),
    path('delete_order/<infos>', views.delete_order)

]
