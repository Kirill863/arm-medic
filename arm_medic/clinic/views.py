from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Appointment
from .forms import AppointmentForm
from datetime import date

def home(request):
    return render(request, 'clinic/index.html')

def save_appointment_data(request):
    if request.method == 'POST':
        # Сохраняем данные в сессии
        request.session['appointment_data'] = {
            'name': request.POST.get('name'),
            'phone': request.POST.get('phone'),
            'specialist': request.POST.get('specialist'),
            'date': request.POST.get('date'),
            'message': request.POST.get('message', ''),
        }
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)

def time_selection(request):
    # Проверяем, есть ли данные в сессии
    if 'appointment_data' not in request.session:
        return redirect('home')
    
    # Получаем данные из сессии
    appointment_data = request.session['appointment_data']
    
    # Получаем занятые временные слоты
    booked_times = Appointment.objects.filter(
        specialist=appointment_data['specialist'],
        date=appointment_data['date']
    ).values_list('time', flat=True)
    
    # Все возможные слоты времени
    all_times = [choice[0] for choice in Appointment.TIME_SLOTS]
    available_times = [t for t in all_times if t not in booked_times]
    
    if request.method == 'POST':
        time = request.POST.get('time')
        if time in available_times:
            # Создаем запись
            Appointment.objects.create(
                name=appointment_data['name'],
                phone=appointment_data['phone'],
                specialist=appointment_data['specialist'],
                date=appointment_data['date'],
                time=time,
                message=appointment_data['message']
            )
            
            # Очищаем сессию
            del request.session['appointment_data']
            
            messages.success(request, 'Запись успешно создана!')
            return redirect('appointment_success')
    
    return render(request, 'clinic/time_selection.html', {
        'available_times': available_times,
        'appointment_data': appointment_data
    })

def appointment_success(request):
    return render(request, 'clinic/appointment_success.html')