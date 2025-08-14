from django.contrib import admin
from .models import Medication

@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'dosage', 'stock', 'critical_level', 'responsible_nurse')
    list_filter = ('responsible_nurse',)
    search_fields = ('name', 'dosage')