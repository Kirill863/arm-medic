from django.shortcuts import render

def landing(request):
    doctors = [
        {
            'id': 1,
            'name': 'Иванов А.П.',
            'specialty': 'Терапевт',
            'experience': '15 лет',
            'photo': 'doctor1.jpg'
        },
        {
            'id': 2,
            'name': 'Петрова Е.В.',
            'specialty': 'Кардиолог',
            'experience': '12 лет', 
            'photo': 'doctor2.jpg'
        }
    ]
    
    nurses = [
        {
            'id': 1,
            'name': 'Смирнова О.И.',
            'position': 'Старшая медсестра',
            'experience': '8 лет',
            'photo': 'nurse1.jpg'
        }
    ]
    
    services = [
        'Консультации специалистов',
        'Диагностика',
        'Физиотерапия',
        'Вакцинация'
    ]
    
    return render(request, 'landing.html', {
        'doctors': doctors,
        'nurses': nurses,
        'services': services
    })