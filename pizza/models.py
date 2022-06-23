from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class customers(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default="")
    name=models.CharField(max_length=200,default="")
    phone=models.CharField(max_length=200,default="")
    city=models.CharField(max_length=200,default="")
   
    def __str__(self):
        return self.user.username
class products(models.Model):
    name=models.CharField(max_length=200,default="")
    description=models.CharField(max_length=200,default="")
    price=models.DecimalField(max_digits=6,decimal_places=2,default=0.0)
    photo=models.ImageField(upload_to='photo/%y/%m/%d',default="")
    is_active=models.BooleanField(default=True)
    date=models.DateField(default=datetime.now)
    def __str__(self):
        return self.name

   



    

