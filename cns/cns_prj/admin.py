from django.contrib import admin

# Register your models here.
# your_app/admin.py
from .models import Collection, Promotion, Product, Customer, Order, Address, OrderItem, Cart, CartItem

admin.site.register(Collection)
admin.site.register(Promotion)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Address)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)
