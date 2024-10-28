# student/views.py
from django.shortcuts import render

def teacher_base(request):
    return render(request, 'teacher/base.html')

def teacher_index(request):
    return render(request, 'teacher/index.html')

def teacher_changepass(request):
    return render(request, 'teacher/changepass.html')

def teacher_edit(request):
    return render(request, 'teacher/edit.html')

def teacher_holiday(request):
    return render(request, 'teacher/holiday.html')

def teacher_logout(request):
    return render(request, 'teacher/logout.html')