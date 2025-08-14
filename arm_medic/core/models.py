from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('doctor', 'Доктор'),
        ('nurse', 'Медсестра'),
        ('admin', 'Администратор'),
    )
    
    phone = models.CharField(max_length=20, verbose_name='Телефон', default='')
    role = models.CharField(max_length=10, choices=ROLES, verbose_name='Роль')
    position = models.CharField(max_length=100, blank=True, null=True, verbose_name='Должность/Специальность')
    
    # Добавляем related_name для разрешения конфликтов
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='Группы',
        blank=True,
        help_text='Группы, к которым принадлежит пользователь',
        related_name='custom_user_set',
        related_query_name='user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='Права доступа',
        blank=True,
        help_text='Конкретные права для этого пользователя',
        related_name='custom_user_set',
        related_query_name='user'
    )
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.get_role_display()})"