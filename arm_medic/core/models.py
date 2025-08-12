from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('nurse', 'Медсестра'),
        ('doctor', 'Врач'),
        ('admin', 'Администратор'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='nurse')
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.get_full_name()} ({self.role})"