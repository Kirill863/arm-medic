from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from patients.models import Patient
from medications.models import Medication
from .models import Prescription
from .forms import PrescriptionForm

@login_required
def create_prescription(request, patient_id):
    if not request.user.role == 'doctor':
        return redirect('access_denied')
    
    patient = get_object_or_404(Patient, id=patient_id)
    
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.doctor = request.user
            prescription.patient = patient
            prescription.save()
            return redirect('doctor_dashboard')
    else:
        form = PrescriptionForm()
    
    medications = Medication.objects.all()
    context = {
        'form': form,
        'patient': patient,
        'medications': medications
    }
    return render(request, 'prescriptions/create_prescription.html', context)

@login_required
def complete_prescription(request, prescription_id):
    if not request.user.role == 'nurse':
        return redirect('access_denied')
    
    prescription = get_object_or_404(Prescription, id=prescription_id)
    
    if prescription.responsible_nurse != request.user:
        return redirect('access_denied')
    
    prescription.completed = True
    prescription.save()
    return redirect('nurse_dashboard')