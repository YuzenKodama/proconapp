# login/views.py
from django.shortcuts import render

def login_home(request):
    return render(request, 'index.html')
