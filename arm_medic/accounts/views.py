from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        
        user = authenticate(username=username, password=password)
        if user is not None and user.role == role:
            login(request, user)
            if role == 'doctor':
                return redirect('doctor_dashboard')
            elif role == 'nurse':
                return redirect('nurse_dashboard')
            elif role == 'admin':
                return redirect('admin_dashboard')
        else:
            messages.error(request, 'Неверные данные или роль')
    return render(request, 'accounts/login.html')