from django.shortcuts import render
from .models import MenuCategory

def menu_view(request):
    categories = MenuCategory.objects.all()
    return render(request, 'kiosk/menu.html', {'categories': categories})


# orders/views.py

from django.shortcuts import render, redirect
from django.contrib import messages

def order_list(request):
    # 주문 목록을 보여주는 뷰
    if request.method == 'POST':
        # 주문을 처리하는 로직
        # 여기서 주문 정보를 처리하고, 예를 들어 주문이 성공적으로 완료되었다는 메시지를 표시합니다.
        messages.success(request, '주문이 성공적으로 완료되었습니다.')
        return redirect('orders:order_list')  # 주문 목록 페이지로 이동
    # GET 요청의 경우 주문 목록을 보여주는 페이지를 렌더링합니다.
    return render(request, 'orders/order_list.html')
