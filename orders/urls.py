# orders/urls.py

from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order_list, name='order_list'),  # 주문 목록을 보여주는 페이지
    path('create/', views.order_create, name='order_create'),  # 주문을 생성하는 페이지
    path('<int:order_id>/', views.order_detail, name='order_detail'),  # 주문 상세 페이지
]
