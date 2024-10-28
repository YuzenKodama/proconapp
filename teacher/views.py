# student/views.py
from django.shortcuts import render

def student_changepass(request):
    return render(request, 'eacher/base.html')

def student_home(request):
    return render(request, 'teacher/index.html')

def student_reason(request):
    return render(request, 'eacher/changepass.html')

def student_changepass(request):
    return render(request, 'eacher/edit.html')

def student_changepass(request):
    return render(request, 'eacher/holiday.html')

def student_logout(request):
    return render(request, 'eacher/logout.html')