from django.shortcuts import render
from clinic.models import Service, Doctor  # если используете модели

def home(request):
    services = Service.objects.all()
    doctors = Doctor.objects.all()
    
    context = {
    'services': services,
    'doctors': doctors,
    }
    return render(request, 'clinic/index.html', context)