from django.shortcuts import render
from .models import Category

def index_view(request):
    return render(request, 'index.html')

def menu_view(request):
    categories = Category.objects.prefetch_related('products__types').all()
    return render(request, 'menu.html', {'categories': categories})

def about_view(request):
    return render(request, 'about.html')