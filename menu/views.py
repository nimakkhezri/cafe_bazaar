from django.shortcuts import render
from .models import Category

def menu_view(request):
    categories = Category.objects.prefetch_related('products__types').all()
    return render(request, 'menu.html', {'categories': categories})
