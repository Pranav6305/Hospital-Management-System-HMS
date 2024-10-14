# members/views.py
from multiprocessing import connection
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Appointment, BookAppointment, NewPatient
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from members.models import Appointment 
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

from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from .models import NewPatient  # Make sure the model is correctly imported

def register_patient(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        dob = request.POST['dob']
        contactno = request.POST['contactno']
        patientid = request.POST['patientid']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Validate password match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register_patient')

        try:
            # Save patient data
            patient = NewPatient(
                firstname=firstname,
                lastname=lastname,
                dob=dob,
                contactno=contactno,
                patientid=patientid,
                password=password  # Ideally, hash the password before storing
            )
            patient.save()
            messages.success(request, "Patient registered successfully!")
            return redirect('home')  # Redirect to the home page or appropriate route

        except IntegrityError:
            messages.error(request, "Patient ID already exists. Please try a different one.")
            return redirect('register_patient')

    return render(request, 'register_patient.html')


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
    appointments = BookAppointment.objects.all().values(
        'patientid', 'issue', 'date', 'time'
    )  # Do not include 'id'
    
    context = {'appointments': appointments}
    return render(request, 'medical_record.html', context)

