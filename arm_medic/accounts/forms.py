from django.contrib.auth.forms import UserCreationForm
from django import forms
from core.models import User  # Импортируем кастомную модель

class SignUpForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.ROLES)  # Теперь ROLES доступен
    phone = forms.CharField(max_length=20, required=True, label="Телефон")
    
    class Meta:
        model = User
        fields = ("username", "phone", "password1", "password2", "role")