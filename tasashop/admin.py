from django.contrib import admin
from .models import *
# Customer, Product, OrderTrans, CartItem, Shipping
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(OrderTrans)
admin.site.register(CartItem)
admin.site.register(Shipping)
