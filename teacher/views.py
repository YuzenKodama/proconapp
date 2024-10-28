# student/views.py
from django.shortcuts import render

def teacher_changepass(request):
    return render(request, 'teacher/base.html')

def teacher_home(request):
    return render(request, 'teacher/index.html')

def teacher_reason(request):
    return render(request, 'teacher/changepass.html')

def teacher_changepass(request):
    return render(request, 'teacher/edit.html')

def teacher_changepass(request):
    return render(request, 'teacher/holiday.html')

def teacher_logout(request):
    return render(request, 'teacher/logout.html')