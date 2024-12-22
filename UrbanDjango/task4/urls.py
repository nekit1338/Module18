from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('shop', views.index_2, name='shop'),
    path('cart', views.index_3, name='cart'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('cart/clear', views.clear_cart, name='clear_cart'),
]