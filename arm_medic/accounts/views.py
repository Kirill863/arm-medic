from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            
            # Дополнительная обработка должности/специальности
            position = form.cleaned_data.get('position')
            if position:
                user.position = position
            
            user.save()
            messages.success(request, 'Регистрация прошла успешно! Теперь вы можете войти.')
            return redirect('login')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = SignUpForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')
        
        if not all([username, password, role]):
            messages.error(request, 'Все поля обязательны для заполнения')
            return render(request, 'accounts/login.html')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Проверяем соответствие роли
            if user.role != role:
                messages.error(request, 'Неверная роль для данного пользователя')
                return render(request, 'accounts/login.html')
            
            login(request, user)
            messages.success(request, f'Добро пожаловать, {user.get_full_name()}!')
            
            # Перенаправление в зависимости от роли
            redirect_map = {
                'doctor': 'doctor_dashboard',
                'nurse': 'nurse_dashboard',
                'admin': 'admin_dashboard'
            }
            return redirect(redirect_map.get(role, 'home'))
        else:
            messages.error(request, 'Неверное имя пользователя или пароль')
    
    return render(request, 'accounts/login.html')

from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из системы')
    return redirect('login')