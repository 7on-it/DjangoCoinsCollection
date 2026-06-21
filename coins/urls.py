from django.urls import path
from . import views

app_name = 'coins'

urlpatterns = [
    path('', views.coin_list, name='coin_list'),           # Главная страница
    path('coin/<int:pk>/', views.coin_detail, name='coin_detail'),  # Детальная страница
    path('register/', views.register, name='register'),
]