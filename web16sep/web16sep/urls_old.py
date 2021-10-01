from django.urls import path
from django.http import HttpResponse

def fun1(request):
    return HttpResponse("My first Django Response !")

def fun2(request):
    return HttpResponse("Help Page !")


urlpatterns = [
    
    path('',fun1),
    path('help',fun2)

]