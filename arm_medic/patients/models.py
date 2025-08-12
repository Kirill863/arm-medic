from django.db import models

# Create your models here.
from django.db import models

class Patient(models.Model):
    name = models.CharField("ФИО", max_length=100)
    diagnosis = models.TextField("Диагноз")
    room = models.CharField("Палата", max_length=10)
    admission_date = models.DateField("Дата поступления")

    def __str__(self):
        return self.name