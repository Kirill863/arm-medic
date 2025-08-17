from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()


    def __str__(self):
        return self.title

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()

    def __str__(self):
        return self.name