from django.urls import path
from TGous import views

urlpatterns = [
    path('hello',views.hellodog),
    path('home_page',views.home_page)
]