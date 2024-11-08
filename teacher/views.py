# student/views.py
from django.shortcuts import render
from .forms import HolidayFormClass

def teacher_base(request):
    return render(request, 'teacher/base.html')

def teacher_home(request):
    return render(request, 'teacher/index.html')

def teacher_changepass(request):
    return render(request, 'teacher/changepass.html')

def teacher_edit(request):
    return render(request, 'teacher/edit.html')

def teacher_holiday(request):
    template_name = "teacher/holiday.html"
    form = HolidayFormClass(request.POST or None)
    ctx = {}
    if form.is_valid():
        is_holiday = form.cleaned_data["is_holiday"]
    ctx["form"] = form
    return render(request, template_name, ctx)

def teacher_logout(request):
    return render(request, 'teacher/logout.html')
