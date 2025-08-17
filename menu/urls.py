from django.urls import path
from .views import index_view, menu_view, about_view

app_name = "menu_app"

urlpatterns = [
    path('', index_view, name='index'),
    path('menu/', menu_view, name='menu'),
    path('about/', about_view, name='about'),
]