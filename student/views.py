# student/views.py
from django.shortcuts import render

def student_home(request):
    return render(request, 'student/index.html')

def student_reason(request):
    return render(request, 'student/reason.html')

def student_changepass(request):
    return render(request, 'student/changepass.html')

def student_logout(request):
    return render(request, 'student/logout.html')