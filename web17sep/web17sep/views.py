from django.shortcuts import render

def home(request):
    title = "Universal Indore"
    num = 45
    lst = ['Vikas','Mohan','Gopal']
    return render(request,'home.htm',{
        'cname' : title,
        'value' : num,
        'data' : lst
    })

def about(request):
    return render(request,'about.htm')

def contact(request):
    return render(request,'contact.htm')

# DTL : Django Template Language    