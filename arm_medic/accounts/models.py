from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('doctor', 'Доктор'),
        ('nurse', 'Медсестра'),
        ('admin', 'Администратор'),
    )
    
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    role = models.CharField(max_length=10, choices=ROLES, verbose_name='Роль')
    position = models.CharField(max_length=100, blank=True, null=True, verbose_name='Должность/Специальность')
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.get_role_display()})"