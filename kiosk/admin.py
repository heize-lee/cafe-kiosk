from django.contrib import admin
from .models import MenuCategory, MenuItem, MenuOption, Order, Payment

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'image']

admin.site.register(MenuCategory)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(MenuOption)
admin.site.register(Order)
admin.site.register(Payment)
