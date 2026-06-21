from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Coin
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def coin_list(request):
    """Главная страница со списком всех монет"""
    coins = Coin.objects.all().order_by('-year')  # Сначала новые
    return render(request, 'coins/coin_list.html', {'coins': coins})

def coin_detail(request, pk):
    """Детальная страница одной монеты"""
    coin = get_object_or_404(Coin, pk=pk)
    return render(request, 'coins/coin_detail.html', {'coin': coin})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('coins:coin_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})