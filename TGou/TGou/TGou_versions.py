from django.urls import path,include

urlpatterns = [
    path('v1.0/TGou/',include('Login.urls')),
    path('v1.0/TGou/',include('TGous.urls')),
    path('',include('TGous.urls'))

]