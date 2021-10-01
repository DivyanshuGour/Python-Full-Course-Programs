from django.shortcuts import render
from django.http import HttpResponse

def save(request):
    name = request.GET.get('ename')
    sal = request.GET.get('salary')
    city = request.GET.get('city')
    print(name,sal,city)
    return HttpResponse("OKay")

def register(request):
    return render(request,'register.htm')

def home(request):
    title = "Universal Informatics, Indore"
    lst = ['vikas','gopal','lokesh','kalpana','divya']

    students = [
        {'roll':101,'name':'vikas','age':21,'marks':234.34},
        {'roll':102,'name':'gopal','age':22,'marks':314.65},
        {'roll':103,'name':'raj','age':23,'marks':424.54},
        {'roll':104,'name':'rohan','age':20,'marks':122.45},
        {'roll':105,'name':'shyam','age':26,'marks':211.4},
    ]

    return render(request,'home.htm',{
        'cname':title,
        'friends':lst,
        'students':students
    })