from django.contrib import admin
from orders.models import orders
from orders.models import orderdetails
from orders.models import payment

# Register your models here.
admin.site.register(orders)
admin.site.register(orderdetails)
admin.site.register(payment)