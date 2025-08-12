from django.db import models

# Create your models here.
class Medication(models.Model):
    name = models.CharField("Название", max_length=100)
    dosage = models.CharField("Дозировка", max_length=50)
    stock = models.IntegerField("Остаток")
    critical_level = models.IntegerField("Критический остаток", default=10)

    def __str__(self):
        return f"{self.name} ({self.dosage})"