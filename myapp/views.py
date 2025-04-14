from django.shortcuts import render,redirect
from .models import ContactUs
def home(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')


def cars(request):
    return render(request,'cars.html')


def contact(request):
    if request.method=="POST":
        nm=request.POST["name"]
        em=request.POST["email"]
        ph=request.POST['phone']
        pr=request.POST["project"]
        msg=request.POST["message"]
        sub=request.POST["subject"]
        print(nm,em,ph)
        data=ContactUs(name=nm,email=em,phone=ph,project=pr,message=msg,subject=sub)
        data.save()
        msg1="Submit your application"
        return render(request,'index.html',{'msg1': msg1})

    return render(request,'contact.html')


def feature(request):
    return render(request,'feature.html')

def team(request):
    return render(request,'team.html')

def service(request):
    return render(request,'service.html')

def testimonial(request):
    return render(request,'testimonial.html')

def error_404(request):
    return render(request,'404.html')





