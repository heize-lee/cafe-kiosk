from django.shortcuts import render
from .models import Menu, Order, Payment

def rich_cafe(request):
    categorys = Menu.objects.all()
    context = {
        "lions" : categorys
    }
    return render(request, 'choonsik_cafe/rich_cafe.html', context)