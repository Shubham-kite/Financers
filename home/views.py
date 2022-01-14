from django.shortcuts import render,HttpResponse
#importing models
from .models import UserInfo


# Create your views here.
def index(request):
    return render(request,"home.html")

def login(request):
    if request.method=="POST":
        name = request.POST.get("user")
        email = request.POST.get("username")
        passwd = request.POST.get("password")
        contact = request.POST.get("contact")
        #posting data into db 
        userdata = UserInfo(name = name,email = email,password = passwd,contact = contact).save()
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")
def main(request):
    return render(request,"main.html")

def help(request):
    return render(request,"help.html")

def about(request):
    return render(request,"about.html")