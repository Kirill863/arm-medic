from django.db import models
from accounts.models import User

class Medication(models.Model):
    name = models.CharField("Название", max_length=100)
    dosage = models.CharField('Дозировка', max_length=100, null=True, blank=True) 
    stock = models.IntegerField("Остаток")
    critical_level = models.IntegerField("Критический остаток", default=10)
    responsible_nurse = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Ответственная медсестра",
        limit_choices_to={'role': 'nurse'}
    )

    def __str__(self):
        return f"{self.name} ({self.dosage})"