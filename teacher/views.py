# student/views.py
from django.shortcuts import render

def student_changepass(request):
    return render(request, 'teacher/base.html')

def student_home(request):
    return render(request, 'teacher/index.html')

def student_reason(request):
    return render(request, 'teacher/changepass.html')

def student_changepass(request):
    return render(request, 'teacher/edit.html')

def student_changepass(request):
    return render(request, 'teacher/holiday.html')

def student_logout(request):
    return render(request, 'teacher/logout.html')