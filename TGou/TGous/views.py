from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,JsonResponse,FileResponse,HttpRequest
from TGou import settings
def home_page(request):
    return render(request,'TGou_page/index.html')


def hellodog(request):
    return HttpResponse('Hello TGou')