from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from arm_medic import settings
from .models import Patient

User = get_user_model ()

class PatientRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(
        label="Дата рождения",
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    address = forms.CharField(
        label="Адрес",
        widget=forms.Textarea(attrs={'rows': 3})
    )
    blood_type = forms.ChoiceField(
        label="Группа крови",
        choices=Patient.BLOOD_TYPES
    )
    allergies = forms.CharField(
        label="Аллергии",
        required=False,
        widget=forms.Textarea(attrs={'rows': 2})
    )
    diagnosis = forms.CharField(
        label="Основной диагноз",
        required=False,
        widget=forms.Textarea(attrs={'rows': 2})
    )
    phone = forms.CharField(
        label="Телефон",
        max_length=20,
        required=True
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'password1',
            'password2',
            'birth_date',
            'address',
            'blood_type',
            'allergies',
            'diagnosis'
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'patient'  # Устанавливаем роль пациента
        if commit:
            user.save()
            Patient.objects.create(
                user=user,
                birth_date=self.cleaned_data['birth_date'],
                address=self.cleaned_data['address'],
                blood_type=self.cleaned_data['blood_type'],
                allergies=self.cleaned_data['allergies'],
                diagnosis=self.cleaned_data['diagnosis']
            )
        return user