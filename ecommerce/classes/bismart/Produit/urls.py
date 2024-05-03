from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
]
