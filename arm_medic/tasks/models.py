from django.db import models

# Create your models here.
from django.db import models
from patients.models import Patient

class Task(models.Model):
    STATUS_CHOICES = [
        ('assigned', 'Назначено'),
        ('in_progress', 'В работе'),
        ('done', 'Выполнено'),
    ]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    title = models.CharField("Название", max_length=200)
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES)
    due_time = models.DateTimeField("Срок выполнения")

    def __str__(self):
        return f"{self.title} ({self.patient.name})"