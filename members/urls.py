# members/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='members'),
    path('signup/', views.signup, name='signup'),
]
