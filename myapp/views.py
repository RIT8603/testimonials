from django.http import HttpResponse
from django.shortcuts import render
from .form import FeedbackForm

import datetime


def home(request):
    
    if request.method=="POST":
        #name=request.POST['name']
        check=request.POST.get('check')
        #mobile=request.POST['mobile']
        #email=request.POST['email']

        #print(name)
        #print(check)
        #print(mobile)
        print(check)
        if check is None:
            isActive=True
        else:
            isActive=False
        
    #isActive=True
    date = datetime.datetime.now()
    name="Ritesh"
    list_of_programs=[
        "WAP to check even or odd",
        "WAP to check prime number",
        "WAP to print all prime numbers from 1 to 100",
        "WAP to print pascals triangle"
    ]
    student={
        "student_name":"Ritesh",
        "student_college":"G.P.Barauni",
        "student_city":"BEG"
    }
    data={
        "date":date,
        #"isActive":isActive,
        "name":name,
        "list_of_programs":list_of_programs,
        "student_data":student
    }

    #return HttpResponse("<h1><b>Welcome to My website🫠💀☠️👾</b></h1>")
    return render(request,"home.html",data)

def about(request):
    return render(request,"about.html",{})
    #return HttpResponse("<h1>This is about page</h1>")

def login(request):
    return render(request,"login.html",{})

def services(request):
    return render(request,"services.html",{})
    date=datetime.datetime.now()
    return HttpResponse("<h1>This is about Services</h1>"+str(date))

def feedback(request):
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['email'])
            print(form.cleaned_data['name'])
            print(form.cleaned_data['feedback'])
            print("data saved")
        else:
            return render(request,"feedback.html",{'form':form})
    else:
        form=FeedbackForm()
        return render(request,"feedback.html",{'form':form})
