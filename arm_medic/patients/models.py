from django.contrib.auth import get_user_model
from django.db import models
from accounts.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.conf import settings  
from django.db import models

from staff.models import Doctor

User = get_user_model()

class Patient(models.Model):
    
    BLOOD_TYPES = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    blood_type = models.CharField("Группа крови", max_length=3, choices=BLOOD_TYPES, blank=True, null=True, default='O+')

    GENDER_CHOICES = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
        
    )

    # Основная информация
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients', verbose_name="Пользователь"), 

    full_name = models.CharField("ФИО", max_length=100)
    birth_date = models.DateField("Дата рождения", null=True, blank=True)
    gender = models.CharField(
        "Пол", 
        max_length=1, 
        choices=GENDER_CHOICES
    )
    blood_type = models.CharField(
        "Группа крови", 
        max_length=3, 
        choices=BLOOD_TYPES
    )
    insurance_number = models.CharField(
        "Страховой номер", 
        max_length=20, 
        unique=True,
        blank=True,
        null=True
    )

    # Медицинская информация
    diagnosis = models.TextField("Основной диагноз")
    allergies = models.TextField(
        "Аллергии", 
        blank=True, 
        null=True
    )
    chronic_diseases = models.TextField(
        "Хронические заболевания", 
        blank=True, 
        null=True
    )
    current_medication = models.TextField(
        "Текущие лекарства", 
        blank=True, 
        null=True
    )

    # Госпитализация
    room = models.CharField(
        "Палата", 
        max_length=10,
        validators=[MinValueValidator(1), MaxValueValidator(999)]
    )
    admission_date = models.DateField(
        "Дата поступления", 
        default=timezone.now
    )
    discharge_date = models.DateField(
        "Дата выписки", 
        blank=True, 
        null=True,
    )
    attending_physician = models.ForeignKey(
        'staff.Doctor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Лечащий врач",
    )
    patient_status = models.CharField(
        "Статус пациента",
        max_length=20,
        choices=[
            ('in_treatment', 'На лечении'),
            ('discharged', 'Выписан'),
            ('transferred', 'Переведен'),
            ('deceased', 'Умер'),
        ],
        default='in_treatment'
    )

    # Контактная информация
    address = models.TextField("Адрес", blank=True, null=True)
    phone = models.CharField("Телефон", max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} ({self.room} палата)" 

    def age(self):
        import datetime
        return int((datetime.date.today() - self.birth_date).days / 365.25)

    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"
        ordering = ['-admission_date', 'room']

# models.py
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    visit_date = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    diagnosis = models.TextField()
    treatment = models.TextField()
    notes = models.TextField(blank=True)

class TestResult(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=200)
    date = models.DateField()
    result_file = models.FileField(upload_to='test_results/')
    notes = models.TextField(blank=True)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    reason = models.TextField()
    completed = models.BooleanField(default=False)