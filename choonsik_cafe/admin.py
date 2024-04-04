from django.contrib import admin
from .models import Menu, Order, Payment

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['drink', 'sub_drink', 'price']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'order_dt', 'quantity', 'price_all', 'order_status']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['payment_id', 'payment_dt', 'type', 'payment_status']
