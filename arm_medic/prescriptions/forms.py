from django import forms
from prescriptions.models import Prescription

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['medication', 'dosage', 'instructions', 'time', 'date', 'responsible_nurse']
        widgets = {
            'time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control'
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'medication': forms.Select(attrs={'class': 'form-control'}),
            'dosage': forms.TextInput(attrs={'class': 'form-control'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control'}),
            'responsible_nurse': forms.Select(attrs={'class': 'form-control'})
        }