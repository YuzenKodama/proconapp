# login/views.py
# views.py
from django.shortcuts import render, redirect

def login(request):
    return render(request, 'login/index.html')