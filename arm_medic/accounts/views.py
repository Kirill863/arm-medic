from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Укажите имя вашего маршрута
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Или другой маршрут
        else:
            # Обработка ошибки аутентификации
            return render(request, 'accounts/login.html', {'error': 'Неверные данные'})
    return render(request, 'accounts/login.html')