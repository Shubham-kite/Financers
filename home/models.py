from django.db import models

# Create your models here.
class UserInfo(models.Model):
    email = models.CharField(max_length=30,primary_key=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    contact = models.IntegerField(null=False)

class Company(models.Model):
    company = models.CharField(max_length=20,primary_key=True)
    volume =  models.IntegerField(null=False)
    date = models.DateField()

class wallet(models.Model):
    current = models.IntegerField(null=False)
    invested = models.IntegerField(null=False)
    profit= models.IntegerField(null=False)
    total = models.IntegerField(null=False)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)