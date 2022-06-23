from django.contrib import admin
from .models import customers
from .models import products

# Register your models here.
admin.site.register(customers)
admin.site.register(products)