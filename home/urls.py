from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('',views.index,name="home"),
    path('home.html',views.index,name="home"),
    path('login.html',views.login,name="login"),
    path('signup.html',views.signup,name="signup"),
    path('help.html',views.help,name="help"),
    path('about.html',views.about,name="about"),
    path('main.html',views.main,name="main"),
    path('login.html',views.login,name="loginpage"),
    path('wallet.html',views.wallet,name="wallet-page")

]