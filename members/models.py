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
        
from django.db import models

class BookAppointment(models.Model):
    patient_id = models.CharField(max_length=50)  # Adjust the field types as needed
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()

    class Meta:
        db_table = 'bookappointments'  # This specifies the table name in MySQL
