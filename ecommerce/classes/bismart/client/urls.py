
from django.urls import path
from .views import clients_list, clients_detail, clients_by_Email, client_login, client_register

urlpatterns = [
    path('by-email/', clients_by_Email, name='client_create'),
    path('list/', clients_list, name='client_list'),
    path('detail/<int:pk>/', clients_detail, name='client_detail'),
    path('login/', client_login, name='client_login'),
    path('register/', client_register, name='client_register'),
]