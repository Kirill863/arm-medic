from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Добавляем выбор ролей
    ROLES = (
        ('doctor', 'Доктор'),
        ('nurse', 'Медсестра'),
        ('admin', 'Администратор'),
    )
    
    role = models.CharField(
        max_length=10,
        choices=ROLES,
        default='doctor',
        verbose_name='Роль'
    )
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='core_user_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='core_user_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    class Meta:
        db_table = 'core_user'