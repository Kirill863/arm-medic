from django.shortcuts import render
from staff.models import Doctor, Nurse
from prescriptions.models import Service

def landing(request):
    doctors = Doctor.objects.all()
    nurses = Nurse.objects.all()
    services = Service.objects.all()
    
    context = {
        'doctors': doctors,
        'nurses': nurses,
        'services': services,
    }
    return render(request, 'landing.html', context)