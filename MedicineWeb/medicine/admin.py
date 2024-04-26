from django.contrib import admin
from .models import Product, Customer, Cart


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_displayed = ['id', 'title', 'discounted_price', 'quantity', 'category', 'product_image']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality', 'city', 'state', 'zipcode']


class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']


admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Cart, CartAdmin)
