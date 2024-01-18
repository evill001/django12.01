from django.contrib import admin
from .models import Products, Orders, Customers

admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(Customers)