from django.db import models
from django.urls import reverse

# from django.db import models

# # Create your models here.
# # models안에 Model이라는 클래스를 상속받자.
# class Category(models.Model):
#     name = models.CharField(max_length=30)
# #연결할거니까 포링키, 어떤거랑 연결할거냐?, ON-delete, what is cascade?
# class Item:
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     name = models.CharField(max_length=30)
#     price = models.IntegerField()
# class Order:
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     order_dt = models.DateTimeField(auto_now_add=True)
#     item_count = models.IntegerField()
#     order_price = models.IntegerField()

# menu: menu_id, {option_id}, drinks, sub_drinks, price 
class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True, verbose_name='Menu ID')
    drink = models.CharField(verbose_name='Drink', max_length=100)
    sub_drink = models.CharField(verbose_name='Sub Drink', max_length=100)
    price = models.IntegerField(verbose_name='Price')

    #매직메서드 return self.name
    def __str__(self):
        return f"{self.drink} - {self.sub_drink}"
    
    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'
        ordering = ['drink', 'sub_drink']

# option: tbd


# order: order_id, order_dt, quantity, price_all, order_status
class Order(models.Model):
    order_id = models.AutoField(primary_key=True, verbose_name='Order ID')
    order_dt = models.DateTimeField(auto_now_add=True, verbose_name='Order Date')
    quantity = models.IntegerField(verbose_name='Quantity')
    price_all = models.IntegerField(verbose_name='Total Price')
    order_status = models.CharField(max_length=100, verbose_name='Order Status')

    def __str__(self):
        return f"Order {self.order_id} - {self.order_dt}"
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-order_dt']

# payment: payment_id, payment_dt, type, payment_status
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True, verbose_name='Payment ID')
    payment_dt = models.DateTimeField(auto_now_add=True, verbose_name='Payment Date')
    type = models.CharField(max_length=100, verbose_name='Payment Type')
    payment_status = models.CharField(max_length=100, verbose_name='Payment Status')

    def __str__(self):
        return f"Payment {self.payment_id} - {self.payment_dt}"
    
    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        ordering = ['-payment_dt']