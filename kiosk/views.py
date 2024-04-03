from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("안녕하세요. 춘식카페입니다. 메뉴를 주문해주세요. :)")