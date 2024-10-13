#models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields for the Patient model


class Appointment(models.Model):
    patient_id = models.IntegerField(default=0)
    issue = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Appointment for Patient {self.patient_id} on {self.date} at {self.time}"
    
    class Meta:
        db_table = 'book_appointments'
        


class BookAppointment(models.Model):
    patientid = models.IntegerField(null=True, blank=True, db_column='patientid')  # Allow null values
    issue = models.CharField(max_length=255, null=True, blank=True, db_column='issue')  # Allow null values
    date = models.CharField(max_length=255, db_column='date')
    time = models.CharField(max_length=255, db_column='time')

    class Meta:
        db_table = 'bookappointments'

    def __str__(self):
        return f"Appointment for Patient {self.patientid} on {self.date} at {self.time}"
