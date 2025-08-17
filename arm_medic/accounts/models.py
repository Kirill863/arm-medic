from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLES = (
        ('doctor', 'Доктор'),
        ('nurse', 'Медсестра'),
        ('admin', 'Администратор'),
        ('patient', 'Пациент'),  # Добавляем роль пациента
    )
    
    phone = models.CharField(
        max_length=20, 
        verbose_name='Телефон',
        default='',  # Добавлено значение по умолчанию
        blank=True   # Разрешаем пустое значение
    )
    role = models.CharField(
        max_length=10, 
        choices=ROLES, 
        verbose_name='Роль'
    )
    position = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        verbose_name='Должность/Специальность'
    )
    
    # Исправленные related_name (должны быть уникальными для проекта)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='Группы',
        blank=True,
        help_text='Группы, к которым принадлежит пользователь',
        related_name='accounts_user_set',  # Уникальный для accounts
        related_query_name='accounts_user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='Права доступа',
        blank=True,
        help_text='Конкретные права для этого пользователя',
        related_name='accounts_user_set',  # Уникальный для accounts
        related_query_name='accounts_user'
    )
    
    def __str__(self):
        if self.get_full_name():
            return f"{self.get_full_name()} ({self.get_role_display()})"
        return f"{self.username} ({self.get_role_display()})"