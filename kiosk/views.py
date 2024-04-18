from django.shortcuts import render
from .models import MenuCategory

def menu_view(request):
    categories = MenuCategory.objects.all()
    return render(request, 'kiosk/menu.html', {'categories': categories})
