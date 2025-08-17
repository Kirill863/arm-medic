from django.contrib import admin
from django.contrib.auth import get_user_model
from staff.models import Doctor, Nurse
from patients.models import Patient, MedicalRecord, TestResult, Appointment
from prescriptions.models import Service

User = get_user_model()

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_date', 'gender', 'room', 'patient_status', 'attending_physician')
    list_filter = ('gender', 'blood_type', 'patient_status', 'admission_date')
    search_fields = ('full_name', 'insurance_number', 'phone')
    raw_id_fields = ('user', 'attending_physician')
    date_hierarchy = 'admission_date'
    ordering = ('-admission_date',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('user', 'full_name', 'birth_date', 'gender', 'blood_type', 'insurance_number')
        }),
        ('Медицинская информация', {
            'fields': ('diagnosis', 'allergies', 'chronic_diseases', 'current_medication')
        }),
        ('Госпитализация', {
            'fields': ('room', 'admission_date', 'discharge_date', 'attending_physician', 'patient_status')
        }),
        ('Контактная информация', {
            'fields': ('address', 'phone'),
            'classes': ('collapse',)
        }),
    )

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'visit_date', 'doctor', 'diagnosis')
    list_filter = ('visit_date', 'doctor')
    search_fields = ('patient__full_name', 'diagnosis')
    date_hierarchy = 'visit_date'
    raw_id_fields = ('patient', 'doctor')

@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ('patient', 'test_name', 'date')
    list_filter = ('date', 'test_name')
    search_fields = ('patient__full_name', 'test_name')
    date_hierarchy = 'date'
    raw_id_fields = ('patient',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'completed')
    list_filter = ('date', 'completed', 'doctor')
    search_fields = ('patient__full_name', 'doctor__name', 'reason')
    date_hierarchy = 'date'
    raw_id_fields = ('patient', 'doctor')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'experience', 'qualification')
    search_fields = ('name', 'specialty', 'qualification')
    list_filter = ('specialty',)
    readonly_fields = ('photo_preview',)
    
    def photo_preview(self, obj):
        from django.utils.html import format_html
        return format_html('<img src="{}" width="150" />'.format(obj.photo.url)) if obj.photo else "-"
    photo_preview.short_description = "Предпросмотр фото"

@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'experience')
    search_fields = ('name', 'position')
    readonly_fields = ('photo_preview',)
    
    def photo_preview(self, obj):
        from django.utils.html import format_html
        return format_html('<img src="{}" width="150" />'.format(obj.photo.url)) if obj.photo else "-"
    photo_preview.short_description = "Предпросмотр фото"

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Опционально: регистрация модели User, если нужно администрировать пользователей
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'phone', 'is_active')
    list_filter = ('role', 'is_active', 'is_staff')
    search_fields = ('username', 'email', 'phone', 'first_name', 'last_name')
    filter_horizontal = ('groups', 'user_permissions')