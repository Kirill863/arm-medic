from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'get_specialist_display', 'date', 'time', 'is_confirmed')
    list_filter = ('specialist', 'date', 'is_confirmed')
    search_fields = ('name', 'phone')
    date_hierarchy = 'date'
    ordering = ('-date', 'time')