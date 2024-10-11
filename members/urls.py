# members/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doctor-login/', views.doctor_login, name='doctor_login'),
    path('patient-login/', views.patient_login, name='patient_login'),
    path('register-patient/', views.register_patient, name='register_patient'),
    path('doctor-home/', views.doctor_home, name='doctor_home'),
    path('patient-home/', views.patient_home, name='patient_home'),
    path('patient-registered/', views.patient_registered, name='patient_registered'),
]