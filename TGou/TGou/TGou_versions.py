from django.urls import path,include

urlpatterns = [
    path('v1.0/TGou/',include('TGous.urls')),
]