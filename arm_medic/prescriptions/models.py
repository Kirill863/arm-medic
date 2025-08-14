from django.db import models
from core.models import User
from patients.models import Patient
from medications.models import Medication

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE, related_name='prescriptions')
    dosage = models.CharField(max_length=100)
    instructions = models.TextField()
    time = models.TimeField()
    date = models.DateField()
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_prescriptions')
    responsible_nurse = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='nurse_prescriptions',
        limit_choices_to={'role': 'nurse'}
    )
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.medication.name} для {self.patient.full_name}"