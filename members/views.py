# members/views.py
from django.shortcuts import render

def members(request):
    return render(request, 'login.html')  