# patients/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import PatientRegistrationForm
from django.contrib.auth.decorators import login_required

def patient_register(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('patient_dashboard')
    else:
        form = PatientRegistrationForm()
    return render(request, 'patients/register.html', {'form': form})

def patient_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.role == 'patient':
            login(request, user)
            return redirect('patient_dashboard')
    return render(request, 'patients/login.html')

@login_required
def patient_dashboard(request):
    if request.user.role != 'patient':
        return redirect('access_denied')
    return render(request, 'patients/dashboard.html')