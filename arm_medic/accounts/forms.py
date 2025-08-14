from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class SignUpForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.ROLES, label="Роль")
    phone = forms.CharField(max_length=20, required=True, label="Телефон")
    position = forms.CharField(max_length=100, required=False, label="Должность/Специальность")
    
    class Meta:
        model = User
        fields = ("username", "phone", "password1", "password2", "role", "position")