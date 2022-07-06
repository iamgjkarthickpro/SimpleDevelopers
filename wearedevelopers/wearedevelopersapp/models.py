from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blogs(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    context = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.title

class Demo(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    context = models.TextField(blank=True,null=True)
    

    def __str__(self):
        return self.title
    
class mobilenumber(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)
    number= models.CharField(max_length=20,blank=True,null=True)
    country_code=models.CharField(max_length = 5,blank=True,null=True)
    otp= models.CharField(max_length=6,blank=True,null=True)
    def __str__(self):
        return self.number

class addcountrycode(models.Model):
    country_code=models.CharField(max_length = 10,blank=True,null=True)
    country=models.CharField(max_length = 100,blank=True,null=True)
    def __str__(self):
        return self.country_code