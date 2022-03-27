from django.shortcuts import render,HttpResponse,redirect
#importing models
from .models import UserInfo
from django.http import JsonResponse
from json import dumps
import requests
#login and authentication 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth


compony = {
    "TCS":"TCS",
    "Wipro":"WTI",
    "ICIC Bank":"IBN",
    "Tata Motors":"TTM",
    "Infosys":"INFY",
    "SBI":"SBI",
    "Reliance":"RCOM",
    "Amazon":"AMZN",
    "Google":"GOOGL",
    "IBM":"IBM"
    }


# Create your views here.
def index(request):
    
    response = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=f3831cf4b9e34369843e9062f75e80f1')
    news = response.json()
    news_title = []
    news_disc = []
    for i in range(6):
        news_title.append(news["articles"][i]["title"])
    data  = {"news_title": news_title}
    data=dumps(data)
    return render(request,"home.html",{'data': data})
    #return render(request,"home.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("./main.html")
        else:
            return redirect('/login.html')
    return render(request,"login.html")
    ''' here we have to add authentication '''
def signup(request):
    if request.method=="POST":
        name = request.POST.get("user")
        email = request.POST.get("username")
        passwd = request.POST.get("password")
        contact = request.POST.get("contact")
        
        if User.objects.filter(username=email).exists():
            return render(request,"signup.html")
        else:
            User.objects.create_user(username=email,password=passwd,first_name=name,email=email)
            userdata = UserInfo(name = name,email = email,password = passwd,contact = contact).save()
            return redirect('/login.html')
    return render(request,"signup.html")

#@login_required(login_url='login.html')
def main(request):
    if request.method == "POST":
        comp = request.POST['company']
        print(comp)
    else:
        comp = "Google"
    time = []
    value = []
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={compony[comp]}&apikey=9GI559N6X7ZBUR94'
    r = requests.get(url)
    data = r.json()
    count = 0
    for i in data["Time Series (Daily)"]:
        time.append(i)
        value.append(float(data["Time Series (Daily)"][i]["2. high"]))
        count+=1
        if(count == 30):
            break
    maxval = max(value)
    minval = min(value)
    open_val = round(float(data["Time Series (Daily)"][time[0]][ "1. open"]),2)
    close_val = round(float(data["Time Series (Daily)"][time[0]]["4. close"]),2)
    volume_val = round(float(data["Time Series (Daily)"][time[0]]["5. volume"]),2)
    last_open = round(float(data["Time Series (Daily)"][time[1]][ "1. open"]),2)
    low = round(float(data["Time Series (Daily)"][time[0]][ "3. low"]),2)

 
    data = {
        "time":time[::-1],
        "value":value[::-1],
        "max":maxval,
        "min":minval,
        "open":open_val,
        "close":close_val,
        "volume":volume_val,
        "last_open":last_open,
        }
        
    stock = {
        "title":comp,
        "open":open_val,
        "close":close_val,
        "volume":volume_val,
        "last_open":last_open,
        "high":value[0],
        "low":low,
    }

    data=dumps(data)
    return render(request,"main.html",{'data': data,"stock":stock})
'''avoid un autherized login '''   

@login_required(login_url='login.html')
def wallet(request):
    return render(request,"wallet.html")

def help(request):
    return render(request,"help.html")

def about(request):
    return render(request,"about.html")