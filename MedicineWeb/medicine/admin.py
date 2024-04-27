from django.contrib import admin
from .models import Product, Customer, Cart, Payment, OrderPlace


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_displayed = ['id', 'title', 'discounted_price', 'quantity', 'category', 'product_image']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality', 'city', 'state', 'zipcode']


class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']


class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'bikaspay_order_id', 'bikaspay_payment_status', 'bikaspay_payment_status',
                    'bikas_payment_id', 'paid']


class OrderPlaceModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product', 'quantity', 'ordered_date', 'status', 'payment']


admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Payment, PaymentModelAdmin)
admin.site.register(OrderPlace, OrderPlaceModelAdmin)
