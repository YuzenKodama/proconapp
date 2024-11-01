# student/views.py
from django.shortcuts import render

def admin_base(request):
    return render(request, 'admin/base.html')

def admin_home(request):
    return render(request, 'admin/index.html')

def admin_changepass(request):
    return render(request, 'admin/changepass.html')

def admin_edit(request):
    return render(request, 'admin/situation_edit.html')

def admin_holiday(request):
    return render(request, 'admin/index.html')

def admin_logout(request):
    return render(request, 'admin/logout.html')

