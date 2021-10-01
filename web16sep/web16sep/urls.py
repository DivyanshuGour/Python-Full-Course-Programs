from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.fun1),
    path('help',views.fun2)

]