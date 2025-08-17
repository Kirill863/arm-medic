from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()


    def __str__(self):
        return self.title

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()

    def __str__(self):
        return self.name
    


class Appointment(models.Model):
    SPECIALIST_CHOICES = [
        ('cardiologist', 'Кардиолог'),
        ('neurologist', 'Невролог'),
        ('orthopedist', 'Ортопед'),
        ('therapist', 'Терапевт'),
        ('dentist', 'Стоматолог'),
        ('pediatrician', 'Педиатр'),
    ]

    TIME_SLOTS = [
        ('09:00', '09:00-10:00'),
        ('10:00', '10:00-11:00'),
        ('11:00', '11:00-12:00'),
        ('13:00', '13:00-14:00'),
        ('14:00', '14:00-15:00'),
        ('15:00', '15:00-16:00'),
    ]

    name = models.CharField(
        verbose_name='Имя пациента',
        max_length=100,
        validators=[MinLengthValidator(2)]
    )
    
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=18,
        validators=[
            RegexValidator(
                regex=r'^\+7\s\(\d{3}\)\s\d{3}-\d{2}-\d{2}$',
                message='Формат телефона: +7 (XXX) XXX-XX-XX'
            )
        ]
    )
    
    specialist = models.CharField(
        verbose_name='Специалист',
        max_length=50,
        choices=SPECIALIST_CHOICES
    )
    
    date = models.DateField(verbose_name='Дата приема')
    time = models.CharField(
        verbose_name='Время приема',
        max_length=5,
        choices=TIME_SLOTS
    )
    
    message = models.TextField(
        verbose_name='Дополнительная информация',
        blank=True,
        null=True,
        max_length=500
    )
    
    created_at = models.DateTimeField(
        verbose_name='Дата создания записи',
        auto_now_add=True
    )
    
    is_confirmed = models.BooleanField(
        verbose_name='Подтверждено',
        default=False
    )

    class Meta:
        verbose_name = 'Запись на прием'
        verbose_name_plural = 'Записи на прием'
        ordering = ['-date', 'time']
        unique_together = ['date', 'time', 'specialist']

    def __str__(self):
        return f'{self.name} - {self.get_specialist_display()} {self.date} {self.time}'