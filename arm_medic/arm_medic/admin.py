from django.contrib import admin
from staff.models import Doctor, Nurse
from prescriptions.models import Service

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'experience')
    search_fields = ('name', 'specialty')

@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'experience')
    search_fields = ('name', 'position')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Зарегистрируйте другие модели аналогично