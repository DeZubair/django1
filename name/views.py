from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def homePage(request):
    # data={ 
    #     'title':'Home Page1',
    #     'bdata':'wel come',
    #     'clist':['php','java','django'],
    #     # 'number':[10,20,30,40,50],
    #     'number':[],
    #     'student_details':[
    #         {'name':'zubair','phone':923077331363},
    #         {'name':'zubi','phone':923081399730}
    #     ]
    # }
    return render(request,"index.html")

def register(request):
    if request.method=='POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('uname')
        user = User(first_name=firstname,last_name=lastname,email=email,password=password,username=username)
        user.save()
        return redirect('/')

    return render(request,"register.html")

def course(request):
    return HttpResponse("welcome to my 2nd page")

def courseDetail(request,courseid):
    return HttpResponse(courseid)