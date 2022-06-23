from django.db import models
from pizza.models import products
from django.contrib.auth.models import User
from creditcards.models import CardNumberField
from creditcards.models import CardExpiryField
from creditcards.models import SecurityCodeField

# Create your models here.
class orders(models.Model):
        user=models.ForeignKey(User,on_delete=models.CASCADE)
        order_date=models.DateTimeField()
        details=models.ManyToManyField(products,through='orderdetails')
        is_finised=models.BooleanField()

        def __str__(self):
            return 'user: ' +self.user.username + ', order id '+str(self.id)

class orderdetails(models.Model):
            product = models.ForeignKey(products,on_delete=models.CASCADE)
            order= models.ForeignKey(orders,on_delete=models.CASCADE)
            price = models.DecimalField(max_digits=6,decimal_places=2)
            quatity = models.IntegerField()

            def __str__(self):
                return 'user :' +self.order.user.username + ', product: '+ self.product.name +', order id: '+str(self.order.id)

class payment(models.Model):
            order=models.ForeignKey(orders,on_delete=models.CASCADE)
            shipmentaddress=models.CharField(max_length=200,default="")
            shipmentphone=models.CharField(max_length=200,default="")
            cardnumber=CardNumberField()
            expiredate=CardExpiryField()
            securitycode=SecurityCodeField()


