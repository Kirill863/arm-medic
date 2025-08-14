from django.contrib.auth.forms import UserCreationForm
from django import forms
from core.models import User  # Импортируем кастомную модель

class SignUpForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.ROLES)  # Теперь ROLES доступен
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'role')