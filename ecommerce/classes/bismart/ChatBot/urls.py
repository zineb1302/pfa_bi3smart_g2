from .views import recuperer_messages
from django.urls import path
urlpatterns = [
    path('generate/', recuperer_messages, name='index'),
]