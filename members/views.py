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

def book_appointment(request):
    if request.method == 'POST':
        return redirect('patient_home')
    return render(request, 'book-appointment.html')

def view_medical_record(request):
    patient_id = request.GET.get('patient_id')
    records = None

    if patient_id:
        with connection.cursor() as cursor:
            # Fetch records from medicalrecord table for the given patient_id
            cursor.execute("SELECT issue, time FROM medicalrecord WHERE patient_id = %s", [patient_id])
            records = cursor.fetchall()

    return render(request, 'medical-record.html', {'records': records, 'patient_id': patient_id})