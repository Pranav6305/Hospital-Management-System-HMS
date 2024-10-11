# members/views.py
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'index.html')

def doctor_login(request):
    if request.method == 'POST':
        # Add authentication logic here
        return redirect('doctor_home')
    return render(request, 'doctor-login.html')

def patient_login(request):
    if request.method == 'POST':
        # Add authentication logic here
        return redirect('patient_home')
    return render(request, 'patient-login.html')

def register_patient(request):
    if request.method == 'POST':
        # Add registration logic here
        return redirect('patient_registered')
    return render(request, 'register-patient.html')

def doctor_home(request):
    return render(request, 'doctor-home.html')

def patient_home(request):
    return render(request, 'patient-home.html')

def patient_registered(request):
    return render(request, 'patient-registered.html')