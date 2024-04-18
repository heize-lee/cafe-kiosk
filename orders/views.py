# orders/views.py

from django.shortcuts import render, redirect  # redirect 추가
from .models import Order

def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})

def order_create(request):
    if request.method == 'POST':
        # POST 요청을 처리하여 주문을 생성하는 로직
        # 이 부분은 실제 주문을 생성하는 코드로 대체해야 합니다.
        # 아래 코드는 주문이 생성되었다고 가정하고 주문 목록 페이지로 리다이렉트합니다.
        return redirect('orders:order_list')
    else:
        return render(request, 'orders/order_create.html')

def order_detail(request, order_id):
    order = Order.objects.get(pk=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})
