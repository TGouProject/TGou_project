from django.urls import path
from TGous import views

urlpatterns = [
    path('message',views.message),
    path('mytgou',views.mytgou),
    path('shopping_car',views.shopping_car),
    path('shopping_type',views.shopping_type),
    path('service_centre',views.service_centre),
    path('favorite',views.favorite),
]