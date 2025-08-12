from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Medication

# Убедитесь, что нет дублирования этой строки
admin.site.register(Medication)