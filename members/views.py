# members/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Appointment, BookAppointment
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import logging

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

logger = logging.getLogger(__name__)

@csrf_exempt
def book_appointment(request):
    if request.method == 'POST':
        logger.info("Received POST request for booking appointment")
        patient_id = request.POST.get('patient_id')
        date = request.POST.get('date')
        time = request.POST.get('time')
        reason = request.POST.get('reason')  # Get 'reason' from the form

        logger.info(f"Received data: patient_id={patient_id}, date={date}, time={time}, reason={reason}")

        try:
            # Create and save the appointment using the BookAppointment model
            appointment = BookAppointment(
                patientid=int(patient_id),  # Convert to integer
                date=date,
                time=time,
                issue=reason  # Map 'reason' from the form to 'issue' in the model
            )
            appointment.save()
            logger.info(f"Appointment saved successfully: {appointment}")
            messages.success(request, 'Appointment booked successfully!')
        except Exception as e:
            logger.error(f"Error saving appointment: {str(e)}")
            messages.error(request, 'Error booking appointment. Please try again.')

        return redirect('patient_home')  # Redirect to patient home page after booking
    
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