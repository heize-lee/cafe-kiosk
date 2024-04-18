from django.urls import path
from . import views

urlpatterns = [
    # 예시: 메뉴 페이지를 보여주는 URL 패턴
    path('menu/', views.menu_view, name='menu'),
    # 여기에 다른 URL 패턴들을 추가할 수 있습니다.
]
