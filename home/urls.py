from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('',views.index,name="home"),
    path('home',views.index,name="home"),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('help',views.help,name="help"),
    path('about',views.about,name="about"),
    path('main',views.main,name="main"),
    path('login',views.login,name="loginpage"),
    path('wallet',views.wallet,name="wallet-page")

]