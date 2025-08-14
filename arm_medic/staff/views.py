from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from patients.models import Patient
from prescriptions.models import Prescription  # Измененный импорт
from prescriptions.forms import PrescriptionForm  # Импорт формы

@login_required
def doctor_dashboard(request):
    if not request.user.role == 'doctor':
        return redirect('access_denied')
    
    patients = Patient.objects.all()
    context = {'patients': patients}
    return render(request, 'staff/doctor_dashboard.html', context)

@login_required
def nurse_dashboard(request):
    if not request.user.role == 'nurse':
        return redirect('access_denied')
    
    prescriptions = Prescription.objects.filter(
        responsible_nurse=request.user,
        completed=False
    ).select_related('patient', 'medication')
    
    context = {'prescriptions': prescriptions}
    return render(request, 'staff/nurse_dashboard.html', context)