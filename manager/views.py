from django.shortcuts import render

# Create your views here.
def manager_index(request):
    return render(request, 'manager/index.html')

def manager_log(request):
    return render(request, 'manager/log.html')

def manager_situation_edit(request):
    return render(request, 'manager/lsituation_edit.html')

def manager_student_management(request):
    return render(request, 'manager/student_management.html')

def manager_teacher_management(request):
    return render(request, 'manager/teacher_management.html')