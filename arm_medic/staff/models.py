from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='doctors/')
    qualification = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name

class Nurse(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='nurses/')
    
    def __str__(self):
        return self.name