from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from patients.models import Patient
from prescriptions.models import Prescription
from prescriptions.forms import PrescriptionForm

@login_required
def doctor_dashboard(request):
    """
    Панель управления врача с фильтрацией пациентов
    """
    # Проверка роли через атрибут профиля (более надежно)
    if not hasattr(request.user, 'doctor_profile'):
        return redirect('access_denied')
    
    # Получаем текущего врача
    current_doctor = request.user.doctor_profile
    
    # Фильтрация пациентов с возможностью поиска
    search_query = request.GET.get('search', '')
    
    patients = Patient.objects.filter(
        attending_physician=current_doctor
    ).filter(
        Q(full_name__icontains=search_query) |
        Q(diagnosis__icontains=search_query) |
        Q(room__icontains=search_query)
    ).order_by('-admission_date')
    
    context = {
        'patients': patients,
        'search_query': search_query,
        'current_doctor': current_doctor
    }
    return render(request, 'staff/doctor_dashboard.html', context)

@login_required
def nurse_dashboard(request):
    """
    Панель управления медсестры с фильтрацией назначений
    """
    # Проверка роли через атрибут профиля
    if not hasattr(request.user, 'nurse_profile'):
        return redirect('access_denied')
    
    # Получаем текущую медсестру
    current_nurse = request.user.nurse_profile
    
    # Фильтрация назначений с поиском
    search_query = request.GET.get('search', '')
    
    prescriptions = Prescription.objects.filter(
        responsible_nurse=current_nurse,
        completed=False
    ).filter(
        Q(patient__full_name__icontains=search_query) |
        Q(medication__name__icontains=search_query)
    ).select_related('patient', 'medication').order_by('administration_time')
    
    context = {
        'prescriptions': prescriptions,
        'search_query': search_query,
        'current_nurse': current_nurse
    }
    return render(request, 'staff/nurse_dashboard.html', context)