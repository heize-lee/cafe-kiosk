# orders/models.py

from django.db import models
from django.contrib.auth.models import User
from kiosk.models import MenuItem

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    # 추가적인 주문 정보는 여기에 정의할 수 있습니다.

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
