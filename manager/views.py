from django.shortcuts import render

# Create your views here.
def manager_index(request):
    return render(request, 'manager/index.html')

def manager_log(request):
    return render(request, 'manager/index.html')

def student_logout(request):
    return render(request, 'student/logout.html')